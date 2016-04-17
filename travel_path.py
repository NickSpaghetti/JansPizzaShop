from itertools import permutations
import neighborhood_generator as ng
import math
import matplotlib.pyplot as plt

def caculate_distance(number_of_calls):
    min_distance = math.inf
    min_path = []

    delivery_coords = []
    for count in range(0,number_of_calls):
        delivery_coords.append(ng.get_order())


    for item in permutations(delivery_coords):
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

        if total_distance < min_distance:
            min_distance = total_distance
            min_path = item

    print(min_path)
    return min_path

def main():
    min_path = caculate_distance(5)
    x_val = [x[0] for x in min_path] #split x_cord
    y_val = [y[1] for y in min_path] #split y_cord
    plt.plot(x_val, y_val, 'r-')
    plt.scatter(x_val,y_val)
    plt.scatter(0,0)
    plt.show()

if __name__ == '__main__':
    main()