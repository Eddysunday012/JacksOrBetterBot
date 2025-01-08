from collections import Counter


class HandChecker:
    def __init__(self, hand):
        self.hand = hand

    def _sort_cards(self):
        suit_map = {"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        card_map = []
        for card in self.hand:
            card_map.append(suit_map[str(card.rank)])
        card_map.sort()
        return card_map

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
