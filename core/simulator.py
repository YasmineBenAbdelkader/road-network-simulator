# core/simulator.py
import json
from models.network import RoadNetwork
from core.analyzer import Analyzer
from io_utils.display import plot_speed_over_time
from io_utils.export import export_to_json, export_to_csv
from models.vehicle import Vehicle

class Simulator:
    def __init__(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
        self.network = RoadNetwork.from_config(config)
        self.analyzer = Analyzer(self.network)
        self.time = 0.0

        # Ajouter véhicules initiaux depuis config
        for v in config.get("vehicles_init", []):
            road = self.network.get_road_by_name(v["road"])
            if road:
                vehicle = Vehicle(
                    vehicle_id=v["id"],
                    road=road,
                    position=v.get("position", 0.0),
                    speed=v.get("speed", 0.0)
                )
                road.add_vehicle(vehicle)

    def lancer_simulation(self, n_tours, delta_t, display=False, export=False):
        """
        Lance la simulation pour n_tours étapes avec pas de temps delta_t (secondes)
        display : si True, affiche un plot à la fin
        export : si True, exporte les résultats en JSON et CSV
        """
        for tour in range(n_tours):
            # Mise à jour des véhicules sur toutes les routes
            for road in self.network.roads:
                road.update_vehicles(delta_t)

            # Mise à jour des statistiques
            self.analyzer.collect(tour, delta_t)
            self.time += delta_t

            # Affichage intermédiaire dans la console
            print(f"Tour {tour+1}/{n_tours} — Temps écoulé: {self.time}s")
            for road in self.network.roads:
                print(f"  {road.name}: {len(road.vehicles)} véhicules")

        # Affichage final si demandé
        if display:
            plot_speed_over_time(self.analyzer.results())

        # Export final si demandé
        if export:
            export_to_json(self.analyzer.results(), "results.json")
            export_to_csv(self.analyzer.results(), "results.csv")

        return self.analyzer.results()
