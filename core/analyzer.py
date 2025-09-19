# core/analyzer.py

class Analyzer:
    def __init__(self, network):
        self.network = network
        self.data = []

    def collect(self, step, delta_t):
        """
        Collecte les statistiques à chaque étape :
        - vitesse moyenne
        - zone de congestion
        - temps de parcours estimé
        """
        stats = {}
        for road in self.network.roads:
            if road.vehicles:
                avg_speed = sum(v.speed for v in road.vehicles) / len(road.vehicles)
            else:
                avg_speed = 0

            # Congestion : True si vitesse moyenne < 50% de la limite
            congested = avg_speed < 0.5 * road.speed_limit

            # Temps de parcours estimé (en secondes)
            if avg_speed > 0:
                estimated_time = (road.length / avg_speed)
            else:
                estimated_time = None  # Route bloquée

            stats[road.name] = {
                "avg_speed": avg_speed,
                "congested": congested,
                "estimated_time_sec": estimated_time
            }

        self.data.append(stats)

    def results(self):
        """
        Retourne toutes les statistiques collectées
        """
        return self.data
