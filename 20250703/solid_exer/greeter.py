from abc import abstractmethod, ABC

class Greeter:
    def __init__(self) -> None:
        self.__formality: Formality = "normal"
        self._greet_style = Normal()

    def greet(self) -> str:
        return self._greet_style.greet()

    def set_formality(self, formality: str):
        self.__formality = formality
        self._greet_style = {
            "normal": Normal,
            "formal": Formal,
            "casual": Casual,
            "intimate": Intimate
        }[formality]()

class Formality(ABC):
    @abstractmethod
    def greet(self) -> str:
        raise NotImplementedError("Subclasses should implement this method")

class Normal(Formality):
    def greet(self) -> str:
        return "Hello."

class Formal(Formality):
    def greet(self) -> str:
        return "Good evening, sir."

class Casual(Formality):
    def greet(self) -> str:
        return "Sup bro?"

class Intimate(Formality):
    def greet(self) -> str:
        return "Hello Darling!"

def test_greeter_normal():
    greeter = Greeter()
    assert greeter.greet() == "Hello."

def test_greeter_back_to_normal():
    greeter = Greeter()
    greeter.set_formality("formal")
    greeter.set_formality("normal")
    assert greeter.greet() == "Hello."

def test_greeter_formal():
    greeter = Greeter()
    greeter.set_formality("formal")
    assert greeter.greet() == "Good evening, sir."

def test_greeter_casual():
    greeter = Greeter()
    greeter.set_formality("casual")
    assert greeter.greet() == "Sup bro?"

def test_greeter_intimate():
    greeter = Greeter()
    greeter.set_formality("intimate")
    assert greeter.greet() == "Hello Darling!"