"""
A module with insertion sort

Author: Walker M. White (wmw2)
Date:   October 20, 2020
"""
import random


def sort(b):
    """
    Insertion Sort: Sorts the array b in n^2 time

    Parameter b: The sequence to sort
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, repr(b)+' is not a list'
    n = len(b)

    # Start from beginning of list
    i = 0

    # b[0..i-1] sorted, b[i..n-1] unknown
    while i < n:
        push_down(b,i)
        i = i + 1

    # b[0..n-1] sorted


def push_down(b, k):
    """
    Moves the value at position k into its sorted position
    in b[0.k-1].

    Parameter b: The list to rearrange
    Precondition: b is a list, with b[0..k-1] sorted

    Parameter k: The position to push down into b[0..k-1]
    Precondition: k is an int and a valid position in b
    """
    # We typically do not enforce preconditions on hidden helpers
    j = k

    while j > 0:
        if b[j-1] > b[j]:
            swap(b,j-1,j)
        j = j - 1


def swap(b, h, k):
    """
    Procedure swaps b[h] and b[k]

    Parameter b: The list to rearrange
    Precondition: b is a mutable sequence (e.g. a list).

    Parameter h: The first position to swap
    Precondition: h is an int and a valid position in b

    Parameter k: The second position to swap
    Precondition: k is an int and a valid position in b
    """
    # We typically do not enforce preconditions on hidden helpers
    temp = b[h]
    b[h] = b[k]
    b[k] = temp


def scramble(b):
    """
    Scrambles the list to resort again

    Parameter b: The list to scramble
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, repr(b)+' is not a list'

    # Start from the beginning
    i = 0
    while i < len(b):
        size = len(b)-i
        pos  = int(random.random()*size)
        _swap(b,i,i+pos)
        i = i+1
