"""
Test Technetium Bitbucket: bitissues
"""
from mock import Mock, patch
import technetium.bitbucket.bitissues as bitissues
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
            'utc_created_on' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            }}]


        # JSON returned from bitbucket with responsible
        self.dummy_issues_assignee = [{
            'title' : 'issue title',
            'status' : 'new',
            'priority' : 'major',
            'utc_created_on' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            },

            'responsible' : {
                'display_name' : 'accountname',
                'avatar' : 'http://mygravatar.com',
            }}]


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
            self.dummy_issues)[0]['assignee'], '')


    def test_parse_issues_with_assignee(self):
        """
        Tests that parses issues with assignee returns correctly
        """
        self.assertEqual(bitissues.parse_issues(
            self.dummy_issues_assignee)[0]['assignee'], 'accountname')


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


    ####################################
    # add_html_issue_rows(parsed_data) #
    ####################################
    def test_add_html_issue_rows(self):
        """
        Tests that bitissues add html returns proper html
        """
        pass
