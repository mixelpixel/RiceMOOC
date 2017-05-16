"""
#- "Mini-Max Tic-Tac-Toe" by pdk
#- For Coursera: Rice U. Principles of Computing pt.2
#---#----1----#----2----#----3----#----4----#----5----#----6----#----7-2--#----8----#----91234567100
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import codeskulptor
codeskulptor.set_timeout(60)

SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    Returns a tuple with two elements: score & desired move as a
    tuple, (row, col).
    """
    return mm_move_helper(board, player, -2, 2)


def mm_move_helper(board, player, alpha, beta):
    """
    helps with moving
    """
    winner = board.check_win()
    if winner != None:
        return ( SCORES[winner], (-1, -1) )

    other = provided.switch_player(player)
    best = -2
    best_move = (-1, -1)

    for move1 in board.get_empty_squares():
        trial_board = board.clone()
        trial_board.move(move1[0], move1[1], player)
        score = mm_move_helper(trial_board, other, -beta, -max(alpha, best))[0]
        alpha = score * SCORES[player]
        if alpha == 1:
            return score, move1
        elif alpha > best:
            best = alpha
            best_move = move1
        if best >= beta:
            break
    return best * SCORES[player], best_move


def move_wrapper(board, player, trials):
    """
    Wrapper like Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

