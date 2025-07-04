class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)  # 정사각형이므로 높이도 설정

    def set_height(self, height):
        super().set_width(height)  # 정사각형이므로 너비도 설정
        super().set_height(height)

import pytest

@pytest.fixture
def rectangle():
    return Rectangle()
@pytest.fixture
def square():
    return Square()

def check_area(ret: Rectangle, width=10, height=20):
    ret.set_width(width)
    ret.set_height(height)
    assert ret.area() == width * height, f"Expected area {width * height}, got {ret.area()}"

def test_rectangle_area(rectangle):
    check_area(rectangle)

def test_square_area(square):
    with pytest.raises(AssertionError):
        check_area(square)