PLAYER='x'
OPPONENT='o'
def neighbors(board):
 score=0
 for i in range(0,3):
   if (board[i][0]==board[i][1]!=""and board[i][2]==""):     
      if (board[i][0]==PLAYER):score=score-1
      elif (board[i][0]==OPPONENT):score=score+1
   if (board[i][0]==board[i][2]!=""and (board[i][1]=="" )):
     
      if board[i][0]==PLAYER:score=score-1
      elif (board[i][0]==OPPONENT):score=score+1
   if (board[i][1]==board[i][2]!=""and (board[i][0]=="" )):
      
      if board[i][1]==PLAYER:score=score-1
      elif (board[i][1]==OPPONENT):score=score+1
 for i in range(0,3):
   if (board[0][i]==board[1][i]!=""and (board[2][i]=="" )):
      
      if board[0][i]==PLAYER:score=score-1
      elif (board[0][i]==OPPONENT):score=score+1
   if (board[0][i]==board[2][i]!=""and (board[1][i]=="" )):
    
      if board[0][i]==PLAYER:score=score-1
      elif (board[0][i]==OPPONENT):score=score+1
   elif (board[1][i]==board[2][i]!=""and (board[0][i]=="")):
    
      if board[1][i]==PLAYER:score=score-1
      elif (board[1][i]==OPPONENT):score=score+1  
 if (board[0][0]==board[1][1]!=""and (board[2][2]=="")):
      if board[0][0]==PLAYER:score=score-1
      elif (board[0][0]==OPPONENT):score=score+1
 if (board[1][1]==board[2][2]!=""and (board[0][0]=="" )):
      if board[1][1]==PLAYER:score=score-1
      elif (board[1][1]==OPPONENT):score=score+1
 if (board[0][2]==board[1][1]!=""and (board[2][0]=="" )):
      if board[1][1]==PLAYER:score=score-1
      elif (board[1][1]==OPPONENT):score=score+1
 if (board[1][1]==board[2][0]!=""and (board[0][2]=="" )):
      if board[1][2]==PLAYER:score=score-1
      elif (board[1][2]==OPPONENT):score=score+1
 if (board[0][2]==board[2][0]!=""and (board[1][1]=="" )):
      if board[1][1]==PLAYER:score=score-1
      elif (board[1][1]==OPPONENT):score=score+1
 if (board[0][0]==board[2][2]!=""and (board[1][1]=="" )):
      if board[2][2]==PLAYER:score=score-1
      elif (board[2][2]==OPPONENT):score=score+1
 return score
