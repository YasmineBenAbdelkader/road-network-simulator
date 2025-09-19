# io/display.py
import matplotlib.pyplot as plt

def plot_speed_over_time(data):
    """
    data : liste de dictionnaires {road_name: avg_speed}
    """
    if not data:
        return

    roads = list(data[0].keys())
    for road in roads:
        speeds = [step[road] for step in data]
        plt.plot(speeds, label=road)

    plt.xlabel("Time step")
    plt.ylabel("Average speed (m/s)")
    plt.title("Traffic speed over time")
    plt.legend()
    plt.show()
