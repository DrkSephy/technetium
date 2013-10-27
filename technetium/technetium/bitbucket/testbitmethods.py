"""
Test Technetium Bitbucket: bitmethods
Running unit tests
"""
import unittest
import bitmethods

class BitmethodsTests(unittest.TestCase):

    def test_make_req_url(self):
        """
        Tests that constructs URL returns correct API request url.
        """
        user = 'technetiumccny'
        repo = 'technetium'
        endpt = 'issues'
        match = 'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues'
        self.assertEqual(bitmethods.make_req_url(user, repo, endpt), match)


if __name__ == '__main__':
    # Run unittests
    unittest.main()
