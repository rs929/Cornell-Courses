"""
A module to demonstrate asserts and error handling.

This module sees the return of time_to_military to military from a previous lab.
However, this time it has no bugs in it.  Instead, you will add assert statements
to this function to assert the (somewhat complex) precondition.  These assert
statements will be aided by the latter functions in this module.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# PART 1: ASSERTS
def time_to_military(s):
    """
    Returns: the time in 24-hour (military) format.

    24-hour format has the form '<hours>:<minutes>'. The hours are between 0 and 23,
    and are always two digits (so there must be a leading zero).  The minutes are
    between 0 and 59, and are always 2 digits.

    Examples:
        '2:45 PM' becomes '14:45'
        '9:05 AM' becomes '09:05'
        '12:00 AM' becomes '00:00'

    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM
    """
    # ADD ASSERT STATEMENTS HERE TO PROPERLY ENFORCE PRECONDITION
    assert is_time_format(s)
    # Split up the string
    pos1 = s.index(':')
    pos2 = s.index(' ')

    # Extract hours and minutes
    hour = int(s[:pos1])
    mins = s[pos1+1:pos2]
    suff = s[pos2+1:]

    # Adjust hour to be correct.
    if (suff == 'PM' and hour < 12):
        hour += 12
    elif (suff == 'AM' and hour == 12):
        hour = 0

    # Add a leading zero if necessary
    if (hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)

    # Glue it back together
    return str(hour)+':'+mins


# ASSERT HELPER
def is_time_format(s):
    """
    Returns: True if s is a string in 12-format <hours>:<min> AM/PM

    Example:
        is_time_format('2:45 PM') returns True
        is_time_format('2:45PM') returns False
        is_time_format('14:45') returns False
        is_time_format('14:45 AM') returns False
        is_time_format(245) returns False

    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)
    """
    if type(s) != str:
        return False
    if ':' in s:
        pos1 = s.index(':')
        if s[:pos1].isdigit:
            if ' ' in s:
                if int(s[:pos1]) <= 12:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    # HINT: Your function must be prepared to do something if s is a string.
    # Even if s is a string, the first number before the colon may be one
    # or two digits.  You must be prepared for either.
    # You might find the method s.isdigit() to be useful.


# PART 2: TRY-EXCEPT
def something_to_military(s):
    """
    Returns: the time in 24-hour (military) format if appropriate.

    The function is the same as time_to_military if s satisfies the
    precondition for that function.  If s does not satisfy the precondition
    then this function returns 'Invalid time format'

    Examples:
        something_to_military('2:45 PM') returns '14:45'
        something_to_military('9:05 AM') returns '09:05'
        something_to_military('12:00 AM') returns '00:00'
        something_to_military(905) returns 'Invalid time format'
        something_to_military('abc') returns 'Invalid time format'
        something_to_military('9:05') returns 'Invalid time format'

    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)
    """
    try:
        assert is_time_format(s)
    except:
        return 'Invalid time format'
    pos1 = s.index(':')
    pos2 = s.index(' ')
    hour = int(s[:pos1])
    mins = s[pos1+1:pos2]
    suff = s[pos2+1:]
    if (suff == 'PM' and hour < 12):
        hour += 12
    elif (suff == 'AM' and hour == 12):
        hour = 0
    if (hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    return str(hour)+':'+mins
    # You are not allowed to use 'if' in this definition. Use try-except instead.
    # Hint: You have to complete PART 2 before you complete this part.
