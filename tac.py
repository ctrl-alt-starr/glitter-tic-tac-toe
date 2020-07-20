player='x'
opponent='o'
def neighbors(board):
 score=0
 for i in range(0,3):
   if (board[i][0]==board[i][1]!=""and board[i][2]==""):     
      if (board[i][0]==player):score=score-1
      elif (board[i][0]==opponent):score=score+1
   if (board[i][0]==board[i][2]!=""and (board[i][1]=="" )):
     
      if board[i][0]==player:score=score-1
      elif (board[i][0]==opponent):score=score+1
   if (board[i][1]==board[i][2]!=""and (board[i][0]=="" )):
      
      if board[i][1]==player:score=score-1
      elif (board[i][1]==opponent):score=score+1
 for i in range(0,3):
   if (board[0][i]==board[1][i]!=""and (board[2][i]=="" )):
      
      if board[0][i]==player:score=score-1
      elif (board[0][i]==opponent):score=score+1
   if (board[0][i]==board[2][i]!=""and (board[1][i]=="" )):
    
      if board[0][i]==player:score=score-1
      elif (board[0][i]==opponent):score=score+1
   elif (board[1][i]==board[2][i]!=""and (board[0][i]=="")):
    
      if board[1][i]==player:score=score-1
      elif (board[1][i]==opponent):score=score+1  
 if (board[0][0]==board[1][1]!=""and (board[2][2]=="")):
      if board[0][0]==player:score=score-1
      elif (board[0][0]==opponent):score=score+1
 if (board[1][1]==board[2][2]!=""and (board[0][0]=="" )):
      if board[1][1]==player:score=score-1
      elif (board[1][1]==opponent):score=score+1
 if (board[0][2]==board[1][1]!=""and (board[2][0]=="" )):
      if board[1][1]==player:score=score-1
      elif (board[1][1]==opponent):score=score+1
 if (board[1][1]==board[2][0]!=""and (board[0][2]=="" )):
      if board[1][2]==player:score=score-1
      elif (board[1][2]==opponent):score=score+1
 if (board[0][2]==board[2][0]!=""and (board[1][1]=="" )):
      if board[1][1]==player:score=score-1
      elif (board[1][1]==opponent):score=score+1
 if (board[0][0]==board[2][2]!=""and (board[1][1]=="" )):
      if board[2][2]==player:score=score-1
      elif (board[2][2]==opponent):score=score+1
 return score
def eval2(board,depth):
   n=0
   for i in range(0,3):
    for j in range(0,3):
      if board[i][j]=="": n=n+1
   if n==9:return 0
   for i in range(0,3):
    if (board[i][0]==board[i][1]==board[i][2]):
      if board[i][0]==player:return -10
      elif (board[i][0]==opponent): return 10
    elif (board[0][i]==board[1][i]==board[2][i]):
      if board[0][i]==player:return -10
      elif (board[0][i]==opponent): return 10
    elif (board[0][0]==board[1][1]==board[2][2]):
      if board[0][0]==player:return -10
      elif (board[0][0]==opponent): return 10
    elif (board[0][2]==board[1][1]==board[2][0]):
      if board[2][0]==player:return -10
      elif (board[2][0]==opponent): return 10
   return 0