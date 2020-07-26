import random
from card import Card

class Deck:

    def __init__(self):
        self.cards = []
        for rank in Card.ranks: 
            for suite in Card.suites: 
                card = Card(rank, suite)
                self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def shuffel(self):
        random.shuffle(self.cards)

    def deal_half(self):
        return [self.cards.pop() for _ in range(0, int(len(self.cards) / 2))]
        