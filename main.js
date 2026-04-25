let vnframe = document.getElementById("vnframe");
let mgframe= document.getElementById("minigameframe")
let gamesLi = ["game1.html","game2.html","game3.html"]
let currentpart = 0;

function loadMiniGame(type){
    if (type=="pizza"){
        mgframe.src = gamesLi[0]
    }
    else if (type=="boba"){
        mgframe.src = gamesLi[1]
    }
}

function swapDisplay(type){
    if (type=="vn"){
    vnframe.style.display= "block";
    mgframe.style.display= "none";
    }
    else {
        mgframe.style.display= "block";
        vnframe.style.display= "none";
    }
}