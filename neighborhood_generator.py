# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:32:16 2016

@author: Nick
"""

import random
import matplotlib.pyplot as plt
import math

def generate_static_neighborhood(): #Example 2.3.7 - 2.3.8 page 67-68
    random.seed(1337) #plant seed
    p = 5 # radious
    house_number = 250
    cord_arry = []
    x_arry = []
    y_arry = []
    while house_number != 0:
        x = random.uniform(-1 * p,p)
        y = random.uniform(-1 * p,p)
        if x * x + y * y <= p * p:
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

def get_order():
    p = 5
    count = 0
    while count != 1:
        x_test_cord = random.uniform(-1 * p,p)
        y_test_cord = random.uniform(-1 * p,p)
        if (x_test_cord * x_test_cord) + (y_test_cord * y_test_cord) <= p * p:
            x_cord = x_test_cord
            y_cord = y_test_cord
            count += 1
    return x_cord,y_cord
            
        
def main():
    #generate_static_neighborhood()
    house_list = []
    for i in range(0,5):
        house_list.append(get_order())
    x_val = [x[0] for x in house_list] #split x_cord 
    y_val = [y[1] for y in house_list] #split y_cord


    plt.scatter(x_val,y_val)
    plt.show()
    
    print(house_list)
if __name__ == '__main__':
    main()