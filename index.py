import numpy as np
class Board:
    def __init__(self,maxDepth):
        self.board= [[ '', '', '' ], [ '', '', '' ],  [ '', '', '' ]]
        self.available_positions=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.maxDepth=maxDepth
    def update_position(self,position,player_symbol):
        self.board[position[0]][position[1]]=player_symbol
        print("_____________")
        print(position)
        print("1")
        if(self.available_positions!=[]):
           self.available_positions.remove(position)
        print("2")
        print(position)
        print("_____________")
    def available_positions_function(self):
        return self.available_positions
    def board_function(self):
        return self.board
    def depth_function(self):
        return self.maxDepth
