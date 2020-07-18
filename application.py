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

app=Flask(__name__)
@app.route('/')
def json():
    global board
    board=index.Board(1)
    return render_template('firstattempt.html')

#background process happening without any refreshing
@app.route('/jstoflask',methods=["POST"])
def jstoflask():
    id=int(request.form["1"])
    position=data[id]
    if(position in board.available_positions_function()):
       board.update_position(position,'o')
       bestmove=bestmoves(board.board_function(),board.depth_function())
       id=reversed_data[tuple(bestmove)]
       board.update_position(bestmove,'x')
       winner=eval(board.board_function())
       return jsonify([id,winner])
    else:
        print("position not available")
        return jsonify(0)

if __name__=="__main__":
   app.run(debug=True)
