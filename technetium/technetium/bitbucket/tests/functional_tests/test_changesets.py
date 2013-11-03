"""
Functional tests for changesets module.
"""

import simplejson as json
import requests
import unittest
import technetium.bitbucket.bitchangesets as changesets

class BitchangesetsTests(unittest.TestCase):

    
    def test_get_public_changesets(self):
        """
        Tests that a public repository query has a 200 status code.
        """
        req_url = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/?limit=2')
        self.assertEqual(req_url.status_code, 200)

    def test_get_private_changesets(self):
        """
        Tests that a private repository query without credentials will fail.
        """
        req_url = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/techetium/issues/?limit=2')
        self.assertEqual(req_url.status_code, 404)



