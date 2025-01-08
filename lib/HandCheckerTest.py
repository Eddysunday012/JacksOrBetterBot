import unittest

from HandChecker import HandChecker
from Card import Card

class HandCheckerTest(unittest.TestCase):
    def test_check_flush(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_flush())

    def test_check_flush2(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_flush())

    def test_check_straight1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_straight())

    def test_check_straight2(self):
        list_of_cards = [Card(1, 'Hearts'), Card(3, 'Hearts'), Card(5, 'Hearts'), Card(7, 'Hearts'), Card(9, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_straight())