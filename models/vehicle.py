# models/vehicule.py

class Vehicle:
    def __init__(self, vehicle_id, road, position=0.0, speed=0.0, max_speed=13.89):
        self.id = vehicle_id
        self.road = road
        self.position = position  # in meters   
        self.speed = speed        # in m/s
        self.max_speed = max_speed

    def move(self, delta_t):
        """
        Avance la véhicule selon la vitesse et  delta_t 
        """
        distance = min(self.speed, self.max_speed) * delta_t
        # self.speed est la vitesse actuelle du véhicule
        self.position += distance
        if self.position > self.road.length:
            self.position = self.road.length
    
    def change_road(self, new_road, position=0.0):
        self.road.remove_vehicle(self)
        self.road = new_road
        self.position = position
        new_road.add_vehicle(self)