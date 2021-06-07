"""Global functions to be used throughout the application"""
import numpy as np
import math


MTGen =  np.random.Generator(np.random.MT19937(555))

def degrees_to_radians(degrees):
    return degrees * math.pi/180.

def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def random_float(minimum=0., maximum=1.):
   return minimum + (maximum - minimum) * MTGen.uniform()

def random_int(minimum, maximum):
    return int(random_float(minimum, maximum+1))
