"""
Test Technetium Bitbucket: bitmethods
"""
from mock import Mock, patch, MagicMock
import technetium.bitbucket.bitmethods as bitmethods
import unittest

class BitmethodsTests(unittest.TestCase):

    def setUp(self):
        self.user = 'technetiumccny'
        self.repo = 'technetium'
        self.issues_endpt = 'issues'
        self.endpoint = 'changesets'
        self.url_issues = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'

         # Set up for dictionary_sum()
        self.data = {}
        self.data2 = {}
        self.data3 = {'a':1, 'b':2}
        self.data4 = {'c':2, 'b':3}


    #######################################################
    # get_api_urls(user, repo, endpoint, start, limit=50) #
    #######################################################
    def test_get_api_urls(self):
        self.req_urls = ['https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/changesets?limit=50&start=50']
        self.start = 51
        self.limit = 50
        self.new_url = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/changesets?start=1&limit=1'

        self.assertEqual(bitmethods.get_api_urls(self.user, self.repo, self.endpoint, self.limit, self.start),
            self.req_urls)

    #########################################################   
    # make_req_url(user, repo, endpoint, limit=50, start=0) #
    #########################################################
    def test_make_req_url(self):
        """
        Tests that constructs URL returns correct API request url.
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50'
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
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt), match)

    def test_make_req_url_with_limit_and_start(self):
        """
        Tests that URL is created with limit and start parameters
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=50), match)

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


    @patch.object(bitmethods, 'make_req_url')
    @patch.object(bitmethods, 'send_bitbucket_request')
    def test_count(self, mock_send_bitbucket_request, mock_make_req_url):
        self.owner = 'DrkSephy'
        self.repo_slug = 'smw-koopa-krisis'
        self.auth_tokens = {}
        self.endpoint = 'changesets'

        # Mock count_url = make_req_url(owner, repo_slug, endpoint, 0)
        mock_make_req_url.return_value = MagicMock()
        # Mock auth tokens in response
        mock_auth_tokens = MagicMock(name='auth_tokens')
        # Mock entire response object (send_bitbucket_request)
        mock_send_bitbucket_request.return_value = {'count': 4}
        self.assertEqual(bitmethods.get_count(self.owner, self.repo_slug, self.auth_tokens, self.endpoint), 3)
        mock_send_bitbucket_request.return_value = False
        self.assertEqual(bitmethods.get_count(self.owner, self.repo_slug, self.auth_tokens, self.endpoint), 0)

    @patch.object(bitmethods, 'grequests')
    @patch.object(bitmethods, 'json')
    def test_send_async_bitbucket_requests(self, mock_grequests, mock_json):
        self.req_urls = ['https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/changesets/?start=5&limit=2']
        self.auth_tokens = {}
        self.json_list = [{
          "count": 693,
          "start": "5",
          "limit": 2,
          "changesets": [
            {
              "node": "982bb31ef6ea",
              "files": [
                {
                  "type": "modified",
                  "file": "lib/game/entities/player.js"
                },
                {
                  "type": "modified",
                  "file": "lib/game/levels/test.js"
                },
                {
                  "type": "modified",
                  "file": "lib/game/main.js"
                }
              ],
              "raw_author": "David Leonard <sephirothcloud1025@yahoo.com>",
              "utctimestamp": "2013-07-27 01:10:46+00:00",
              "author": "DrkSephy",
              "timestamp": "2013-07-27 03:10:46",
              "raw_node": "982bb31ef6ea9e0a071a59c6c38c900e2b9e78a6",
              "parents": [
                "db8e184555a2"
              ],
              "branch": "default",
              "message": "Player entity added",
              "revision": 5,
              "size": -1
            }
          ]
        }]
        mock_grequests.map.return_value = MagicMock()
        mock_grequests.response.content.return_value = MagicMock()
        mock_grequests.get.return_value = self.json_list
        self.assertEqual(bitmethods.send_async_bitbucket_requests(self.req_urls, self.auth_tokens), [])

    def test_package_context(self):
        self.subscriptions = {}
        self.assertEqual(bitmethods.package_context(self.subscriptions), 
            {'subscription_count': 0, 'subscriptions': {}})

    @patch.object(bitmethods, 'datetime')
    @patch.object(bitmethods, 'time')
    def test_to_unix_time(self, mock_datetime, mock_time):
        mock_datetime.return_value = ''
        mock_time.return_value = ''
        self.timestamp = ''
        self.assertEqual(bitmethods.to_unix_time(self.timestamp), 1000)


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

