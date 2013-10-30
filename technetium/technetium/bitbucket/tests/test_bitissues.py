"""
Test Technetium Bitbucket: bitissues
"""
import unittest
import technetium.bitbucket.bitissues as bitissues


class BitissuesTests(unittest.TestCase):

    def test_get_issues_not_empty(self):
        """
        Tests that get issues return a non-empty list.
        """
        user = 'DrkSephy'
        repo = 'smw-koopa-krisis'
        self.assertGreater(bitissues.get_issues(user, repo), 0)

