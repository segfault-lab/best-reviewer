class Robot:
    def __init__(self, hp):
        self.hp = hp
        self._status = "Idle"

    def move(self):
        print("[Robot] Moving...")

    def stop(self):
        print("[Robot] Stopping...")

class SpeedRobot(Robot):
    def __init__(self, model_id, hp):
        super().__init__(hp)
        self.model_id = model_id

    def run(self):
        print(f"[Speed{self.model_id}] Running...")

    def walk(self):
        print(f"[Speed{self.model_id}] Walking...")

class PowerRobot(Robot):
    def __init__(self, hp, mp):
        super().__init__(hp)
        self.mp = mp

    def attack(self):
        print(f"[PowerRobot] Attacking...")

    def jump(self):
        print(f"[PowerRobot] Jumping...")
        