"""
Unit Test for Assignment A3

This module shows off what a good unit test for a3 should look like.

YOUR NAME(S) AND NETID(S) HERE: Noelle Pappous (ntp26) and Richie Sun (rs929)
DATE COMPLETED HERE: 10/8/21
"""
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    print('Testing str5')
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('1.000',  a3.str5(1))
    introcs.assert_equals('0.000',  a3.str5(0.0000000001))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsl')

    # Tests for str5_cmyk (add one more test)
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    text = a3.str5_cmyk(introcs.CMYK(5.3211, 21.0, 0.0000000001, .13))
    introcs.assert_equals('(5.321, 21.00, 0.000, 0.130)',text)

    # Tests for str5_hsl (add two)
    text = a3.str5_hsl(introcs.HSL(359, 0.000000001, 1))
    introcs.assert_equals('(359.0, 0.000, 1.000)',text)

    text = a3.str5_hsl(introcs.HSL(255.599, .52, 0.222222))
    introcs.assert_equals('(255.6, 0.520, 0.222)',text)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places
    rgb = introcs.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    rgb = introcs.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    rgb = introcs.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')
    # ADD TESTS TO ME
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, round(rgb.red,3))
    introcs.assert_equals(255, round(rgb.green,3))
    introcs.assert_equals(255, round(rgb.blue,3))

    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    cmyk = introcs.CMYK(25.0, 8.0, 21.0, 81.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(36, round(rgb.red,3))
    introcs.assert_equals(45, round(rgb.green,3))
    introcs.assert_equals(38, round(rgb.blue,3))

    cmyk = introcs.CMYK(0.0, 0.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    cmyk = introcs.CMYK(100.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(255, round(rgb.blue,3))


def test_rgb_to_hsl():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsl')

    # ADD TESTS TO ME
    # Red max, blue min (green > blue)
    rgb = introcs.RGB(250, 100, 50)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(15.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(.588, round(hsl.lightness, 3))

    # Blue max, Red min
    rgb = introcs.RGB(50, 100, 250)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(225.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(.588, round(hsl.lightness, 3))

    # Red max, Green min (blue > green)
    rgb = introcs.RGB(250, 50, 100)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(345.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(0.588, round(hsl.lightness, 3))

    # Red max, Green and Blue min (blue = green)
    rgb = introcs.RGB(250, 50, 50)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(0.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(0.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(0.588, round(hsl.lightness, 3))

    # Green max, Red mins
    rgb = introcs.RGB(50, 250, 100)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(135.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(.588, round(hsl.lightness, 3))

    # Green max, Blue mins
    rgb = introcs.RGB(100, 250, 50)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(105.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(.588, round(hsl.lightness, 3))

    # Blue max, Green min
    rgb = introcs.RGB(100, 50, 250)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(255.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(0.952, round(hsl.saturation, 3))
    introcs.assert_floats_equal(0.588, round(hsl.lightness, 3))

    #All the same number (min = max)
    rgb = introcs.RGB(100, 100, 100)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(0.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(0.0, round(hsl.saturation, 3))
    introcs.assert_floats_equal(0.392, round(hsl.lightness, 3))

    #All max
    rgb = introcs.RGB(255, 255, 255)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(0.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(0.0, round(hsl.saturation, 3))
    introcs.assert_floats_equal(1, round(hsl.lightness, 3))

    #All min
    rgb = introcs.RGB(0, 0, 0)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_floats_equal(0.0, round(hsl.hue, 3))
    introcs.assert_floats_equal(0.0, round(hsl.saturation, 3))
    introcs.assert_floats_equal(0.0, round(hsl.lightness, 3))


def test_hsl_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsl_to_rgb')
    # ADD TESTS TO ME
    # Hi == 0
    hsl = introcs.HSL(0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(191, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(64, rgb.blue)

    # Hi == 5
    hsl = introcs.HSL(320.0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(320.0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(191, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(149, rgb.blue)

    # Hi == 1
    hsl = introcs.HSL(65.0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(65.0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(181, rgb.red)
    introcs.assert_equals(191, rgb.green)
    introcs.assert_equals(64, rgb.blue)

    # Hi == 2
    hsl = introcs.HSL(125.0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(125.0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(64, rgb.red)
    introcs.assert_equals(191, rgb.green)
    introcs.assert_equals(74, rgb.blue)

    # Hi == 3
    hsl = introcs.HSL(185.0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(185.0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(64, rgb.red)
    introcs.assert_equals(181, rgb.green)
    introcs.assert_equals(191, rgb.blue)

    # Hi == 4
    hsl = introcs.HSL(245.0, 0, 0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(245.0, 0.5, 0.5)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(74, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(191, rgb.blue)


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    result = a3.contrast_value(1.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,-0.5)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4,-0.4)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9,-0.3)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.0)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6,0.0)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.0)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.3)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4,0.5)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.4)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')

    # Negative contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,-0.4)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)

    # Add two more tests
    # Positive Contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,0.4)
    introcs.assert_equals(248, rgb.red)
    introcs.assert_equals(6,  rgb.green)
    introcs.assert_equals(105, rgb.blue)

    # Zero Contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,0.0)
    introcs.assert_equals(240, rgb.red)
    introcs.assert_equals(15,  rgb.green)
    introcs.assert_equals(118, rgb.blue)


# Script Code (Prevents tests running on import)
if __name__ == "__main__":
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsl()
    test_hsl_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
