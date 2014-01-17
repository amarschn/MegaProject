# Author: Drew Marschner
# Date: 1/16/2014

# Enter a number and have the program generate PI up to that many decimal
# places. Keep a limit to how far the program will go.

import math

'''
Just use the constant found in the math module
'''
def python_pi(number):
    if number > 11:
        print "Too many decimal places"
        return math.pi
    else:
        # return the floating point form of the string given by the format function
        return float(format(math.pi, "0.%df" % number))
    


'''
Calculates pi using the Gregory Lebniz series
'''
def leibniz_pi(number):
    pi = 0.0
    n = 0.0
    while (number > 0):
        pi += (2.0/((4*n + 1) * (4*n + 3)))
        number-= 1
        n += 1
    return 4*pi

print leibniz_pi(1000)
print python_pi(12)
