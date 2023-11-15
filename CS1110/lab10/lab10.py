"""
A module to demonstrate debugging and error handling.

This module contains several functions with bugs in it.  You are to
find and remove the bugs using the techniques that we talked about in
class.

In addition, you will also add assert statements to this functions to
assert the (somewhat complex) precondition.  These assert statements
will be aided by the latter two functions in this module.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def time_to_military(s):
    """
    Returns: the time in 24-hour (military) format.

    24-hour format has the form '<hours>:<minutes>'. The hours are between 0 and 23,
    and are always two digits (so there must be a leading zero).  The minutes are
    between 0 and 59, and are always 2 digits.

    Examples:
        time_to_military('2:45 PM') returns '14:45'
        time_to_military('9:05 AM') returns '09:05'
        time_to_military('12:00 AM') returns '00:00'

    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM
    """

    # Split up the string
    pos1 = s.index(':')
    pos2 = s.index(' ')

    # Extract hours and minutes
    hour = int(s[:pos1])
    mins = s[pos1+1:pos2]
    suff = s[pos2+1:]

    # Adjust hour to be correct.
    if (suff == 'PM') and (hour != 12):              # Add 12 to PM values
        hour += 12
    if (s == '12:00 AM'):                       # Set midnight to 0
        hour = 0

    # Add a leading zero if necessary
    if (hour < 10):
        hour = '0'+str(hour)
    else:
        hour = str(hour)

    # Glue it back together
    return str(hour)+':'+mins


def time_to_minutes(s):
    """
    Returns: number of minutes since midnight

    Examples:
        time_to_minutes('2:45 PM') returns 14*60+45 = 885
        time_to_minutes('9:05 AM') returns 9*60+5 = 545
        time_to_minutes('12:00 AM') returns 0

    Parameter s: string representation of the time
    Precondition: s is a string in 12-format <hours>:<min> AM/PM
    """

    # Find the separators
    pos1 = s.index(':')
    pos2 = s.index(' ')

    # Get hour and convert to int
    hour = s[:pos1]
    hour = int(hour)

    # Adjust hour to be correct.
    suff = s[pos2+1:]
    if (suff == 'PM'):                  # Add 12 to PM values
        hoar = hour+12
    elif (suff == 'AM' and hour == 12): # Set midnight to 0
        hour = 0

    # Get min and convert to int
    mins = s[pos1:pos2]
    mins = int(mins)

    return hour*60+mins
