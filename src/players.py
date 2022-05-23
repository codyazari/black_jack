import deck


class Hand:

    def __init__(self, built_deck):
        self.hand = []
        self.built_deck = built_deck

    def draw(self):
        for i in range(2):
            self.hand.append(self.built_deck.pop())
        return self.hand

    def calculate_power(self):
        total_power = 0
        for card in self.hand:
            for variable in card:
                if isinstance(i, int):
                    total_power += i
        return total_power

    def hit(self):
        self.hand.append(self.built_deck.pop())
        return self.hand

    def walk(self):
        pass


class Player(Hand):
    pass


class House(Hand):
    pass


# Initializing Decks
test_deck = deck.Deck().get_deck()
compared_test_deck = deck.Deck().get_deck()
# Initializing Hands
test_hand = Hand(test_deck)
compared_test_hand = Hand(compared_test_deck)
# Hitting Method
drawn_hand = test_hand.hit()
# compared_drawn_hand = compared_test_hand.hit()
# # Testing hit method
# print(test_hand.hand)
# print(compared_test_hand.hand)
print(test_hand.calculate_power())
