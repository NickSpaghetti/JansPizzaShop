import run_sim as sim
import matplotlib.pyplot as plt

'''
generates the graph that plots average number of houses
per trip vs the amount of minutes that the shop is open.
gap_time = 5 minutes
'''
def avg_houses_graph():

    avg_houses = []

    for minutes in range(60, 721, 30):
        total_houses = 0
        total_trips = 0
        for sims in range(0, 100):
            stats = sim.run_sim(5, minutes)
            total_trips += stats.total_trips
            total_houses += stats.total_houses
        avg = total_houses / total_trips
        avg_houses.append(avg)

    plt.scatter(range(60, 721, 30), avg_houses)
    plt.title("Average Delivery Route Size vs Length Shop is Open")
    plt.xlabel("Minutes Shop is Open")
    plt.ylabel("Average Number of Houses on Delivery Route")
    plt.show()
    #comment

def main():
    avg_houses_graph()

if __name__ == '__main__':
    main()


