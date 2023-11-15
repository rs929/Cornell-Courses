"""
Unit tests for extras.py

This file is to help you with the optional functions. There is nothing for you to do
here.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""
import introcs
import extras


def test_normalize():
    """
    Test the function normalize.
    """
    print('Testing normalize')
    
    v = introcs.Vector2(1,0)
    result = extras.normalize(v)
    introcs.assert_equals(None,result,'Procedure normalize has a return value')
    introcs.assert_floats_equal(1,v.x)
    introcs.assert_floats_equal(0,v.y)
    
    v = introcs.Vector2(0,1)
    result = extras.normalize(v)
    introcs.assert_equals(None,result,'Procedure normalize has a return value')
    introcs.assert_floats_equal(0,v.x)
    introcs.assert_floats_equal(1,v.y)
    
    v = introcs.Vector2(0,0)
    result = extras.normalize(v)
    introcs.assert_equals(None,result,'Procedure normalize has a return value')
    introcs.assert_floats_equal(0,v.x)
    introcs.assert_floats_equal(0,v.y)
    
    v = introcs.Vector2(1,1)
    result = extras.normalize(v)
    introcs.assert_equals(None,result,'Procedure normalize has a return value')
    introcs.assert_floats_equal(0.70710678,v.x)
    introcs.assert_floats_equal(0.70710678,v.y)
    
    v = introcs.Vector2(-2,3)
    result = extras.normalize(v)
    introcs.assert_equals(None,result,'Procedure normalize has a return value')
    introcs.assert_floats_equal(-0.55470020,v.x)
    introcs.assert_floats_equal( 0.83205029,v.y)


def test_project():
    """
    Test the function project.
    """
    print('Testing project')
    
    u = introcs.Vector2(-2,3)
    v = introcs.Vector2(1,0)
    result = extras.project(u,v)
    introcs.assert_floats_equal(-2,result.x)
    introcs.assert_floats_equal(0,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(-2,u.x,'Procedure project modified u')
    introcs.assert_equals(3,u.y,'Procedure project modified u')
    introcs.assert_equals(1,v.x,'Procedure project modified v')
    introcs.assert_equals(0,v.y,'Procedure project modified v')
    
    # Swap and test
    result = extras.project(v,u)
    introcs.assert_floats_equal( 0.307692307,result.x)
    introcs.assert_floats_equal(-0.461538461,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(-2,u.x,'Procedure project modified u')
    introcs.assert_equals(3,u.y,'Procedure project modified u')
    introcs.assert_equals(1,v.x,'Procedure project modified v')
    introcs.assert_equals(0,v.y,'Procedure project modified v')
    
    u = introcs.Vector2(4,2)
    v = introcs.Vector2(0,1)
    result = extras.project(u,v)
    introcs.assert_floats_equal(0,result.x)
    introcs.assert_floats_equal(2,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(4,u.x,'Procedure project modified u')
    introcs.assert_equals(2,u.y,'Procedure project modified u')
    introcs.assert_equals(0,v.x,'Procedure project modified v')
    introcs.assert_equals(1,v.y,'Procedure project modified v')
    
    # Swap and test
    result = extras.project(v,u)
    introcs.assert_floats_equal( 0.4,result.x)
    introcs.assert_floats_equal( 0.2,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(4,u.x,'Procedure project modified u')
    introcs.assert_equals(2,u.y,'Procedure project modified u')
    introcs.assert_equals(0,v.x,'Procedure project modified v')
    introcs.assert_equals(1,v.y,'Procedure project modified v')
    
    u = introcs.Vector2(4,1)
    v = introcs.Vector2(1,3)
    result = extras.project(u,v)
    introcs.assert_floats_equal(0.7,result.x)
    introcs.assert_floats_equal(2.1,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(4,u.x,'Procedure project modified u')
    introcs.assert_equals(1,u.y,'Procedure project modified u')
    introcs.assert_equals(1,v.x,'Procedure project modified v')
    introcs.assert_equals(3,v.y,'Procedure project modified v')
    
    # Swap and test
    result = extras.project(v,u)
    introcs.assert_floats_equal(1.647058824,result.x)
    introcs.assert_floats_equal(0.411764706,result.y)
    
    # Make sure they were not modified
    introcs.assert_equals(4,u.x,'Procedure project modified u')
    introcs.assert_equals(1,u.y,'Procedure project modified u')
    introcs.assert_equals(1,v.x,'Procedure project modified v')
    introcs.assert_equals(3,v.y,'Procedure project modified v')


if __name__ == '__main__':
    test_normalize()
    test_project()
    print('Module extras passed all tests.')
