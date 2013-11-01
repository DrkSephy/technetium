"""
Test Technetium Bitbucket: bitstats
"""
import unittest
import technetium.bitbucket.bitstatistics

class BitstatsTest(unittest.TestCase):

	def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'

        # Private user repository
        self.priv_user = 'technetiumccny'
        self.priv_repo = 'technetium'

    # These tests might need to be mocked
	def test_get_diffstat_not_empty(self):
		"""
		Test that get changeset statistics 
		"""
		pass

	def test_get_diff_not_empty(self):
		"""
		Test that get diffs 
		"""
		pass				