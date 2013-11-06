"""
Test Technetium Bitbucket: bitfilter
"""
import unittest
import technetium.bitbucket.bitfilter as bitfilter
 

class BitfilterTest(unittest.TestCase):

    def setUp(self):
        """
        setup to define global variables for testing
        """
        self.bug_issue = {'type':'bug'}
        self.enhancement_issue = {'type':'enhancement'}
        self.proposal_issue = {'type':'proposal'}
        self.task_issue= {'type':'task'}

        self.type_issues = [self.bug_issue, self.enhancement_issue, self.proposal_issue, self.task_issue]


        self.new_issue = {'status':'new'}
        self.open_issue = {'status':'open'}
        self.resolved_issue = {'status':'resolved'}
        self.duplicate_issue = {'status':'duplicate'}
        self.invalid_issue = {'status':'invalid'}
        self.on_hold_issue = {'status':'on hold'}
        self.wontfix_issue = {'status':'wontfix'}

        self.status_issues = [self.new_issue, self.open_issue, self.resolved_issue, self.duplicate_issue, self.invalid_issue, self.on_hold_issue, self.wontfix_issue]


    def test_filter_issues(self):
    	"""
    	Test to filter issues
    	"""
    	pass

    def test_filter_issue_type_by_bug(self):
        """
        Test to filter issue type by bug
        """
        expected_result_issue = [self.bug_issue]
        self.assertEqual(bitfilter.filter_issues_by_type(self.type_issues, 'bug'), expected_result_issue)

    def test_filter_issue_type_by_enhancement(self):
        """
        Test to filter issue type by enhancement
        """
        expected_result_issue = [self.enhancement_issue]
        self.assertEqual(bitfilter.filter_issues_by_type(self.type_issues, 'enhancement'), expected_result_issue)

    def test_filter_issue_type_by_proposal(self):
        """
        Test to filter issue type by proposal
        """
        expected_result_issue = [self.proposal_issue]
        self.assertEqual(bitfilter.filter_issues_by_type(self.type_issues, 'proposal'), expected_result_issue)

    def test_filter_issue_type_by_task(self):
        """
        Test to filter issue type by task
        """
        expected_result_issue = [self.task_issue]
        self.assertEqual(bitfilter.filter_issues_by_type(self.type_issues, 'task'), expected_result_issue)


    def test_filter_changesets(self):
    	"""
    	Test to filter changesets
    	"""
    	pass


    def test_filter_changesets_by_user(self):
        """
        Test to get individual changeset
        """
        pass