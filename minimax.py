# -*- coding: utf-8 -*-
from tac import neighbors
import numpy as np
import random

player='x'
opponent='o'
global a

def movesover(board):
  for i in range(0,3):
    for j in range(0,3):
      if(board[i][j]==''):
         return 0
  return 1

def eval(board,game):
  z=0
  for i in range(0,3):
    for j in range(0,3):
      if board[i][j]=="":
        z=z+1
  if z==9:
    return 0
  for i in range(0,3):
    if (board[i][0]==board[i][1]==board[i][2]):
      if board[i][0]==player: 
        if game==1: return 10
        elif game==2: return -10
      elif (board[i][0]==opponent): 
        if game==1: return -10
        elif game==2: return 10
    elif (board[0][i]==board[1][i]==board[2][i]):
      if board[0][i]==player:
        if game==1: return 10
        elif game==2: return -10
      elif (board[0][i]==opponent): 
        if game==1: return -10
        elif game==2: return 10
    elif (board[0][0]==board[1][1]==board[2][2]):
      if board[0][0]==player:
        if game==1: return 10
        elif game==2: return -10
      elif (board[0][0]==opponent):
        if game==1: return -10
        elif game==2: return 10
    elif (board[0][2]==board[1][1]==board[2][0]):
      if board[2][0]==player:
        if game==1: return 10
        elif game==2:return -10
      elif (board[2][0]==opponent):
        if game==1: return -10
        elif game==2: return 10
  return 0

def bestmoves(board,max_depth,game):
  moves=[[ -100, -100, -100 ], [ -100, -100, -100 ],  [ -100, -100, -100 ]]
  for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        if(max_depth==1):
          moves[i][j]=0
        else:
          board[i][j]=player
          if(game==1):
             moveval=minimax(board,0, False,max_depth,game,-1000,1000)
          else:
             moveval=minimax(board,0, False,max_depth,game,-1000,1000)+neighbors(board)
          moves[i][j]=moveval
          board[i][j]=''   
  choice=random_move(moves)
  print(choice)
  return choice

def random_move(moves):
  max_value=max(np.concatenate(moves))
  max_moves=[]
  for i in range(0,3):
    for j in range(0,3):
       if moves[i][j]==max_value:
          max_moves.append([i,j])
  print([max_value,max_moves])
  return random.choice(max_moves)
  

def minimax(board,depth,ismax,max_depth,game,alpha,beta):                                                         
  score=eval(board,game)
  if score==10 : 
    return score-depth
  if score == -10 :
    return score+depth
  if depth==max_depth:
    return score
  if movesover(board) : 
    return 0
  if (ismax):
   best=-1000
   for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        board[i][j]=player
        best=max(best,minimax(board,depth+1,not (ismax),max_depth,game,alpha,beta)) 
        alpha = max(alpha, best) 
        board[i][j]=''
        if beta <= alpha:  
          break 
   return best
  else:
   best=1000
   for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        board[i][j]=opponent
        best=min(best,minimax(board,depth+1,not (ismax),max_depth,game,alpha,beta))   
        beta = min(beta, best)     
        board[i][j]=''
        if beta <= alpha:  
          break 
   return best



