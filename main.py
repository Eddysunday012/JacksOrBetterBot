from lib.Deck import Deck

def main():
    deck = Deck()
    deck.shuffle()
    hand = deck.deal_hand()
    print(hand)


if __name__ == "__main__":
    main()
