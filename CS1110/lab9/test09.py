"""
Unit tests for the time functions ONLY.

Because you are new to testing files on objects, and to keep the lab short, we
have provided test cases for you.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""
import introcs
import lab09
from clock import Time

def text_add_time1():
    """
    Test the function add_time1.
    """
    print('Testing add_time1')
    
    t = Time(1,30)
    s = Time(2,10)
    result = lab09.add_time1(t,s)
    introcs.assert_equals( 3,result.hours)
    introcs.assert_equals(40, result.minutes)
    
    # Make sure they were not modified
    introcs.assert_equals( 1, t.hours,'Procedure project modified time1')
    introcs.assert_equals(30, t.minutes,'Procedure project modified time1')
    introcs.assert_equals( 2, s.hours,'Procedure project modified time2')
    introcs.assert_equals(10, s.minutes,'Procedure project modified time2')
    
    t = Time(1,30)
    s = Time(3,40)
    result = lab09.add_time1(t,s)
    introcs.assert_equals( 5,result.hours)
    introcs.assert_equals(10, result.minutes)
    
    # Make sure they were not modified
    introcs.assert_equals( 1, t.hours,'Procedure project modified time1')
    introcs.assert_equals(30, t.minutes,'Procedure project modified time1')
    introcs.assert_equals( 3, s.hours,'Procedure project modified time2')
    introcs.assert_equals(40, s.minutes,'Procedure project modified time2')
    
    t = Time(12,29)
    s = Time(13,30)
    result = lab09.add_time1(t,s)
    introcs.assert_equals(25,result.hours)
    introcs.assert_equals(59, result.minutes)
    
    # Make sure they were not modified
    introcs.assert_equals(12, t.hours,'Procedure project modified time1')
    introcs.assert_equals(29, t.minutes,'Procedure project modified time1')
    introcs.assert_equals(13, s.hours,'Procedure project modified time2')
    introcs.assert_equals(30, s.minutes,'Procedure project modified time2')
    
    t = Time(1,59)
    s = Time(3,2)
    result = lab09.add_time1(t,s)
    introcs.assert_equals(5,result.hours)
    introcs.assert_equals(1, result.minutes)
    
    # Make sure they were not modified
    introcs.assert_equals( 1, t.hours,'Procedure project modified time1')
    introcs.assert_equals(59, t.minutes,'Procedure project modified time1')
    introcs.assert_equals( 3, s.hours,'Procedure project modified time2')
    introcs.assert_equals( 2, s.minutes,'Procedure project modified time2')


def test_add_time2():
    """
    Test the function add_time2.
    """
    print('Testing add_time2')
    
    t = Time(1,30)
    s = Time(2,10)
    result = lab09.add_time2(t,s)
    introcs.assert_equals(None,result,'Procedure add_time2 has a return value')
    introcs.assert_equals( 3, t.hours)
    introcs.assert_equals(40, t.minutes)

    # Make sure s was not modified
    introcs.assert_equals( 2, s.hours,'Procedure project modified time2')
    introcs.assert_equals(10, s.minutes,'Procedure project modified time2')
    
    t = Time(1,30)
    s = Time(3,40)
    result = lab09.add_time2(t,s)
    introcs.assert_equals(None,result,'Procedure add_time2 has a return value')
    introcs.assert_equals( 5, t.hours)
    introcs.assert_equals(10, t.minutes)
    
    # Make sure s was not modified
    introcs.assert_equals( 3, s.hours,'Procedure project modified time2')
    introcs.assert_equals(40, s.minutes,'Procedure project modified time2')
    
    t = Time(12,29)
    s = Time(13,30)
    result = lab09.add_time2(t,s)
    introcs.assert_equals(None,result,'Procedure add_time2 has a return value')
    introcs.assert_equals(25, t.hours)
    introcs.assert_equals(59, t.minutes)
    
    # Make sure s was not modified
    introcs.assert_equals(13, s.hours,'Procedure project modified time2')
    introcs.assert_equals(30, s.minutes,'Procedure project modified time2')
    
    t = Time(1,59)
    s = Time(3,2)
    result = lab09.add_time2(t,s)
    introcs.assert_equals(None,result,'Procedure add_time2 has a return value')
    introcs.assert_equals(5, t.hours)
    introcs.assert_equals(1, t.minutes)
    
    # Make sure s was not modified
    introcs.assert_equals( 3, s.hours,'Procedure project modified time2')
    introcs.assert_equals( 2, s.minutes,'Procedure project modified time2')


if __name__ == '__main__':
    text_add_time1()
    test_add_time2()
    print('Module lab09 passed all (Time) tests.')
