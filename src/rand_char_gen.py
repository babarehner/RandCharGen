'''
Created on Sep 4, 2013
Updated on Mar 14, 2019

@author: mike rehner

updated Mar 14, 2019 to work with Python 3
and to use Python 3.6 secrets module
'''

import random
import secrets
import string

# How I would teach how to write a random string generator
def make_ran_char1():
    output = ''
    for i in range(6): #PyDev gives a warning here unless you add an underscore to i as in function below
        # line below only works with Python 2.7 but not Python 3
        # output += (random.choice(string.lowercase + string.digits))

        # line below works with python 3
        output += (random.choice(string.ascii_letters + string.digits))

    return output
 
# Pythonistic way- also more efficient
def make_ran_char2():
    # make sure random is called with current time as a seed value
    random.seed()
    # line below only works with Python 2.7 but not Python 3
    # return ''.join(random.choice(string.lowercase + string.digits)for _i in range(6))

    # line below works with python 3
    return ''.join(random.choice(string.ascii_letters + string.digits) for _i in range(6))


# Requires secrets module from Python 3.6, used for generating cryptographically strong random numbers
# below the 6 characters generated must include at least 1 lowercase, 1 uppercase, and 1 digit
def make_secret_char():
    while True:
        secret = "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(6))
        # keep trying until there is a secret with 1 lowercase, 1 uppercase and 1 digit, then break
        if (any(c.islower() for c in secret)
                and any(c.isdigit() for c in secret)
                and any(c.isupper for c in secret)):
            break
    return secret


  
if __name__ == '__main__':
    #prints out  random strings for each function definition above
    for i in range(5):
        print("Func1: "+ make_ran_char1(), '  |  Func2: '+ make_ran_char2(), '  |  ',
              "Func3: " + make_secret_char())

    