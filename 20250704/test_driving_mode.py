import pytest
from vehicle import Vehicle, DrivingMode
from event_handler import EventHandler

@pytest.fixture
def vehicle():
    return Vehicle()

@pytest.fixture
def handler(vehicle):
    return EventHandler(vehicle)

def test_sport_mode(handler, vehicle):
    handler.change_driving_mode(DrivingMode.SPORT)
    assert vehicle.get_power() == 500
    assert vehicle.get_suspension_height() == 10

def test_comfort_mode(handler, vehicle):
    handler.change_driving_mode(DrivingMode.COMFORT)
    assert vehicle.get_power() == 400
    assert vehicle.get_suspension_height() == 20

def test_default_mode(handler, vehicle):
    handler.change_driving_mode(None)  # Assuming None is treated as default
    assert vehicle.get_power() == 400
    assert vehicle.get_suspension_height() == 20