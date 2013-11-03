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
        Tests send_bitbucket_request status_code != 200 returns {}
        """
        req_url = self.url_issues
        bitbucket_req = Mock()
        auth_tokens = {'oauth_token' : 'abc', "oauth_token_secret" : '123'}
        with patch('technetium.bitbucket.bitmethods.requests') as mock_requests:
            mock_requests.get.return_value = mock_response = Mock()
            mock_response.status_code = 201
            results = bitmethods.send_bitbucket_request(req_url, auth_tokens)
            self.assertEqual(results, {})


    # Tests For: transform_url()
    def test_transform_url_empty(self):
        """
        Tests that transform url on empty returns empty string
        """
        self.assertEqual(bitmethods.transform_url(''), '')

    def test_transform_url_issues(self):
        """
        Tests that transform url returns valid URL for issues resource
        """
        resource = "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/13"
        match = "https://bitbucket.org/DrkSephy/smw-koopa-krisis/issue/13"
        self.assertEqual(bitmethods.transform_url(resource), match)
