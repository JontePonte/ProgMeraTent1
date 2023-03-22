""" Solutions to assignment 1 in the final exams by John Nordstrand S2300891"""

import numpy as np
import matplotlib.pyplot as plt

print("")
print("---------------------------------------- a) ---------------------------------------------------")
print("")

def func1(x, y):
    """ function given in assignment """
    return x+x**y

# Set array dimensions
rows = 10
cols = 8

# Create the numpy array using the function
NP_A = np.fromfunction(func1, (rows, cols), dtype=int)
print(NP_A) # I leave this in if you want to confirm my solution


print("")
print("---------------------------------------- b) ---------------------------------------------------")
print("")

# This one way a lot easier :)
print(NP_A[2:7:2, 1:6:2]) # I might forget to uncomment this one


print("")
print("---------------------------------------- c) ---------------------------------------------------")
print("")

# simple numpy conversion
NP_A_list = NP_A.tolist()
print(NP_A_list)

# I guess you want me to solve it the old fashion python way?
print("All values between 10 an 100 in the array:")
for row in NP_A_list:
    for value in row:
        if value > 10 and value < 100:
            print(value)


print("")
print("---------------------------------------- d) ---------------------------------------------------")
print("")

# Collect all necessary data
max_row = np.max(NP_A, axis=1)
min_row = np.min(NP_A, axis=1)
mean_row = np.mean(NP_A, axis=1)

min_col = np.min(NP_A, axis=0)
max_col = np.max(NP_A, axis=0)
mean_col = np.mean(NP_A, axis=0)

# The sum of max and min values and mean values last
print("The sum om max and min values for each row:")
print(min_row+max_row)

print("The sum om max and min values for each column:")
print(min_col+max_col)

print("The mean values for each row:")
print(mean_row)

print("The mean values for each column:")
print(mean_col)


print("")
print("---------------------------------------- e) ---------------------------------------------------")
print("")

NP_Ae = np.where(NP_A>100, -1, NP_A) # just using where()
print(NP_Ae)


print("")
print("---------------------------------------- f) ---------------------------------------------------")
print("")

NP_Arr = NP_A.flatten() # just using flatten()
print(NP_Arr)


print("")
print("---------------------------------------- g) ---------------------------------------------------")
print("")

plot_vals_1 = 1+NP_Arr**3+1+3*NP_Arr**2 + 6*NP_Arr
plot_vals_2 = 1+ 1+3*NP_Arr**2 + 6*NP_Arr
plot_vals_3 = 1+NP_Arr**3+ 6*NP_Arr

plt.plot(plot_vals_1, label="fist")
plt.plot(plot_vals_2, label="second")
plt.plot(plot_vals_3, label="third")

plt.legend()
plt.title("Assignment 1 g)")

plt.show()