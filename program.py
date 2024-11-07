import pdb
import numpy as np
import matplotlib.pyplot as plt

# save_state(vars())
with open('helper.py') as file: exec(file.read())

def quadratic_function(x):
    c = 3
    pdb.set_trace()
    return  x**2

x_values = np.linspace(-10, 10, 400)
y_values = quadratic_function(x_values)
