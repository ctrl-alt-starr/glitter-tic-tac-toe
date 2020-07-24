from flask import Flask, jsonify, request, render_template
import json
from tictactoe import bestmoves,eval
from gameredirection import game_redirection
import index
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
global i
i=0

app=Flask(__name__)
@app.route('/')
def start():
    global start
    start=0
    return render_template('index.html')

@app.route('/ai',methods=["POST"])
def ai():
    global game,difficulty,opponent,board,start   
    if(start!=1):
        return jsonify("Choose the settings first and start a new game to start playing!")
    id=int(request.form["1"])
    symbol=(request.form["2"]) # This is for Last turn tic tac toe
    position=data[id]
    if(board.isWinner()):#If a game has already been won and the player is attempting to play again
        return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':["None","None"],'computermove':"None","updateopponent":False,"updateplayer":False}) 
        #[winner,winnerboxes,who_won,[player_symbol,opponent_symbol],bestmove]]
    if(position in board.available_positions_function() and not (board.isWinner())):
       if(game==3):
           opponent_symbol=symbol
       else:
           opponent_symbol='o'
       board.update_position(position,opponent_symbol,"opponent")
       if(board.isWinner()):# If the human player has won with their move
           if(game==2):winner="player"
           else:winner="opponent"
           return jsonify({'winner':True,'winner_boxes':board.winner_boxes(),'whoWon':winner,'symbol':['None',opponent_symbol],'computermove':"None","updateopponent":False,"updateplayer":True}) 
        
       bestmove=game_redirection(board.board_function(),board.depth_function(),board.available_positions_function(),game)
       if(bestmove[0]==[-1,-1]): #When all the moves are over, the algorithm simply returns [-1,-1]
           return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':["None",opponent_symbol],'computermove':"None","updateopponent":True,"updateplayer":False})
       bestmove_id=reversed_data[tuple(bestmove[0])]
       
       if(board.available_positions!=[]):
          if(game==3):
             player_symbol=bestmove[1]
          else:
             player_symbol='x'
          board.update_position(bestmove[0],player_symbol,"player") 
       if(board.available_positions!=[]):
          if((board.isWinner())):#If the computer has won with their move
             if(game!=2):winner="player"
             else:winner="opponent"
             return jsonify({'winner':True,'winner_boxes':board.winner_boxes(),'whoWon':winner,'symbol':[player_symbol,opponent_symbol],'computermove':bestmove_id,"updateopponent":True,"updateplayer":True})     
          return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':[player_symbol,opponent_symbol],'computermove':bestmove_id,"updateopponent":True,"updateplayer":True}) #Nobody won, the game is still going on
       else: return jsonify({'winner':"tie",'winner_boxes':"None",'whoWon':"None",'symbol':["None",opponent_symbol],'computermove':bestmove_id,"updateopponent":True,"updateplayer":False}) # It is a tie
    else:
         return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':["None","None"],'computermove':"None","updateopponent":False,"updateplayer":False}) #Nobody won but the moves are over
@app.route('/setting',methods= ['POST'])
def setting():
  global game,difficulty,opponent,board,start,i
  game= int(request.form['game'])
  difficulty= int (request.form['difficulty'])
  opponent= request.form['opponent']
  board=index.Board(difficulty,game)
  start=1
  i=0
  return jsonify([game,opponent,difficulty])
@app.route('/human',methods= ['POST'])
def human():
    global i
    id=int(request.form["1"])
    symbol=(request.form["2"])
    position=data[id]
    if(position in board.available_positions_function() and not (board.isWinner())):
         if(i%2==0):
             if(game!=3):
                 symbol='o'
             board.update_position(position,symbol,"player")
             
             i+=1
             if(board.isWinner()):
                 if(game==2):winner="opponent"
                 else:winner="player"
                 return jsonify({'winner':True,'winner_boxes':board.winner_boxes(),'whoWon':winner,'symbol':symbol,"updateplayer":True,"updateoppponent":False,"player2":False})
             elif(not len(board.available_positions_function())):return jsonify({'winner':"tie",'winner_boxes':"None",'whoWon':"None",'symbol':symbol,"updateplayer":True,"updateoppponent":False,"player2":False})
             else: return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':symbol,"updateplayer":True,"updateoppponent":False,"player2":False})     
             
       
         else:
             if(game!=3):
                 symbol='x'
             board.update_position(position,symbol,"opponent")
             i+=1
             if(board.isWinner()):
                 if(game!=2):winner="opponent"
                 else:winner="player"
                 return jsonify({'winner':True,'winner_boxes':board.winner_boxes(),'whoWon':winner,'symbol':symbol,"updateplayer":True,"updateoppponent":True,"player2":True})
             elif(not len(board.available_positions_function())):return jsonify({'winner':"tie",'winner_boxes':"None",'whoWon':"None",'symbol':symbol,"updateplayer":True,"updateoppponent":True,"player2":True})
             else: return jsonify({'winner':False,'winner_boxes':"None",'whoWon':"None",'symbol':symbol,"updateplayer":True,"updateoppponent":True,"player2":True})
            
    else:
        return jsonify([0,0])
@app.route('/help')
def help():  
    return render_template('rules.html') 
 

if __name__=="__main__":
   app.run(debug=True)
