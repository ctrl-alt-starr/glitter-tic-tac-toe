import minimax
import last_turn_tic_tac_toe
def game_redirection(board,depth,game):
    if(game==1 or game ==2):
        return minimax.bestmoves(board,depth,game)
    elif(game==3):
        return last_turn_tic_tac_toe.bestmove(board,depth)

