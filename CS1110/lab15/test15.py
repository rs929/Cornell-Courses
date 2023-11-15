"""
Unit test script for Lab 15

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2021
"""
import introcs
import person
import lab15


def test_replace():
    """
    Tests for function replace
    """
    print('Testing replace')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals([],  lab15.replace([], 1, 2))
    introcs.assert_equals([4], lab15.replace([5],5,4))
    introcs.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab15.replace(mylist,3, 20))
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3],   lab15.replace(mylist, 1, 3))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3], mylist)
    introcs.assert_equals(False, mylist is lab15.replace(mylist, 1, 3))


def test_oddsevens():
    """
    Tests for function oddsevens
    """
    print('Testing oddsevens')
    mylist = [1,2,3,4,5,6]
    introcs.assert_equals([],     lab15.oddsevens([]))
    introcs.assert_equals([3],    lab15.oddsevens([3]))
    introcs.assert_equals([3,4],  lab15.oddsevens([4,3]))
    introcs.assert_equals([-1,1,2,0],    lab15.oddsevens([-1,0,1,2]))
    introcs.assert_equals([1,3,5,6,4,2], lab15.oddsevens(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,3,4,5,6], mylist)
    introcs.assert_equals(False, mylist is lab15.oddsevens(mylist))


### OPTIONAL EXERCISES ###

# Sequences Examples #

def test_flatten():
    """
    Tests for function flatten
    """
    print('Testing flatten')
    introcs.assert_equals([],  lab15.flatten([]))
    introcs.assert_equals([3], lab15.flatten([3]))
    introcs.assert_equals([3], lab15.flatten([[3]]))
    introcs.assert_equals([1,2,3,4], lab15.flatten([[1,2],[3,4]]))
    introcs.assert_equals([1,2,3,4,5,6,7], lab15.flatten([[1,[2,3]],[[4,[5,6]],7]]))
    introcs.assert_equals([1,2,3], lab15.flatten([1,2,3]))
    introcs.assert_equals([],  lab15.flatten([[[]],[]]))


def test_sum_to():
    """
    Tests for function sum_to
    """
    print('Testing sum_to')
    introcs.assert_equals(1,  lab15.sum_to(1))
    introcs.assert_equals(6,  lab15.sum_to(3))
    introcs.assert_equals(15, lab15.sum_to(5))


def test_num_digits():
    """
    Tests for function num_digits
    """
    print('Testing num_digits')
    introcs.assert_equals(1, lab15.num_digits(0))
    introcs.assert_equals(1, lab15.num_digits(3))
    introcs.assert_equals(2, lab15.num_digits(34))
    introcs.assert_equals(4, lab15.num_digits(1356))


def test_sum_digits():
    """
    Tests for function sum_digits
    """
    print('Testing sum_digits')
    introcs.assert_equals(0,  lab15.sum_digits(0))
    introcs.assert_equals(3,  lab15.sum_digits(3))
    introcs.assert_equals(7,  lab15.sum_digits(34))
    introcs.assert_equals(12, lab15.sum_digits(345))


def test_number2():
    """
    Tests for function number2
    """
    print('Testing number2')
    introcs.assert_equals(0, lab15.number2(0))
    introcs.assert_equals(1, lab15.number2(2))
    introcs.assert_equals(2, lab15.number2(232))
    introcs.assert_equals(0, lab15.number2(333))
    introcs.assert_equals(3, lab15.number2(234252))


def test_into():
    """
    Tests for function into
    """
    print('Testing into')
    introcs.assert_equals(0, lab15.into(5, 3))
    introcs.assert_equals(1, lab15.into(6, 3))
    introcs.assert_equals(2, lab15.into(9, 3))
    introcs.assert_equals(2, lab15.into(18, 3))
    introcs.assert_equals(4, lab15.into(3*3*3*3*7,3))


def test_related():
    """
    Tests for function related
    """
    print('Testing related')
    # GRANDPARENTS
    # John Smith Jr.
    gd1 = person.Person('John','Smith')
    gm1 = person.Person('Jane','Dare')

    gd2 = person.Person('John','Evans')
    gm2 = person.Person('Ellen',"O'Reilly")

    # PARENTS & Uncles
    # John Smith III
    d = person.Person('John','Smith',gm1,gd1)
    m = person.Person('Pamela','Evans',gm2,gd2)
    u = person.Person('Roger','Smith',gm1,gd1)

    # FINAL GENERATION
    # John Smith IV
    p = person.Person('John','Smith',m,d)
    s = person.Person('Ellen','Smith',m,d)
    c = person.Person('Douglas','Smith',None,u)

    introcs.assert_false(lab15.related(p,None))
    introcs.assert_false(lab15.related(None,p))
    introcs.assert_false(lab15.related(None,None))
    introcs.assert_true(lab15.related(p,p))
    introcs.assert_true(lab15.related(p,s))
    introcs.assert_true(lab15.related(p,c))
    introcs.assert_true(lab15.related(d,u))
    introcs.assert_false(lab15.related(m,u))


# Script Code
if __name__ == '__main__':
    test_replace()
    test_oddsevens()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    test_flatten()
    test_sum_to()
    test_num_digits()
    test_sum_digits()
    test_number2()
    test_into()
    test_related()
    print('Module lab15 passed all tests.')
