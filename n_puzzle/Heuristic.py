from Board import Board
import math as m
import numpy as np


class Heuristic:
    def Hamming(self, board):
        heuristic = 0
        for x in range(len(board)):
            for y in range(len(board)):
                if board[y][x] and Board(len(board)).getBoard()[y][x] != board[y][x]:
                    heuristic += 1
        return heuristic

    def Euclidean(self, board):
        b = Board(len(board))
        heuristic = 0
        for x1 in range(len(board)):
            for y1 in range(len(board)):
                found = False
                for x2 in range(len(board)):
                    for y2 in range(len(board)):
                        if b.getBoard()[x1][y1] == board[x2][y2]:
                            found = True
                            dx = int(m.fabs(x2 - x1))
                            dy = int(m.fabs(y2 - y1))
                            heuristic += int(m.floor(m.sqrt(dx * dx + dy * dy)))
                            break
                    if found:
                        break
        return heuristic

    def Manhattan(self, board):
        heuristic = 0
        board = np.array(board)
        b = Board(len(board))
        goal = np.array(b.getBoard())
        for x in range(len(board)):
            for y in range(len(board)):
                if board[y][x] and goal[y][x] != board[y][x]:
                    row, col = np.where(goal == board[y][x])
                    heuristic += abs(row[0] - y) + abs(col[0] - x)
        return heuristic

    def Permutation(self, board):
        heuristic = 0
        board = np.array(board)
        board = np.transpose(board).flatten()
        for x in range(len(board) - 1):
            for y in range(x + 1, len(board)):
                if board[x] and board[y] and board[x] > board[y]:
                    heuristic += 1

        if board[len(board) - 1]:
            heuristic += 1
        return heuristic
