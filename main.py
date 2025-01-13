from lib.Deck import Deck
from lib.HandChecker import HandChecker
from lib.SelectHand import SelectHand

def main():
    deck = Deck()
    deck.shuffle()
    hand = deck.deal_hand()
    print(hand)
    checker = HandChecker(hand)
    print(checker)


if __name__ == "__main__":
    main()
