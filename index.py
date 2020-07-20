from minimax import eval
class Board:
    def __init__(self,maxDepth,game):
        self.board= [[ '', '', '' ], [ '', '', '' ],  [ '', '', '' ]]
        self.available_positions=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.maxDepth=maxDepth
        self.winner= None
        self.game=game
    def update_position(self,position,player_symbol):
        self.board[position[0]][position[1]]=player_symbol
        if(self.available_positions!=[]):
           self.available_positions.remove(position)
        self.winner_function()
    def winner_function(self):
        self.result= eval(self.board,self.game)        
        return self.result
    def isWinner(self):
        if self.winner==10 or self.winner==-10:
            return True
        else:
            return False
    def available_positions_function(self):
        return self.available_positions
    def board_function(self):
        return self.board
    def depth_function(self):
        return self.maxDepth