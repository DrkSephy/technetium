"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class BitauthTest(TestCase):
	pass


class BitissuesTest(TestCase):
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
    def test_add_repository():
        """
        Tests that a repository is added to the endpoint.
        """

        pass

    def test_remove_repository():
        """
        Tests that a repository is removed from the endpoint.
        """

        pass
	