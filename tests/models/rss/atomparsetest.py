#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import datetime
from xml.dom import minidom

from models.rss.rss_parse.rss_parse_atom import RssParseAtom
from google.appengine.api import urlfetch


class AtomParseTest(unittest.TestCase):
    def testParseFeed(self):
        rss_parsed = minidom.parseString(self._contents)
        objARP = RssParseAtom(rss_parsed)
        self.assertEqual(objARP.title(), "Let's go Curious")
        self.assertEqual(objARP.base_link(), "http://www.curious-eyes.com/blog/shuhei")
        self.assertEqual(objARP.lastbuilddate(), datetime.datetime(2013, 6, 20, 11, 38, 35))

    def setUp(self):
        feedinput = urlfetch.fetch('http://www.curious-eyes.com/blog/shuhei/?feed=atom')
        # print (feedinput.content)
        self._contents = feedinput.content

    def tearDown(self):
        pass
