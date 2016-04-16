# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:46:32 2016

@author: Nick
"""
import neighborhood_generator as ng
import random

class EventList:
    def __init__(self):
        self.order = 0
        self.finish = 0
        self.depart_shop = False
        self.at_shop = True

class State:
    def _init__(self):
        self.completed_pizza = 0
        self.unfinished_order = 0
        self.time_of_order = 0
        self.locations = []
        self.status = 0
        self.preperation = ['Not Started','started','baking','complete']
        self.delevery = 0
        

def main():
    s = State()
    s.locations = ng.generate_neighborhood()
    print("subject to change")
    

if __name__ == 'main':
    main()
