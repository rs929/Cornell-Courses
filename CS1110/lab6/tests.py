"""
A test script to test the module funcs.py

<YOUR NAME HERE>
<DATE HERE>
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the introcs asserts')
    introcs.assert_equals('b c', 'ab cd'[1:4])
    #introcs.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED

    introcs.assert_true(3 < 4)
    introcs.assert_equals(3, 1+2)

    introcs.assert_equals(3.0, 1.0+2.0)
    #introcs.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED
def test_has_a_vowel():
    """
    This is a simple test procedure to show you if function has_a_vowel is working
    """
    print('Testing function has_a_vowel')
    input='aeiou'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='b'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(False,result)
    input='ae'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='a'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='aba'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='acu'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='bai'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
    input='sleigh'
    result=funcs.has_a_vowel(input)
    introcs.assert_equals(True,result)
test_has_a_vowel()
# SCRIPT CODE (Call Test Procedures here)
test_asserts()
print('Module funcs is working correctly')
