# models/vehicle.py

class Vehicle:
    def __init__(self, vehicle_id, road, position=0.0, speed=0.0, max_speed=13.89):
        """
        vehicle_id : str
        road : Road object
        position : float (meters)
        speed : float (m/s)
        max_speed : float (m/s)
        """
        self.id = vehicle_id
        self.road = road
        self.position = position
        self.speed = speed
        self.max_speed = max_speed

    def move(self, delta_t):
        """
        Avance le véhicule sur sa route
        """
        distance = min(self.speed, self.max_speed) * delta_t
        self.position += distance
        if self.position >= self.road.length:
            self.position = self.road.length

    def change_road(self, new_road, position=0.0):
        """
        Change le véhicule de route
        """
        self.road.remove_vehicle(self)
        self.road = new_road
        self.position = position
        new_road.add_vehicle(self)
