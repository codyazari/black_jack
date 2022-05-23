import deck
import players


def check_score(player_hand, house_hand):
    while True:
        if player_hand.



if __name__ == '__main__':
    playing_deck = deck.Deck().get_deck()
    player_hand = players.Hand(playing_deck)
    house_hand = players.Hand(playing_deck)
    player_hand.draw()
    house_hand.draw()
    print(player_hand.hand)
