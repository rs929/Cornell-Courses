"""
Unit tests for extra.py

This file is to help you with the optional function. There is nothing for you to do here.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""
import introcs
import extra


def test_europeanize():
    """
    Test the function europeanize.
    """
    print('Testing europeanize')
    
    result = extra.europeanize('3/6/12') 
    introcs.assert_equals('06/03/12',result)

    result = extra.europeanize('12/11/19')
    introcs.assert_equals('11/12/19',result)
    
    result = extra.europeanize('01/29/11')
    introcs.assert_equals('29/01/11',result)
    
    result = extra.europeanize('3/29/17')
    introcs.assert_equals('29/03/17',result)
    
    result = extra.europeanize('12/4/18')
    introcs.assert_equals('04/12/18',result)


if __name__ == '__main__':
    test_europeanize()
    print('Module extra passed all tests.')
