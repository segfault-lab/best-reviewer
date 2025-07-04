class Phone:
    def __init__(self):
        self.class_name = "Phone"
    def call(self):
        print(f"[{self.class_name}] Calling...")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.class_name = "SmartPhone"

    def internet(self):
        print(f"[{self.class_name}] Browsing the internet")

    def call(self):
        print(f"[{self.class_name}] Smart calling...")


class RadioPhone(Phone):
    def __init__(self):
        super().__init__()
        self.class_name = "RadioPhone"

    def call(self):
        print(f"[{self.class_name}] Radio calling...")


def phone_call(phone: Phone):
    phone.call()

def raio_phone_call(phone: RadioPhone):
    phone.call()

if __name__ == "__main__":
    phone = Phone()
    smart_phone = SmartPhone()
    radio_phone = RadioPhone()

    phone_call(phone)
    phone_call(smart_phone)
    phone_call(radio_phone)

    raio_phone_call(radio_phone)
    try:
        raio_phone_call(smart_phone)
    except TypeError as e:
        print(f"Error: {e}")
