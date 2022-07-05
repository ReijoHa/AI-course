"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    playerX = 0
    playerO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                playerX += 1
            elif board[i][j] == O:
                playerO += 1

    if playerX > playerO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfAll = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                add = (i, j)
                setOfAll.add(add)

    return setOfAll


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newMove = deepcopy(board)
    i, j = action

    if (newMove[i][j] != EMPTY):
        raise ValueError
    else:
        newMove[i][j] = player(board)

    return newMove


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for winnerOf in (X, O):
        for row in board:
            if 3 * [winnerOf] == row:
                return winnerOf

        for i in range(3):
            v = [board[0][i], board[1][i], board[2][i]]
            if 3 * [winnerOf] == v:
                return winnerOf

        if 3 * [winnerOf] == [board[0][0], board[1][1], board[2][2]]:
            return winnerOf
        elif 3 * [winnerOf] == [board[2][0], board[1][1], board[0][2]]:
            return winnerOf

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X or winner(board) == O):
        return True
    elif not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    minboard = minvalue(board)

    maxboard = maxvalue(board)

    if player(board) == O:
        return minboard[1]

    else:
        return maxboard[1]


def minvalue(board):
    if terminal(board):
        return utility(board), ()
    else:
        v = math.inf
        for act in actions(board):
            max_value = maxvalue(result(board, act))[0]
            if max_value < v:
                v = max_value
                optimal = act
        return v, optimal


def maxvalue(board):
    if terminal(board):
        return utility(board), ()
    else:
        v = -math.inf
        for act in actions(board):
            min_value = minvalue(result(board, act))[0]
            if min_value > v:
                v = min_value
                optimal = act
        return v, optimal

