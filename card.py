class Card:

    values = {"Two": 2, "Three": 3, "Four" : 4, "Five" : 5, "Six": 6, "Seven" : 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }

    suites = ("Hearts", "Diamonds", "Speads", "Clubs")
    ranks = ("Two", "Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack", "Queen","King","Ace")

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
        self.value = Card.values[rank]

    
    def __str__(self):
        return self.rank + " of " + self.suite
