import unittest
import random

from HandChecker import HandChecker
from Card import Card

'''
TESTS FOR HandChecker

Each test organized into specific pattern:
- pattern checks True
- pattern checks False
- pattern checks True when randomized
'''
class HandCheckerTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.straightFlush = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.notStraightFlush = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Spades')]

    @classmethod
    def tearDownClass(cls):
        del cls.straightFlush
        del cls.notStraightFlush

    # Tests for flush
    def test_check_flush1(self):
        list_of_cards = HandCheckerTest.straightFlush
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_flush())

    def test_check_flush2(self):
        list_of_cards = HandCheckerTest.notStraightFlush
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_flush())

    def test_check_flush3(self):
        list_of_cards = HandCheckerTest.straightFlush.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_flush())

    # Tetss for straight
    def test_check_straight1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Spades'), Card(3, 'Clubs'), Card(4, 'Diamonds'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_straight())

    def test_check_straight2(self):
        list_of_cards = [Card(1, 'Hearts'), Card(3, 'Hearts'), Card(5, 'Hearts'), Card(7, 'Hearts'), Card(9, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_straight())

    # Tests for four of a kind
    def test_check_four1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_four())

    def test_check_four2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_four())

    # Tests for three of a kind
    def test_check_three1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_three())

    def test_check_three2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_three())

    # Tests for Fullhouse
    def test_check_fullhouse1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_fullhouse())

    def test_check_fullhouse2(self):
        list_of_cards = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_fullhouse())

    # Tests for twopair
    def test_check_twopair1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades'), Card(3, 'Spades')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_twopair())

    def test_check_twopair2(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_twopair())

    # Tests for JacksOrBetter
    def test_check_jacksorbetter1(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_jacksorbetter())

    def test_check_jacksorbetter2(self):
        list_of_cards = [Card('J', 'Hearts'), Card('J', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter3(self):
        list_of_cards = [Card('Q', 'Hearts'), Card('Q', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter4(self):
        list_of_cards = [Card('K', 'Hearts'), Card('K', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter5(self):
        list_of_cards = [Card('A', 'Hearts'), Card('A', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter6(self):
        list_of_cards = [Card('10', 'Hearts'), Card('10', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_jacksorbetter())

    # Tests for CheckHand
    def test_check_checkhand_straightflush(self):
        list_of_cards = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 9)

    def test_check_checkhand_fours(self):
        list_of_cards = [Card(1, 'Spades'), Card(1, 'Hearts'), Card(1, 'Diamonds'), Card(1, 'Clubs'), Card(5, 'Hearts')]
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 8)




