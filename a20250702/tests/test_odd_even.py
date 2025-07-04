from a20250702.odd_even import OddEven
import pytest
import random

@pytest.fixture
def even():
    print()
    print("## Prepare even numbers ##")
    yield [2*n for n in range(1, 6)]
    print("## Even numbers fixture cleanup ##")

@pytest.fixture
def odd():
    print()
    print("## Prepare odd numbers ##")
    yield [2*n + 1 for n in range(1, 6)]
    print("## Odd numbers fixture cleanup ##")

@pytest.fixture
def mixed():
    print()
    print("## Prepare mixed numbers ##")
    yield [random.choice([2*n, 2*n + 1]) for n in range(1, 6)]
    print("## Mixed numbers fixture cleanup ##")

def test_even(even):
    print()
    print("## Test even conversion ##")
    result = OddEven.convert(even)
    assert result is None, "Expected None for even numbers"

def test_odd(odd):
    print()
    print("## Test odd conversion ##")
    result = OddEven.convert(odd)
    assert result is None, "Expected None for odd numbers"

def test_mixed(mixed):
    print()
    print("## Test mixed conversion ##")
    result = OddEven.convert(mixed)
    assert result is not None, "Expected a list of 'O' and 'X' for mixed numbers"
    assert len(result) == len(mixed), "Result length should match input length"
    assert all(x in ['O', 'X'] for x in result), "Result should only contain 'O' and 'X'"