#!/usr/bin/env python3

from collections import Counter
import re
import argparse
import sys
import urllib.parse

# INFO  - 2018-11-12 08:42:22.162; org.apache.solr.core.SolrCore; [core1]
LINE_RE = re.compile(
    r"INFO.*?\[(?P<core>\w+)\]\s+webapp=/\w+\s+path=(?P<path>/\w+)\s+params={(?P<search>.*)}\s+(hits=(?P<hits>\w+)\s+)?status=\w+\s+QTime=(?P<qtime>\w+).*")
FACET_FIELD_RE = re.compile(r"facet.field=(.+?)(&|$)")
"""
lines we want:
INFO  2018-11-12 08:42:22.162; org.apache.solr.core.SolrCore; [arstechnicacogtree] webapp=/solr path=/mlt params={mlt.count=16&fl=link,title,author,pub_date,thumb_url_medium,metadata,section&start=0&q=link_aliases:http\://arstechnica.com/apple/news/2009/02/the\-case\-of\-the\-app\-store\-ripoff.ars&wt=json&fq=pub_date:[NOW/DAY-14DAYS+TO+NOW/DAY%2B1DAY]&rows=16} status=0 QTime=2
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260326940083812,51.759690475011105&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
"""


class CoreCounter(object):
    def __init__(self, corename):
        self.corename = corename
        self.endpoints = Counter()
        self.urls = Counter()
        self.linesread = 0
        self.qtimes = Counter()
        self.hits = Counter()
        self.facet_fields = Counter()

    def __repr__(self):
        return "<Core '%s' with %i endpoints %i search urls>" % (self.corename, len(self.endpoints), len(self.urls))

    def timestats(self):
        sqtimes = sorted(self.qtimes.values())
        numitems = len(sqtimes)
        percent_50 = sqtimes[int(numitems / 2)]
        percent_75 = sqtimes[int(numitems * .75)]
        percent_90 = sqtimes[int(numitems * .90)]
        percent_99 = sqtimes[int(numitems * .99)]
        return (("Median", percent_50),
                ("75%", percent_75),
                ("90%", percent_90),
                ("99%", percent_99))

    def print_top_queries(self, n, counter, title, unit):
        """Print the top N entries of a counter with its title.
        """
        s = "{0}\n{1}\n".format(title, "=" * 40)
        top = counter.most_common(n)
        for index, item in enumerate(top):
            label, cnt = item
            s += 'QUERY %i: %i %s \n\n  "%s"\n\n' % (index + 1, cnt, unit, label)
        return s

    def print_top_items(self, n, counter, title, unit):
        """Print the top N entries of a counter with its title.
        """
        s = "{0}\n{1}\n".format(title, "=" * 40)
        top = counter.most_common(n)
        for index, item in enumerate(top):
            label, cnt = item
            s += 'ITEM %-5i: %-15s "%s"\n' % (index + 1, str(cnt) + " times", label)
        return s

    def pprint_stats(self):
        """Print statistics for a core
        """
        print(self.print_top_queries(args.max, self.endpoints, "Top Endpoints for {0}".format(self.corename), "times"))
        print(self.print_top_queries(args.max, self.urls, "Top Search URLs for {0}".format(self.corename), "times"))
        print(self.print_top_queries(args.max, self.qtimes, "Slowest Searches for {0}".format(self.corename), "ms"))
        print(self.print_top_items(args.max, self.facet_fields, "Top Factet Fields for {0}".format(self.corename), "times"))

        # qtimes
        print("Search Time for {0}\n{1}\n".format(self.corename, '=' * 40))
        stats = self.timestats()
        for st in stats:
            print("%-10s %sms" % (st[0], st[1]))
        return ""


class StatCounter(object):

    def __init__(self, write_file_fd=None, write_base_url=None, debug=False):
        self.corecounters = {}
        self.queries = 0
        self.lines = 0
        self.debug = debug
        self.write_file_fd = write_file_fd
        self.write_base_url = write_base_url

    def write_file_line(self, core, path, query):

        if self.write_base_url:
            line = self.write_base_url
        else:
            line = ""

        line += core
        line += path + "?"

        query_args = query.split("&")
        query_args_new = []
        for query_arg in query_args:
            # print(query_arg)
            m = re.match("^(.+)=(.+)$", query_arg)
            if m:
                if m.group(1) == "fq" or m.group(1) == "q":
                    query_args_new.append(m.group(1) + "=" + urllib.parse.quote_plus(m.group(2).replace("+", " ")))
                else:
                    query_args_new.append(query_arg)

        line += "&".join(query_args_new)
        line += "\n"

        self.write_file_fd.write(line)

    def process(self, iterinput):
        for line in iterinput:
            self.lines += 1

            matches = LINE_RE.match(line)
            if not matches:
                if self.debug:
                    print("not matched: >>>{0}<<<".format(line))
                continue

            core = matches.group("core")
            path = matches.group("path")

            search = matches.group("search")

            qtime = matches.group("qtime")
            hits = matches.group("hits")

            if self.write_file_fd is not None:
                self.write_file_line(core, path, search)

            corecounter = self.corecounters.get(core, CoreCounter(core))
            corecounter.endpoints[path] += 1
            corecounter.urls[search] += 1
            corecounter.linesread += 1
            corecounter.qtimes[search] = int(qtime)

            self.corecounters[core] = corecounter
            self.queries += 1

            for match in FACET_FIELD_RE.findall(search):
                corecounter.facet_fields[match[0]] += 1

    def allcounterstats(self):
        for cc in self.corecounters.values():
            print(cc.pprint_stats())
            print("*" * 100)
            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--max',
        type=int,
        default=10,
        nargs='?',
        help='number of top queries')

    parser.add_argument(
        '--debug',
        help='Output debug information',
        action='store_true',
    )

    parser.add_argument(
        '--write_file',
        type=str,
        default=None,
        nargs='?',
        help='write query file (can be used for the siege loadtest tool)')

    parser.add_argument(
        '--write_base_url',
        type=str,
        default=None,
        nargs='?',
        help='base url for query file')

    args, remaining_args = parser.parse_known_args()

    if args.write_file is not None:
        write_file_fd = open(args.write_file, "w")
    else:
        write_file_fd = None

    sc = StatCounter(write_file_fd=write_file_fd, write_base_url=args.write_base_url, debug=args.debug)

    if len(remaining_args) <= 0:
        sc.process(sys.stdin)
    else:
        for filename in remaining_args:
            print("parsing %s" % filename)
            with open(filename, "r") as fd:
                sc.process(fd)

    sc.allcounterstats()

    print("parsed %s lines with %s queries" % (sc.lines, sc.queries))

    if write_file_fd is not None:
        print("wrote urls to file '%s'" % args.write_file)
        write_file_fd.close()
