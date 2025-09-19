# tests/test_simulator.py
import pytest
from models.road import Road
from models.vehicle import Vehicle

def test_vehicle_move():
    road = Road("TestRoad", length=100, speed_limit=10)
    vehicle = Vehicle("v1", road, speed=5)
    road.add_vehicle(vehicle)
    
    vehicle.move(2)  # delta_t = 2s
    assert vehicle.position == 10

def test_add_remove_vehicle():
    road = Road("R", 50, 10)
    vehicle = Vehicle("v2", road)
    road.add_vehicle(vehicle)
    assert vehicle in road.vehicles
    road.remove_vehicle(vehicle)
    assert vehicle not in road.vehicles
