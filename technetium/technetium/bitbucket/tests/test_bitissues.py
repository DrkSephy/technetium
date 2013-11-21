"""
Test Technetium Bitbucket: bitissues
"""
from mock import Mock, patch
import technetium.bitbucket.bitissues as bitissues
import unittest


class BitissuesTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'

        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'

    def test_parse_issues_empty(self):
        """
        Tests that parse issues on empty dict returns empty list
        """
        self.assertEqual(bitissues.parse_issues({}), [])

    def test_parse_all_issues_empty(self):
        """
        Tests that parse all issues returns blank properly
        """
        self.assertEqual(bitissues.parse_all_issues([]), [])

    def test_attach_meta_empty(self):
        """
        Tests that bitissues attach meta returns blank list
        """
        self.assertEqual(bitissues.attach_meta([], []), [])
