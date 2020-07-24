        window.start = "no"
        window.moon = "/static/moon.png"
        window.star = "/static/star.png"
        window.firstturn=true
        window.iterative=0
        window.gamehasbeenplayedbefore=false

        function human(id, symbol) {
            
            if(iterative==0&&game==3 && id==5){
                window.alert("In Last turn tic-tac-toe,the first move cannot be in the centre square!")
                return null;
            }          
            iterative=1
            if (start == "no") {
                window.alert("Choose the settings first and start a new game to start playing!");
                return null
            }
            if (opponent == "computer") {//the opponent is ai
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
//{'winner':True,'winner_boxes':board.winner_boxes(),'whoWon':"opponent",'symbol':['None',opponent_symbol],'computermove':"None","updateopponent":False,"updateplayer":False}
                        
                        success: function(data) {     
                            console.log(data) 
                            console.log("___________")
                            console.log(id)
                            console.log("___________")
                        for (i = 0; i < 9; i++) {
                            document.getElementsByTagName("td")[i].style.cursor = "pointer";
                        }    
                        
                        if(data["winner"]=="tie"){
                            console.log("inside here1")
                            if(data["updateplayer"]){
                                updateposition(data["computermove"],data["symbol"][0])
                                updateposition(id,data["symbol"][1])
                            }
                            else if(data["updateopponent"]){                                
                                console.log("winnerplayerupdate2")
                                updateposition(id,data["symbol"][1])
                            }
                            tie()
                            return null
                        }
                        else if(!data["winner"]&&data["updateopponent"]){
                            console.log("inside here2")
                            if(data["updateplayer"]){
                                console.log("1")
                                console.log(data["symbol"])
                                updateposition(data["computermove"],data["symbol"][0])
                                updateposition(id,data["symbol"][1])
                            }
                            else if(data["opponent"]){
                                console.log("1")
                                updateposition(id,data["symbol"][1])
                            }
                            if(game==3) {
                                disablebuttons(false,id)
                                disablebuttons(false,data["computermove"])
                            }
                            return null
                        }
                        else if(data["winner"]){
                            console.log("inside here3")
                            if(data["updateplayer"]){
                                console.log("1")
                                console.log(data["symbol"])
                                updateposition(data["computermove"],data["symbol"][0])
                                updateposition(id,data["symbol"][1])
                            }
                            else if(data["opponent"]){
                                console.log("1")
                                updateposition(id,data["symbol"][1])
                            }
                            winnerupdate(data["winner_boxes"],data["whoWon"])
                            disablebuttons(false,0)
                            return null;
                        }
                        else{
                            console.log("inside here4")
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
                            console.log(data)
                            
                            if(data["player2"]){    
                                console.log("opponent")                            
                                document.getElementById("winner").innerHTML="Its Player 1's chance!"
                            }
                            else{
                                console.log("player")                            
                                document.getElementById("winner").innerHTML="Its Player 2's chance!"
                            }
                            if(data["winner"]=="tie"){
                                console.log("inside here1")                                
                                updateposition(id,data["symbol"])
                                tie()
                                return null
                            }
                            
                            else if(!data["winner"]&&data["updateplayer"]){
                                console.log("inside here2")
                                updateposition(id,data["symbol"])
                                if(game==3) {
                                    disablebuttons(false,id)
                                }
                                return null
                            }
                            else if(data["winner"]){
                                console.log("inside here3")
                                updateposition(id,data["symbol"])
                                winnerupdate(data["winner_boxes"],data["whoWon"])
                                disablebuttons(false,0)
                                return null;
                            }
                            else{
                                console.log("inside here4")
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
                        window.opponent = data[1];
                        window.start = "yes"
                        window.game = data[0];
                        if(game==3){
                            gamehasbeenplayedbefore= true; //this is used to make the moon and star buttons disappear once last turn tic tac toe is over
                        }
                        iterative=0 // this is to make sure the first move in last turn tic tac toe is not in centre
                        if(opponent=="friend"&&game!=3){
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
                        gamesettings(game);
                        


                    });
                event.preventDefault();
            });
        });

        function refreshPage() {
            window.location.reload();
        }

        function difficulty_setting(data) {
            if (data.value == 'friend') {
                document.getElementById("difficulty").style.visibility = "hidden";
                document.getElementById("difficultyid").style.visibility = "hidden";
            } else {
                document.getElementById("difficulty").style.visibility = "visible";
                document.getElementById("difficultyid").style.visibility = "visible";
            }


        }

        function gamesettings(game) {
            if (game == 3) {
                window.clickarray=[]
                for (i = 1; i < 10; i++) {
                    var click1 = 'table' + i;
                    var click2 = 'symbolmoon' + i
                    var click3 = 'symbolstar' + i 
                    clickarray.push(document.getElementById(click1).onclick)   
                    console.log(clickarray[i])                
                    document.getElementById(click1).onclick = null;
                    document.getElementById(click2).disabled = false;
                    document.getElementById(click3).disabled = false;
                    document.getElementById(click2).style.visibility = "visible";
                    document.getElementById(click3).style.visibility = "visible";
                }
            } else {
                console.log("trying to disable buttons")

                disablebuttons(false,0)
            }
        }
        $(document).ready(function() {
            disablebuttons(true,0)
        });

        function disablebuttons(start,id) {
            var i
            for (i = 1; i < 10; i++) {
                if(id!=0){i=id
                console.log("first if")}
                var click1 = 'table' + i;
                var click2 = 'symbolmoon' + i
                var click3 = 'symbolstar' + i
                if(!start&&id==0&&gamehasbeenplayedbefore){
                    document.getElementById(click1).onclick= clickarray[i-1]}
                document.getElementById(click2).disabled = true;
                document.getElementById(click3).disabled = true;
                document.getElementById(click2).style.visibility = "hidden";
                document.getElementById(click3).style.visibility = "hidden";
                if(id!=0){break;}
            }
        }
 function tie(){                            
            
            if(game==3){disablebuttons(false,0)}
            document.getElementById("winner").innerHTML="Aww shucks it's a tie <br> ¯\_| ✖ 〜 ✖ |_/¯"
            sound = document.createElement("audio");                                    
            sound.src = "static/lost.mp3"
            sound.volume = 0.1;
            sound.play();
}
    function updateposition(position,symbol){
         click='moon'+position
         console.log(symbol)
         if(symbol=="x"){document.getElementById(click).src = star}
         else if (symbol=="o"){
             console.log("moon")
             document.getElementById(click).src = moon}
    }
    function winnerupdate(winner_boxes,player){
        var x;
        for (x of winner_boxes) {

            var click = 'table' + x
            var click1 = 'moon' + x            
            document.getElementById(click).style.background = "#FF1493";}
           
        sound = document.createElement("audio");
        win = "static/win.mp3"
        lose = "static/lost.mp3"
        console.log(player)
        if (player == "player") {
                if(opponent=="computer"){
                    sound.src = lose
                    document.getElementById("winner").innerHTML="This is you right now <br> (ಥ ͜ʖಥ) <br>, isn't? Sucks to lose lol"
               }
               else{
                sound.src = win
                if(game==3){document.getElementById("winner").innerHTML="Omg! Player 1 sure knows how to play last turn tic tac toe!"
            }
                 else{document.getElementById("winner").innerHTML="Player1 is a mighty fella! The moon wins after all"}  
                }
                
            } 
        else {
                sound.src = win
                if (opponent == "computer"){
                    document.getElementById("winner").innerHTML="This is me right now<br> ᕕ༼✪ل͜✪༽ᕗ So proud of your win kiddo"
                } 
              else{
                if(game!=3){ document.getElementById("winner").innerHTML="Player2 is marvellous! The glitter of the stars defeated the moon!"
            }else{
                document.getElementById("winner").innerHTML="Hey player 2? Did you spend your whole life playing this game or what? Because you are splendid!"
            }

            }
            }
        
        
        sound.volume = 0.1;
        sound.play();
        if(game==3){
        disablebuttons(false,0)
    }
}

