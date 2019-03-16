RandCharGen
===========

Updated March 14, 2019 to use Python 3 and the Python 3.6 secrets module

Creates a set of random characters. Can be used as a password generator, a salt generator or create a GAE (Google App Engine) site name generator. Two functions, each returns a random set of characters. One is written in a clearer polyglot way and the other is written in a more Pythonic way. String constants can be changed out to change your random set of characters.



7.1.1. String constants from Python Documentation (http://docs.python.org/2/library/string.html)

The constants defined in this module are:

string.ascii_letters

    The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

string.ascii_lowercase

    The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase

    The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits

    The string '0123456789'.

string.hexdigits

    The string '0123456789abcdefABCDEF'.

string.letters

    The concatenation of the strings lowercase and uppercase described below. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.lowercase

    A string containing all the characters that are considered lowercase letters. On most systems this is the string 'abcdefghijklmnopqrstuvwxyz'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.octdigits

    The string '01234567'.

string.punctuation

    String of ASCII characters which are considered punctuation characters in the C locale.

string.printable

    String of characters which are considered printable. This is a combination of digits, letters, punctuation, and whitespace.

string.uppercase

    A string containing all the characters that are considered uppercase letters. On most systems this is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.whitespace

    A string containing all characters that are considered whitespace. On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

