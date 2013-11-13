"""
Test Technetium Bitbucket: bitstats
"""

import technetium.bitbucket.bitstats as bitstats
import unittest

class BitstatsTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'
        self.data = [{'author': 'Kevin Chan'}, {'author': 'Kevin Chan'}]
        self.data2 = [{'author': 'Kevin Chan'}, {'author': 'DrkSephy'}]
    

    def test_commit_counter(self):
        """
        Tests that commit counter returns valid data for single user
        """
        self.assertEqual(bitstats.tally_changesets(self.data), {'Kevin Chan': 2})

    def test_commit_counter_multiple_users(self):
        """
        Tests that commit counter returns valid data for multiple users
        """
        self.assertEqual(bitstats.tally_changesets(self.data2), {'Kevin Chan': 1, 'DrkSephy': 1})