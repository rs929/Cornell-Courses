"""
The for-loop functions for Lab 16.

These functions all require for-loops.  They include looping over lists,
nested-lists, and dictionaries.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL FOUR OF THESE FUNCTIONS

def clamp(alist,min,max):
    """
    MODIFIES the list so that every element is between min and max.

    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.

    This is a PROCEDURE. It modifies alist, but does not return a new list.

    Example: if alist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    alist to have [0,1,3,4] as its contents.

    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)

    Parameter min: the minimum value for the list
    Precondition: min <= max is a number

    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    for x in alist:
        ind = alist.index(x)
        if x < min:
            alist[ind] = min
        elif x > max:
            alist[ind] = max
        else:
            alist[ind] = x


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only
    numbers in it.

    Example: row_sums([[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]])
    returns [0.9, 1.5, 1.7]

    Example: row_sums([[0.2, 0.1], [-0.2, 0.1], [0.2, -0.1], [-0.2, -0.1]])
    returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with no header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) each row contains
    only numbers, and (3) each row is the same length.
    """
    list = []
    for x in table:
        list.append(sum(x))
    return list


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This
    function returns a new dictionary with netids for keys and letter grades
    (strings) for values.  Our cut-off is 90 for an A, 80 for a B, 70 for a C,
    60 for a D.  Anything below 60 is an F.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values
    """
    dict = {}
    for x in adict:
        if adict[x] >= 90:
            dict[x] = 'A'
        elif adict[x] < 90 and adict[x] >=80:
            dict[x] = 'B'
        elif adict[x] < 80 and adict[x] >=70:
            dict[x] = 'C'
        elif adict[x] < 70 and adict[x] >=60:
            dict[x] = 'D'
        elif adict[x] < 60:
            dict[x] = 'F'
    return dict

    # HINT: You will need a dictionary that acts as an accumulator
    # Start with result = {}.  Then add to this dictionary.
    pass # Implement me


### OPTIONAL EXERCISES ###

def uniques(alist):
    """
    Returns the number of unique elements in the list.

    Example: uniques([5, 9, 5, 7]) evaluates to 3
    Example: uniques([5, 5, 1, 'a', 5, 'a']) evaluates to 3

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    # Create a copy with no duplicates
    pass # Implement me


def removeall(alist,n):
    """
    Returns a copy of alist, removing all instances of n

    Example: removeall([1,2,2,3,1],1) returns [2,2,3]
    Example: removeall([1,2,2,3,1],2) returns [1,3,1]
    Example: removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
    Example: removeall([1,1,1],1) returns []
    Example: removeall([],1) returns []

    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)

    Parameter n: the number to remove
    Precondition: n is a number
    """
    pass # Implement me


def place_sums(table):
    """
    MODIFIES the table to add a column summing previous elements in the row.

    This function assumes that table has a header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends
    the sum of that row.

    This is a PROCEDURE. It modifies the table, but does not return a new table.

    Example: Suppose that a is

        [['First', 'Second', 'Third'],
         [0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]]

    then place_sums(a) modifies the table a so that it is now

         [['First', 'Second', 'Third', 'Sum'],
          [0.1, 0.3, 0.5, 0.9], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """
    pass # Implement me


def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.

    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
    Example: crossout([[1,3],[6,2]],0,0) returns [[2]]
    Example: crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    # This is easier if you loop over positions, not elements
    pass # Implement me


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This
    function averages those grades and returns a value.

    Example: letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to (55+90+86)/3 = 77.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values
    """
    pass # Implement me


def convert_grades(adict):
    """
    MODIFIES the dictionary to replace numerical grades with letter grades.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam. This
    function replaces all numerical grades with letter grades (strings)
    for values. Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for
    a D. Anything below 60  is an F.

    This is a PROCEDURE. It modifies the dictionary, but does not return a
    new dictionary.

    Example: If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a)
             changes a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
    Example: If a = {}, letter_grades(a) changes a to {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    pass # Implement me


def drop_below(adict,limit):
    """
    Deletes all students in the dictionary with grades below limit.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.

    This is a PROCEDURE. It modifies the dictionary, but does not return a
    new dictionary.


    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints

    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    # Hint: Create a list of netids to drop, and THEN drop them
    pass # Implement me
