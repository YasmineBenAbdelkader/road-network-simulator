# main.py
from core.simulator import Simulator
from io_utils.display import display_console, plot_speed_over_time, plot_congestion_over_time
from io_utils.export import export_to_json, export_to_csv

def main():
    # Initialiser le simulateur avec le fichier de configuration
    sim = Simulator("data/network_config.json")
    
    # Lancer la simulation : 60 tours, pas de temps 60s, afficher et exporter
    results = sim.lancer_simulation(n_tours=60, delta_t=60, display=False, export=False)
    
    # Affichage console
    display_console(results)
    
    # Graphiques
    plot_speed_over_time(results)
    plot_congestion_over_time(results)
    
    # Export fichiers
    export_to_json(results, "results.json")
    export_to_csv(results, "results.csv")

if __name__ == "__main__":
    main()
