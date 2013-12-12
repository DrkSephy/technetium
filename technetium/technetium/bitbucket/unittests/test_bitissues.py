"""
Test Technetium Bitbucket: bitissues
"""
from mock import Mock, patch, MagicMock
import technetium.bitbucket.bitissues as bitissues
import technetium.bitbucket.bitmethods as bitmethods
import unittest


class BitissuesTests(unittest.TestCase):

    def setUp(self):
        """
        Setup example JSON data returned from bitbucket
        """

        # JSON returned from bitbucket with no assignee
        self.dummy_issues = [{
            'title' : 'issue title',
            'status' : 'new',
            'priority' : 'major',
            'utc_last_updated' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            }}]

        self.dummy_issues2 = [{
            'title' : 'issue title',
            "content": "???",
            'status' : 'new',
            'priority' : 'major',
            'local_id': 1,
            'reported_by': {
              'display_name': 'David Leonard'
            },
            'utc_last_updated' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            }}]



        # JSON returned from bitbucket with responsible
        self.dummy_issues_assignee = [{
            'title' : 'issue title',
            'status' : 'new',
            'priority' : 'major',
            'utc_last_updated' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            },

            'responsible' : {
                'display_name' : 'accountname',
                'avatar' : 'http://mygravatar.com',
            }}]

        self.user = 'DrkSephy'
        self.repo = 'smw-koopa-krisis'
        self.endpoint = 'issues'

    def test_parse_issues(self):
        self.data = {}
        self.assertEqual(bitissues.parse_issues(self.dummy_issues2), [{'status': 'New', 'priority': 'Major', 'title': 'Issue title', 'assignee_avatar': '', 'reporter': 'David Leonard', 'content': '???', 'assignee': '', 'issue_id': 1, 'date': '', 'type': 'Task'}])
    ########################################################
    # get_issues_urls(user, repo, endpoint, end, limit=50) #
    ########################################################
    def test_get_issues_urls_empty(self):
        """
        Tests that we can get urls to send to the issue endpoint.
        """
        self.req_urls = []
        self.end = 0
        self.assertEqual(bitissues.get_issues_urls(self.user, self.repo, self.endpoint,
            self.end, limit=50), self.req_urls )
        
    def test_get_issues_urls_not_empty(self):
        self.req_urls = ['https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues?limit=50&start=0']
        self.count = 0
        self.limit = 50
        self.end = 50

        self.assertEqual(bitissues.get_issues_urls(self.user, self.repo, self.endpoint,
            self.end, self.limit), self.req_urls)

    #################################
    # parse_all_issues(repo_issues) #
    #################################
    def test_parse_all_issues_empty(self):
        """
        Tests that parse all issues returns blank properly
        """
        self.assertEqual(bitissues.parse_all_issues([]), [])

    def test_parse_all_issues(self):
        """
        Tests that parse all issues returns len of correct size
        """
        self.assertEqual(len(bitissues.parse_all_issues(
            self.dummy_issues)), 1)


    ########################
    # parse_issues(issues) #
    ########################
    def test_parse_issues_empty(self):
        """
        Tests that parse issues on empty dict returns empty list
        """
        self.assertEqual(bitissues.parse_issues({}), [])


    def test_parse_issues_no_assignee(self):
        """
        Tests that parses issues with no assignee returns blank
        """
        self.assertEqual(bitissues.parse_issues(
            self.dummy_issues2), [{'status': 'New', 'priority': 'Major', 'title': 'Issue title', 'assignee_avatar': '', 'reporter': 'David Leonard', 'content': '???', 'assignee': '', 'issue_id': 1, 'date': '', 'type': 'Task'}])


    def test_parse_issues_with_assignee(self):
        """
        Tests that parses issues with assignee returns correctly
        """
        self.assertEqual(bitissues.parse_issues(
            self.dummy_issues2), [{'status': 'New', 'priority': 'Major', 'title': 'Issue title', 'assignee_avatar': '', 'reporter': 'David Leonard', 'content': '???', 'assignee': '', 'issue_id': 1, 'date': '', 'type': 'Task'}])


    ##########################################
    # attach_meta(subscription, repo_issues) #
    ##########################################
    def test_attach_meta_empty(self):
        """
        Tests that bitissues attach_meta returns blank list
        """
        self.assertEqual(bitissues.attach_meta([], []), [])

    def test_attach_meta_subscription(self):
        """
        Tests bitissues attach_meta with subscription
        """
        mock_subscription = Mock()
        mock_subscription.repository = 'Technetium'
        mock_subscription.owner = 'technetiumccny'
        mock_subscription.slug_url = 'http://somebitbucketlink.com'
        list_subscriptions = [mock_subscription]
        self.assertEqual(
            len(bitissues.attach_meta(
                list_subscriptions, self.dummy_issues)), 1)


    def test_get_issue_comments_urls(self):
        self.repo_owner = 'DrkSephy'
        self.repo_slug = 'smw-koopa-krisis'
        self.issues = [{'status': 'new', 'opened_by': 'Jorge Yau', 'issue_id': 104, 'assigned': None, 'timestamp': '2013-12-11 02:54:09+00:00'}, {'status': 'resolved', 'opened_by': 'Albert Chieu', 'issue_id': 2, 'assigned': None, 'timestamp': '2013-10-24 22:06:34+00:00'}, {'status': 'resolved', 'opened_by': 'Jorge Yau', 'issue_id': 1, 'assigned': None, 'timestamp': '2013-11-01 16:07:09+00:00'}]
        self.assertEqual(bitissues.get_issue_comments_urls(self.issues, 
            self.repo_owner, self.repo_slug), ['https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/104/comments/', 'https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/2/comments/', 'https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/1/comments/'])

    ####################################
    # add_html_issue_rows(parsed_data) #
    ####################################
    @patch.object(bitissues, 'render_to_string')
    def test_add_html_issue_rows(self, mock_render_to_string):
        """
        Tests that bitissues add html returns proper html
        """
        self.html = 'includes/issues/issues-list.html'
        self.data = {}
        mock_render_to_string.return_value = {}
        self.assertEqual(bitissues.make_html_issue_rows(self.data), {})
        

    @patch.object(bitmethods, 'make_req_url')
    @patch.object(bitmethods, 'send_bitbucket_request')
    @patch.object(bitissues,  'parse_issues')
    @patch.object(bitissues,  'make_html_issue_rows')
    def test_ajax_process_issues(self, mock_send_bitbucket_request, mock_make_req_url,
        mock_parse_issues, mock_make_html_issue_rows):
        """
        Tests that ajax works on issues.
        """
        self.repo_owner = 'DrkSephy'
        self.repo_slug = 'smw-koopa-krisis'
        self.count = 1
        self.queries = {}
        self.auth_tokens = {}

        mock_make_req_url.return_value = MagicMock()
        mock_send_bitbucket_request.return_value = [{}]
        mock_parse_issues.return_value = MagicMock() 
        mock_make_html_issue_rows.return_value = ''

        self.assertEqual(bitissues.ajax_process_issues(self.auth_tokens, 
            self.repo_owner, self.repo_slug, self.count, self.queries), [{}])
