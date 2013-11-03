"""
Functional tests for changesets module.
"""

import simplejson as json
import requests
import unittest
import technetium.bitbucket.bitchangesets as changesets

class BitchangesetsTests(unittest.TestCase):
    
    def test_get_changesets(self):
        """
        Tests that a public repository query has a 200 status code.
        """
        req_url = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/?limit=2')
        self.assertEqual(req_url.status_code, 200)

