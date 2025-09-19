# models/road.py
from .vehicle import Vehicle

class Road:
    def __init__(self, name, length, speed_limit):
        self.name = name
        self.length = length
        self.speed_limit = speed_limit
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        self.vehicles.sort(key=lambda v: v.position)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def update_vehicles(self, delta_t):
        for vehicle in list(self.vehicles):
            vehicle.move(delta_t)
            # Si le véhicule atteint la fin de la route
            if vehicle.position >= self.length:
                # Pour l'instant, on le garde à la fin
                vehicle.position = self.length
