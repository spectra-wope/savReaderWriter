#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import unittest
from tempfile import gettempdir
from os.path import join

from savReaderWriter import SavWriter


# issue 51 "Subtle bug/difference difference in Python 2 and 3 with SavWriter.spssDateTime"
class test_SavWriter_encode_SPSSDate(unittest.TestCase):

    def setUp(self):
        self.savFileName = join(gettempdir(), "encode_SPSSDate.sav")

    def test_date_encoding(self):
        with SavWriter(self.savFileName, [b'date'], {b'date': 0}) as writer:
            seconds1 = writer.spssDateTime(b"2000-01-01", "%Y-%m-%d")
            seconds2 = writer.spssDateTime("2000-01-01", "%Y-%m-%d")
            self.assertEqual(seconds1, 13166064000.0)
            self.assertEqual(seconds1, seconds2)

    def tearDown(self):
        try:
            os.remove(self.savFileName)
        except Exception:
            pass
    
if __name__ == "__main__":
    unittest.main()
