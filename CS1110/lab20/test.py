"""
A unit test for module blackjack

Run this test script to make sure everything is working properly.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:     October 29, 2019
"""
import introcs
import card
import wild

def test_wild_eq():
    """
    Tests that __eq__ works properly for WildCard.
    """
    print('Testing wild method __eq__')

    card1 = wild.WildCard(1,12,False)
    card2 = card.Card(1,12)
    introcs.assert_equals(card1,card1)
    introcs.assert_not_equals(card1,card2)

    card2 = wild.WildCard(1,12)
    introcs.assert_equals(card1,card1)

    card2 = wild.WildCard(1,12,True)
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(3,12)
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(1,1)
    introcs.assert_not_equals(card1,card2)


def test_wild_lt():
    """
    Tests that __lt__ works properly for WildCard.
    """
    print('Testing wild method __lt__')

    card1 = wild.WildCard(code='QD')
    card2 = wild.WildCard(code='QS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='JD')
    card2 = wild.WildCard(code='QD')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='2C')
    card2 = wild.WildCard(code='AS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card3 = wild.WildCard(code='WC')
    introcs.assert_true(card3<card2)
    introcs.assert_false(card2<card3)
    introcs.assert_true(card1<card3)
    introcs.assert_false(card3<card1)


def test_wild_deck():
    """
    Tests that the classmethod deck works properly for WildCard.
    """
    print('Testing wild method deck')

    deck1 = card.Card.deck()
    deck2 = wild.WildCard.deck()

    introcs.assert_equals(len(deck1)+2,len(deck2))
    for pos in range(len(deck1)):
        introcs.assert_equals(deck1[pos].getSuit(),deck2[pos].getSuit())
        introcs.assert_equals(deck1[pos].getRank(),deck2[pos].getRank())
        introcs.assert_false(deck2[pos].isWild())

    rdjoker = deck2[-2]
    introcs.assert_equals(2,rdjoker.getSuit())
    introcs.assert_equals(1,rdjoker.getRank())
    introcs.assert_true(rdjoker.isWild())

    bkjoker = deck2[-1]
    introcs.assert_equals(3,bkjoker.getSuit())
    introcs.assert_equals(1,bkjoker.getRank())
    introcs.assert_true(bkjoker.isWild())


# Script code
if __name__ == '__main__':
    test_wild_eq()
    test_wild_lt()
    test_wild_deck()

    print('The module wild passed all tests.')
