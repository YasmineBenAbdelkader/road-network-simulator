# io_utils/display.py
import matplotlib
matplotlib.use('TkAgg')  # pour Windows / scripts classiques
import matplotlib.pyplot as plt

def display_console(data, step=None):
    """
    Affiche les statistiques dans la console.
    
    Parameters:
    - data : liste des dicts renvoyés par Analyzer.results()
    - step : étape spécifique à afficher (None = toutes)
    """
    if step is not None:
        data_to_show = [data[step]]
    else:
        data_to_show = data

    for t, stats in enumerate(data_to_show):
        print(f"\n--- Step {step if step is not None else t+1} ---")
        for road, road_data in stats.items():
            # Vérification si estimated_time_sec est None
            est_time = "N/A" if road_data['estimated_time_sec'] is None else f"{road_data['estimated_time_sec']:.2f}"
            print(f"Road {road}: Avg Speed={road_data['avg_speed']:.2f} m/s, "
                  f"Congested={'Yes' if road_data['congested'] else 'No'}, "
                  f"Est. Time={est_time} s")


def plot_speed_over_time(data):
    """
    Trace les vitesses moyennes des routes au fil du temps.
    """
    if not data:
        print("No data to plot")
        return

    roads = list(data[0].keys())
    for road in roads:
        speeds = [step[road]["avg_speed"] for step in data]
        plt.plot(speeds, label=road)

    plt.xlabel("Time step")
    plt.ylabel("Average speed (m/s)")
    plt.title("Traffic speed over time")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_congestion_over_time(data):
    """
    Trace un graphique des zones de congestion (1 = congested, 0 = free).
    """
    if not data:
        print("No data to plot")
        return

    roads = list(data[0].keys())
    for road in roads:
        congestion = [1 if step[road]["congested"] else 0 for step in data]
        plt.plot(congestion, label=road)

    plt.xlabel("Time step")
    plt.ylabel("Congested (1=Yes, 0=No)")
    plt.title("Traffic congestion over time")
    plt.legend()
    plt.grid(True)
    plt.show()
