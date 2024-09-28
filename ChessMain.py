"""
Main driver file, handles user input and displays current position
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
MAX_FPS = 15
global IMAGES
IMAGES = {}

def loadPics():
    pieces = ["wp", "wR", "wB", "wQ", "wK", "wN", "bp", "bR", "bB", "bK", "bQ", "bN"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/"+piece+".png")
