# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:32:16 2016

@author: Nick
"""

import random
import rngs
import rvgs
import rvms
import matplotlib.pyplot as plt
import math

def generate_neighborhood(): #Example 2.3.7 - 2.3.8 page 67-68
    random.seed(1337) #plant seed
    p = 5 # radious
    house_number = 250
    cord_arry = []
    x_arry = []
    y_arry = []
    while house_number != 0:
        x = random.uniform(-1 * p,p)
        y = random.uniform(-1 * p,p)
        if(x * x + y * y <= p * p):
            x = 0 + x
            y = 0 + y
            cord_arry.append((x,y))
            x_arry.append(x)
            y_arry.append(y)
            house_number -= 1
    #print(cord_arry)
    print(len(cord_arry))
    plt.scatter(x_arry,y_arry)
    plt.show()
    return cord_arry

def main():
    generate_neighborhood()

if __name__ == '__main__':
    main()