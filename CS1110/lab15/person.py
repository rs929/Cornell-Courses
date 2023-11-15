"""
A class to rerpresent a genealogical tree

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""


class Person(object):
    """
    A class to represent a person in a genealogical tree.

    INSTANCE ATTRIBUTES:
        fname: First Name [str]
        lname: Last Name  [str]
        mom:   Mother     [Person, None if not known]
        dad:   Father     [Person, None if not known]"""

    def __init__(self,fname,lname,mom=None,dad=None):
        """
        Creates a new instance of person

        Parameter fname: The first name
        Precondition: fname is a string

        Parameter lname: The last name
        Precondition: lname is a string

        Parameter mom: The mother of this person (optional)
        Precondition: mom is a Person or None

        Parameter dad: The father of this person (optional)
        Precondition: dad is a Person or None
        """
        self.fname = fname
        self.lname = lname
        self.mom = mom
        self.dad = dad

    def __str__(self):
        """
        Returns a string representation of this person
        """
        result = '(Person: '+self.name()

        if not self.mom is None:
            result += '; mom: '+self.mom.name()

        if not self.dad is None:
            result += '; dad: '+self.dad.name()

        return result+')'

    def __repr__(self):
        """
        Returns an unambigious string representation of this person
        """
        return str(self)

    def name(self):
        """
        Returns the full name of this person
        """
        return self.fname+' '+self.lname

