"""
Test Technetium Bitbucket: bitfilter
"""
import unittest
import datetime
import technetium.bitbucket.bitfilter as bitfilter
 

class BitfilterTest(unittest.TestCase):

    def setUp(self):
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

        # global variables to filter issues by date created
        today = datetime.date.today()
        j_today = datetime.datetime.strftime(today,'%m-%d-%Y')
        self.today_issue = {'created':j_today}

        current_monday = today - datetime.timedelta(today.weekday())
        j_current_monday = datetime.datetime.strftime(current_monday,'%m-%d-%Y')
        self.current_monday_issue = {'created':j_current_monday}

        last_monday = current_monday - datetime.timedelta(7)
        j_last_monday = datetime.datetime.strftime(last_monday,'%m-%d-%Y')
        self.last_monday_issue = {'created':j_last_monday}

        first_day_of_month = datetime.date(day=1, month=today.month, year=today.year)
        last_day_prev_month = first_day_of_month - datetime.timedelta(days=1)
        j_last_day_prev_month = datetime.datetime.strftime(last_day_prev_month,'%m-%d-%Y')
        self.last_day_prev_month_issue = {'created':j_last_day_prev_month}

        last_year = today - datetime.timedelta(365)
        j_last_year = datetime.datetime.strftime(last_year,'%m-%d-%Y')
        self.last_year_issue = {'created':j_last_year}

        # test input for today
        self.date_created_issues_0 = [self.today_issue, self.last_monday_issue]

        # test input for today, this week, last week
        self.date_created_issues_1 = [self.today_issue, self.current_monday_issue, self.last_monday_issue]

        # test input for this month, last month
        self.date_created_issues_2 = [self.today_issue, self.last_day_prev_month_issue]

        # test input for this year, last year
        self.date_created_issues_3 = [self.today_issue, self.last_year_issue]

        # global variables to filter issues by user
        self.albert_issue = {'assignee':'Albert Chieu'}
        self.jorge_issue = {'assignee':'Jorge Yau'}
        self.david_issue = {'assignee':'David Leonard'}
        self.unassigned_issue = {'assignee':''}
        self.assignee_issues = [self.albert_issue, self.jorge_issue, self.david_issue, self.unassigned_issue]

        # global variables to filter changesets by user
        self.albert_changeset = {'author':'Albert Chieu'}
        self.jorge_changeset = {'author':'Jorge Yau'}
        self.david_changeset = {'author':'David Leonard'}
        self.author_changesets = [self.albert_changeset, self.jorge_changeset, self.david_changeset]

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

    def test_filter_issue_by_today(self):
        """
        Test to filter issues by today
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_0, 'today'), expected_result_issue)        

    def test_filter_issue_by_this_week(self):
        """
        Test to filter issues by this week
        """
        expected_result_issue = [self.today_issue, self.current_monday_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_1, 'this_week'), expected_result_issue)        

    def test_filter_issue_by_last_week(self):
        """
        Test to filter issues by last week
        """
        expected_result_issue = [self.last_monday_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_1, 'last_week'), expected_result_issue)        

    def test_filter_issue_by_this_month(self):
        """
        Test to filter issues by this month
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_2, 'this_month'), expected_result_issue)        

    def test_filter_issue_by_last_month(self):
        """
        Test to filter issues by last month
        """
        expected_result_issue = [self.last_day_prev_month_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_2, 'last_month'), expected_result_issue)        

    def test_filter_issue_by_this_year(self):
        """
        Test to filter issues by this year
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_3, 'this_year'), expected_result_issue)        

    def test_filter_issue_by_last_year(self):
        """
        Test to filter issues by last year
        """
        expected_result_issue = [self.last_year_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_3, 'last_year'), expected_result_issue)        

    def test_filter_issues_by_user_albert(self):
        """
        Test to filter issues by user 'Albert Chieu'
        """
        expected_result_issue = [self.albert_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues,'Albert Chieu'), expected_result_issue)
        
    def test_filter_issues_by_user_jorge(self):
        """
        Test to filter issues by user 'Jorge Yau'
        """
        expected_result_issue = [self.jorge_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'Jorge Yau'), expected_result_issue)        

    def test_filter_issues_by_user_david(self):
        """
        Test to filter issues by user 'David Leonard'
        """
        expected_result_issue = [self.david_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'David Leonard'), expected_result_issue)        

    def test_filter_issues_by_user_unassigned(self):
        """
        Test to filter issues by unassigned user
        """
        expected_result_issue = [self.unassigned_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'unassigned'), expected_result_issue)        

    def test_filter_changesets_by_user_albert(self):
        """
        Test to filter changesets by user 'Albert Chieu'
        """
        expected_result_changeset = [self.albert_changeset]
        self.assertEqual(bitfilter.filter_changesets_by_user(self.author_changesets, 'Albert Chieu'), expected_result_changeset)                

    def test_filter_changesets_by_user_jorge(self):
        """
        Test to filter changesets by user 'Jorge Yau'
        """
        expected_result_changeset = [self.jorge_changeset]
        self.assertEqual(bitfilter.filter_changesets_by_user(self.author_changesets, 'Jorge Yau'), expected_result_changeset)                

    def test_filter_changesets_by_user_david(self):
        """
        Test to filter changesets by user 'David Leonard'
        """
        expected_result_changeset = [self.david_changeset]
        self.assertEqual(bitfilter.filter_changesets_by_user(self.author_changesets, 'David Leonard'), expected_result_changeset)                

