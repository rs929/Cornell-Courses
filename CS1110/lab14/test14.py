"""
Unit test script for Lab 13

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2019
"""
import introcs
import lab14


def test_sum_list():
    """
    Tests for function sum_list
    """
    print('Testing sum_list')
    introcs.assert_equals(0,  lab14.sum_list([]))
    introcs.assert_equals(34, lab14.sum_list([34]))
    introcs.assert_equals(46, lab14.sum_list([7,34,1,2,2]))


def test_numberof():
    """
    Tests for function numberof
    """
    print('Testing numberof')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab14.numberof([],4))
    introcs.assert_equals(1, lab14.numberof([4],4))
    introcs.assert_equals(3, lab14.numberof(mylist,74))
    introcs.assert_equals(2, lab14.numberof(mylist,3))
    introcs.assert_equals(0, lab14.numberof(mylist,4))


### OPTIONAL EXERCISES ###

# Sequences Examples #

def test_remove_dups():
    """
    Tests for function remove_dups
    """
    print('Testing remove_dups')
    mylist = [1,2,2,3,3,3,4,5,1,1,1]
    introcs.assert_equals([],  lab14.remove_dups([]))
    introcs.assert_equals([3], lab14.remove_dups([3,3]))
    introcs.assert_equals([4], lab14.remove_dups([4]))
    introcs.assert_equals([5], lab14.remove_dups([5, 5]))
    introcs.assert_equals([1,2,3,4,5,1], lab14.remove_dups(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,2,3,3,3,4,5,1,1,1], mylist)
    introcs.assert_equals(False, mylist is lab14.remove_dups(mylist))


def test_number_not():
    """
    Tests for function number_not
    """
    print('Testing number_not')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab14.number_not([],4))
    introcs.assert_equals(0, lab14.number_not([4],4))
    introcs.assert_equals(4, lab14.number_not(mylist,74))
    introcs.assert_equals(5, lab14.number_not(mylist,3))
    introcs.assert_equals(7, lab14.number_not(mylist,4))


def test_remove_first():
    """
    Tests for function remove_first
    """
    print('Testing remove_first')
    introcs.assert_equals([],  lab14.remove_first([],3))
    introcs.assert_equals([],  lab14.remove_first([3],3))
    introcs.assert_equals([3], lab14.remove_first([3],4))
    introcs.assert_equals([3, 4, 4, 5],    lab14.remove_first([3, 4, 4, 4, 5],4))
    introcs.assert_equals([3, 5, 4, 4, 4], lab14.remove_first([3, 4, 5, 4, 4, 4],4))


# Script Code
if __name__ == '__main__':
    test_sum_list()
    test_numberof()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_remove_dups()
    #test_number_not()
    #test_remove_first()

    print('Module lab14 passed all tests.')
