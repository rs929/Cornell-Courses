"""
A test script for Lab 12

These unit tests are for the functions in lists.py.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""
import introcs
import lists


def test_put_in():
    """
    Test procedure for function put_in
    """
    print('Testing function put_in')

    alist = [0,1,2,4]
    result = lists.put_in(alist,3)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([0,1,2,3,4],alist)

    result = lists.put_in(alist,-1)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([-1,0,1,2,3,4],alist)

    result = lists.put_in(alist,2)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([-1,0,1,2,2,3,4],alist)

    result = lists.put_in(alist,0)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([-1,0,0,1,2,2,3,4],alist)

    alist = []
    result = lists.put_in(alist,0)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([0],alist)

    result = lists.put_in(alist,1)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([0,1],alist)


def test_replace_first():
    """
    Test procedure for function replace_first
    """
    print('Testing function replace_first')
    thelist  = [5, 9, 5, 7, 3, 10, 4]
    original = thelist[:]

    # This should return nothing and not modify the list.
    result = lists.replace_first(thelist,2,8)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals(original,thelist) #If fails, modified the list.

    result = lists.replace_first(thelist,9,-1)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([5, -1, 5, 7, 3, 10, 4],thelist)

    result = lists.replace_first(thelist,5,2)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([2, -1, 5, 7, 3, 10, 4],thelist)

    result = lists.replace_first(thelist,5,2)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([2, -1, 2, 7, 3, 10, 4],thelist)

    result = lists.replace_first(thelist,5,2)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([2, -1, 2, 7, 3, 10, 4],thelist)

    result = lists.replace_first(thelist,4,-1)
    introcs.assert_equals(None,result)      #If fails, a value returned
    introcs.assert_equals([2, -1, 2, 7, 3, 10, -1],thelist)


def test_lesser_than():
    """
    Test procedure for function lesser_than
    """
    print('Testing function lesser_than')
    thelist = [5, 9, 5, 7, 3, 10, 4]
    introcs.assert_equals(2,lists.lesser_than(thelist,5))
    introcs.assert_equals(1,lists.lesser_than(thelist,4))
    introcs.assert_equals(0,lists.lesser_than(thelist,3))
    introcs.assert_equals(4,lists.lesser_than(thelist,6))
    introcs.assert_equals(6,lists.lesser_than(thelist,10))
    introcs.assert_equals(7,lists.lesser_than(thelist,20))


# Script code
if __name__ == '__main__':
    test_put_in()
    test_replace_first()
    test_lesser_than()
    print('Module lists passed all tests.')
