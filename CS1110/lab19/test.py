"""
A unit test for module wild

Run this test script to make sure everything is working properly.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:     October 29, 2019
"""
import introcs
import card
import wild


def test_wild_setters():
    """
    Tests the setters for the WildCard objects

    This test does not require that the initializer work yet.  If you still
    have pass in the initilizer, these tests should be fine.

    This test does not require that setCode support the 'WC' code.  This is
    an optional exercise.
    """
    print('Testing wild setters')

    # This will create an empty card if the initializer is not defined
    card = wild.WildCard()

    card.setSuit(1)
    introcs.assert_equals(1,card.getSuit())
    card.setRank(3)
    introcs.assert_equals(3,card.getRank())

    card.setWild(True)
    introcs.assert_true(card.isWild())
    card.setWild(False)
    introcs.assert_false(card.isWild())

    try:
        card.setWild(5)
        introcs.quit_with_error('setWild does not enforce preconditions')
    except:
        pass

    # Check that setCode works on codes OTHER than 'WC'
    card.setCode('AS')
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals('AS',card.getCode())


def test_wild_init():
    """
    Tests the initializer for the WildCard objects

    This test does not require that setCode support the 'WC' code.  This is
    an optional exercise.
    """
    print('Testing wild __init__')

    # This will create an empty card if the initializer is not defined
    card = wild.WildCard(1,12)
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card = wild.WildCard(2,11,True)
    introcs.assert_equals(2,card.getSuit())
    introcs.assert_equals(11,card.getRank())
    introcs.assert_true(card.isWild())

    card = wild.WildCard(2,11,True,'AS')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_false(card.isWild())

    try:
        card = wild.WildCard(5,11,True)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass

    try:
        card = wild.WildCard(2,0,True)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass

    try:
        card = wild.WildCard(2,11,3)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass


def test_wild_str():
    """
    Tests that __str__ works properly for WildCard.
    """
    print('Testing wild method __str__')

    card = wild.WildCard(1,12)
    introcs.assert_equals('Queen of Diamonds',str(card))
    card = wild.WildCard(0,3)
    introcs.assert_equals('3 of Clubs',str(card))
    card = wild.WildCard(3,1,True)
    introcs.assert_equals('Ace of Spades [WILD]',str(card))
    card = wild.WildCard(1,12,True)
    introcs.assert_equals('Queen of Diamonds [WILD]',str(card))
    card = wild.WildCard(0,3,True)
    introcs.assert_equals('3 of Clubs [WILD]',str(card))


def test_wild_code():
    """
    Tests that setCode (and the initializer) works properly for WildCard.
    """
    print('Testing wild methods setCode and getCode')

    # This will create an empty card if the initializer is not defined
    card = wild.WildCard()
    card.setCode('QD')
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card.setCode('WC')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())

    try:
        card.setCode(23)
        introcs.quit_with_error('setCode does not enforce preconditions')
    except:
        pass

    try:
        card.setCode('WD')
        introcs.quit_with_error('setCode does not enforce preconditions')
    except:
        pass

    card = wild.WildCard(code='QD')
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card = wild.WildCard(code='WC')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())

    card = wild.WildCard(2,11,True)
    introcs.assert_equals(2,card.getSuit())
    introcs.assert_equals(11,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())


# Script code
if __name__ == '__main__':
    test_wild_setters()
    test_wild_init()
    test_wild_str()
    test_wild_code()

    print('The module wild passed all tests.')
