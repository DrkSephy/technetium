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
        self.auth_tokens = {}
        self.data3 = { "count": 532, "start": "0", "limit": 0, "changesets": []}
        self.changeset = {
              "raw_author": "David Leonard <sephirothcloud1025@yahoo.com>",
              "timestamp": "2013-07-27 01:56:46",
        }
        self.changeset2 = {
              "raw_author": "David Leonard",
              "timestamp": "2013-07-27 01:56:46",
        }
        

    def test_get_parse_not_empty(self):
        """
        Tests that parsing changesets returns a non-empty list.
        """
        
        self.assertEqual(bitchangesets.parse_changeset(self.changeset), {'timestamp': '2013-07-27 01:56:46', 'parsed_author': 'David Leonard'}) 

    def test_parse_changesets_emails(self):
        """
        Tests that parsing a changeset list with user emails returns a properly parsed list.
        """
        
        self.assertEqual(bitchangesets.parse_changeset(self.changeset), {'timestamp': '2013-07-27 01:56:46', 'parsed_author': 'David Leonard'}) 

    def test_parse_changesets_no_emails(self):
        """
        Tests that parsing a changeset list without user emails returns a properly parsed list.
        """
        
        self.assertEqual(bitchangesets.parse_changeset(self.changeset2), {'timestamp': '2013-07-27 01:56:46', 'parsed_author': 'David Leonard'}) 
