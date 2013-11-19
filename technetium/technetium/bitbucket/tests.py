"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase


class BitauthTest(TestCase):
    pass


class BitissuesTest(TestCase):
    def test_get_issues(self):
        """
        Tests that our API call to the `repositories`
        endpoint returns JSON data.
        """
        pass

    def test_parse_issues(self):
        """
        Tests that on JSON input, outputs properly
        stripped/formatted JSON data.
        """
        pass


class BitchangesetsTest(TestCase):
    def test_get_changesets(self):
        """
        Tests that our API call to the `repositories`
        endpoint returns JSON data.
        """
        pass

    def test_parse_changesets(self):
        """
        Tests that on JSON input, outputs properly
        stripped/formatted JSON data.
        """
        pass


class BitmanagerTest(TestCase):
    def test_add_repository(self):
        """
        Tests that a repository is added to the endpoint.
        """

        pass

    def test_remove_repository(self):
        """
        Tests that a repository is removed from the endpoint.
        """

        pass

    def test_remove_all_repositories(self):
        """
        Tests that all repositories are removed from the list.
        """

        pass

class BitmethodsTest(TestCase):

    def test_get_repositories(self):
        """
        Tests that we get a list of repositories that a user
        has access to.
        """
        pass


class BitdashboardTest(TestCase):
    pass
    

class BitfilterTest(TestCase):
    def test_filter_issues_by_type(self):
        """
        Tests filtering of issues by type.
        """

        pass

    def test_filter_issues_by_priority(self):
        """
        Tests filtering of issues by priority.
        """

        pass

    def test_filter_issues_by_user(self):
        """
        Tests filtering of issues by user.
        """

        pass

    def test_filter_issues_by_date(self):
        """
        Tests filtering of issues by date.
        """

        pass

    def test_filter_issues_by_status(self):
        """
        Tests filtering of issues by status.
        """

        pass

    def test_filter_changesets_by_date(self):
        """
        Tests filtering changesets by date.
        """

        pass

    def test_filter_changesets_by_user(self):
        """
        Tests filtering changesets by user.
        """

        pass
