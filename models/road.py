# models/road.py
class Road:
    def __init__(self, name, length, speed_limit):
        self.name = name
        self.length = length
        self.speed_limit = speed_limit
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        self.vehicles.sort(key=lambda v: v.position)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def update_vehicles(self, delta_t):
        for vehicle in list(self.vehicles):
            vehicle.move(delta_t)
            if vehicle.position >= self.length:
                # signaler au réseau que le véhicule a atteint la fin
                pass
