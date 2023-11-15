"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

YOUR NAME(S) AND NETID(S) HERE: Noelle Pappous (ntp26) and Richie Sun (rs929)
DATE COMPLETED HERE: 10/8/21
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    red = 255 - rgb.red
    green = 255 - rgb.green
    blue = 255 - rgb.blue
    return introcs.RGB(red, green, blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending
    # on how big value is. Look at the examples in the specification.
    string = str(value)
    if 'e' in string:
        return '0.000'
    #print(len(string))
    if len(string) == 5:
        #print(len(string))
        return string
    elif len(string) < 5:
        #print('2')
        if '.' in string:
            zeros = 5 - len(string)
            if zeros == 1:
                return string + '0'
            elif zeros == 2:
                return string + '00'
            elif zeros == 3:
                return string + '000'
            elif zeros == 4:
                return string + '0000'
        else:
            string = string + '.'
            zeros = 5 - len(string)
            if zeros == 1:
                return string + '0'
            elif zeros == 2:
                return string + '00'
            elif zeros == 3:
                return string + '000'
            elif zeros == 4:
                return string + '0000'
    else:
        if '.' in string:
            decimal = string.index('.') + 1
            #print(decimal)
            numbers = 5 - decimal
            #print(numbers)
            rounds = round(value, numbers)
            #print(rounds)
            result = str(rounds)
            #print(result)
            zeros = 5 - len(result)
            #print(zeros)
            if zeros == 1:
                return result + '0'
            elif zeros == 2:
                return result + '00'
            elif zeros == 3:
                return result + '000'
            elif zeros == 4:
                return result + '0000'
            return result
        else:
            return string[:5]


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    cyan = str5(cmyk.cyan)
    magenta = str5(cmyk.magenta)
    yellow = str5(cmyk.yellow)
    black = str5(cmyk.black)
    return '(' + cyan + ', ' + magenta + ', ' + yellow + ', ' + black + ')'


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "(H, S, L)".

    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsl) is

          '(0.0,0.313725490196,0.5)'

    then str5_hsl(hsl) is '(0.000, 0.314, 0.500)'. Note the spaces after the
    commas. These must be there.

    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    hue = str5(hsl.hue)
    saturation = str5(hsl.saturation)
    lightness = str5(hsl.lightness)
    return '(' + hue + ', ' + saturation + ', ' + lightness + ')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    red = rgb.red / 255.0
    green = rgb.green / 255.0
    blue = rgb.blue / 255.0
    k = 1 - max(red, green, blue)
    if k == 1:
        cyan = 0
        magenta = 0
        yellow = 0
    else:
        cyan = ((1 - red - k) / (1 - k)) * 100
        magenta = ((1 - green - k) / (1 - k)) * 100
        yellow = ((1 - blue - k) / (1 - k)) * 100

    return introcs.CMYK(cyan, magenta, yellow, k * 100)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. Deal with them in the
    # same way as the RGB numbers in rgb_to_cmyk()
    cyan = cmyk.cyan / 100
    magenta = cmyk.magenta / 100
    yellow = cmyk.yellow / 100
    k = cmyk.black / 100

    red = round(((1 - cyan) * (1 - k)) * 255)
    green = round(((1 - magenta) * (1 - k)) * 255)
    blue = round(((1 - yellow) * (1 - k)) * 255)

    return introcs.RGB(red, green, blue)


def rgb_to_hsl(rgb):
    """
    Return an HSL object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter rgb: the color to convert to a HSL object
    Precondition: rgb is an RGB object
    """
    red = rgb.red / 255
    green = rgb.green / 255
    blue = rgb.blue / 255

    maximum = max(red, green, blue)
    minimum = min(red, green, blue)

    if maximum == minimum:
        hue = 0
    elif maximum == red and green >= blue:
        hue = 60.0 * (green - blue) / (maximum - minimum)
    elif maximum == red and green < blue:
        hue =  60.0 * (green - blue) / (maximum - minimum) + 360.0
    elif maximum == green:
        hue =  60.0 * (blue - red) / (maximum - minimum) + 120.0
    elif maximum == blue:
        hue =  60.0 * (red - green) / (maximum - minimum) + 240.0

    lightness = (maximum + minimum) / 2

    if lightness == 0 or lightness == 1:
        saturation = 0
    else:
        saturation = (maximum - lightness) / min(lightness, 1 - lightness)

    return introcs.HSL(hue, saturation, lightness)


def hsl_to_rgb(hsl):
    """
    Returns an RGB object equivalent to hsl

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsl: the color to convert to a RGB object
    Precondition: hsl is an HSL object.
    """
    hi = math.floor(hsl.hue / 60)
    f = hsl.hue / 60 - hi
    c = min(hsl.lightness, 1 - hsl.lightness) * hsl.saturation
    p = hsl.lightness + c
    q = hsl.lightness - c
    u = hsl.lightness - (1 - 2 * f) * c
    v = hsl.lightness + (1 - 2 * f) * c
    if hi == 0 or hi == 5:
        red = round(p * 255)
    if hi == 1:
        red = round(v * 255)
    if hi == 2 or hi == 3:
        red = round(q * 255)
    if hi == 4:
        red = round(u * 255)

    if hi == 0:
        green = round(u * 255)
    if hi == 1 or hi == 2:
        green = round(p * 255)
    if hi == 3:
        green = round(v * 255)
    if hi == 4 or hi == 5:
        green = round(q * 255)

    if hi == 0 or hi == 1:
        blue = round(q * 255)
    if hi == 2:
        blue = round(u * 255)
    if hi == 3 or hi == 4:
        blue = round(p * 255)
    if hi == 5:
        blue = round(v * 255)

    return introcs.RGB(red, green, blue)


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart,
    with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """

    if -1 <= contrast < 1:
        if value < (0.25 + 0.25 * contrast):
            y = ((1 - contrast)/(1 + contrast)) * value
        elif value > (0.75 - 0.25 * contrast):
            y = ((1 - contrast)/(1 + contrast))*(value - (3 -
            contrast)/4) + ((3 + contrast)/4)
        else:
            y = ((1 + contrast)/(1 - contrast))*(value - (1 +
            contrast)/4) + ((1 - contrast)/4)
    else:
        if value >= 0.5:
            y = 1
        else:
            y = 0

    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    red = rgb.red / 255
    green = rgb.green / 255
    blue = rgb.blue / 255

    redc = contrast_value(red, contrast)
    greenc = contrast_value(green, contrast)
    bluec = contrast_value(blue, contrast)

    redf = int(redc * 255)
    greenf = int(greenc * 255)
    bluef = int(bluec * 255)

    rgb.red = redf
    rgb.green = greenf
    rgb.blue = bluef
