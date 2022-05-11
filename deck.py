import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        self.cards = []
        self.build()
        # self.shuffle()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.cards)
