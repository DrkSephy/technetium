"""
Test Technetium Bitbucket: bitfilter
"""
import unittest
import datetime
import technetium.bitbucket.bitfilter as bitfilter
 

class BitfilterTest(unittest.TestCase):

    def setUp(self):
        # global variable to filter issues
        self.all_parsed_issues = [{'status': 'On hold', 'issues_url': '#', 'title': 'Implement post new issue', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-09-2013', 'type': 'Task'}, {'status': 'New', 'issues_url': '#', 'title': 'Render the issue comments on the reports', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'New', 'issues_url': '#', 'title': 'Write a parser method and tally method for issue comments data', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'New', 'issues_url': '#', 'title': 'Create method needed for getting data for issue comments', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'New', 'issues_url': '#', 'title': 'Unit test for methods module', 'assignee_avatar': 'https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'David Leonard', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'Invalid', 'issues_url': '#', 'title': 'Functional test to get repositories', 'assignee_avatar': '', 'priority': 'Major', 'assignee': '', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'Invalid', 'issues_url': '#', 'title': 'Functional test to filter issues by type', 'assignee_avatar': '', 'priority': 'Major', 'assignee': '', 'date': '12-06-2013', 'type': 'Task'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Fix show more button for filters', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Albert Chieu', 'date': '12-06-2013', 'type': 'Bug'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Parse changeset is weird', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-04-2013', 'type': 'Bug'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'D3 bar graph for issue data', 'assignee_avatar': 'https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'David Leonard', 'date': '12-04-2013', 'type': 'Task'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Ajax to filter issues by status', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Albert Chieu', 'date': '12-05-2013', 'type': 'Task'}, {'status': 'On hold', 'issues_url': '#', 'title': 'Show detailed issue data in issue tracker', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-09-2013', 'type': 'Task'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Fix bug with repo having 1 commit', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-05-2013', 'type': 'Bug'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Fix report bugs', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-05-2013', 'type': 'Bug'}, {'status': 'Resolved', 'issues_url': '#', 'title': 'Ajax to filter issues by type', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'priority': 'Major', 'assignee': 'Jorge Yau', 'date': '12-05-2013', 'type': 'Task'}]

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
        self.today_issue = {'date':j_today}

        current_monday = today - datetime.timedelta(today.weekday())
        j_current_monday = datetime.datetime.strftime(current_monday,'%m-%d-%Y')
        self.current_monday_issue = {'date':j_current_monday}

        last_monday = current_monday - datetime.timedelta(7)
        j_last_monday = datetime.datetime.strftime(last_monday,'%m-%d-%Y')
        self.last_monday_issue = {'date':j_last_monday}

        first_day_of_month = datetime.date(day=1, month=today.month, year=today.year)
        last_day_prev_month = first_day_of_month - datetime.timedelta(days=1)
        j_last_day_prev_month = datetime.datetime.strftime(last_day_prev_month,'%m-%d-%Y')
        self.last_day_prev_month_issue = {'date':j_last_day_prev_month}

        last_year = today - datetime.timedelta(365)
        j_last_year = datetime.datetime.strftime(last_year,'%m-%d-%Y')
        self.last_year_issue = {'date':j_last_year}

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


    def test_filter_issues_by_type(self):
        """
        Test to filter issues by type
        """
        expected_result_issue = [{'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Fix show more button for filters', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Parse changeset is weird', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-04-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Fix bug with repo having 1 commit', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-05-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Fix report bugs', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-05-2013', 'priority': 'Major'}]
        self.assertEqual(bitfilter.filter_issues({'type':'bug'}, self.all_parsed_issues), expected_result_issue)

    
    def test_filter_issues_by_priority(self):
        """
        Test to filter issues by priority
        """
        expected_result_issue = [{'status': 'On hold', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Implement post new issue', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-09-2013', 'priority': 'Major'}, {'status': 'New', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Render the issue comments on the reports', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'New', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Write a parser method and tally method for issue comments data', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'New', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Create method needed for getting data for issue comments', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'New', 'issues_url': '#', 'assignee': 'David Leonard', 'title': 'Unit test for methods module', 'assignee_avatar': 'https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Invalid', 'issues_url': '#', 'assignee': '', 'title': 'Functional test to get repositories', 'assignee_avatar': '', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Invalid', 'issues_url': '#', 'assignee': '', 'title': 'Functional test to filter issues by type', 'assignee_avatar': '', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Fix show more button for filters', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Parse changeset is weird', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-04-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'David Leonard', 'title': 'D3 bar graph for issue data', 'assignee_avatar': 'https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-04-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Ajax to filter issues by status', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-05-2013', 'priority': 'Major'}, {'status': 'On hold', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Show detailed issue data in issue tracker', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-09-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Fix bug with repo having 1 commit', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-05-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Fix report bugs', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-05-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Jorge Yau', 'title': 'Ajax to filter issues by type', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-05-2013', 'priority': 'Major'}]
        self.assertEqual(bitfilter.filter_issues({'priority':'major'}, self.all_parsed_issues), expected_result_issue)


    def test_filter_issues_by_status(self):
        """
        Test to filter issues by status
        """
        expected_result_issue = [{'status': 'Invalid', 'issues_url': '#', 'assignee': '', 'title': 'Functional test to get repositories', 'assignee_avatar': '', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Invalid', 'issues_url': '#', 'assignee': '', 'title': 'Functional test to filter issues by type', 'assignee_avatar': '', 'type': 'Task', 'date': '12-06-2013', 'priority': 'Major'}]
        self.assertEqual(bitfilter.filter_issues({'status':'invalid'}, self.all_parsed_issues), expected_result_issue)


    def test_filter_issues_by_assignee(self):
        """
        Test to filter issues by assignee
        """
        expected_result_issue = [{'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Fix show more button for filters', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Bug', 'date': '12-06-2013', 'priority': 'Major'}, {'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Ajax to filter issues by status', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-05-2013', 'priority': 'Major'}]
        self.assertEqual(bitfilter.filter_issues({'assignee':'Albert Chieu'}, self.all_parsed_issues), expected_result_issue)        


    def test_filter_issues_by_combination(self):
        """
        Test filter issues by combination of type, priority, status, assignee, and date
        """
        expected_result_issue = [{'status': 'Resolved', 'issues_url': '#', 'assignee': 'Albert Chieu', 'title': 'Ajax to filter issues by status', 'assignee_avatar': 'https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F386386f55761%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32', 'type': 'Task', 'date': '12-05-2013', 'priority': 'Major'}]
        self.assertEqual(bitfilter.filter_issues({'type':'task', 'priority':'major', 'status':'resolved', 'assignee':'Albert Chieu'}, self.all_parsed_issues), expected_result_issue)        


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
        Test to filter issue date by today
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_0, 'today'), expected_result_issue)        

    
    def test_filter_issue_by_this_week(self):
        """
        Test to filter issue date by this week
        """
        expected_result_issue = [self.today_issue, self.current_monday_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_1, 'this_week'), expected_result_issue)        

    
    def test_filter_issue_by_last_week(self):
        """
        Test to filter issue date by last week
        """
        expected_result_issue = [self.last_monday_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_1, 'last_week'), expected_result_issue)        

    
    def test_filter_issue_by_this_month(self):
        """
        Test to filter issue date by this month
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_2, 'this_month'), expected_result_issue)        

    
    def test_filter_issue_by_last_month(self):
        """
        Test to filter issue date by last month
        """
        expected_result_issue = [self.last_day_prev_month_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_2, 'last_month'), expected_result_issue)        


    def test_filter_issue_by_this_year(self):
        """
        Test to filter issue date by this year
        """
        expected_result_issue = [self.today_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_3, 'this_year'), expected_result_issue)        


    def test_filter_issue_by_last_year(self):
        """
        Test to filter issue date by last year
        """
        expected_result_issue = [self.last_year_issue]
        self.assertEqual(bitfilter.filter_issues_by_date(self.date_created_issues_3, 'last_year'), expected_result_issue)        


    def test_filter_issues_by_user_albert(self):
        """
        Test to filter issue assignee by user 'Albert Chieu'
        """
        expected_result_issue = [self.albert_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues,'Albert Chieu'), expected_result_issue)
        

    def test_filter_issues_by_user_jorge(self):
        """
        Test to filter issue assignee by user 'Jorge Yau'
        """
        expected_result_issue = [self.jorge_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'Jorge Yau'), expected_result_issue)        


    def test_filter_issues_by_user_david(self):
        """
        Test to filter issue assignee by user 'David Leonard'
        """
        expected_result_issue = [self.david_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'David Leonard'), expected_result_issue)        


    def test_filter_issues_by_user_unassigned(self):
        """
        Test to filter issue assignee by unassigned user
        """
        expected_result_issue = [self.unassigned_issue]
        self.assertEqual(bitfilter.filter_issues_by_user(self.assignee_issues, 'unassigned'), expected_result_issue)        

