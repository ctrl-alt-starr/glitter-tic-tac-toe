from flask import Flask, jsonify, request, render_template
import json
from minimax import bestmoves,eval
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
def json():
    global start
    start=0
    return render_template('firstattempt.html')

@app.route('/ai',methods=["POST"])
def ai():
    global game,difficulty,opponent,board,start   
    if(start!=1):
        return jsonify("Choose the settings first and start a new game to start playing!")
    id=int(request.form["1"])
    symbol=(request.form["2"])
    position=data[id]
    isWinner=board.isWinner()
    if(isWinner):
        return jsonify([0,0])
    if(position in board.available_positions_function() and not (board.isWinner())):
       if(game==3):
           opponent_symbol=symbol
       else:
           opponent_symbol='o'
       board.update_position(position,opponent_symbol,"opponent")
       bestmove=game_redirection(board.board_function(),board.depth_function(),board.available_positions_function(),game)
       if(bestmove[0]==[-1,-1]):
           return jsonify([0,0,position])
       else: bestmove_id=reversed_data[tuple(bestmove[0])]
       if(board.isWinner()):
           return jsonify([0,board.winner_boxes(),"opponent",['None',opponent_symbol,"None"]])
       if(board.available_positions!=[]):
          if(game==3):
             player_symbol=bestmove[1]
          else:
             player_symbol='x'
          board.update_position(bestmove[0],player_symbol,"player") 
          if((board.isWinner())):
             print("went through this")
             return jsonify([0,board.winner_boxes(),"player",[player_symbol,opponent_symbol,bestmove_id]])     
          return jsonify([bestmove_id,0,0,[player_symbol,opponent_symbol]])
       else: return jsonify(["None",0])
    else:
         return jsonify([0,0])
@app.route('/setting',methods= ['POST'])
def setting():
  print("HII")
  global game,difficulty,opponent,board,start
  game= int(request.form['game'])
  difficulty= int (request.form['difficulty'])
  opponent= request.form['opponent']
  print([game,difficulty,opponent])
  board=index.Board(difficulty,game)
  start=1
  return jsonify([game,opponent,difficulty])
@app.route('/human',methods= ['POST'])
def human():
    global i
    id=int(request.form["1"])
    symbol=(request.form["2"])
    position=data[id]
    if(position in board.available_positions_function() and not (board.isWinner())):
         if(i%2==0):
             if(game!=3):board.update_position(position,'x',"player")
             else: board.update_position(position,symbol,"player")
             i+=1
             if(board.isWinner()):return jsonify([0,board.winner_boxes(),"player1"])
             else: return jsonify(["player1",0])     
             
       
         else:
             if(game!=3):board.update_position(position,'o',"opponent")
             else: board.update_position(position,symbol,"opponent")
             i+=1
             if(board.isWinner()):return jsonify([0,board.winner_boxes(),"player2"])
             else: return jsonify(["player2",0])
            
    else:
        return jsonify([0,0])
@app.route('/help')
def help():  
    return render_template('rules.html')


    
    

if __name__=="__main__":
   app.run(debug=True)
