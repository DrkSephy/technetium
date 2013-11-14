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
        self.data = [{'utctimestamp': '2013-11-11 03:14:50+00:00', 'author': 'DrkSephy', 
                    'timestamp': '2013-11-11 04:14:50', 'raw_author': 'David Leonard <sephirothcloud1025@yahoo.com>'}]


    # These tests might need to be mocked
    def test_get_changesets_not_empty(self):
        """
        Tests that get changesets return a non-empty list.
        """
        self.assertEqual(bitchangesets.parse_changesets(self.data), [{'author': 'DrkSephy'}])
        pass

    def test_parse_changesets_empty(self):
        """
        Tests that parsing an empty changeset list returns empty list
        """
        self.assertEqual(bitchangesets.parse_changesets([]), [])