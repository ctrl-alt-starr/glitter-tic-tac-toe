window.START = "no"
window.MOON = "/static/moon.png"
window.STAR = "/static/star.png"
window.ITERATIVE=0
window.ALREADY_PLAYED=false

function human(id, symbol) {
            if (START == "no") {
                window.alert("Choose the settings first and start a new game to start playing!");
                return null
            }
            if(ITERATIVE==0&&GAME==3 && id==5){
                window.alert("In Last turn tic-tac-toe,the first move cannot be in the centre square!")
                return null;
            }          
            ITERATIVE=1
            
            if (OPPONENT == "computer") {//the opponent is ai
                $(function() {
                    $.ajax({
                        type: 'POST',
                        url: "/ai",
                        data: {
                            1: id,
                            2: symbol

                        },
                        beforeSend: function() {
                            for (i = 0; i < 9; i++) {
                                document.getElementsByTagName("td")[i].style.cursor = "wait";
                            }

                        },
                        
                        success: function(data) {
                        for (i = 0; i < 9; i++) {
                            document.getElementsByTagName("td")[i].style.cursor = "pointer";
                        }    
                        
                        if(data["winner"]=="tie"){
                            if(data["updateplayer"]){
                                updatePosition(data["computermove"],data["symbol"][0])
                                updatePosition(id,data["symbol"][1])
                            }
                            else if(data["updateopponent"]){
                                updatePosition(id,data["symbol"][1])
                            }
                            tie()
                            return null
                        }
                        else if(!data["winner"]&&data["updateopponent"]){
                            if(data["updateplayer"]){
                                updatePosition(data["computermove"],data["symbol"][0])
                                updatePosition(id,data["symbol"][1])
                            }
                            else if(data["opponent"]){
                                updatePosition(id,data["symbol"][1])
                            }
                            if(GAME==3) {
                                disableButtons(false,id)
                                disableButtons(false,data["computermove"])
                            }
                            return null
                        }
                        else if(data["winner"]){
                            if(data["updateplayer"]){
                                updatePosition(data["computermove"],data["symbol"][0])
                                updatePosition(id,data["symbol"][1])
                            }
                            else if(data["opponent"]){
                                updatePosition(id,data["symbol"][1])
                            }
                            winnerUpdate(data["winner_boxes"],data["whoWon"])
                            disableButtons(false,0)
                            return null;
                        }
                        else{
                            return null;
                        }

                        }


                    });
                });




            } else { //opponent is human
                $(function() {
                    $.ajax({
                        type: 'POST',
                        url: "/human",
                        data: {
                            1: id,
                            2: symbol
                        },

                        success: function(data) {
                            
                            if(data["player2"]){                          
                                document.getElementById("winner").innerHTML="Its Player 1's chance!"
                            }
                            else{                          
                                document.getElementById("winner").innerHTML="Its Player 2's chance!"
                            }
                            if(data["winner"]=="tie"){                                
                                updatePosition(id,data["symbol"])
                                tie()
                                return null
                            }
                            
                            else if(!data["winner"]&&data["updateplayer"]){
                                updatePosition(id,data["symbol"])
                                if(GAME==3) {
                                    disableButtons(false,id)
                                }
                                return null
                            }
                            else if(data["winner"]){
                                updatePosition(id,data["symbol"])
                                winnerUpdate(data["winner_boxes"],data["whoWon"])
                                disableButtons(false,0)
                                return null;
                            }
                            else{
                                return null;
                            }
    
                            
    
                          


                        }


                    });
                });




            }
        }


$(document).ready(function() {
    $('form').on('submit', function(event) {
                $.ajax({
                        data: {
                            game: $('#game').val(),
                            opponent: $('#opponent').val(),
                            difficulty: $('#difficulty').val()

                        },
                        type: 'POST',
                        url: '/setting'
                    })
                    .done(function(data) {

                        document.getElementById("winner").innerHTML="Tic Tac Toe with extra glitter <br><br>  ( ͡~ ͜ʖ ͡°)<br>"
                        window.OPPONENT = data[1];
                        window.START = "yes"
                        window.GAME = data[0];
                        if(GAME==3){
                            ALREADY_PLAYED= true; //this is used to make the moon and star buttons disappear once last turn tic tac toe is over
                        }
                        ITERATIVE=0 // this is to make sure the first move in last turn tic tac toe is not in centre
                        if(OPPONENT=="friend"&&GAME!=3){
                            document.getElementById("winner").innerHTML="First player gets moon and second player gets stars!"
                        }
                        var i;
                        for (i = 1; i < 10; i++) {
                            click1 = 'moon' + i;
                            click2 = 'table' + i;
                            document.getElementById(click1).src = ""
                            document.getElementById(click2).style.background = "";
                        }
                        if (data[0] == '2') {
                            document.getElementById("title").innerHTML = "Tac-Toe-Tic!";
                            document.getElementById("title").style.marginLeft = "350px";
                        } else if (data[0] == '1') {
                            document.getElementById("title").innerHTML = "Tic-Tac-Toe!";
                            document.getElementById("title").style.marginLeft = "350px";
                        } else {
                            document.getElementById("title").innerHTML = "Last turn Tic-Tac-Toe!";
                            document.getElementById("title").style.marginLeft = "20px";
                        }
                        gameSettings(GAME);
                        


                    });
                event.preventDefault();
            });
        });

