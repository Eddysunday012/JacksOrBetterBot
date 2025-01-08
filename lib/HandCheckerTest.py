import unittest

from HandChecker import HandChecker
from Card import Card

class HandCheckerTest(unittest.TestCase):
    def test_check_flush1(self):
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

    def test_check_four1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_four())

    def test_check_four2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_four())

    def test_check_three1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_three())

    def test_check_three2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_three())

    def test_check_fullhouse1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_fullhouse())

    def test_check_fullhouse2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_fullhouse())

    def test_check_twopair1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades'), Card(3, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_twopair())

    def test_check_twopair2(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_twopair())

    def test_check_jacksorbetter1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_jacksorbetter())

    def test_check_jacksorbetter2(self):
        list_of_cards = [Card('J', 'Hearts'), Card('J', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())


