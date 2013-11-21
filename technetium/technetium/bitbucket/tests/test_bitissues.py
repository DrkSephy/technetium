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


    def test_parse_all_issues_empty(self):
        """
        Tests that parse all issues returns blank properly
        """
        self.assertEqual(bitissues.parse_all_issues([]), [])


    def test_attach_meta_empty(self):
        """
        Tests that bitissues attach meta returns blank list
        """
        self.assertEqual(bitissues.attach_meta([], []), [])
