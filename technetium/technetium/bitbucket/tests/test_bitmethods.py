"""
Test Technetium Bitbucket: bitmethods
"""
import unittest
import technetium.bitbucket.bitmethods as bitmethods

class BitmethodsTests(unittest.TestCase):

    def setUp(self):
        self.user = 'technetiumccny'
        self.repo = 'technetium'
        self.issues_endpt = 'issues'


    # Series of tests for make request URL
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
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=20), match)

    def test_make_req_url_with_start(self):
        """
        Tests that URL has proper start parameter
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?start=20'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, start=20), match)

    def test_make_req_url_with_limit_and_start(self):
        """
        Tests that URL is created with limit and start parameters
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=20&start=5'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=20, start=5), match)

    def test_make_req_url_max_limit_50(self):
        """
        Tests that any generated URL has a max limit of 50
        """
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50'
        self.assertEqual(bitmethods.make_req_url
            (self.user, self.repo, self.issues_endpt, limit=9001), match)
