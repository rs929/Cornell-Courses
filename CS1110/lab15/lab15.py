"""
A module with several recursive functions

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b.

    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    # HINT: Divide and conquer only applies to one of the arguments, not all three
    #Handle Small Data
    if a not in thelist:
        result = thelist[:]
        return result
    elif len(thelist)==1:
        result = list([b])
        return result
    #Break into 2 parts
    left = thelist[0]
    right = thelist[1:]
    return replace(list([left]), a, b) + replace(right, a, b)


def oddsevens(thelist):
    """
    Returns a COPY of the list with odds at front, evens in the back.

    Odd numbers are in the same order as thelist. Evens are reversed.

    Example:
        oddsevens([3,4,5,6]) returns [3,5,6,4].
        oddsevens([2,3,4,5,6]) returns [3,5,6,4,2].
        oddsevens([1,2,3,4,5,6]) returns [1,3,5,6,4,2].

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints (may be empty)
    """
    # HINT: How you break up the list is important.  A bad division will
    # make it almost impossible to combine the answer together.
    # However, if you look at all three examples in the specification you
    # will see a pattern that should help you define the recursion.
    #Handle Small Data
    if len(thelist) == 0:
        return thelist
    #Break into Parts
    left = thelist[:1]
    right = thelist[1:]

    right = oddsevens(right)

    if left[0] % 2 == 0:
        return right + left
    if left[0] % 2 != 0:
        return left + right


# OPTIONAL EXERCISES

def flatten(thelist):
    """
    Returns a COPY of thelist flattened to remove all nested lists

    Flattening takes any nested list and recursively dumps its contents into the
    parent list.

    Examples:
        flatten([[1,2],[3,4]]) is [1,2,3,4]
        flatten([[1,[2,3]],[[4],[5,[6,7]]]]) is [1,2,3,4,5,6,7]
        flatten([1,2,3]) is [1,2,3]

    Parameter thelist: the list to flatten
    Precondition: thelist is a list of either ints or lists which satisfy the precondition
    """
    if thelist == []:
        return thelist

    left = thelist[:1]
    right = thelist[1:]

    if type(left[0]) == list:
        left = flatten(left[0])
    return left + flatten(right)



### Numeric Examples ###

def sum_to(n):
    """
    Returns the sum of numbers 1 to n.

        Example: sum_to(3) = 1+2+3 = 6,
        Example: sum_to(5) = 1+2+3+4+5 = 15

    Parameter n: the number of ints to sum
    Precondition: n >= 1 is an int.
    """
    if n == 1:
        return 1

    return sum_to(n-1)+n


def num_digits(n):
    """
    Returns the number of the digits in the decimal representation of n.

        Example: num_digits(0) = 1
        Example: num_digits(3) = 1
        Example: num_digits(34) = 2
        Example: num_digits(1356) = 4

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int
    """
    if n < 10:
        return 1

    return num_digits(n//10) + 1


def sum_digits(n):
    """
    Returns the sum of the digits in the decimal representation of n.

        Example: sum_digits(0) = 0
        Example: sum_digits(3) = 3
        Example: sum_digits(34) = 7
        Example: sum_digits(345) = 12

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int.
    """
    if n < 10:
        return n

    return sum_digits(n//10) + sum_digits(n%10)


def number2(n):
    """
    Returns the number of 2's in the decimal representation of n.

        Example: number2(0) = 0
        Example: number2(2) = 1
        Example: number2(234252) = 3

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int.
    """
    if n < 10 and n != 2:
        return 0
    if n == 2:
        return 1

    return number2(n//10) + number2(n%10)


def into(n, c):
    """
    Returns the number of times that c divides n,

        Example: into(5,3) = 0 because 3 does not divide 5.
        Example: into(3*3*3*3*7,3) = 4.

    Parameter n: the number to analyze
    Precondition: n >= 1 is an int

    Parameter c: the number to divide by
    Precondition: c > 1 are ints.
    """
    if n == c:
        return 1
    if n%c != 0:
        return 0

    return into(n/c, c) + 1


# IF YOU REALLY WANT A CHALLENGE
def related(p,q):
    """
    Returns True if Persons p and q are related; False otherwise.

    We say that two people are related if they have a common person in their family
    tree (including themselves). A recursive way of saying this is that they are
    related if

        (1) they are the same person, or
        (2) one is related to an ancestor (parent, grandparent, etc.) of another

    If either p or q is None, this function returns False.

    Parameter p: a person to compare
    Precondition: p is a Person object OR None

    Parameter q: a person to compare
    Precondition: q is a Person object OR None
    """
    if p == None or q == None:
        return False
    elif p == q:
        return True

    m1 = p.mom
    m2 = q.mom
    d1 = p.dad
    d2 = q.dadz

    return related(m1,m2) or related(d1,d2) or related(m1,d2) or related(m2, d1)
