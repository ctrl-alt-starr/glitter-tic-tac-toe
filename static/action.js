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
                            document.documentElement.style.cursor = 'wait';
                            for (i = 0; i < 9; i++) {
                                document.getElementsByTagName("td")[i].style.cursor = "wait";
                            }

                        },

                        success: function(data) {                           
                            document.documentElement.style.cursor = 'pointer';
                            for (i = 0; i < 9; i++) {
                                document.getElementsByTagName("td")[i].style.cursor = "pointer";
                            }
                            if(data[0]=='None'&&data[1]==0&&data[2]==0){tie(0,0,0)} //tie
                            if (data[0] != 0) { //There is no winner, no tie and there are moves left
                                if (game != 3) {
                                    click1 = 'moon' + id
                                    document.getElementById(click1).src = moon
                                    if (data[0] != "None") {
                                        click2 = 'moon' + data[0]
                                        document.getElementById(click2).src = star
                                    }
                                } else {

                                    click1 = 'moon' + id
                                    if (data[3][1] == "x") {
                                        document.getElementById(click1).src = star
                                    } else {
                                        document.getElementById(click1).src = moon
                                    }
                                                                   
                                    disablebuttons(false,id)
                                    if (data[0] != "None") {
                                        click4 = 'moon' + data[0]
                                        if (data[3][0] == "x") {
                                            document.getElementById(click4).src = star
                                        } else {
                                            document.getElementById(click4).src = moon
                                        }
                                        disablebuttons(false,data[0])
                                    }
                                    

                                }



                            } else {//There is a winner or its a null move

                                if (data[1] != 0) {//There is a winner                                 

                                    var x;
                                    for (x of data[1]) {

                                        var click = 'table' + x
                                        var click1 = 'moon' + x
                                        
                                        document.getElementById(click).style.background = "#FF1493";
                                        if (game==1) {
                                            if (data[2] == 'player') {
                                                document.getElementById(click1).src = star;
                                            } else {
                                                document.getElementById(click1).src = moon;
                                            }
                                        }


                                    }
                                    if(game==2){
                                        var click1='moon'+id
                                        document.getElementById(click1).src = moon;
                                        if(data[3][2]!="None"){                                            
                                            var click1='moon'+data[3][2]
                                            document.getElementById(click1).src = star;                                            
                                        }
                                    }
                                    if (game == 3) {
                                        click1 = 'moon' + id                                    
                                        if (data[3][1] == "x") {
                                            document.getElementById(click1).src = star;
                                        } else if (data[3][1] == "o") {
                                            document.getElementById(click1).src = moon
                                        }
                                        click2 = 'moon' + data[3][2]
                                        if (data[3][0] == "x") {
                                            document.getElementById(click2).src = star
                                        } else if (data[3][0] == "o") {                                
                                            document.getElementById(click2).src = moon
                                        }
                                        disablebuttons(false,0)

                                    }
                                    sound = document.createElement("audio");
                                    win = "static/win.mp3"
                                    lose = "static/lost.mp3"
                                    if (game == 1 || game == 3) {
                                        if (data[2] == "player") {
                                            document.getElementById("winner").innerHTML="This is you right now <br> (ಥ ͜ʖಥ) <br>, isn't? Sucks to lose lol"
                                            sound.src = lose
                                        } else {
                                            sound.src = win
                                            document.getElementById("winner").innerHTML="This is me right now<br> ᕕ༼✪ل͜✪༽ᕗ So proud of your win kiddo"
                                        }
                                    } else {
                                        if (data[2] == "player") {
                                            sound.src = win
                                            document.getElementById("winner").innerHTML="Ah the taste of victory <br>(◕‿◕✿)"
                                        } else {
                                            sound.src = lose
                                            document.getElementById("winner").innerHTML="Me: You Lose <br> You: ( ⚈̥̥̥̥̥́⌢⚈̥̥̥̥̥̀) "
                                        }
                                    }
                                    sound.volume = 0.1;
                                    sound.play();

                                }
                                if(data[0]==0 && data[1]==0){//moves are over but have to update the previous moves
                                    if(data[2]!=0){
                                        click='moon'+id
                                        if(game!=3){
                                            document.getElementById(click).src = moon
                                        }
                                        else{
                                            disablebuttons(false,id);
                                            if(symbol=='x'){document.getElementById(click).src = star
                                            }
                                            else{document.getElementById(click).src = moon}
                                        }
                                                                               
                                    }
                                }

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
                            if(data[0]=="tie"){                               
                                tie(id,data[1],symbol);
                                return 0;
                            }
                            console.log(data)
                            if (data[0] != 0) {// there is no winner yet and the move is not a null move
                                click = 'moon' + id
                                if (game != 3) {
                                    if (data[0] == "player1") {
                                        document.getElementById(click).src = moon;
                                        document.getElementById("winner").innerHTML="Its Player 2's chance!"
                                    } else if (data[0] == "player2") {
                                        document.getElementById(click).src = star;
                                        document.getElementById("winner").innerHTML="Its Player 1's chance!"
                                    }
                                } else {
                                    if (symbol == 'x') {
                                        document.getElementById(click).src = star;
                                    } else {
                                        document.getElementById(click).src = moon;
                                    }
                                    disablebuttons(false,id)

                                }
                            }
                            if (data[1] != 0) {//winner
                                if(game==3&&data[3]=="x" || data[2]=="player2"){image=star}
                                else if((game==3&&data[3]=="o") || data[2]=="player1"){image=moon}
                                click = 'moon' + id
                                document.getElementById(click).src = image;
                                if(game!=2&&data[2]=="player1" || game==2&&data[2]=="player2"){document.getElementById("winner").innerHTML="Player1 is a mighty fella! The moon wins after all"}
                                else if(game==2&&data[2]=="player1" || game!=2&&data[2]=="player2"){ document.getElementById("winner").innerHTML="Player2 is marvellous! The glitter of the stars defeated the moon!"}
                                disablebuttons(false,0)                        
                                var x;
                                for (x of data[1]) {
                                    click = 'table' + x           
                                    document.getElementById(click).style.background = "#FF1493";                         
                                                                   
                                                                       
                        
                                }
                                
                                sound = document.createElement("audio");
                                sound.src = "static/win.mp3"
                                sound.volume = 0.1;
                                sound.play();

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
        function tie(id,player,symbol){ 
            if(id!=0){
                click = 'moon' + id
                if (game != 3) {
                   if (player == "player1") {
                        document.getElementById(click).src = moon;}
                    else{document.getElementById(click).src = star;    }
                                           
                     
                 } else {
                       if (symbol == 'x') {
                           document.getElementById(click).src = star;
                        } else {
                         document.getElementById(click).src = moon;
                         }
                        disablebuttons(false,id)

                        }    
            }                            
            
            
            document.getElementById("winner").innerHTML="Aww shucks it's a tie <br> ¯\_| ✖ 〜 ✖ |_/¯"
            sound = document.createElement("audio");                                    
            sound.src = "static/lost.mp3"
            sound.volume = 0.1;
            sound.play();}
    
