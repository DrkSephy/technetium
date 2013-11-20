"""
Test Technetium Bitbucket: bitmethods
"""
from mock import Mock, patch
import technetium.bitbucket.bitmethods as bitmethods
import unittest

class BitmethodsTests(unittest.TestCase):

    def setUp(self):
        self.user = 'technetiumccny'
        self.repo = 'technetium'
        self.issues_endpt = 'issues'
        self.url_issues = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'

         # Set up for dictionary_sum()
        self.data = {}
        self.data2 = {}
        self.data3 = {'a':1, 'b':2}
        self.data4 = {'c':2, 'b':3}

    # Tests For: make_req_url()
    def test_make_req_url(self):
        """
        Tests that constructs URL returns correct API request url.
        """
        match = self.url_issues
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt), match)

    def test_make_req_url_with_limit(self):
        """
        Tests that URL has proper limit parameter
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=20), match)

    def test_make_req_url_with_start(self):
        """
        Tests that URL has proper start parameter
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?start=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, start=20), match)

    def test_make_req_url_with_limit_and_start(self):
        """
        Tests that URL is created with limit and start parameters
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20&start=5'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=20, start=5), match)

    def test_make_req_url_max_limit_50(self):
        """
        Tests that any generated URL has a max limit of 50
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=9001), match)


    # Tests For: send_bitbucket_request()
    def test_send_bitbucket_request_not_200(self):
        """
        Tests send_bitbucket_request status_code not 200 returns empty dict
        """
        req_url = self.url_issues
        bitbucket_req = Mock()
        auth_tokens = {'oauth_token' : 'Fake', "oauth_token_secret" : 'Invalid'}
        match = {}
        with patch('technetium.bitbucket.bitmethods.requests') as mock_requests:
            mock_requests.get.return_value = mock_response = Mock()
            mock_response.status_code = 201
            results = bitmethods.send_bitbucket_request(req_url, auth_tokens)
            self.assertEqual(results, match)

    def test_send_bitbucket_request_200(self):
        """
        Tests send_bitbucket_request with status 200 returns dictionary
        """
        req_url = self.url_issues
        bitbucket_req = Mock()
        auth_tokens = {'oauth_token' : 'Real', "oauth_token_secret" : 'Valid'}
        match = {"count" : 49, "issues" : [{"status": "new"}]}

        # Mock string json in request.content matches expected match JSON
        with patch('technetium.bitbucket.bitmethods.requests') as mock_requests:
            mock_requests.get.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = '{"count" : 49, "issues" : [{"status": "new"}]}'
            results = bitmethods.send_bitbucket_request(req_url, auth_tokens)
            self.assertEqual(results, match)


    # Tests For: format_timestamp()
    def test_format_timestamp_empty(self):
        """
        Tests that empty timestamp returns empty string
        """
        self.assertEqual(bitmethods.format_timestamp(''), '')


    def test_format_timestamp_valid(self):
        """
        Tests that valid time stamp is returned in correct format
        """
        timestamp = '2013-10-29 18:36:11+00:00'
        match = '10-29-2013'
        self.assertEqual(bitmethods.format_timestamp(timestamp), match)

    # Tests for: dictionary_sum()
    def test_dictionary_sum_empty(self):
        """
        Tests that summing two empty dictionaries returns an empty dictionary.
        """

        self.assertEqual(bitmethods.dictionary_sum(self.data, self.data2), {})

    def test_dictionary_sum(self):
        """
        Tests that summing two non-empty dictionaries returns the proper result.
        """

        self.assertEqual(bitmethods.dictionary_sum(self.data3, self.data4), {'a': 1, 'c': 2, 'b': 5})

