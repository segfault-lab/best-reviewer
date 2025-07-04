from notifier import Notifier

class Phone(Notifier):
    def __init__(self):
        super().__init__()
        self.type = 'Phone'

    def generate_weather_alert(self, weather_conditions: str) -> str:
        if weather_conditions == 'rainy':
            return 'It is ' + weather_conditions
        return ''
