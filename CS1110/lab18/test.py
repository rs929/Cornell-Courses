"""
A test script for the class lab

Author: Walker M. White (wmw2)
Date:   November 1, 2020
"""
import introcs
import leng
import traceback


def test_length_init():
    """
    Test procedure for the initializer in the Length class
    """
    print('Testing class Length (__init__)')
    
    try:
        result = leng.Length(13.5,'m')
    except:
        traceback.print_exc() # Display the stack trace
        introcs.quit_with_error("The constructor call Length(13.5,'m') crashed.")
    
    introcs.assert_equals(leng.Length, type(result))
    introcs.assert_true(hasattr(result,'_value'), "Class Length has no attribute '_value'")
    introcs.assert_true(hasattr(result,'_unit'), "Class Length has no attribute '_unit'")
    introcs.assert_floats_equal(13.5, result._value )
    introcs.assert_equals('m', result._unit)
    
    try:
        result = leng.Length(13.5)
    except:
        traceback.print_exc() # Display the stack trace
        introcs.quit_with_error("The constructor call Length(13.5) crashed.")
    
    introcs.assert_equals(leng.Length, type(result))
    introcs.assert_true(hasattr(result,'_value'), "Class Length has no attribute '_value'")
    introcs.assert_true(hasattr(result,'_unit'), "Class Length has no attribute '_unit'")
    introcs.assert_floats_equal(13.5, result._value )
    introcs.assert_equals('ft', result._unit)
    
    # Check for precondition enforcement
    introcs.assert_error(leng.Length,12,message='Class Length does not enforce float values.')
    introcs.assert_error(leng.Length,'12.5',message='Class Length does not enforce float values.')
    introcs.assert_error(leng.Length,12.5,4,message='Class Length does not enforce string units.')
    introcs.assert_error(leng.Length,12.5,'meters',message='Class Length does not enforce unit names.')


def test_length_str():
    """
    Test procedure for the __str__ method in the Length class
    """
    print('Testing class Length (__str__)')
    
    result = leng.Length(13.5,'m')
    introcs.assert_equals('13.5 m', str(result))
    
    result = leng.Length(12.0,'ft')
    introcs.assert_equals('12.0 ft', str(result))
    
    result = leng.Length(1.5,'ft')
    introcs.assert_equals('1.5 ft', str(result))
    
    result = leng.Length(0.0,'m')
    introcs.assert_equals('0.0 m', str(result))


def test_length_unit():
    """
    Test procedure for the encapsulation of _unit in Length
    """
    print('Testing class Length (attribute Unit)')
    
    cls = leng.Length
    introcs.assert_true(hasattr(cls,'getUnit'), "Class Length has no method 'getUnit'")
    introcs.assert_false(hasattr(cls,'setUnit'), "Class Length has an illegal setter for '_unit'")

    result = leng.Length(13.5,'m')
    introcs.assert_equals('m',result.getUnit())

    result = leng.Length(-5.5,'ft')
    introcs.assert_equals('ft',result.getUnit())
    
    result = leng.Length(0.0)
    introcs.assert_equals('ft',result.getUnit())


def test_length_value():
    """
    Test procedure for the encapsulation of _value in Length
    """
    print('Testing class Length (attribute Value)')
    
    cls = leng.Length
    introcs.assert_true(hasattr(cls,'getValue'), "Class Length has no method 'getValue'")
    introcs.assert_true(hasattr(cls,'setValue'), "Class Length has no method 'setValue'")
    
    result = leng.Length(13.5,'m')
    introcs.assert_floats_equal(13.5,result.getValue())
    
    result.setValue(0.25)
    introcs.assert_floats_equal(0.25,result.getValue())
    
    result = leng.Length(0.0)
    introcs.assert_floats_equal(0.0,result.getValue())
    
    result.setValue(-2.5)
    introcs.assert_floats_equal(-2.5,result.getValue())
    
    # Check for precondition enforcement
    introcs.assert_error(result.setValue,12,message='The setter for Length does not enforce float values.')
    introcs.assert_error(result.setValue,'12.5',message='The setter for Length does not enforce float values.')


def test_length_measure():
    """
    Test procedure for the measure method in the Length class
    """
    print('Testing class Length (measure)')
    
    cls = leng.Length
    introcs.assert_true(hasattr(cls,'measure'), "Class Length has no method 'measure'")
    
    result = leng.Length(13.5,'m')
    introcs.assert_floats_equal(13.5,result.measure('m'))
    introcs.assert_floats_equal(44.29133858,result.measure('ft'))
    
    result = leng.Length(12.0,'ft')
    introcs.assert_floats_equal(3.6576,result.measure('m'))
    introcs.assert_floats_equal(12.0,result.measure('ft'))
    
    # Check for precondition enforcement
    introcs.assert_error(result.measure,4,message='Method measure does not enforce string units.')
    introcs.assert_error(result.measure,'meters',message='Method measure does not enforce unit names.')
    


# Script code
if __name__ == '__main__':
    test_length_init()
    test_length_str()
    test_length_unit()
    test_length_value()
    test_length_measure()
    print('The class length passed all tests')
