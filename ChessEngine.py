"""
Storing information about current state of a game, as well as legal moves
"""

class GameState():
    def __init__(self):
        # The board is an 8x8 2d array, each piece is represented by 2 letters. The first 
        # letter is the color of the piece and the second character represents the type
        # of piece, as per standard chess notation. Two dashes represents an empty board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []