# -*- coding: utf-8 -*-
from django.test import TestCase


class DemoTestCase(TestCase):
    def setUp(self):
        self.odd_numbers = range(1, 11, 2)  # [1, 3, 5, 7, 9]
        self.even_numbers = range(2, 12, 2) # [2, 4, 6, 8, 10]

    def test_evens_are_even(self):
        for odd in self.odd_numbers:
            self.assertEqual(odd % 2, 1)

    def test_odds_are_odd(self):
        for odd in self.even_numbers:
            self.assertEqual(odd % 2, 0)
