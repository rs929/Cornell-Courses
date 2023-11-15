"""
A test script to verify the generators

Author: Walker M. White (wmw2)
Date: November 15, 2021
"""
import introcs
import gens


def add_one(x):
    """
    Returns x+1
    """
    return x+1


def test_emit_alpha():
    """
    A test procedure for the generator emit_alpha
    """
    print('Testing emit_alpha')
    
    # First test
    g = gens.emit_alpha('ab12c!')
    
    result = next(g)
    introcs.assert_equals('a',result)
    
    result = next(g)
    introcs.assert_equals('b',result)
    
    result = next(g)
    introcs.assert_equals('c',result)
    
    introcs.assert_error(next,g,error=StopIteration)

    # Second test
    g = gens.emit_alpha('3X6y#Z')
    
    result = next(g)
    introcs.assert_equals('X',result)
    
    result = next(g)
    introcs.assert_equals('y',result)
    
    result = next(g)
    introcs.assert_equals('Z',result)
    
    introcs.assert_error(next,g,error=StopIteration)
    
    # Third test
    g = gens.emit_alpha('123$')
    
    introcs.assert_error(next,g,error=StopIteration)


def test_pair_swap():
    """
    A test procedure for the generator pair_swap
    """
    print('Testing pair_swap')
    
    # First test
    g = gens.pair_swap(range(4))
    
    result = next(g)
    introcs.assert_equals(1,result)
    
    result = next(g)
    introcs.assert_equals(0,result)
    
    result = next(g)
    introcs.assert_equals(3,result)

    result = next(g)
    introcs.assert_equals(2,result)
    
    introcs.assert_error(next,g,error=StopIteration)

    # Second test
    g = gens.pair_swap(range(5))
    
    result = next(g)
    introcs.assert_equals(1,result)
    
    result = next(g)
    introcs.assert_equals(0,result)
    
    result = next(g)
    introcs.assert_equals(3,result)

    result = next(g)
    introcs.assert_equals(2,result)
    
    result = next(g)
    introcs.assert_equals(4,result)
    
    introcs.assert_error(next,g,error=StopIteration)

    # Third test
    g = gens.pair_swap('ab12c')
    
    result = next(g)
    introcs.assert_equals('b',result)
    
    result = next(g)
    introcs.assert_equals('a',result)
    
    result = next(g)
    introcs.assert_equals('2',result)

    result = next(g)
    introcs.assert_equals('1',result)

    result = next(g)
    introcs.assert_equals('c',result)
    
    introcs.assert_error(next,g,error=StopIteration)
    
    # Fourth test (prevent len from being used)
    g = gens.pair_swap(map(add_one,(-1,1,0,2,-2)))

    result = next(g)
    introcs.assert_equals(2,result)
    
    result = next(g)
    introcs.assert_equals(0,result)
    
    result = next(g)
    introcs.assert_equals(3,result)

    result = next(g)
    introcs.assert_equals(1,result)

    result = next(g)
    introcs.assert_equals(-1,result)
    
    introcs.assert_error(next,g,error=StopIteration)
    
    # Fifth test
    g = gens.pair_swap('')
    
    introcs.assert_error(next,g,error=StopIteration)


if __name__ == '__main__':
    test_emit_alpha()
    test_pair_swap()
    print('The module gens passed all tests.')