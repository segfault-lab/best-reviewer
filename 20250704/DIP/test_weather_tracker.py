from weather_tracker import WeatherTracker
import pytest

@pytest.fixture
def tracker():
    return WeatherTracker()

def test_rainy(tracker):
    tracker.set_current_conditions('rainy')
    assert tracker.alarm() == 'Phone Alert: It is rainy'

def test_sunny(tracker):
    tracker.set_current_conditions('sunny')
    assert tracker.alarm() == 'Emailer Alert: It is sunny'