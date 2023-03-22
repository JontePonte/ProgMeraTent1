""" Solutions to assignment 1 in the final exams by John Nordstrand S2300891"""

import numpy as np


# ---------------------------------------- a) ---------------------------------------------------

def func1(x, y):
    """ function given in assignment """
    return x+x**y

# Set array dimensions
rows = 10
cols = 8

# Create the numpy array using the function
NP_A = np.fromfunction(func1, (rows, cols), dtype=int)
# print(NP_A) # I leave this in if you want to confirm my solution


# ---------------------------------------- b) ---------------------------------------------------

