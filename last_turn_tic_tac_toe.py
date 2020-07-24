import random
def movesover(board):
  for i in range(0,3):
    for j in range(0,3):
      if(board[i][j]==''):return 0
  return 1
def eval(board,turn):
   n=0
   for i in range(0,3):
    for j in range(0,3):
      if board[i][j]=="": n=n+1
   if n==9:return 0
   for i in range(0,3):
    if (board[i][0]==board[i][1]==board[i][2]!=""):
      if turn=="player": 
        return 10
      elif (turn=="opponent"): return -10
    elif (board[0][i]==board[1][i]==board[2][i]!=""):
      if turn=="player":
        return 10
      elif (turn=="opponent"): return -10
    elif (board[0][0]==board[1][1]==board[2][2]!=""):
      if turn=="player":
        return 10
      elif (turn=="opponent"): return -10
    elif (board[0][2]==board[1][1]==board[2][0]!=""):
      if turn=="player":
        return 10
      elif (turn=="opponent"): return -10
   return 0
def bestmoves(board,max_depth,available_positions):
  if(len(available_positions)==8):
    for i in range(0,3):
      for j in range(0,3):
        if(board[i][j]!=''):
          occupied_box= [i,j]
          occupied_by=board[i][j]
    if(occupied_box==[1,1]):
      available_positions=[[0,1],[1,0],[1,2],[2,1]]
    if(occupied_by=='x'):
      return [random.choice(available_positions),'o']
    else:
      return [random.choice(available_positions),'x']
  if(max_depth==0):
    return [random.choice(available_positions),random.choice(['x','o'])]
  bestval=-1000
  bestmove='x'
  bestmoveposition=[-1,-1]
  for i in range(0,3):
    for j in range(0,3):
      for move in['x','o']:
       if (board[i][j])=='':
        board[i][j]=move
        moveval=minimax(board,0, max_depth,False,"player",-1000,1000)
        board[i][j]=''
        if (moveval>bestval):
          bestval=moveval
          bestmoveposition=[i,j]
          bestmove=move        
  return [bestmoveposition,bestmove]
def minimax(board,depth,max_depth,ismax,player,alpha,beta):
  if (player=="player"):
    score=eval(board,"player")
  else:
    score=eval(board,"opponent")  
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
      for move in ['x','o']:
       if (board[i][j])=='':
        board[i][j]=move
        b=minimax(board,depth+1,max_depth,not (ismax),"player",alpha,beta)        
        best=max(best,b)    
        alpha= max(best,alpha)      
        board[i][j]=''    
        if beta <= alpha:  
          break              
   return best
  else:
   best=1000
   for i in range(0,3):
    for j in range(0,3):
      if (board[i][j])=='':
       for move in ['x','o']:
        
        board[i][j]=move
        b=minimax(board,depth+1,max_depth,not (ismax),"opponent",alpha,beta) 
        best=min(best,b)
        beta=min(best,beta)        
        board[i][j]='' 
        if beta <= alpha:  
          break 
   return best