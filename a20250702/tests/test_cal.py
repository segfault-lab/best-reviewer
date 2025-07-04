import pytest
from a20250702.cal import Cal

def test_cal1():
    cal = Cal()
    assert cal.add(1, 2) == 3

def test_cal2():
    cal = Cal()
    assert cal.add(10, 20) == 30