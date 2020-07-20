from minimax import eval
global data 
data= {
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
reversed_data = {tuple(value) : key for (key, value) in data.items()}
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
        self.winner= eval(self.board,self.game)    
        return self.winner
    def isWinner(self):
        if self.winner==10 or self.winner==-10:
            print("winner")
            return True
        else:
            return False
    def available_positions_function(self):
        return self.available_positions
    def board_function(self):
        return self.board
    def depth_function(self):
        return self.maxDepth
    def winner_orientation(self):
        for i in range(0,3):
            if (self.board[i][0]==self.board[i][1]==self.board[i][2]): return [[i,0],[i,1],[i,1]]     
            elif (self.board[0][i]==self.board[1][i]==self.board[2][i]): return [[0,i],[1,i],[2,i]]  
            elif (self.board[0][0]==self.board[1][1]==self.board[2][2]): return [[0,0],[1,1],[2,2]]
            elif (self.board[0][2]==self.board[1][1]==self.board[2][0]):return [[0,2],[1,1],[2,0]]
    def winner_boxes(self):
        boxes=self.winner_orientation()
        box_id=[]
        for box in boxes:
           box_id.append( reversed_data[tuple(box)])
        return box_id
        
      
    
