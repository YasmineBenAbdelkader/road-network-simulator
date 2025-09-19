# core/analyzer.py
class Analyzer:
    def __init__(self, network):
        self.network = network
        self.data = []

    def collect(self, step, delta_t):
        """
        Collecte des statistiques simples : vitesse moyenne par route
        """
        stats = {}
        for road in self.network.roads:
            if road.vehicles:
                avg_speed = sum(v.speed for v in road.vehicles) / len(road.vehicles)
            else:
                avg_speed = 0
            stats[road.name] = avg_speed
        self.data.append(stats)

    def results(self):
        """
        Retourne toutes les statistiques collectées
        """
        return self.data
