"""
The list functions for Lab 12

This module contains three functions that each works with a list.  The first
two are mutable functions; the third is fruitful.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def put_in(alist,value):
    """
    MODIFIES the sorted list to include value, resorting as necessary.

    This function is a PROCEDURE.  It does not return a new list.  Instead,
    it modifies the existing list.

    Examples:
        If a = [0,2,3,4], put_in(a,1) makes a = [0,1,2,3,4]
        If a = [0,2,3,4], put_in(a,2) makes a = [0,2,2,3,4]
        If a = [], put_in(a,3) makes a = [3]

    Parameter a: The list to append to
    Precondition: a is a sorted list of ints

    Parameter value: The value to append
    Precondition: value is an int
    """
    alist.sort()
    alist.insert(0,value)
    alist.sort()


def replace_first(alist,ovalue,nvalue):
    """
    MODIFIES the list so that the first appearance of ovalue becomes nvalue.

    This function is a PROCEDURE.  It does not return a new list.  Instead,
    it modifies the existing list.

    We do not guarantee that ovalue is in the list.  If it is not there, then
    the list should remain unchanged.

    Example: If alist is [5, 9, 1, 9, 7], then replace_first(alist,9,3) modifies
    the list so that alist is now [5, 3, 1, 9, 7].

    Example: If alist is [5, 9, 1, 9, 7], then replace_first(alist,3,2) does
    not modify the list at all.

    Parameter alist: the list to modify
    Precondition: alist is a list of ints

    Parameter ovalue: the value to replace
    Precondition: ovalue is an int

    Parameter nvalue: the value to substitute with
    Precondition: nvalue is an int
    """
    if ovalue in alist:
        index = alist.index(ovalue)
        alist[index] = nvalue


def lesser_than(alist,value):
    """
    Returns the number of elements in alist strictly less than value

    Example: lesser_than([5, 9, 1, 7], 6) evaluates to 2

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list of ints

    Parameter value:  the value to compare to the list
    Precondition:  value is an int
    """
    pass # Implement me
