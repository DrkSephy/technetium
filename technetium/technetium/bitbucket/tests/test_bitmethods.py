"""
Test Technetium Bitbucket: bitmethods
"""
import unittest
import bitmethods

class BitmethodsTests(unittest.TestCase):

    def setUp(self):
        self.user = 'technetiumccny'
        self.repo = 'technetium'
        self.issues_endpt = 'issues'

    def test_make_req_url(self):
        """
        Tests that constructs URL returns correct API request url.
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt), match)

    def test_make_req_url_with_limit(self):
        """
        Tests that URL has proper limit parameter
        """
        limit = 20
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, 20), match)

    def test_make_req_url_with_start(self):
        """
        Tests that URL has proper start parameter
        """
        start = 20
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, start=20), match)
