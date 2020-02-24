"""
Classes to represent Games.
"""

class Game:
    """
    General representation of an abstract game
    """
    fun_level = 5

    def __init__(self, player1='Alice', player2='Bob'):
        self.rounds = 2
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

def print_players(self):
    """Print the players of the game."""
    print('{} is playing {}'.format(self.player1, self.player2))

def add_round(self):
    self.round += 1

class TicTacToe(Game):
    """TicTacToe game representation."""
    def print_players(self):
        print('{} is playing Tic-Tac-Toe with {}'.format(self.player1,
                                                         self.player2))
