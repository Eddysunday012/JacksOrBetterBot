from lib.Deck import Deck
from lib.HandChecker import HandChecker
from lib.SelectHand import SelectHand
import sys

def main():

    if len(sys.argv) == 1:
        deck = Deck()
        deck.shuffle()
        hand = deck.deal_hand()
        select = SelectHand(hand)
        print(hand)
        inputValues = input("Choose cards to keep: ")
        string_list = inputValues.split(',')
        values = [int(x.strip()) for x in string_list] #strip whitespace

        new_hand = select.chooseHand(values)
        newVals = deck.deal_hand(5 - len(new_hand))
        new_hand += newVals
        checker = HandChecker(new_hand)

        print(new_hand)
        print(checker)
        return

    hand_size = int(sys.argv[1])
    rounds = int(sys.argv[2])
    strategyVal = sys.argv[3]
        
    dummy = HandChecker([])
    hands = dummy.pokerHands
    handCounts = {}

    for h in hands:
        handCounts[h] = 0

    for _ in range(int(rounds)):
        deck = Deck()
        deck.shuffle()
        hand = deck.deal_hand(int(hand_size))
        select = SelectHand(hand)
        new_hand = []

        if strategyVal == "-r":
            new_hand = select.chooseRandomHand(hand_size)
        elif strategyVal == "-s1":
            new_hand = select.strategy1()
            
        newVals = deck.deal_hand(5 - len(new_hand))
        new_hand += newVals
        checker = HandChecker(new_hand)
        handCounts[checker.__str__()] += 1

    print(handCounts)

if __name__ == "__main__":
    main()
