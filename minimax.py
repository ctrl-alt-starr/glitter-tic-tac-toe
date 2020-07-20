# -*- coding: utf-8 -*-
from tac import neighbors,eval2
import numpy as np

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
        else: return -10
      elif (board[i][0]==opponent): 
        if game==1: return -10
        else: return 10
    elif (board[0][i]==board[1][i]==board[2][i]):
      if board[0][i]==player:
        if game==1: return 10
        else: return -10
      elif (board[0][i]==opponent): 
        if game==1: return -10
        else: return 10
    elif (board[0][0]==board[1][1]==board[2][2]):
      if board[0][0]==player:
        if game==1: return 10
        else: return -10
      elif (board[0][0]==opponent):
        if game==1: return -10
        else: return 10
    elif (board[0][2]==board[1][1]==board[2][0]):
      if board[2][0]==player:
        if game==1: return 10
        else: return -10
      elif (board[2][0]==opponent):
        if game==1: return -10
        else: return 10
  return 0

def bestmoves(board,max_depth,game):
  bestval=-1000
  bestmove=[-1,-1]
  for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        board[i][j]=player
        if(game==1):
          moveval=minimax(board,0, False,max_depth,game)
        else:
          moveval=minimax(board,0, False,max_depth,game)+neighbors(board)
        #print([i,j])
        #print(moveval)
        board[i][j]=''
        if (moveval>bestval):
          bestval=moveval
          bestmove=[i,j]
  return bestmove

def minimax(board,depth,ismax,max_depth,game):
                                                            
  score=eval(board,game)
  if movesover(board) : 
    return 0
  if score==10 : 
    return score-depth
  if score == -10 :
    return score+depth
  if depth==max_depth:
    return score
  if (ismax):
   best=-1000
   for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        board[i][j]=player
        best=max(best,minimax(board,depth+1,not (ismax),max_depth,game)) 
        #if (b==0):
          #print("__________")
          #print("B is zero")
        board[i][j]=''
   return best
  else:
   best=1000
   for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
        board[i][j]=opponent
        best=min(best,minimax(board,depth+1,not (ismax),max_depth,game))      
        board[i][j]=''
   return best



