"""
A unit test for module blackjack

Run this test script to make sure everything is working properly.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:     October 29, 2019
"""
import introcs
import card
import bjack


def test_game_init():
    """
    Tests the __init__ method for Blackjack objects
    """
    print('Testing blackjack __init__')
    c1 = card.Card(0, 12)
    c2 = card.Card(1, 10)
    c3 = card.Card(2, 9)
    c4 = card.Card(0, 1)

    # Initialize deck and start game.
    deck = [c1, c2, c3, c4]
    game = bjack.Blackjack(deck)

    introcs.assert_equals([c1, c2], game.playerHand)
    introcs.assert_equals([c3], game.dealerHand)
    introcs.assert_equals([c4], deck)  # check that cards were removed

    deck = card.Card.deck()  # non-shuffled deck
    game = bjack.Blackjack(deck)
    c1 = card.Card(0, 1)
    c2 = card.Card(0, 2)
    c3 = card.Card(0, 3)
    c4 = card.Card(0, 4)

    introcs.assert_equals([c1, c2], game.playerHand)
    introcs.assert_equals([c3], game.dealerHand)

    # check that right cards were removed
    introcs.assert_equals(card.Card.deck()[3:], deck)


def test_game_str():
    """
    Tests the __str__ function for Blackjack objects
    """
    print('Testing blackjack method __str__')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)
    introcs.assert_equals('player: 20; dealer: 9', str(game))

    game.playerHand=[]
    introcs.assert_equals('player: 0; dealer: 9', str(game))
    game.dealerHand.append(card.Card(2,1))
    introcs.assert_equals('player: 0; dealer: 20', str(game))
    game.dealerHand.append(card.Card(2,5))
    introcs.assert_equals('player: 0; dealer: 25', str(game))


def test_game_score():
    """
    Tests the _score method (which is hidden, but we access anyway)
    """
    print('The the blackjack _score attribute')
    # need a dummy game object to call its _score function (and test it)
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(13, game._score([card.Card(2, 2), card.Card(3, 1)]))
    introcs.assert_equals(13, game._score([card.Card(1, 13), card.Card(0, 3)]))
    introcs.assert_equals(22, game._score([card.Card(1, 1), card.Card(0, 1)]))
    introcs.assert_equals(9, game._score([card.Card(1, 2), card.Card(0, 3), card.Card(3, 4)]))
    introcs.assert_equals(0, game._score([]))


def test_dealerScore():
    """
    Tests the dealerScore method for Blackjack objects
    """
    print('Testing blackjack method dealerScore')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(9, game.dealerScore())
    game.dealerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.playerHand = [card.Card(1, 13), card.Card(0, 3)]
    introcs.assert_equals(13, game.dealerScore())


def test_playerScore():
    """
    Tests the playerScore method for Blackjack objects
    """
    print('Testing blackjack method playerScore')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(20, game.playerScore())
    game.playerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.dealerHand = [card.Card(1, 13), card.Card(0, 3)]
    introcs.assert_equals(13, game.playerScore())


def test_playerBust():
    """
    Tests the playerBust method for Blackjack objects
    """
    print('Testing blackjack method playerBust')
    # get dummy deck
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10)]
    introcs.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    introcs.assert_true(game.playerBust())


def test_dealerBust():
    """
    Tests the dealerBust method for Blackjack objects
    """
    print('Testing blackjack method dealerBust')
    # get dummy deck
    deck = [card.Card(0, 12),  card.Card(2, 9), card.Card(1, 10),]
    game = bjack.Blackjack(deck)

    introcs.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10)]
    introcs.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    introcs.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.dealerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    introcs.assert_true(game.playerBust())


# Script code
if __name__ == '__main__':
    test_game_init()
    test_game_score()
    test_dealerScore()
    test_playerScore()
    test_dealerBust()
    test_playerBust()
    test_game_str()

    print('The module bjack passed all tests.')
