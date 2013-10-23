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


class BitmanagerTest(TestCase):
    pass
	