from enum import Enum

class GameStatus(Enum):
    ONGOING = "Ongoing"
    TIE = "Tie"
    WINNER = "Winner"

class Board:
    def __init__(self):
        self.player1 = 1
        self.player2 = -1
        self.turn = self.player1
        self.winner = 0
        self.state = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
            ]

    def available_moves(self) -> [int]:
        available_moves = []
        for i, pos in enumerate(self.state):
            if pos == 0:
                available_moves.append(i)
        return available_moves

    def check_winner(self) -> GameStatus:
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        
        for combo in winning_combinations:
            values = [self.state[i] for i in combo]
            if values[0] == values[1] == values[2] != 0:
                self.winner = values[0]
                return GameStatus.WINNER
        
        if 0 not in self.state:
            return GameStatus.TIE

        return GameStatus.ONGOING

    def reward(self, role: int) -> int:
        if self.winner == 0:
            return 0
        elif self.winner == role:
            return 1
        return 0

    def make_move(self, pos: int) -> GameStatus:
        if pos not in self.available_moves():
            return self.check_winner()
        self.state[pos] = self.turn
        self.turn = self.player2 if self.turn is self.player1 else self.player1
        return self.check_winner()

    def current_player(self):
        return self.turn
    
    def reset_board(self):
        self.state = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
            ]
        self.turn = self.player1
