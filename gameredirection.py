import tictactoe
import last_turn_tic_tac_toe
def game_redirection(board,depth,available_positions,game):
    if(game==1 or game ==2):
        return [tictactoe.bestmoves(board,depth,game),0]
    elif(game==3):
        return last_turn_tic_tac_toe.bestmoves(board,depth,available_positions)

