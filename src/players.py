import deck


class Hand:
    """
    A class that takes in the playing deck and allows the player and computer
    to draw cards from a shared built deck


    Attributes:
        hand : list
            where the active cards are stored for the player and the computer
        built_deck : list
            the object of class Deck, which contains the playing deck shared between
            the computer and the player
    """

    def __init__(self, built_deck):
        self.hand = []
        self.built_deck = built_deck

    def draw(self):
        """
        Method that draws 2 cards from the bottom of the deck when called, and stores them
        within your hand
        """
        for i in range(2):
            self.hand.append(self.built_deck.pop())
        return self.hand

    def calculate_power(self):
        counter = 0
        for card in self.hand:
            card.get_power() + counter
        return counter

    def hit(self):
        """ Method that adds a card to your hand from the bottom of the deck when called """
        self.hand.append(self.built_deck.pop())
        return self.hand
