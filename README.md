solr-loganalyzer
=================

A query analyzer that parses Solr's log file to get some basic query statistics 

Note that you need to enable logging at the INFO level for this to
work and you need to have cores enabled. You also need python2.7 installed.

Usage:
    # reading from stdin
    head -n <NUMBER OF LINES TO ANALYZE> solrlog| ./loganalyzer.py

    # reading a file
    head -n <...> > /tmp/outfile.txt
    ./loganalyzer.py /tmp/outfile.txt

The analyzer outputs statistics grouped by Solr core. Here is an example:

<pre>
Top Endpoints for core1
========================================
1) "/mlt" 3
   
Top Searh URLs for core1
========================================
1) "mlt.count=16&&q=qrows=16" 1
2) "mlt.count=16&start=0&q=&rows=16" 1
   
Slowest Searches for core1
========================================
1) "mlt.count=16&&q=qrows=16" 30
2) "mlt.count=16&start=0&q=&rows=16" 11
   
Search Time for core1
========================================
Median     2
75%     11
90%     11
99%     30

****************************************************************************************************

Top Endpoints for core2
========================================
1) "/mlt" 3
   
Top Searh URLs for core2
========================================
1) "mlt.count=5&&q=qrows=16" 1
2) "mlt.count=5&start=0&q=&rows=16" 1
   
Slowest Searches for core2
========================================
1) "mlt.count=5&&q=qrows=16" 30
2) "mlt.count=5&start=0&q=&rows=16" 11
   
Search Time for core2
========================================
Median     2
75%     11
90%     11
99%     30
</pre>

This tool is inspired by [redis-faina](https://github.com/Instagram/redis-faina)
