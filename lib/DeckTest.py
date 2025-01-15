from .Deck import Deck

class HandError(Exception):
    pass

for i in range(1000):
    deck = Deck()
    deck.shuffle()
    hand = deck.deal_hand()
    if len(hand) != len(set(hand)):
       raise HandError("Duplicate card in hand") 
