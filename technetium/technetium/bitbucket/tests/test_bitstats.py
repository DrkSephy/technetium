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
        self.json = """
        [{'author': 'Kevin Chan'}]
        """

    def test_commit_counter(self):
        self.assertEqual(bitstats.tally_changesets([]), {})