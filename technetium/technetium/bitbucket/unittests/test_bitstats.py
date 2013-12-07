"""
Test Technetium Bitbucket: bitstats
"""

import technetium.bitbucket.bitstats as bitstats
import unittest

class BitstatsTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'
        self.data = [{'author': 'Kevin Chan'}, {'author': 'Kevin Chan'}]
        self.data2 = [{'author': 'Kevin Chan'}, {'author': 'DrkSephy'}]
        self.data3 = {'DrkSephy': 29, 'Kevin Chan': 11}
        self.data4 = {'David Leonard': {'changesets': 1}}

    

    def test_commit_counter(self):
        """
        Tests that commit counter returns valid data for single user
        """

        pass
    def test_commit_counter_multiple_users(self):
        """
        Tests that commit counter returns valid data for multiple users
        """
        
        pass

    def test_commit_counter_empty(self):
        """
        Tests that an empty list returns an empty dictionary
        """
        self.assertEqual(bitstats.tally_changesets([]), {})

    def test_list_non_empty_users(self):
        """
        Tests that a non-empty dictionary returns a list of users.
        """
        self.assertEqual(bitstats.list_users(self.data3), ['DrkSephy', 'Kevin Chan'])
        

    def test_list_empty_users(self):
        """
        Tests that an empty dictionary returns an empty list of users.
        """

        self.assertEqual(bitstats.list_users({}), [])

    def test_list_non_empty_commits(self):
        """
        Tests that a non-empty dictionary returns a list of commits.
        """

        pass
        

    def test_list_empty_commits(self):
        """
        Tests that an empty dictionary returns an empty list of commits.
        """

        self.assertEqual(bitstats.list_data({}), [])

        pass

    def test_tally_issues(self):

        self.tally = {}
        self.issues = [{'status': 'new', 'opened_by': 'Albert Chieu', 'issue_id': 102, 'assigned': 'Jorge Yau', 
            'timestamp': '2013-12-06 05:07:11+00:00'}]
        self.assertEqual(bitstats.tally_issues(self.issues), {'Albert Chieu': {'issues_assigned': 0, 'issues_opened': 1, 'issues_completed': 0}, 'Jorge Yau': 
            {'issues_assigned': 1, 'issues_opened': 0, 'issues_completed': 0}})


