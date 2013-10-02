'''
Created on Sep 4, 2013

@author: mike
'''

import random
import string

# How I would teach how to write a random string generator
def make_ran_char1():
    output = ''
    for i in range(5): #PyDev gives a warning here unless you add an underscore to i as in function below
        output += (random.choice(string.lowercase + string.digits))
    return output
 
# Pythonistic way- also more efficient
def make_ran_char2():
    return ''.join(random.choice(string.lowercase + string.digits)for _i in range(5))
  
if __name__ == '__main__':
    #prints out 5 random strings for each function definition above
    for i in range(5):
        print "Func1: "+ make_ran_char1(), '  |  Func2: '+ make_ran_char2()
    