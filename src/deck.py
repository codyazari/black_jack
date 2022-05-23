import random


class Card:

    def __init__(self, suit, value, power):
        self.suit = suit
        self.value = value
        self.power = power

    def __repr__(self):
        return "{} of {}; power = {}".format(self.value, self.suit, self.power)


class Deck:

    def __init__(self):
        self.cards = []
        self.build()
        # self.shuffle()

    def get_deck(self):
        return self.cards

    def build(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
                if value in {'Jack', 'Queen', 'King'}:
                    self.cards.append(Card(suit, value, 10))
                elif value != 'Ace':
                    self.cards.append(Card(suit, value, int(value)))
                else:
                    self.cards.append(Card(suit, value, 0))

    def shuffle(self):
        random.shuffle(self.cards)