$(document).ready(function() {
            disableButtons(true,0)
});
function refreshPage() {
            window.location.reload();
}

function setDifficulty(data) {
     if (data.value == 'friend') {
                document.getElementById("difficulty").style.visibility = "hidden";
                document.getElementById("difficultyid").style.visibility = "hidden";
    } else {
                document.getElementById("difficulty").style.visibility = "visible";
                document.getElementById("difficultyid").style.visibility = "visible";
         }


    }

function gameSettings(GAME) {
     if (GAME == 3) {
                window.clickarray=[]
                for (i = 1; i < 10; i++) {
                    var click1 = 'table' + i;
                    var click2 = 'symbolmoon' + i
                    var click3 = 'symbolstar' + i 
                    clickarray.push(document.getElementById(click1).onclick)                
                    document.getElementById(click1).onclick = null;
                    document.getElementById(click2).disabled = false;
                    document.getElementById(click3).disabled = false;
                    document.getElementById(click2).style.visibility = "visible";
                    document.getElementById(click3).style.visibility = "visible";
                }
            } else {
                disableButtons(false,0)
            }
        }


function disableButtons(start,id) {
            var i
            for (i = 1; i < 10; i++) {
                if(id!=0){i=id}
                var click1 = 'table' + i;
                var click2 = 'symbolmoon' + i
                var click3 = 'symbolstar' + i
                if(!start&&id==0&&ALREADY_PLAYED){
                    document.getElementById(click1).onclick= clickarray[i-1]}
                document.getElementById(click2).disabled = true;
                document.getElementById(click3).disabled = true;
                document.getElementById(click2).style.visibility = "hidden";
                document.getElementById(click3).style.visibility = "hidden";
                if(id!=0){break;}
            }
        }
function tie(){                            
            
            if(GAME==3){disableButtons(false,0)}
            document.getElementById("winner").innerHTML="Aww shucks it's a tie <br> ¯\_| ✖ 〜 ✖ |_/¯"
            sound = document.createElement("audio");                                    
            sound.src = "static/lost.mp3"
            sound.volume = 0.1;
            sound.play();
}
function updatePosition(position,symbol){
         click='moon'+position
         if(symbol=="x"){document.getElementById(click).src = STAR}
         else if (symbol=="o"){
             document.getElementById(click).src = MOON}
}
function winnerUpdate(winner_boxes,player){
        var x;
        for (x of winner_boxes) {

            var click = 'table' + x
            var click1 = 'moon' + x            
            document.getElementById(click).style.background = "#FF1493";}
           
        sound = document.createElement("audio");
        WIN = "static/win.mp3"
        LOSE = "static/lost.mp3"
        if (player == "player") {
                if(OPPONENT=="computer"){
                    sound.src = LOSE
                    document.getElementById("winner").innerHTML="This is you right now <br> (ಥ ͜ʖಥ) <br>, isn't? Sucks to lose lol"
               }
               else{
                sound.src = WIN
                if(GAME==3){document.getElementById("winner").innerHTML="Omg! Player 1 sure knows how to play last turn tic tac toe!"
            }
                 else{document.getElementById("winner").innerHTML="Player1 is a mighty fella! The moon wins after all"}  
                }
                
            } 
        else {
                sound.src = WIN
                if (OPPONENT == "computer"){
                    document.getElementById("winner").innerHTML="This is me right now<br> ᕕ༼✪ل͜✪༽ᕗ So proud of your win kiddo"
                } 
              else{
                if(GAME!=3){ document.getElementById("winner").innerHTML="Player2 is marvellous! The glitter of the stars defeated the moon!"
            }else{
                document.getElementById("winner").innerHTML="Hey player 2? Did you spend your whole life playing this game or what? Because you are splendid!"
            }

            }
            }
        
        
        sound.volume = 0.1;
        sound.play();
        if(GAME==3){
        disableButtons(false,0)
    }
}

