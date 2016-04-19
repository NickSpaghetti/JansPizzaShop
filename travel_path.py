from itertools import permutations
import neighborhood_generator as ng
import math
import matplotlib.pyplot as plt

def get_minPath(delivery_coords):

    min_distance = math.inf
    min_path = []

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

    return min_path

def graph_minPath(min_path):

    x_val = [x[0] for x in min_path] #split x_cord
    y_val = [y[1] for y in min_path] #split y_cord
    plt.plot(x_val, y_val, 'r-')
    plt.plot([0, x_val[0]], [0, y_val[0]], 'r-')
    plt.scatter(x_val,y_val)
    plt.plot(0,0, "yo")
    circle = plt.Circle((0,0), radius=5, color='g', fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.axis([-7, 7, -7, 7])
    plt.show()
    #comment


def main():
    delivery_coords = []

    for count in range(0,10):
        delivery_coords.append(ng.get_order())

    min_path = get_minPath(delivery_coords)
    print(min_path)
    graph_minPath(min_path)


if __name__ == '__main__':
    main()

