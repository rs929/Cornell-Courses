"""
A test script to verify the sorting functions

Author: Walker M. White (wmw2)
Date: November 15, 2021
"""
import random
import introcs
import funcs



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
        swap(b,i,i+pos)
        i = i+1


def test_push_up():
    """
    A test procedure for the function push_up
    """
    print('Testing push_up')
    
    # First test
    b = [8,6,1,9]
    result = funcs.push_up(b,1)
    introcs.assert_equals(None,result)
    introcs.assert_equals([8,1,6,9],b)
    
    # Second test
    b = [8,6,1,9]
    result = funcs.push_up(b,2)
    introcs.assert_equals(None,result)
    introcs.assert_equals([8,6,1,9],b)
    
    # Third test
    b = [8,6,1,9]
    result = funcs.push_up(b,3)
    introcs.assert_equals(None,result)
    introcs.assert_equals([8,6,1,9],b)
    
    # Fourth test
    b = [8,1,6,9]
    result = funcs.push_up(b,0)
    introcs.assert_equals(None,result)
    introcs.assert_equals([1,6,8,9],b)


def test_isort():
    """
    A test procedure for the function isort
    """
    print('Testing isort')
    
    # First test
    b = [8,6,1,9]
    result = funcs.isort(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals([1,6,8,9],b)
    
    # Second test
    result = funcs.isort(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals([1,6,8,9],b)
    
    # Third test
    a = list(range(10))
    b = a[:]
    scramble(b)
    result = funcs.isort(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)

    # Fourth test
    a = list(range(20))
    b = a[:]
    scramble(b)
    result = funcs.isort(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)


def test_compare_tuple():
    """
    A test procedure for the function compare_tuple
    """
    print('Testing compare_tuple')
    
    # First test
    a = (1,3,2,7)
    b = (1,5,1,0)
    result = funcs.compare_tuple(a,b)
    introcs.assert_equals(-1,result)
    
    # Second test
    result = funcs.compare_tuple(b,a)
    introcs.assert_equals(1,result)
    
    # Third test
    result = funcs.compare_tuple(a,a)
    introcs.assert_equals(0,result)
    
    # Fourth test
    a = (1,3,2,7)
    b = (1,3,2,5,0)
    result = funcs.compare_tuple(a,b)
    introcs.assert_equals(1,result)
    
    # Fifth test
    result = funcs.compare_tuple(b,a)
    introcs.assert_equals(-1,result)
    
    # Sixth test
    a = (1,3,2,5)
    b = (1,3,2,5,0)
    result = funcs.compare_tuple(a,b)
    introcs.assert_equals(-1,result)
    
    # Seventh test
    result = funcs.compare_tuple(b,a)
    introcs.assert_equals(1,result)


def test_sort_tuples():
    """
    A test procedure for the function sort_tuples
    """
    print('Testing sort_tuples')
    
    # First test
    a = [(1,2,3),(1,3,2),(2,3,1),(3,2,1)]
    b = a[:]
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)
    
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)
    
    # Second test
    a = [(1,),(1,2),(1,2,3),(1,2,3,4)]
    b = a[:]
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)
    
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)
    
    # Third test
    a = [(1,),(1,2),(1,2,3),(1,2,3,4),(1,2,4),(1,2,4,0),(1,2,4,1),(1,3)]
    b = a[:]
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)
    
    scramble(b)
    result = funcs.sort_tuples(b)
    introcs.assert_equals(None,result)
    introcs.assert_equals(a,b)


if __name__ == '__main__':
    test_push_up()
    test_isort()
    test_compare_tuple()
    test_sort_tuples()
    print('The module funcs passed all tests.')