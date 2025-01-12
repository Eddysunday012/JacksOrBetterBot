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

        cls.flush = [Card(1, 'Hearts'), Card(3, 'Hearts'), Card(5, 'Hearts'), Card(7, 'Hearts'), Card(9, 'Hearts')]
        cls.notFlush = [Card(1, 'Hearts'), Card(3, 'Spades'), Card(5, 'Clubs'), Card(7, 'Diamonds'), Card(9, 'Hearts')]

        cls.straight = [Card(1, 'Hearts'), Card(2, 'Spades'), Card(3, 'Clubs'), Card(4, 'Diamonds'), Card(5, 'Spades')]
        cls.notStraight = [Card(1, 'Hearts'), Card(3, 'Hearts'), Card(5, 'Hearts'), Card(7, 'Hearts'), Card(9, 'Spades')]

        cls.fours = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]
        cls.notFours = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades')]

        cls.threes = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(4, 'Spades')]
        cls.notThrees = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]

        cls.fullHouse = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]
        cls.notFullHouse = [Card(3, 'Hearts'), Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades')]

        cls.twopair = [Card(1, 'Hearts'), Card(1, 'Hearts'), Card(5, 'Spades'), Card(5, 'Spades'), Card(3, 'Spades')]
        cls.notTwopair = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]

        cls.jacksorbetter = [Card('J', 'Hearts'), Card('J', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.queensorbetter = [Card('Q', 'Hearts'), Card('Q', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.kingsorbetter = [Card('K', 'Hearts'), Card('K', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.acesorbetter = [Card('A', 'Hearts'), Card('A', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.notJacksOrBetter = [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]
        cls.notJacksOrBetter2 = [Card('10', 'Hearts'), Card('10', 'Spades'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')]

    @classmethod
    def tearDownClass(cls):
        del cls.straightFlush
        del cls.notStraightFlush
        del cls.flush
        del cls.notFlush
        del cls.straight
        del cls.notStraight
        del cls.fours
        del cls.notFours
        del cls.threes
        del cls.notThrees
        del cls.fullHouse
        del cls.notFullHouse

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

    # Tests for straight
    def test_check_straight1(self):
        list_of_cards = HandCheckerTest.straight
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_straight())

    def test_check_straight2(self):
        list_of_cards = HandCheckerTest.notStraight
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_straight())

    def test_check_straight3(self):
        list_of_cards = HandCheckerTest.straight.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_straight())

    # Tests for four of a kind
    def test_check_four1(self):
        list_of_cards = HandCheckerTest.fours
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_four())

    def test_check_four2(self):
        list_of_cards = HandCheckerTest.notFours
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_four())

    def test_check_four3(self):
        list_of_cards = HandCheckerTest.fours.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_four())

    # Tests for three of a kind
    def test_check_three1(self):
        list_of_cards = HandCheckerTest.threes
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_three())

    def test_check_three2(self):
        list_of_cards = HandCheckerTest.notThrees
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_three())

    def test_check_three3(self):
        list_of_cards = HandCheckerTest.threes.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_three())

    # Tests for Fullhouse
    def test_check_fullhouse1(self):
        list_of_cards = HandCheckerTest.fullHouse
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_fullhouse())

    def test_check_fullhouse2(self):
        list_of_cards = HandCheckerTest.notFullHouse
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_fullhouse())

    def test_check_fullhouse3(self):
        list_of_cards = HandCheckerTest.fullHouse.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_fullhouse())

    # Tests for twopair
    def test_check_twopair1(self):
        list_of_cards = HandCheckerTest.twopair
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_twopair())

    def test_check_twopair2(self):
        list_of_cards = HandCheckerTest.notTwopair
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_twopair())

    def test_check_twopair3(self):
        list_of_cards = HandCheckerTest.twopair.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_twopair())

    # Tests for JacksOrBetter
    def test_check_jacksorbetter1(self):
        list_of_cards = HandCheckerTest.notJacksOrBetter
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_jacksorbetter())

    def test_check_jacksorbetter2(self):
        list_of_cards = HandCheckerTest.jacksorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter3(self):
        list_of_cards = HandCheckerTest.queensorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter4(self):
        list_of_cards = HandCheckerTest.kingsorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter5(self):
        list_of_cards = HandCheckerTest.acesorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertTrue(hand._check_jacksorbetter())

    def test_check_jacksorbetter6(self):
        list_of_cards = HandCheckerTest.notJacksOrBetter
        hand = HandChecker(list_of_cards)
        self.assertFalse(hand._check_jacksorbetter())

    # Tests for CheckHand
    def test_check_checkhand_straightflush(self):
        list_of_cards = HandCheckerTest.straightFlush
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 9)

    def test_check_checkhand_straightflush_random(self):
        list_of_cards = HandCheckerTest.straightFlush.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 9)

    def test_check_checkhand_fours(self):
        list_of_cards = HandCheckerTest.fours
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 8)

    def test_check_checkhand_fours_random(self):
        list_of_cards = HandCheckerTest.fours.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 8)

    def test_check_checkhand_fullhouse(self):
        list_of_cards = HandCheckerTest.fullHouse
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 7)

    def test_check_checkhand_fullhouse_random(self):
        list_of_cards = HandCheckerTest.fullHouse.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 7)

    def test_check_checkhand_flush(self):
        list_of_cards = HandCheckerTest.flush
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 6)

    def test_check_checkhand_flush_random(self):
        list_of_cards = HandCheckerTest.flush.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 6)

    def test_check_checkhand_straight(self):
        list_of_cards = HandCheckerTest.straight
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 5)

    def test_check_checkhand_straight_random(self):
        list_of_cards = HandCheckerTest.straight.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 5)

    def test_check_checkhand_three(self):
        list_of_cards = HandCheckerTest.threes
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 4)

    def test_check_checkhand_three_random(self):
        list_of_cards = HandCheckerTest.threes.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 4)

    def test_check_checkhand_twopair(self):
        list_of_cards = HandCheckerTest.twopair
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 3)

    def test_check_checkhand_twopair_random(self):
        list_of_cards = HandCheckerTest.twopair.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 3)

    def test_check_checkhand_jacksorbetter(self):
        list_of_cards = HandCheckerTest.jacksorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 2)

    def test_check_checkhand_queensorbetter(self):
        list_of_cards = HandCheckerTest.queensorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 2)

    def test_check_checkhand_kingsorbetter(self):
        list_of_cards = HandCheckerTest.kingsorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 2)

    def test_check_checkhand_acesorbetter(self):
        list_of_cards = HandCheckerTest.acesorbetter.copy()
        random.shuffle(list_of_cards)
        hand = HandChecker(list_of_cards)
        self.assertEqual(hand.check_hand(), 2)


