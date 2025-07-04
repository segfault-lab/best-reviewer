from phone import Phone
from emailer import Emailer
from notifier import Notifier

class WeatherTracker:
    def __init__(self) -> None:
        super().__init__()
        self.__current_conditions = ""
        self.__notifiers: list[Notifier] = [Phone(), Emailer()]

    def set_current_conditions(self, weather_description: str) -> None:
        self.__current_conditions = weather_description

    def alarm(self) -> str:
        msgs = []
        for notifier in self.__notifiers:
            msg = notifier.notify(self.__current_conditions)
            if msg:
                msgs.append(msg)
        return '\n'.join(msgs)

