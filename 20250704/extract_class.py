import pytest


class Player:
    def __init__(self, name, level=1, hp=100, mp=100):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.mp -= 20


def test_game_player_effect():
    player = Player(name="hwan", level=10, hp=180, mp=200)
    player.level_up()

    assert player.hp == 190
    assert player.mp == 180
    assert player.level == 11
