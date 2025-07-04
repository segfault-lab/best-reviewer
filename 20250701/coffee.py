from abc import ABC, abstractmethod

class Coffee:
    VOLUME = {"tall": 280, "grande": 365, "venti": 500}
    def __init__(self):
        self._volume: int = 0

    def brew(self, size: str):
        if size not in Coffee.VOLUME:
            raise ValueError(f"Invalid size: {size}. Choose from {list(Coffee.VOLUME.keys())}.")
        self._volume = self.VOLUME[size]

    def _check_volume(self):
        if self._volume == 0:
            raise ValueError("No coffee brewed. Please brew coffee first.")

    def get_size(self):
        self._check_volume()
        return self._volume

    @abstractmethod
    def drink(self):
        pass

class Americano(Coffee):
    def drink(self):
        self._check_volume()
        print(f"Drinking Americano of size {self._volume}ml.")

class IcedAmericano(Coffee):
    def drink(self):
        self._check_volume()
        print(f"Drinking Iced Americano of size {self._volume}ml.")

class Latte(Coffee):
    def drink(self):
        self._check_volume()
        print(f"Drinking Latte of size {self._volume}ml.")

class Barista:
    @staticmethod
    def make_coffee(menu: str, size: str) -> Coffee:
        coffee_classes = {
            "americano": Americano,
            "iced_americano": IcedAmericano,
            "latte": Latte
        }
        if menu not in coffee_classes:
            raise ValueError(f"Invalid menu item: {menu}. Choose from {list(coffee_classes.keys())}.")

        coffee = coffee_classes[menu]()
        coffee.brew(size)
        return coffee

if __name__ == "__main__":
    try:
        coffee = Barista.make_coffee("americano", "tall")
        coffee.drink()
        print(f"Size: {coffee.get_size()}ml")

        coffee = Barista.make_coffee("iced_americano", "grande")
        coffee.drink()
        print(f"Size: {coffee.get_size()}ml")

        coffee = Barista.make_coffee("latte", "venti")
        coffee.drink()
        print(f"Size: {coffee.get_size()}ml")

    except ValueError as e:
        print(e)