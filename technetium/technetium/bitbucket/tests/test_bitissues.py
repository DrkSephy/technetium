"""
Test Technetium Bitbucket: bitissues
"""
import unittest
import technetium.bitbucket.bitissues as bitissues


class BitissuesTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'

        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'


    # These tests might need to be mocked
    def test_get_issues_not_empty(self):
        """
        Tests that get issues return a non-empty list.
        """
        pass
