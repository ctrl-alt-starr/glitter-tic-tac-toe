from flask import Flask, jsonify, request, render_template
import json
from minimax import bestmoves,eval
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
    position=data[id]
    isWinner=board.isWinner()
    if(isWinner):
        return jsonify([0,0])
    if(position in board.available_positions_function() and not (board.isWinner())):
       board.update_position(position,'o')
       bestmove=bestmoves(board.board_function(),board.depth_function(),game)
       bestmove_id=reversed_data[tuple(bestmove)]
       if(board.isWinner()):
           return jsonify([0,board.winner_boxes(),"opponent"])
       if(board.available_positions!=[]):
          board.update_position(bestmove,'x') 
          if((board.isWinner())):
             return jsonify([0,board.winner_boxes(),"player"])     
          return jsonify([bestmove_id,0])
       else: return jsonify(["None",0])
    else:
         return jsonify([0,0])
@app.route('/setting',methods= ['POST'])
def setting():
  global game,difficulty,opponent,board,start
  game= int(request.form['game'])
  difficulty= int (request.form['difficulty'])
  opponent= request.form['opponent']
  board=index.Board(difficulty,game)
  start=1
  return jsonify([game,opponent,difficulty])
@app.route('/human',methods= ['POST'])
def human():
    global i
    id=int(request.form["1"])
    position=data[id]
    if(position in board.available_positions_function() and not (board.isWinner())):
         if(i%2==0):
             board.update_position(position,'x')
             i+=1
             return jsonify("player1")
             
       
         else:
             board.update_position(position,'o')
             i+=1
             return jsonify("player2")
            
    else:
        return jsonify(0)
@app.route('/help')
def help():  
    return render_template('rules.html')


    
    

if __name__=="__main__":
   app.run(debug=True)
