let vnframe = document.getElementById("vnframe");
let mgframe= document.getElementById("minigameframe")
let gamesLi = ["pizza.html","boba.html","bean.html", "hack.html"]
let currentpart = 0;

vnframe.onload = () => swapDisplay("vn");


function loadMinigame(type){
    if (type=="pizza"){
        mgframe.src = gamesLi[0];
    }
    else if (type=="boba"){
        mgframe.src = gamesLi[1];
    }
    else if (type=="bean"){
        mgframe.src = gamesLi[2];
    }
    else if (type=="hack"){
        mgframe.src = gamesLi[3];
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
