# core/simulator.py : classe principale qui lance la simulation.
import json
from models.network import RoadNetwork
from core.analyzer import Analyzer

class Simulator:
    def __init__(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
        self.network = RoadNetwork.from_config(config)
        self.analyzer = Analyzer(self.network)
        self.time = 0.0

    def run_simulation(self, n_steps, delta_t):
        for step in range(n_steps):
            # Mettre à jour tous les véhicules
            for road in self.network.roads:
                road.update_vehicles(delta_t)

            # Collecte des statistiques
            self.analyzer.collect(step, delta_t)
            self.time += delta_t

            print(f"Step {step+1}/{n_steps} — Time: {self.time}s")

        # Retourne les résultats finaux
        return self.analyzer.results()
