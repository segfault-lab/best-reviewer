from abc import ABC, abstractmethod

class Notifier(ABC):
    def __init__(self):
        self.type = 'Notifier'

    def notify(self, weather_description: str) -> str:
        msg = self.generate_weather_alert(weather_description)
        if not msg:
            return ''
        alarm_message = f"{self.type} Alert: {msg}"
        return alarm_message

    @abstractmethod
    def generate_weather_alert(self, weather_conditions: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")
