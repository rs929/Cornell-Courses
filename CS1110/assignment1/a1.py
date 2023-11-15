"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Noelle Pappous (ntp26) Richie Sun (rs929)
Date:   09/18/21
"""
import introcs


def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    index = s.find(' ')
    first = s[:index]
    return first


def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    index = s.find(' ')
    first = s[index+1:]
    return first


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    a = s.index('"')
    first = s[a+1:]
    b = first.index('"')
    last = first[:b]
    return last


def get_old(json):
    """
    Returns the original value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "old". For example, if the JSON is

    '{ "err":"", "old":"1 Bitcoin", "new":"38781.518240835 Euros", "valid":true }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    index = json.find('old')
    string1 = json[index+5:]
    string2 = first_inside_quotes(string1)
    return string2


def get_new(json):
    """
    Returns the converted value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "new". For example, if the JSON is

    a

    then this function returns '38781.518240835 Euros' (not
    '"38781.518240835 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    index = json.find('new')
    string1 = json[index+5:]
    string2 = first_inside_quotes(string1)
    return string2


def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "valid". For example,
    if the JSON is

    '{ "err":"Currency amount is invalid.", "old":"", "new":"", "valid":false }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    index = json.find('false')
    result = index > 0
    return result


def query_website(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "err":"", "old":"<old-amt>", "new":"<new-amt>", "valid":true }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "valid" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    result = introcs.urlread('https://cs1110.cs.cornell.edu/2021fa/a1/?src='
            + src + '&dst=' + dst + '&amt=' + str(amt))
    return result


def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    boolean = has_error(query_website(code, 'USD', 2.5))
    boolean2 = (boolean == False)
    return boolean2


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency
    src to the currency dst. The value returned represents the
    amount in currency dst.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json = query_website(src, dst, amt)
    string = get_new(json)
    newMoney = before_space(string)
    number = float(newMoney)
    return number
