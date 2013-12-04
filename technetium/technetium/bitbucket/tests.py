"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
import unittest


class SimpleTest(TestCase):
    def test_basic_operations(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)
        self.assertIsNone(None)
        self.assertIn(1, [1, 2, 3])



class BitissuesTest(TestCase):
    def test_get_issues(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)