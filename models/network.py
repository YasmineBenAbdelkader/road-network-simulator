# models/network.py
from .road import Road

class RoadNetwork:
    def __init__(self):
        self.roads = []

    @classmethod
    def from_config(cls, config):
        network = cls()
        for r in config.get("roads", []):
            road = Road(r["name"], r["length"], r["speed_limit"])
            network.roads.append(road)
        return network

    def get_road_by_name(self, name):
        for road in self.roads:
            if road.name == name:
                return road
        return None
