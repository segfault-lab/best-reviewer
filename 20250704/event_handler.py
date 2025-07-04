from abc import abstractmethod, ABC

from vehicle import Vehicle, DrivingMode

class DrivingStrategy(ABC):
    @abstractmethod
    def setup(self, vehicle: Vehicle):
        raise NotImplementedError

class DefaultStrategy(DrivingStrategy):
    def setup(self, vehicle: Vehicle):
        vehicle.set_power(400)
        vehicle.set_suspension_height(20)

class SportStrategy(DrivingStrategy):
    def setup(self, vehicle: Vehicle):
        vehicle.set_power(500)
        vehicle.set_suspension_height(10)

class ComfortStrategy(DrivingStrategy):
    def setup(self, vehicle: Vehicle):
        vehicle.set_power(400)
        vehicle.set_suspension_height(20)


class EventHandler:
    strategies = {
        DrivingMode.SPORT: SportStrategy(),
        DrivingMode.COMFORT: ComfortStrategy(),
        None: DefaultStrategy()
    }

    def __init__(self, vehicle:Vehicle) -> None:
        super().__init__()
        self.__vehicle = vehicle
        self.__strategies = DefaultStrategy()

    def set_strategy(self, driving_mode: DrivingMode | None):
        self.__strategies = self.strategies.get(driving_mode)

    def change_driving_mode(self, driving_mode: DrivingMode | None):
        self.set_strategy(driving_mode)
        self.__strategies.setup(self.__vehicle)

        # when we need to add another mode (e.g. ECONOMY) 2 classes will change DrivingMode and EventHandler.
