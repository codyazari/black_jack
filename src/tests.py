import unittest
import random
from src import deck
from src import players


class TestCard(unittest.TestCase):

    def test_single_card(self):
        """ Testing a single card object """
        card = deck.Card('Spades', 'Ace', 11)
        self.assertEqual((card.suit, card.value, card.power), ('Spades', 'Ace', 11))


class TestDeck(unittest.TestCase):

    def test_is_card(self):
        """ Testing whether the card stays a card after being passed into the deck class """
        test_deck = deck.Deck()
        self.assertIsInstance(test_deck.cards[0], deck.Card)

    def test_get_deck(self):
        """ Testing whether the get_deck() method opens the initialized deck """
        test_deck = deck.Deck()
        self.assertEqual(test_deck.cards, test_deck.get_deck())

    def test_shuffle(self):
        """ Tests whether the shuffled deck does not equal the unshuffled deck """
        test_deck = deck.Deck()
        unshuffled_test_deck = deck.Deck().get_deck()
        random.seed(69)
        shuffled_test_deck = test_deck.shuffle()
        self.assertNotEqual(unshuffled_test_deck, shuffled_test_deck)


class TestHand(unittest.TestCase):

    def test_draw(self):
        """ Testing if the draw method draws  """
        # Initializing Decks
        test_deck = deck.Deck().get_deck()
        compared_test_deck = deck.Deck().get_deck()
        random.seed(69)
        # Initializing the Hands
        test_hand = players.Hand(test_deck)
        compared_test_hand = players.Hand(compared_test_deck)
        drawn_hand = test_hand.draw()
        compared_drawn_hand = compared_test_hand.draw()
        # Testing Equivalence
        self.assertEqual(str(drawn_hand), str(compared_drawn_hand))

    def test_hit(self):
        # Initializing Decks
        test_deck = deck.Deck().get_deck()
        compared_test_deck = deck.Deck().get_deck()
        # Initializing Hands
        test_hand = players.Hand(test_deck)
        compared_test_hand = players.Hand(compared_test_deck)
        # Hitting Method
        drawn_hand = test_hand.hit()
        compared_drawn_hand = compared_test_hand.hit()
        # Testing hit method
        self.assertEqual(str(drawn_hand), str(compared_drawn_hand))


if __name__ == '__main__':
    unittest.main()
    # Test Card Functions
    TestCard.test_single_card()
    # Test Deck Functions
    TestDeck.test_is_card()
    TestDeck.test_shuffle()
    # Test Hand Functions
    TestHand.test_draw()
    TestHand.test_hit()
