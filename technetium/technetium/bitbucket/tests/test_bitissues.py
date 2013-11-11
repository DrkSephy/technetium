"""
Test Technetium Bitbucket: bitissues
"""
from mock import Mock, patch
import technetium.bitbucket.bitissues as bitissues
import unittest


class BitissuesTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'

        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'

        self.unparsed_1 = """
        [{'raw_issues': {'count': 0,
         'filter': {},
         'search': None,
         'issues': []},
         'repo_meta': {'repo_owner': u'DrkSephy',
         'req_url': u'bitbucket.url,
         'repo_name': u'smw-koopa-krisis'}}]
        """

        self.unparsed_2 = """
        [{'raw_issues': {'count': 13,
         'filter': {},
         'search': None,
         'issues': [{'status': 'resolved',
         'content': "Description",
         'title': 'Title',
         'reported_by': {'username': 'user',
         'first_name': 'Kevin',
         'last_name': 'Chan',
         'display_name': 'Kevin Chan',
         'is_team': False,
         'avatar': 'gravatar.com',
         'resource_uri': '/1.0/users/user'},
         'utc_last_updated': '2013-10-11 01:53:43+00:00',
         'priority': 'major',
         'created_on': '2013-10-10T03:57:14.888',
         'local_id': 13,
         'is_spam': False,
         'utc_created_on': '2013-10-10 01:57:14+00:00',
         'resource_uri': 'resource.url',
         'metadata': {'kind': 'proposal',
         'version': None,
         'component': None,
         'milestone': None}}]},
         'repo_meta': {'repo_owner': u'DrkSephy',
         'req_url': u'bitbucket.url,
         'repo_name': u'smw-koopa-krisis'}}]
        """

    # These tests might need to be mocked
    def test_get_issues_from_subscribed_empty(self):
        """
        Tests that get issues from subscribed empty repo_data
        """
        with patch('technetium.bitbucket.bitissues.bitmethods') as mock_req:
            mock_req.get.return_value = []
            self.assertEqual(bitissues.get_issues_from_subscribed([],None), [])

    def test_parse_issues_empty():
        """
        Tests that empty parse issue returns list of empty issues
        """
        self.assertEqual(bitissues.parse_issues([]), [])

    def test_parse_issues(self):
        """
        Tests that parse issues returns list of proper size
        """
        self.assertTrue(bitissues.parse_issues(self.unparsed_2))

