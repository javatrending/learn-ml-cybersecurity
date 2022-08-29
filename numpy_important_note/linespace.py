## Linespace function return number space evenly w.r.t interval
## Similar to numpy.arange() function but instea of step it uses sample number

# -> start  : [optional] start of interval range. By default start = 0
# -> stop   : end of interval range
# -> restep : If True, return (samples, step). By default restep = False
# -> num    : [int, optional] No. of samples to generate
# -> dtype  : type of output array

import numpy as geek
import matplotlib.pyplot as plt

# restep set to True
print("This set retstep to True: \n", geek.linspace(2.0, 3.0, num=5, retstep=True), "\n")

# To evaluate sin() in long range
x = geek.linspace(0, 2, 10)
print("This output before evalute with sin: \n", x, "\n")
print("This output after evaluate with sin: \n", geek.sin(x), "\n")

plt.plot(geek.cos(x))
plt.show()


