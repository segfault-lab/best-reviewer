from collections import OrderedDict as Odict


class TennisGame:
    SCORE_TEXT = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.players = Odict({player1_name: 0, player2_name: 0})

    def won_point(self, player_name):
        self.players[player_name] += 1

    def _even_score(self, score):
        if score >= 3:
            return "Deuce"
        return f"{self.SCORE_TEXT[score]}-All"

    def _advantage_or_win(self, scores: list[int]) -> str:
        names = list(self.players.keys())
        diff = scores[0] - scores[1]
        leading = names[0] if diff > 0 else names[1]
        status = "Advantage" if abs(diff) == 1 else "Win for"
        return f"{status} {leading}"

    def score(self):
        scores = list(self.players.values())
        if scores[0] == scores[1]:
            return self._even_score(scores[0])
        elif scores[0] >= 4 or scores[1] >= 4:
            return self._advantage_or_win(scores)
        else:
            return f"{self.SCORE_TEXT[scores[0]]}-{self.SCORE_TEXT[scores[1]]}"


if __name__ == "__main__":
    test_cases = [
        (0, 0, "Love-All", 'player1', 'player2'),
        (1, 1, "Fifteen-All", 'player1', 'player2'),
        (2, 2, "Thirty-All", 'player1', 'player2'),
        (3, 3, "Deuce", 'player1', 'player2'),
        (4, 4, "Deuce", 'player1', 'player2'),

        (1, 0, "Fifteen-Love", 'player1', 'player2'),
        (0, 1, "Love-Fifteen", 'player1', 'player2'),
        (2, 0, "Thirty-Love", 'player1', 'player2'),
        (0, 2, "Love-Thirty", 'player1', 'player2'),
        (3, 0, "Forty-Love", 'player1', 'player2'),
        (0, 3, "Love-Forty", 'player1', 'player2'),
        (4, 0, "Win for player1", 'player1', 'player2'),
        (0, 4, "Win for player2", 'player1', 'player2'),

        (2, 1, "Thirty-Fifteen", 'player1', 'player2'),
        (1, 2, "Fifteen-Thirty", 'player1', 'player2'),
        (3, 1, "Forty-Fifteen", 'player1', 'player2'),
        (1, 3, "Fifteen-Forty", 'player1', 'player2'),
        (4, 1, "Win for player1", 'player1', 'player2'),
        (1, 4, "Win for player2", 'player1', 'player2'),

        (3, 2, "Forty-Thirty", 'player1', 'player2'),
        (2, 3, "Thirty-Forty", 'player1', 'player2'),
        (4, 2, "Win for player1", 'player1', 'player2'),
        (2, 4, "Win for player2", 'player1', 'player2'),

        (4, 3, "Advantage player1", 'player1', 'player2'),
        (3, 4, "Advantage player2", 'player1', 'player2'),
        (5, 4, "Advantage player1", 'player1', 'player2'),
        (4, 5, "Advantage player2", 'player1', 'player2'),
        (15, 14, "Advantage player1", 'player1', 'player2'),
        (14, 15, "Advantage player2", 'player1', 'player2'),

        (6, 4, 'Win for player1', 'player1', 'player2'),
        (4, 6, 'Win for player2', 'player1', 'player2'),
        (16, 14, 'Win for player1', 'player1', 'player2'),
        (14, 16, 'Win for player2', 'player1', 'player2'),
    ]

    for p1Score, p2Score, result, name1, name2 in test_cases:
        game = TennisGame(name1, name2)
        for i in range(p1Score):
            game.won_point(name1)
        for i in range(p2Score):
            game.won_point(name2)

        ret = game.score()
        if ret == result:
            print('P', end='')
        else:
            print(f"{p1Score} : {p2Score} 는 {result} 여야 합니다. 현재 결과는 {ret} 입니다")
            print("FAIL")
