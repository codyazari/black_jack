import unittest
import random
import deck


class TestCard(unittest.TestCase):

    def test_single_card(self):
        card = deck.Card('Spades', 'Ace')
        self.assertEqual((card.suit, card.value), ('Spades', 'Ace'))


class TestDeck(unittest.TestCase):

    def test_is_card(self):
        test_deck = deck.Deck()
        self.assertIsInstance(test_deck.cards[0], deck.Card)

    def test_shuffle(self):
        test_deck = deck.Deck()
        random.seed(0)
        shuffled_test_deck = test_deck.shuffle()
        self.assertNotEqual(test_deck, shuffled_test_deck)


if __name__ == '__main__':
    unittest.main()
    TestCard.test_single_card()
    TestDeck.test_is_card()
    TestDeck.test_shuffle()
