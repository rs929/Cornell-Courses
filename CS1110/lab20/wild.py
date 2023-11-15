"""
A module providing a class for playing cards with Jokers

This class is a subclass of Card.  It shows of how to work with subclasses.

Author: Walker White (wmw2)
Date:   October 29, 2019
"""
from functools import total_ordering  # for implementing comparisons in Python3
import card


# decorator "fills in" missing comparisons, at the cost of speed
@total_ordering
class WildCard(card.Card):
    """
    A class to represent a deck of cards with jokers.

    Most decks have two jokers: a red joker and a black joker.  We will not
    make a difference between these two jokers, since color does not matter
    during play.

    Jokers are wild cards, meaning that they can be turned into whatever card
    you want to turn them into.  This means that a Joker card can have a normal
    suit and rank (representing what we want to convert the joker to).  So we
    identify jokers with a new attribute wild (which has getters and setters).

    This class does not need to make any changes to the setters and getters
    for suit and rank, as those attributes are unchanged.  However, the
    introduction of Jokers does change the meaning of the setter/getter for
    the codes. Jokers are represented by the two-character code 'WC'. Setting
    a card with that code creates a Joker equivalent to the Ace of Spades.
    """
    ### HIDDEN INSTANCE ATTRIBUTES (In addition to those for Card):
    # Attribute _wild:  whether this card is a Joker
    # Invariant: _wild is a bool

    def isWild(self):
        """
        Returns True if this a Joker or wild card.
        """
        return self._wild

    def setWild(self, value):
        """
        Sets whether this is a Joker or wild card.

        The card will retain is suit and rank values no matter what happens
        to its wild status.

        Parameter value: Whether this is a Joker or wild card.
        Precondition: value is a bool
        """
        # ASSERT THE PRECONDITIONS (BEST YOU CAN)
        assert type(value) == bool
        self._wild = value

    # This is a DERIVED attribute (it is a combination of suit and rank)
    def getCode(self):
        """
        Returns a two-character code for the card.

        The code is a two-character string whose first character generally
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.

        All wild cards return the code 'WC' no matter what their suit or
        rank is.
        """
        # Replace this line with proper code to support 'WC'
        if self._wild == True:
            return 'WC'
        else:
            return super().getCode()



    def setCode(self,value):
        """
        Sets the rank and suit of this card using a two-character code.

        The code should be a two-character string whose first character
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.  All cards set this way are not jokers/wild.

        If the value is 'WC', this creates a joker/wild card that is
        equivalent to the Ace of Spades. Otherwise, the card is not wild.

        Parameter value: The code for the new rank and suit
        Precondition: value is a 2-char string that is either 'WC' or has
        value[0] in 'A23456789TJQK' and value[1] in 'CDHS'.
        """
        # DO YOU NEED TO ASSERT PRECONDITIONS?
        # Replace this line with proper code to support 'WC'
        if value != 'WC':
            super().setCode(value)
            self.setWild(False)
        else:
            super().setRank(self, 1)
            super().setSuit(self, 3)
            self.setWild(True)

    def __init__(self, suit=0, rank=1, wild=False, code=None):
        """
        Initializes a card with given the suit and rank.

        The suits and rank are represented as integers. Alternatively,
        suit and rank can be encoded together in a two-character string like
        '3H' (3 of hearts) or 'KS' (king of spades).  We use 'T' for Ten.
        The code 'WC' indicates a joker.  By default, jokers are equivalent
        to the Ace of Spades.

        The possible suits are given in SUIT_NAMES, while the possible ranks
        are given in RANK_NAMES.  There is no rank 0.

        Example: if we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since SUIT_NAMES[0] is 'Clubs' and RANK_NAMES[12] is 'Queen'.
        The same card could be created by Card(code='QC').

        If the code parameter is used, the suit, rank, and wild parameters are
        ignored.  A code of 'WC' creates a wild Ace of Spades.

        Parameter suit: the suit encoding (optional)
        Precondition: suit is an int in 0..len(SUIT_NAMES)-1 (inclusive)

        Parameter rank: the rank encoding (optional)
        Precondition: rank is an int in 1..len(RANK_NAMES)-1 (inclusive)

        Parameter wild: whether this is a wild card (optional)
        Precondition: wild is a bool

        Parameter code: the card encoded as a string (optional)
        Precondition: code is a 2-char string that is either 'WC' or has
        code[0] in 'A23456789TJQK' and code[1] in 'CDHS'
        """
        # DO YOU NEED TO ASSERT PRECONDITIONS?
        super().__init__(suit, rank, code)
        if code == None:
            self.setWild(wild)

    def __str__(self):
        """
        Returns a readable string representation of this card.

        If this card is a Joker, the indicator '[WILD]' appears after the name.
        Otherwise, the result is the same as for the Card class.

        Example: '2 of Hearts [WILD]'
        """
        if self._wild == True:
            return super().__str__() + " [WILD]"
        else:
            return super().__str__()

        # TODO: implement me, according to my spec
        pass

    # THESE ARE ONLY NEEDED FOR THE OPTIONAL EXERCISES
    def __eq__(self, other):
        """
        Returns True if other is an equivalent card; False otherwise

        It is not enough for two cards to share the same suit and rank to
        be equal.  They must either both be wild or neither wild.

        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        # TODO: implement me, according to my spec
        if isinstance(self, WildCard) and isinstance(other, WildCard):
            if self.isWild() != other.isWild():
                return False
            s = super().__eq__(self)
            o = super().__eq__(other)
            return s == o
        else:
            return False

    def __lt__(self, other):
        """
        Returns True if this card is less than other

        Cards are compared according to poker ordering, with Aces high. In the
        case of ties, wild cards are worth LESS than the natural cards.

        Parameter other: the value to compare
        Precondition: other is a Card
        """
        if super().__eq__(self) == super().__eq__(other):
            if self.isWild() == True and other.isWild() == False:
                return True
            elif self.isWild() == False and other.isWild() == True:
                return False
        else:
            return super().__lt__(other)
        # TODO: implement me, according to my spec
        pass

    @classmethod
    def deck(cls):
        """
        Returns the list of the standard 52 cards + 2 jokers

        The cards are returned in the same order as for the class Card, except
        that it adds the two jokers at the end.  The first joker is equivalent
        to the Ace of Hearts (red joker) and the second joker is equivalent to
        the Ace of Spades (black joker).

        This is a CLASS method, as indicated by the decorator above.  It is
        designed to be called by the class name before the period: Card.deck()
        Notice the variable is cls, not self.  It holds the id of the CLASS
        FOLDER, not the object folder.
        """
        output = []  # list of cards so far to be returned
        for suit in range(len(cls.SUIT_NAMES)):
            for rank in range(1,len(cls.RANK_NAMES)):  # skip the None value
                output.append(cls(suit,rank))
        w1 = WildCard(2, 1, True)
        w2 = WildCard(3, 1, True)
        output.append(w1)
        output.append(w2)
        return output
