"""
Test Technetium Bitbucket: bitfilter
"""
import unittest
import requests
import technetium.bitbucket.bitfilter as bitfilter
 

class BitfilterTest(unittest.TestCase):

    def setUp(self):
        # global variable for filtering
        self.request = requests.request

        # global variables to filter issues by type
        self.bug_issue = {'type':'bug'}
        self.enhancement_issue = {'type':'enhancement'}
        self.proposal_issue = {'type':'proposal'}
        self.task_issue= {'type':'task'}
        self.type_issues = [self.bug_issue, self.enhancement_issue, self.proposal_issue, self.task_issue]

        # global variables to filter issues by status
        self.new_issue = {'status':'new'}
        self.open_issue = {'status':'open'}
        self.resolved_issue = {'status':'resolved'}
        self.duplicate_issue = {'status':'duplicate'}
        self.invalid_issue = {'status':'invalid'}
        self.on_hold_issue = {'status':'on hold'}
        self.wontfix_issue = {'status':'wontfix'}
        self.status_issues = [self.new_issue, self.open_issue, self.resolved_issue, self.duplicate_issue, self.invalid_issue, self.on_hold_issue, self.wontfix_issue]

        # global variables to filter issues by priority
        self.major_issue = {'priority':'major'}
        self.trivial_issue = {'priority':'trivial'}
        self.minor_issue = {'priority':'minor'}
        self.critical_issue = {'priority':'critical'}
        self.blocker_issue = {'priority':'blocker'}
        self.priority_issues = [self.major_issue, self.trivial_issue, self.minor_issue, self.critical_issue, self.blocker_issue]



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

    def test_filter_issue_status_by_new(self):
        """
        Test to filter issue status by new
        """
        expected_result_issue = [self.new_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'new'), expected_result_issue)

    def test_filter_issue_status_by_open(self):
        """
        Test to filter issue status by open
        """
        expected_result_issue = [self.open_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'open'), expected_result_issue)

    def test_filter_issue_status_by_resolved(self):
        """
        Test to filter issue status by resolved
        """
        expected_result_issue = [self.resolved_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'resolved'), expected_result_issue)

    def test_filter_issue_status_by_duplicate(self):
        """
        Test to filter issue status by duplicate
        """
        expected_result_issue = [self.duplicate_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'duplicate'), expected_result_issue)

    def test_filter_issue_status_by_invalid(self):
        """
        Test to filter issue status by invalid
        """
        expected_result_issue = [self.invalid_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'invalid'), expected_result_issue)

    def test_filter_issue_status_by_on_hold(self):
        """
        Test to filter issue status by on hold
        """
        expected_result_issue = [self.on_hold_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'on hold'), expected_result_issue)

    def test_filter_issue_status_by_wontfix(self):
        """
        Test to filter issue status by wontfix
        """
        expected_result_issue = [self.wontfix_issue]
        self.assertEqual(bitfilter.filter_issues_by_status(self.status_issues, 'wontfix'), expected_result_issue)

    def test_filter_issue_priority_by_major(self):
        """
        Test to filter issue priority by major
        """
        expected_result_issue = [self.major_issue]
        self.assertEqual(bitfilter.filter_issues_by_priority(self.priority_issues, 'major'), expected_result_issue)

    def test_filter_issue_priority_by_trivial(self):
        """
        Test to filter issue priority by trivial
        """
        expected_result_issue = [self.trivial_issue]
        self.assertEqual(bitfilter.filter_issues_by_priority(self.priority_issues, 'trivial'), expected_result_issue)

    def test_filter_issue_priority_by_minor(self):
        """
        Test to filter issue priority by minor
        """
        expected_result_issue = [self.minor_issue]
        self.assertEqual(bitfilter.filter_issues_by_priority(self.priority_issues, 'minor'), expected_result_issue)

    def test_filter_issue_priority_by_critical(self):
        """
        Test to filter issue priority by critical
        """
        expected_result_issue = [self.critical_issue]
        self.assertEqual(bitfilter.filter_issues_by_priority(self.priority_issues, 'critical'), expected_result_issue)

    def test_filter_issue_priority_by_blocker(self):
        """
        Test to filter issue priority by blocker
        """
        expected_result_issue = [self.blocker_issue]
        self.assertEqual(bitfilter.filter_issues_by_priority(self.priority_issues, 'blocker'), expected_result_issue)

    def test_filter_issue_date_by_today(self):
        """
        Test to filter issue date by today
        """
        pass

    def test_filter_issue_date_by_this_week(self):
        """
        Test to filter issue date by this week
        """
        pass

    def test_filter_issue_date_by_last_week(self):
        """
        Test to filter issue date by last week
        """
        pass

    def test_filter_issue_date_by_this_month(self):
        """
        Test to filter issue date by this month
        """
        pass

    def test_filter_issue_date_by_last_month(self):
        """
        Test to filter issue date by last month
        """
        pass

    def test_filter_issue_date_by_this_year(self):
        """
        Test to filter issue date by this year
        """
        pass

    def test_filter_issue_date_by_last_year(self):
        """
        Test to filter issue date by last year
        """
        pass

    def test_filter_changesets(self):
    	"""
    	Test to filter changesets
    	"""
    	pass


    def test_filter_changesets_by_user(self):
        """
        Test to filter changesets by user
        """
        pass