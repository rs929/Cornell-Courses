"""
A module with several generators

<YOUR NAME HERE>
<DATE HERE>
"""


def emit_alpha(string):
    """
    Generates the letters in string, in the order given

    Example: emit_alpha('ab12c!') yields 'a', 'b', and 'c' in that order.

    Parameter string: The string to process
    Precondition: string is a str
    """
    for x in range(len(string)):
        if string[x].isalpha():
            yield string[x]


def pair_swap(input):
    """
    Generates outputing contests of input, all adjacent pairs swapped

    Example: pair_swap((1,2,3,4,5)) yields 2, 1, 4, 3, and 5 in that order.

    Parameter input: The input to process
    Precondition: input is an iterable or iterator
    """
    for x in input:
        if x%2==0:
            yield input[x+1]
        else:
            yield input[x-1]
    # HINT: input is NOT guaranteed to be sliceable, nor have a len value
