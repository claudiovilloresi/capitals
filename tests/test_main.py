''' test_main.py module is the module made
    for running tets on the main function parse_allowed_input.

    Here after settin up a temporary file in which running the tests
    are run two main tests:

    1. test 1 is testing the datafile with a wrong datafile
    2. test 2 is testing the datafile with an empy one.

    The last function tears down the temporary file in
    which all the tests were run. '''

import unittest
from main import parse_allowed_input
import os


class TestMain(unittest.TestCase):

    # open the test
    def setUp(self):
        self.temporary_file = "/tmp/test_empty_datafile"
        f = open(self.temporary_file, 'w')
        f.close()

# CSV tests
# test 1
    def test_no_datafile(self):  # test the csv
        u, r = parse_allowed_input(datafile="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(u)
        self.assertFalse(r)

# test 2

    def test_empty_datafie(self):  # test the datafile in an empty situation
        u, r = parse_allowed_input(datafile=self.temporary_file)
        self.assertFalse(u)
        self.assertFalse(r)

# close the test
    def tearDown(self):
        os.remove(self.temporary_file)
