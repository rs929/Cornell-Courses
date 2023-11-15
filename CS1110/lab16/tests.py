"""
A unit test for Lab 16

Author: Walker M. White (wmw2)
Date:   October 20, 2021
"""
import introcs
import funcs
import copy
import traceback


def test_clamp():
    """
    Test procedure for function clamp
    """
    print('Testing function clamp')

    thelist = [-1, 1, 3, 5]
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([0,1,3,4],thelist)

    thelist = [1, 3]
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([1,3],thelist)

    thelist = [-1, 1, 3, 5]
    funcs.clamp(thelist,1,1)
    introcs.assert_equals([1,1,1,1],thelist)

    thelist = []
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([],thelist)


def test_row_sums():
    """
    Test procedure for function row_sums

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function row_sums')
    result = funcs.row_sums([[0.8, 0.2], [0.6, 0.9], [0.4, 0.3]])
    introcs.assert_float_lists_equal([1.0, 1.5, 0.7],result)
    result = funcs.row_sums([[0.2, -0.6, 0.1], [0.9, 0.8, -1.0]])
    introcs.assert_float_lists_equal([-0.3, 0.7],result)
    result = funcs.row_sums([[0.4, 0.8, 0.5, 0.4]])
    introcs.assert_float_lists_equal([2.1],result)
    result = funcs.row_sums([[0.3], [0.5], [0.8], [0.4]])
    introcs.assert_float_lists_equal([0.3, 0.5, 0.8, 0.4],result)


def test_letter_grades():
    """
    Test procedure for function letter_grades
    """
    print('Testing function letter_grades')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    actual = ['F',    'A',      'B',     'C',     'A',       'D',     'C'    ]

    inputs = dict(zip(netids[:1],grades[:1]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:1],actual[:1])), result)
    introcs.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:3],grades[:3]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:3],actual[:3])), result)
    introcs.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:5],grades[:5]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:5],actual[:5])), result)
    introcs.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified

    inputs = dict(zip(netids,grades))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids,actual)), result)
    introcs.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


### OPTIONAL EXERCISES ###

def test_uniques():
    """
    Test procedure for function uniques
    """
    print('Testing function uniques')
    thelist = [5, 9, 5, 7]
    introcs.assert_equals(3,funcs.uniques(thelist))

    thelist = [5, 5, 1, 'a', 5, 'a']
    introcs.assert_equals(3,funcs.uniques(thelist))

    thelist = [1, 2, 3, 4, 5]
    introcs.assert_equals(5,funcs.uniques(thelist))

    thelist = []
    introcs.assert_equals(0,funcs.uniques(thelist))

    # Make sure the function does not modify the original
    thelist = [5, 9, 5, 7]
    result  = funcs.uniques(thelist)
    introcs.assert_equals([5, 9, 5, 7],thelist)


def test_removeall():
    """
    Test procedure for removeall
    """
    print('Testing function removeall')

    alist = [1,2,2,3,1]
    result = funcs.removeall(alist,1)
    introcs.assert_equals([2,2,3],result)
    introcs.assert_equals([1,2,2,3,1],alist)

    result = funcs.removeall(alist,2)
    introcs.assert_equals([1,3,1],result)
    introcs.assert_equals([1,2,2,3,1],alist)

    result = funcs.removeall(alist,5)
    introcs.assert_equals([1,2,2,3,1],result)
    introcs.assert_equals([1,2,2,3,1],alist)

    alist = [3,3,3]
    result = funcs.removeall(alist,3)
    introcs.assert_equals([],result)
    introcs.assert_equals([3,3,3],alist)

    alist = [3,3,3]
    result = funcs.removeall(alist,1)
    introcs.assert_equals([3,3,3],result)
    introcs.assert_equals([3,3,3],alist)

    alist = [7]
    result = funcs.removeall(alist,7)
    introcs.assert_equals([],result)
    introcs.assert_equals([7],alist)

    alist = []
    result = funcs.removeall(alist,7)
    introcs.assert_equals([],result)
    introcs.assert_equals([],alist)


def test_place_sums():
    """
    Test procedure for function place_sums

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function place_sums')

    table = [['I1','I2','I3'], [0.8, 0.2], [0.6, 0.9], [0.4, 0.3]]
    goal  = [['I1','I2','I3','Sum'], [0.8, 0.2, 1.0], [0.6, 0.9, 1.5], [0.4, 0.3, 0.7]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2'], [0.2, -0.6, 0.1], [0.9, 0.8, -1.0]]
    goal  = [['I1','I2','Sum'], [0.2, -0.6, 0.1, -0.3], [0.9, 0.8, -1.0, 0.7]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1'], [0.4, 0.8, 0.5, 0.4]]
    goal  = [['I1','Sum'], [0.4, 0.8, 0.5, 0.4, 2.1]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2','I3','I4'], [0.3], [0.5], [0.8], [0.4]]
    goal  = [['I1','I2','I3','I4','Sum'], [0.3, 0.3], [0.5, 0.5], [0.8, 0.8], [0.4, 0.4]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])


def test_crossout():
    """
    Test procedure for function crossout.

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function crossout')

    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = funcs.crossout(table,1,2)
    introcs.assert_float_lists_equal([[0.1,0.3],[1.5,2.3]],result)
    introcs.assert_float_lists_equal(orig,table)

    result = funcs.crossout(table,0,0)
    introcs.assert_float_lists_equal([[0.2,0.7],[2.3,0.4]],result)
    introcs.assert_float_lists_equal(orig,table)

    result = funcs.crossout(table,2,1)
    introcs.assert_float_lists_equal([[0.1,0.5],[0.6,0.7]],result)
    introcs.assert_float_lists_equal(orig,table)

    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4],[0.1,0.2,0.3]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = funcs.crossout(table,1,2)
    introcs.assert_float_lists_equal([[0.1,0.3],[1.5,2.3],[0.1,0.2]],result)
    introcs.assert_float_lists_equal(orig,table)

    table = [[0.1,0.3,0.5,1.0],[0.6,0.2,0.7,2.0],[1.5,2.3,0.4,3.0]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = funcs.crossout(table,1,2)
    introcs.assert_float_lists_equal([[0.1,0.3,1.0],[1.5,2.3,3.0]],result)
    introcs.assert_float_lists_equal(orig,table)

    table = [[1,2],[3,4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = funcs.crossout(table,1,0)
    introcs.assert_float_lists_equal([[2]],result)
    introcs.assert_float_lists_equal(orig,table)

    result = funcs.crossout(table,0,1)
    introcs.assert_float_lists_equal([[3]],result)
    introcs.assert_float_lists_equal(orig,table)

    table = [[5]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = funcs.crossout(table,0,0)
    introcs.assert_equals([],result)
    introcs.assert_float_lists_equal(orig,table)


def test_average_grade():
    """
    Test procedure for function average_grade
    """
    print('Testing function average_grade')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]

    inputs = dict(zip(netids[:1],grades[:1]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(55.0,result)
    introcs.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:3],grades[:3]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(76.666666667,result)
    introcs.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:5],grades[:5]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(80.4,result)
    introcs.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified

    inputs = dict(zip(netids,grades))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(77.428571428,result)
    introcs.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


def test_convert_grades():
    """
    Test procedure for function convert_grades.
    """
    print('Testing function convert_grades')

    grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    answer = {'wmw2': 'F', 'abc3': 'A', 'jms45': 'B'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50}
    answer = {'abc123': 'F','abc456':'D','jms457':'F'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,'xyz456':80,'wmw4':90}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C','xyz456':'B','wmw4':'A'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A','tor3':'B'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'wmw2' : 55, 'abc3' : 90}
    answer = {'wmw2' : 'F', 'abc3' : 'A'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {'abc3' : 90}
    answer = {'abc3' : 'A'}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = {}
    answer = {}
    result = funcs.convert_grades(grades)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)


def test_drop_below():
    """
    Test procedure for function drop_below.
    """
    print('Testing function drop_below')

    orignl = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    answer = {'abc3': 90, 'jms45': 86}
    result = funcs.drop_below(grades,20)
    introcs.assert_equals(None,result)
    introcs.assert_equals(orignl,grades)

    result = funcs.drop_below(grades,55)
    introcs.assert_equals(None,result)
    introcs.assert_equals(orignl,grades)

    result = funcs.drop_below(grades,60)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = copy.deepcopy(orignl)
    result = funcs.drop_below(grades,86)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    grades = copy.deepcopy(orignl)
    result = funcs.drop_below(grades,95)
    introcs.assert_equals(None,result)
    introcs.assert_equals({},grades)

    orignl = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    grades = copy.deepcopy(orignl)
    answer = {'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}

    result = funcs.drop_below(grades,0)
    introcs.assert_equals(None,result)
    introcs.assert_equals(orignl,grades)

    result = funcs.drop_below(grades,80)
    introcs.assert_equals(None,result)
    introcs.assert_equals(answer,grades)

    orignl = {'abc3' : 90}
    grades = {'abc3' : 90}
    result = funcs.drop_below(grades,90)
    introcs.assert_equals(None,result)
    introcs.assert_equals(orignl,grades)

    result = funcs.drop_below(grades,100)
    introcs.assert_equals(None,result)
    introcs.assert_equals({},grades)

    grades = {}
    result = funcs.drop_below(grades,0)
    introcs.assert_equals(None,result)
    introcs.assert_equals({},grades)


# Script code
if __name__ == '__main__':
    test_clamp()
    test_row_sums()
    test_letter_grades()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_uniques()
    #test_removeall()
    #test_place_sums()
    #test_crossout()
    #test_average_grade()
    #test_convert_grades()
    #test_drop_below()
    print('The modules for lab 15 passed all tests')
