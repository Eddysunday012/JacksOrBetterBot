import random
from .HandChecker import HandChecker

class SelectHand():

    def __init__(self, hand):
        self.hand = hand
        self.handChecker = HandChecker(hand)

    def chooseHand(self, keep):
        return [self.hand[x] for x in keep]

    def chooseRandomHand(self, hand_size):
        return random.sample(self.hand, hand_size)

    def strategy1(self):
        fiveCardHands = ["Straight Flush", "Flush", "Straight", "Full House"]
        if self.handChecker in fiveCardHands:
            return self.hand
        return []
