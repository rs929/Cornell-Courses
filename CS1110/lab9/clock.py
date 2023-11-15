"""
Module that provides a simple Time class

This class illustrates the concept of invariants, which you will see later
in Assignment 3.  Invariants limit what values can be assigned to the attributes
of an object.

You are not expected to understand any of the code in this file.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""


class Time(object):
    """
    An instance represents a unit of time.
    
    Attributes:
        hours:   Time in hours   [int, must be nonnegative]
        minutes: Time in minutes [int in the rage 0..59]
    """
    
    # Properties
    @property
    def hours(self):
        """
        The number of hours in this time.
        
        **Invariant**: Value must be a positive int.
        """
        return self._hours
       
    @hours.setter
    def hours(self, value):
        assert (type(value) == int), "value %s is not an int" % repr(value)
        assert (value >= 0), "value %s is not nonnegative" % repr(value)
        self._hours = value
    
    @property
    def minutes(self):
        """
        The number of minutes in this time.
        
        **Invariant**: Value must be an int between 0 and 59, inclusive.
        """
        return self._minutes
       
    @minutes.setter
    def minutes(self, value):
        assert (type(value) == int), "value %s is not an int" % repr(value)
        assert (value >= 0 and value <= 59), "value %s is outside of range [0,59]" % repr(value)
        self._minutes = value
    
    
    # Initializer
    def __init__(self,hours,minutes):
        """
        **Constructor**: creates a new Time object with the given hours, minutes.
        
        Precondition: hours is a nonnegative int.  Minutes is an int between
        0 and 59, inclusive.
        """
        self.hours = hours
        self.minutes = minutes
    
    def __eq__(self, other):
        """
        Returns: True if self and other are equivalent Time objects. 
        """
        return (type(other) == Time and self.hours == other.hours and 
                self.minutes == other.minutes)
    
    def __ne__(self, other):
        """
        Returns: True if self and other are not equivalent Time objects. 
        """
        return not (self == other)
    
    def __str__(self):
        """
        Returns: Readable string representation of this time. 
        """
        min = str(self.minutes)
        if self.minutes < 10:
            min = '0'+min
        return str(self.hours)+":"+min
    
    def __repr__(self):
        """
        Returns: Unambiguous String representation of this time. 
        """
        return "%s(%s)" % (self.__class__,self.__str__())