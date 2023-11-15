"""
A module with two sorting functions (and helpers)

<YOUR NAME HERE>
<DATE HERE>
"""


def push_up(b, k):
    """
    Moves the value at position k into its sorted position in b[k+1..n-1].

    Parameter b: The list to rearrange
    Precondition: b is a list, with b[k+1..n-1] sorted

    Parameter k: The position to push down into b[k+1..n-1]
    Precondition: k is an int and a valid position in b
    """
    n = len(b)
    j = k
    # Finish the rest of me
    while j < n-1:
        if b[j]>b[j+1]:
            swap(b, j+1, j)
        j = j+1


def isort(b):
    """
    Insertion Sort: Sorts the array b in n^2 time

    This version use push_up instead of push_down.

    Parameter b: The sequence to sort
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, 'IS NOT LIST'
    n = len(b)
    i = n
    # Finish the rest of me
    while i > 0:
        push_up(b, i-1)
        i = i - 1


def compare_tuple(a,b):
    """
    Returns -1, 0, or 1 indicating the relationship between a and b

    If a < b, this function returns -1.  If a > b, this function returns 1.
    Otherwise (a == b), this function returns 0.

    To compute this function, first check each  k < min(len(a),len(b)), and
    find the first k where a[k] != b[k]. If a[k] < b[k] then a < b. Otherwise
    if b[k] < a[k], then b > a.

    If there is no such k, compare len(a) to len(b). If len(a) < len(b) then
    a < b.  Otherwise if len(a) > len(b), then b < a. If len(a) == len(b) then
    the two tuples are equal.

    Examples: compare_tuple((1,3,5),(1,4,0)) returns -1
              compare_tuple((1,3,5),(1,2,7)) returns 1
              compare_tuple((1,3,5),(1,3,5)) returns 0
              compare_tuple((1,3,5),(1,3,5,2)) returns -1

    Parameter a: The first tuple to compare
    Precondition: a is a tuple of ints

    Parameter b: The first tuple to compare
    Precondition: b is a tuple of ints
    """
    pass # IMPLEMENT ME


def sort_tuples(b):
    """
    TimSort: Sorts a list of tuples using the built-in sort.

    This function uses the compare_tuples to order the elements of b.

    Parameter b: The sequence to sort.
    Precondition: b is a mutable sequence (e.g. a list) of tuples of ints.
    """
    # We implemented this one for you (see directions)
    import functools
    b.sort(key=functools.cmp_to_key(compare_tuple))


# HELPER FUNCTION
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
    temp = b[h]
    b[h] = b[k]
    b[k] = temp
