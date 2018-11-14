#!/usr/bin/env python3

import unittest
import os, sys

RUNDIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(RUNDIR + "/../")

from solr_loganalyzer import StatCounter


class TestCoreCounter(unittest.TestCase):

    def setUp(self):
        self.stats = StatCounter(debug=True)

    def test_parse(self):
        with open("%s/resources/solr.log" % RUNDIR) as log_fd:
            self.stats.process(log_fd)
        cores = self.stats.corecounters
        print("Cores: "+ str(cores))
        self.assertEqual(len(cores), 1)
        self.assertEqual(self.stats.queries, self.stats.lines)


if __name__ == '__main__':
    unittest.main()
