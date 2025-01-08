from collections import deque
import random
from .Card import Card

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = deque([Card(rank, suit) for rank in ranks for suit in suits])

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self):
        return [self.cards.popleft() for _ in range(5)]

    def reshuffle_deck(self, Cards):
        for card in Cards:
            self.cards.append(card)

        self.shuffle()
