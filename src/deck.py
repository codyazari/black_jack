import random


class Card:
    """
    A class to represent the basic unit of a card


    Attributes:
        suit : string
            the suit of the playing card
        value : string
            the face value of the playing card
        power : integer
            how "strong" a card is
    """

    def __init__(self, suit, value, power):
        self.suit = suit
        self.value = value
        self.power = power

    def __repr__(self):
        """ Allows me to print attributes of card objects for testing """
        return "{} of {}; power = {}".format(self.value, self.suit, self.power)

    def get_power(self):
        """ Getter function to obtain the power from an individual card object """
        return self.power


class Deck:
    """
    A class that takes in 52 card objects and builds them into a unified deck


    Attributes:
        cards : list
            where the 52 card objects are stored
    """

    def __init__(self):
        self.cards = []
        self.build()
        # self.shuffle()

    def get_deck(self):
        """ Getter function to access the playing deck """
        return self.cards

    def build(self):
        """
        The method that builds the 52 card deck by iterating through suits and face-values and designating a power
        depending on its face value
        """
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
                if value in {'Jack', 'Queen', 'King'}:
                    self.cards.append(Card(suit, value, 10))
                elif value != 'Ace':
                    self.cards.append(Card(suit, value, int(value)))
                else:
                    self.cards.append(Card(suit, value, 0))

    def shuffle(self):
        """ Shuffles the 52 cards within the deck """
        random.shuffle(self.cards)
