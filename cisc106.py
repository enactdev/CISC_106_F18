'''
CISC106 Module that includes some basic helper functions such as assertEqual().

Versions:
0.142 - 2014-APR-23, Modified by Jon Leighton
 + Modified success and failure messages to print "SUCCESS" and "FAILURE" at the
   beginning of each result. This makes it much easier to quickly discern the
   outcome visually.
0.141 - 2014-MAR-26, Modified by Jon Leighton
 + Removed unused function print_verbose().
 + Appended text to FAILURE message for incompatible types to indicate that types
   involved can't be compared.
0.14 - 2014-MAR-26, Modified by Andrew Roosen
 + Modified assertEqual() to return False on failure and True on success.
 + Introduced QUITE option to supress output on SUCCESS.
 + Modified FAILURE message for incompatible data types to be consistent with
 + FAILURE message for unequal values.
 + Modified names of internal functions isEqual() and isseqtype() to __isEqual()
   and __isseqtype(), respectively
0.13 - 2014-MAR-25, Modified by Jon Leighton
 + added elif clause to __isEqual(), to avoid comparing ints and floats to anything
   that is not an int or a float, and to return None in this case. The previous
   comparison tried to subtract these quantities from each other, causing a
   runtime error.
 + Modified assertEqual() to check for __isEqual() returning None, which now
   indicates an attempt to compare unrelated data types. Failure message is
   modified in this case to report the attempt to compare unrelated types.
 + Removed unused global variables fail and success.
 + Added version numbers to Paul Amer's modifications, and bumped version number to
   reflect my modifications.
 + Changed version number to string, to match recommended practice.
0.122 - 2012-APR-17, Modified by Paul Amer
 + removed graphics stuff; just kept AssertEqual
0.121 - 2011-SEP-08, Modified by Paul Amer
 +improved success-failure messages
0.12
 + display can be called multiple times
 + assertEqual supports PIL.Image.Image
0.1
 + Initial assertEqual, display, animate, bind
'''
__version__ = '0.141'

import sys, traceback, types, os

# Don't print message from assertEqual on success
QUIET=False

def assertEqual(x, y, *args):
    """
    Checks an expected value using the __isEqual function.
    Prints a message if the test case passed or failed.
    """
    
    trace = traceback.extract_stack()
    frame = trace[len(trace)-2]

    # messages modified 2014-MAR-25, JTL
    # messages modified 2011-SEP-09, PDA
    # variables fail and success not used
    result = __isEqual(x, y, *args)
    if result == None:
        print('FAILURE - [line', frame[1], '] ', frame[3], ', predicted answer was ',
              y, ' ', type(y), ', computed answer was ', x, ' ', type(x),
              ' (Attempting to compare unrelated data types.)', sep = '')
        return False
    elif not result:
        print("FAILURE - [line %d] %s, predicted answer was %s, computed answer was %s " \
            % (frame[1], frame[3], y, x))
        return False
    elif not QUIET:
        print("SUCCESS - [line %d] %s" % (frame[1], frame[3]))
    return True

def __isEqual(x, y, *args):
    """
    __isEqual : thing thing -> boolean
    __isEqual : number number number -> boolean
    Determines whether the two arguments are equal, or in the case of
    floating point numbers, within a specified number of decimal points
    precision (by default, checks to with 4 decimal points for floating
    point numbers). Returns None when attempting to compare ints and floats
    to anything other than ints and floats.
    
    Examples:
    >>> __isEqual('ab', 'a'+'b')
     True
     
    >>> __isEqual(12.34, 12.35)
     False
     
    >>> __isEqual(12.3456, 12.34568, 4)
     True
         
    >>> __isEqual(12.3456, 12.34568w5)
     False
    """
    if (x is None and y is not None) or (y is None and x is not None):
        return False
    elif x is None and y is None:
        return True
    elif (type(x) == int or type(x) == float) and \
             (type(y) != int and type(y) != float) or \
         (type(y) == int or type(y) == float) and \
             (type(x) != int and type(x) != float):
        return None
    elif type(x) == int and type(y) == int:
        return x == y
    elif type(x) == float or type(y) == float:
        if len(args) == 1:
            error = 10 ** (- args[0])
        else:
            error = 0.0001
        return abs(x - y) < error
    elif __isseqtype(x) and __isseqtype(y) and len(x)==len(y):
        res = True
        for (x1,y1) in zip(x, y):
            res = res and __isEqual(x1, y1, *args)
        return res
    else:
        return x == y

def __isseqtype(x):
    return type(x) == list or type(x) == tuple
