
class Player:

    def __init__(self, name, deck):
        self.deck = deck
        self.name = name
        self.collected_cards = []

    def __str__(self):
        return "Player " + self.name

    def hit(self):
        return self.deck.pop()

    def pull3(self):
        num_to_pull = 3
        if int(len(self.deck)) < 3:
            num_to_pull = int(len(self.deck))
        return [self.deck.pop() for _ in range(0, num_to_pull)]

    def collect(self, stack):
        self.collected_cards.extend(stack)