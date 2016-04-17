# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:46:32 2016

@author: Nick
"""
import neighborhood_generator as ng
import random
import math
import travel_path

class StatsSums:
    def __init__(self):
        self.total_travel_distance = 0.0
        self.total_delivery_distance = 0.0
        self.total_houses = 0
        self.total_departs = 0


class Statistics:
    def __init__(self):
        self.avg_travel_distance = 0.0
        self.avg_delivery_distance = 0.0
        self.avg_travel_time = 0.0
        self.avg_delivery_time = 0.0

class TimeStructure:
    def __init__(self):
        self.departure = -1       # time delivery driver departs
        self.done = -1       # time the next pizza is done
        self.demand = -1       # time of next call-in for delivery
        self.arrival = -1       # time when the delivery driver arrives at the pizza shop
        self.current = -1       # current time


def getDemand(low, high, mode):
    return random.triangular(low, high, mode)


def run_sim(gap, low, high, mode, maxTime):

    stat_sums = StatsSums()

    t = TimeStructure()
    infinity = math.inf

    t.demand = getDemand(low, high, mode)
    t.done = infinity
    t.departure = infinity
    t.arrival = infinity
    t.current = 0

    delivery_coords = []

    while t.current < maxTime:
        next_event = min(t.demand, t.arrival, t.done, t.departure)
        t.current = next_event

        if next_event == t.demand:
            if t.current < maxTime:
                t.done = t.current + 15
                delivery_coords.append(ng.get_order())
                t.demand = t.current + getDemand(low, high, mode)
                stat_sums.total_houses += 1
            else:
                t.demand = infinity

        if next_event == t.done:
            if t.departure == infinity:
                if t.arrival == infinity:
                    t.departure = t.current + gap
                else:
                    if t.current + gap < t.arrival:
                        t.departure = t.arrival
                    else:
                        t.current + gap

        if next_event == t.departure:
            deliver_route = travel_path.get_minPath(delivery_coords)
            for item in deliver_route:
                total_distance = 0
                x1 = 0
                y1 = 0
                for house in range(0, len(item)):
                    x2 = item[house][0]
                    y2 = item[house][1]

                    d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
                    total_distance += d

                    x1 = x2
                    y1 = y2
            stat_sums.total_delivery_distance += total_distance

            d = math.sqrt(((x2-0)**2) + ((y2-0)**2))
            stat_sums.total_travel_distance += (total_distance + d)

            travel_time = stat_sums.total_travel_distance * 1.72
            t.arrival = t.current + travel_time
            t.departure = infinity
            stat_sums.total_departs += 1

        if next_event == t.arrival:
            t.arrival = infinity

    stats = Statistics()

    stats.avg_travel_distance = stat_sums.total_travel_distance / stat_sums.total_departs
    stats.avg_delivery_distance = stat_sums.total_delivery_distance / stat_sums.total_houses
    stats.avg_travel_time = stats.avg_travel_distance * 1.72
    stats.avg_delivery_time = stats.avg_delivery_distance * 1.72

    return stats

        

def main():

    stats = run_sim(5, 1, 10, 5, 720)

    print("Average travel distance {1:6.2f}".format(stats.avg_travel_distance))
    print("Average delivery distance {0:4.2f}".format(stats.avg_delivery_distance))
    print("Average travel time = ({0},{1})\n".format(stats.avg_travel_time))
    print("Average delivery distance = {0:6.2f}".format(stats.avg_delivery_time))

    print("here")

if __name__ == 'main':
    main()
