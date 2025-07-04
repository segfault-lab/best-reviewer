import random

class Zergling:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self):
        if self.mp < 10:
            print(f"[{self.name}] Not enough MP to attack")
            return
        self.hp += 1
        self.mp -= 10

    def move(self):
        if self.hp < 10:
            print(f"[{self.name}] Not enough HP to move")
            return
        self.hp -= 10
        self.mp += 5

    def status(self):
        return f"[{self.name}] HP: {self.hp}, MP: {self.mp}"

if __name__ == "__main__":
    zergling1 = Zergling("Zergling1", 100, 50)
    zergling2 = Zergling("Zergling2", 110, 40)
    random.seed(1)
    for _ in range(5):
        attaker = random.choice([zergling1, zergling2])
        mover = zergling1 if attaker == zergling2 else zergling2
        attaker.attack()
        mover.move()
        print(zergling1.status())
        print(zergling2.status())