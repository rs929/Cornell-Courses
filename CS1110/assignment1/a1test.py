"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Noelle Pappous (ntp26) Richie Sun (rs929)
Date:   09/18/21
"""
import introcs
import a1


def testA():
    """
    Test procedure for Part A
    """
    #testing before_space function
    result = a1.before_space('sss ddd')
    introcs.assert_equals('sss', result)

    #testing before_space function
    result = a1.before_space('sss ddd sss')
    introcs.assert_equals('sss', result)

    #testing before_space function
    result = a1.before_space(' sss ddd')
    introcs.assert_equals('', result)

    #testing before_space function
    result = a1.before_space(' sss ddd ')
    introcs.assert_equals('', result)

    #testing before_space function
    result = a1.before_space('      ')
    introcs.assert_equals('', result)

    #testing before_space function
    result = a1.before_space('sss ')
    introcs.assert_equals('sss', result)

    #testing before_space function
    result = a1.before_space('    sss')
    introcs.assert_equals('', result)

    #testing after_space function
    result2 = a1.after_space('sss ddd')
    introcs.assert_equals('ddd', result2)

    #testing after_space function
    result2 = a1.after_space('sss ddd sss')
    introcs.assert_equals('ddd sss', result2)

    #testing after_space function
    result2 = a1.after_space(' sss ddd')
    introcs.assert_equals('sss ddd', result2)

    #testing after_space function
    result2 = a1.after_space(' sss ddd ')
    introcs.assert_equals('sss ddd ', result2)

    #testing after_space function
    result2 = a1.after_space('sss ')
    introcs.assert_equals('', result2)

    #testing after_space function
    result2 = a1.after_space('sss ddd sss    ')
    introcs.assert_equals('ddd sss    ', result2)

    #testing after_space function
    result2 = a1.after_space('    sss ddd')
    introcs.assert_equals('   sss ddd', result2)

    #testing after_space function
    result2 = a1.after_space('      ')
    introcs.assert_equals('     ', result2)
    pass


def testB():
    """
    Test procedure for Part B
    """
    #testing first_inside_quotes function
    result = a1.first_inside_quotes('""')
    introcs.assert_equals('', result)

    #testing first_inside_quotes function
    result = a1.first_inside_quotes('"a"')
    introcs.assert_equals('a', result)

    #testing first_inside_quotes function
    result = a1.first_inside_quotes('a"b"c"d"')
    introcs.assert_equals('b', result)

    #testing first_inside_quotes function
    result = a1.first_inside_quotes('"a"      b')
    introcs.assert_equals('a', result)

    #testing get_old function
    result2 = a1.get_old('{ "err":"", "old":"1 Bitcoin", "new":' + \
                        '"38781.518240835 Euros", "valid":true }')
    introcs.assert_equals('1 Bitcoin', result2)

    #testing get_old function
    result2 = a1.get_old('{ "err":"", "old":"2.5 United States Dollars",' + \
                        ' "new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals('2.5 United States Dollars', result2)

    #testing get_old function
    result2 = a1.get_old('{ "err":"Currency amount is invalid.",' + \
    ' "old":"", "new":"", "valid":false }')
    introcs.assert_equals('', result2)

    #testing get_new function
    result3 = a1.get_new('{ "err":"", "old":"1 Bitcoin", "new":' + \
                        '"38781.518240835 Euros", "valid":true }')
    introcs.assert_equals('38781.518240835 Euros', result3)

    #testing get_new function
    result3 = a1.get_new('{ "err":"", "old":"2.5 United States Dollars",' + \
                        ' "new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals('64.375 Cuban Pesos', result3)

    #testing get_new function
    result3 = a1.get_new('{ "err":"Currency amount is invalid.",' + \
    ' "old":"", "new":"", "valid":false }')
    introcs.assert_equals('', result3)

    #testing has_error function
    result4 = a1.has_error('{ "err":"", "old":"1 Bitcoin", "new":' + \
                        '"38781.518240835 Euros", "valid":true }')
    introcs.assert_equals(False, result4)

    #testing has_error function
    result4 = a1.has_error('{ "err":"Currency amount is invalid.",' + \
                        ' "old":"", "new":"", "valid":false }')
    introcs.assert_equals(True, result4)
    pass


def testC():
    """
    Test procedure for Part C
    """
    #testing query_website function
    result = a1.query_website('EUR', 'USD', 2.5)
    introcs.assert_equals('{ "err":"", "old":"2.5 Euros", "new":"2.953086' + \
                    '0930907 United States Dollars", "valid":true }', result)

    #testing query_website function
    result = a1.query_website('eur', 'USD', 2.5)
    introcs.assert_equals('{ "err":"Source currency code is invalid.", "old":"", "new":' + \
            '"", "valid":false }', result)

    #testing query_website function
    result = a1.query_website('eur', 'usd', 2.5)
    introcs.assert_equals('{ "err":"Source currency code is invalid.", "old":"", "new":' + \
            '"", "valid":false }', result)

    pass


def testD():
    """
    Test procedure for Part D
    """
    #testing is_currency function
    result = a1.is_currency('EUR')
    introcs.assert_equals(True, result)

    #testing is_currency function
    result = a1.is_currency('eur')
    introcs.assert_equals(False, result)

    #testing is_currency function
    result = a1.is_currency('que')
    introcs.assert_equals(False, result)

    #testing exchange function
    result2 = a1.exchange('EUR', 'USD', 2.5)
    introcs.assert_floats_equal(2.9530860930907, result2)


testA()
testB()
testC()
testD()
print('Module a1 passed all tests')
