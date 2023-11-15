"""
Module for implementing Lab 07 functions.

The first function first_vowel is a helper function of the second function
pigify (which is the primary function). Function pigify converts English words
to Pig-Latin.

IMPLEMENT both functions.

While you are encouraged to test your answers, you do not need to write a unit
test.

Riche Sun (rs929)
THE DATE COMPLETED HERE
"""

def first_vowel(w):
    """
    Returns: position of the first vowel; -1 if no vowels.

    Parameter w: the word to search
    Precondition: w is a nonempty string with only lowercase letters
    """

    if 'a' in w or 'e' in w or 'i' in w or 'o' in w or 'u' in w or 'y' in w[1:]:
        if 'a' in w:
            v1 = w.find('a')
        else:
            v1 = len(w) + 1
        if 'e' in w:
            v2 = w.find('e')
        else:
            v2 = len(w) + 1
        if 'i' in w:
            v3 = w.find('i')
        else:
            v3 = len(w) + 1
        if 'o' in w:
            v4 = w.find('o')
        else:
            v4 = len(w) + 1
        if 'u' in w:
            v5 = w.find('u')
        else:
            v5 = len(w) + 1
        if 'y' in w[1:]:
            v6 = w[1:].find('y') + 1
        else:
            v6 = len(w) + 1
        return min(v1, v2, v3, v4, v5, v6)
    else:
        return -1



def pigify(w):
    """
    Returns: copy of w converted to Pig Latin

    See the lab handout for the complete rules on Pig Latin.

    Parameter w: the word to change to Pig Latin
    Precondition: w is a nonempty string with only lowercase letters
    """
    if first_vowel(w) == 0:
        result = w + 'hay'
        return result
    elif w.find('q') == 0:
        result = w[2:] + 'quay'
        return result
    elif first_vowel(w) > 0:
        position = first_vowel(w)
        result = w[position:] + w[:position] + 'ay'
        return result
    elif first_vowel(w) == -1:
        result = w + 'ay'
        return result
