"""
Test Technetium Bitbucket: bitchangesets
"""
import unittest
import technetium.bitbucket.bitchangesets as bitchangesets


class BitchangesetsTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'

        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'


    # These tests might need to be mocked
    def test_get_changesets_not_empty(self):
        """
        Tests that get changesets return a non-empty list.
        """
        pass
