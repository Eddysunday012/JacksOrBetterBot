from collections import Counter

class HandChecker:
    def __init__(self, hand):
        self.hand = hand
        self.pokerHands = ["Straight Flush", "Fours", "Full House", "Flush", "Straight", "Three", "Two Pair", "Jacks or Better", "High Card"]

    def __str__(self):
        if self.check_hand() == 9:
            return "Straight Flush"
        if self.check_hand() == 8:
            return "Fours"
        if self.check_hand() == 7:
            return "Full House"
        if self.check_hand() == 6:
            return "Flush"
        if self.check_hand() == 5:
            return "Straight"
        if self.check_hand() == 4:
            return "Three"
        if self.check_hand() == 3:
            return "Two Pair"
        if self.check_hand() == 2:
            return "Jacks or Better"
        return "High Card"

    def _sort_cards(self):
        suit_map = {"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        card_map = []
        for card in self.hand:
            card_map.append(suit_map[str(card.rank)])
        card_map.sort()
        return card_map

    def check_hand(self):
        isFlush = self._check_flush()
        isStraight = self._check_straight()
        if isFlush and isStraight:
            return 9
        if self._check_four():
            return 8
        if self._check_fullhouse():
            return 7
        if isFlush:
            return 6
        if isStraight:
            return 5
        if self._check_three():
            return 4
        if self._check_twopair():
            return 3
        if self._check_jacksorbetter():
            return 2
        return 1

    def _check_flush(self):
        suit = self.hand[0].suit
        for card in self.hand:
            if card.suit != suit:
                return False
        return True

    def _check_straight(self):
        card_map = self._sort_cards()
        curr_val = card_map[0]
        for i in range(1, len(card_map)):
            if curr_val + 1 != card_map[i]:
                return False
            curr_val = card_map[i]
        return True


    def _check_four(self):
        card_map = self._sort_cards()
        count = Counter(card_map)
        for _, value in count.items():
            if value == 4:
                return True
        return False

    def _check_three(self):
        card_map = self._sort_cards()
        count = Counter(card_map)
        for _, value in count.items():
            if value == 3:
                return True
        return False

    def _check_fullhouse(self):
        card_map = self._sort_cards()
        count = Counter(card_map)
        
        return 2 in count.values() and 3 in count.values()

    def _check_twopair(self):
        card_map = self._sort_cards()
        count = Counter(card_map)
        val_count = Counter(count.values())
        return 2 in val_count.keys() and val_count[2] == 2

    def _check_jacksorbetter(self):
        card_map = self._sort_cards()
        count = Counter(card_map)
        for key, value in count.items():
            if key > 10 and value == 2:
                return True
        return False

