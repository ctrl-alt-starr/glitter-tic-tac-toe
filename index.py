import tictactoe
import last_turn_tic_tac_toe
global DATA 
DATA= {
                1:[0,0],
                2:[0,1],
                3:[0,2],
                4:[1,0],
                5:[1,1],
                6:[1,2],
                7:[2,0],
                8:[2,1],
                9:[2,2]
            }
reversed_data = {tuple(value) : key for (key, value) in DATA.items()}
class Board:
    def __init__(self,max_depth,game):
        self.board= [[ '', '', '' ], [ '', '', '' ],  [ '', '', '' ]]
        self.available_positions=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.max_depth=max_depth
        self.winner= None
        self.game=game
    def update_position(self,position,player_symbol,turn):
        self.board[position[0]][position[1]]=player_symbol
        if(self.available_positions!=[]):
           self.available_positions.remove(position)
        self.winner_function(turn)
    def winner_function(self,turn):
        if(self.game==1 or self.game ==2):
           self.winner= tictactoe.eval(self.board,self.game)  
        else:
          self.winner= last_turn_tic_tac_toe.eval(self.board,turn)  
        return self.winner
    def is_winner(self):
        if self.winner==10 or self.winner==-10:
            return True
        else:
            return False
    def available_positions_function(self):
        return self.available_positions
    def board_function(self):
        return self.board
    def depth_function(self):
        return self.max_depth
    def winner_orientation(self):
        for i in range(0,3):
            if(self.game!=2):
                 if (self.board[i][0]==self.board[i][1]==self.board[i][2]!=""): return [[i,0],[i,1],[i,2]]     
                 elif (self.board[0][i]==self.board[1][i]==self.board[2][i]!=""): return [[0,i],[1,i],[2,i]]  
                 elif (self.board[0][0]==self.board[1][1]==self.board[2][2]!=""): return [[0,0],[1,1],[2,2]]
                 elif (self.board[0][2]==self.board[1][1]==self.board[2][0]!=""):return [[0,2],[1,1],[2,0]]
            else:
                if(self.winner==10):symbol='x'
                else: symbol='o'
                winnerboxes=[]
                for i in range(0,3):
                    for j in range(0,3):
                        if(self.board[i][j]==symbol):
                            winnerboxes.append([i,j])
                return winnerboxes
            

    def winner_boxes(self):
        boxes=self.winner_orientation()
        box_id=[]
        for box in boxes:
           box_id.append( reversed_data[tuple(box)])
        return box_id
        
      
    
