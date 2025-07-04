from notifier import Notifier

class Emailer(Notifier):
    def __init__(self):
        super().__init__()
        self.type = 'Emailer'

    def generate_weather_alert(self, weather_conditions: str) -> str:
        if weather_conditions == 'sunny':
            return 'It is ' + weather_conditions
        return ''
