"""
Test Technetium Bitbucket: bitchangesets
"""

from mock import Mock, patch
import unittest
import technetium.bitbucket.bitchangesets as bitchangesets
import technetium.bitbucket.bitchangesets as bitmethods


class BitchangesetsTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.user= 'DrkSephy'
        self.repo = 'smw-koopa-krisis'
        self.endpoint = 'changesets'
        self.url = 'https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/changesets/0/0'
        self.limit = 0
        self.start = 0
        self.auth_tokens = {}
        self.data3 = { "count": 532, "start": "0", "limit": 0, "changesets": []}
        self.data3['parsed_author'] = {'raw_author': 'David Leonard'}


        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'
        self.data = [{'utctimestamp': '2013-11-11 03:14:50+00:00', 'author': 'DrkSephy', 
                    'timestamp': '2013-11-11 04:14:50', 'raw_author': 'David Leonard <sephirothcloud1025@yahoo.com>'}]
        self.data2 = [{'utctimestamp': '2013-11-11 03:14:50+00:00', 'author': 'DrkSephy', 
                    'timestamp': '2013-11-11 04:14:50', 'raw_author': 'David Leonard'}]


    def test_get_parse_not_empty(self):
        """
        Tests that parsing changesets returns a non-empty list.
        """
        self.assertEqual(bitchangesets.parse_changesets(self.data), self.data['parsed_author'])
        pass

    def test_parse_changesets_empty(self):
        """
        Tests that parsing an empty changeset list returns empty list.
        """
        self.assertEqual(bitchangesets.parse_changesets([]), [])

    def test_parse_changesets_emails(self):
        """
        Tests that parsing a changeset list with user emails returns a properly parsed list.
        """
        self.assertEqual(bitchangesets.parse_changesets(self.data), [{'raw_author': 'David Leonard'}])

    def test_parse_changesets_no_emails(self):
        """
        Tests that parsing a changeset list without user emails returns a properly parsed list.
        """
        self.assertEqual(bitchangesets.parse_changesets(self.data2), [{'raw_author': 'David Leonard'}])
