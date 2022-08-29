## The arange function returns an array with evenly spaced element as per the interval

# start : [optional] start of interval range. By default start = 0
# stop  : end of interval range
# step  : [optional] step size of interval. By default step size = 1,  For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
# dtype : type of output array

import numpy as geek
 
print("Output before reshape: ", geek.arange(4))
print("Output after reshape in 2x2 dimension: \n", geek.arange(4).reshape(2,2), "\n")
print(50*("="))

print("This output is not use step: ", geek.arange(4, 10))
print("This output is use step: ", geek.arange(4, 20, 3))
