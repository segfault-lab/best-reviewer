from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, initial_feather_count) -> None:
        super().__init__()
        self.__current_location = ""
        self.__number_of_feathers = initial_feather_count

    @property
    def current_location(self):
        return self.__current_location

    @property
    def number_of_feathers(self):
        return self.__number_of_feathers

    def set_current_location(self, location: str):
        self.__current_location = location

    def set_number_of_feathers(self, feather_count: int):
        self.__number_of_feathers = feather_count

class Flyable(ABC):
    @abstractmethod
    def fly(self): pass

class Moltable(ABC):
    @abstractmethod
    def molt(self): pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass