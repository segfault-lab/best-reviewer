import pytest
from eagle import Eagle
from penguin import Penguin

@pytest.fixture
def eagle():
    return Eagle(initial_feather_count=100)

@pytest.fixture
def penguin():
    return Penguin(initial_feather_count=100)

def test_eagle_fly(eagle):
    eagle.fly()
    assert eagle.current_location == "in the air"

def test_eagle_molt(eagle):
    initial_feather_count = eagle.number_of_feathers
    eagle.molt()
    assert eagle.number_of_feathers == initial_feather_count - 1

def test_penguin_swim(penguin):
    penguin.swim()
    assert penguin.current_location == "in the water"

def test_penguin_molt(penguin):
    initial_feather_count = penguin.number_of_feathers
    penguin.molt()
    assert penguin.number_of_feathers == initial_feather_count - 1