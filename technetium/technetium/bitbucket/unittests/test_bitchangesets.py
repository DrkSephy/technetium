"""
Test Technetium Bitbucket: bitchangesets
"""

from mock import Mock, patch
import unittest
import technetium.bitbucket.bitchangesets as bitchangesets
import technetium.bitbucket.bitmethods as bitmethods


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

    #################################################
    # iterate_all_changesets(req_urls, auth_tokens) #
    #################################################
    @patch.object(bitmethods,'send_async_bitbucket_requests')
    def test_iterate_all_changesets(self, mock_async):
        self.auth_tokens = {}
        self.req_urls = ['https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/changesets/?start=1&limit=1']
        self.parsed_changesets= []
        self.raw_changesets = [{
          "count": 569,
          "start": "1",
          "limit": 1,
          "changesets": [
            {
              "node": "51dbaae3ff56",
              "files": [
                {
                  "type": "added",
                  "file": "README.md"
                }
              ],
              "raw_author": "David Leonard <sephirothcloud1025@yahoo.com>",
              "utctimestamp": "2013-07-26 23:56:46+00:00",
              "author": "DrkSephy",
              "timestamp": "2013-07-27 01:56:46",
              "raw_node": "51dbaae3ff56392daab82e370b6a3fd5d089df59",
              "parents": [
                "e551c1f26bca"
              ],
              "branch": "default",
              "message": "Created: README.md",
              "revision": 1,
              "size": -1
            }
          ]
        }]
        mock_async.return_value = self.raw_changesets
        self.assertEqual(bitchangesets.iterate_all_changesets(self.req_urls, self.auth_tokens), 
          [{'timestamp': '2013-07-27 01:56:46', 'parsed_author': 'David Leonard'}])


    ##############################
    # parse_changeset(changeset) #
    ##############################
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
