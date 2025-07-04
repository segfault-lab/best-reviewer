class CoinSlot:
    def __init__(self):
        self._coin = 0

    def input_coin(self, count):
        if count > 5:
            raise ValueError("최대 5개까지만 가능합니다")
        if self._coin + count > 10:
            raise ValueError("총 코인은 10개를 초과할 수 없습니다")
        self._coin += count

    def show_coin(self):
        print(f"현재 coin은 {self._coin}개 있습니다")

    def use_coin(self):
        if self._coin <= 0:
            raise ValueError("코인이 부족합니다")
        self._coin -= 1

class GameMachine:
    def __init__(self):
        self.coin_slot = CoinSlot()

    def play(self):
        try:
            self.coin_slot.use_coin()
            print("게임 시작!")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    game_machine = GameMachine()
    game_machine.coin_slot.input_coin(3)
    game_machine.coin_slot.show_coin()

    for _ in range(4):
        game_machine.play()
        game_machine.coin_slot.show_coin()

    try:
        game_machine.coin_slot.input_coin(8)
    except ValueError as e:
        print(e)

    try:
        for _ in range(3):
            game_machine.coin_slot.input_coin(4)
    except ValueError as e:
        print(e)

    try:
        while True:
            game_machine.coin_slot.use_coin()
    except ValueError as e:
        print(e)