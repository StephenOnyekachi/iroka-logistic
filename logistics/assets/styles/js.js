

// for displaying and hidding mune bar on media screen
let bars = document.querySelector('.bars')
let menus = document.querySelector('.menus')

bars.addEventListener("click", e =>{

    if(menus.style.display === "none"){
        menus.style.display = "block";
    }
    else{
        menus.style.display = "none";
    }
})


// for the typing
const texts = ['Delivers on time', 'Reliable','100% Security']
let count = 0;
let indext = 0; 
let currentText = ''; 
let letter = '';

(function type(){
    if(count === texts.length){
        count = 0;
    }
    currentText = texts[count];
    letter = currentText.slice(0, ++ indext);
    document.querySelector('.typing').textContent = letter;
    if(letter.length === currentText.length){
        count ++;
        indext = 0;
    }
    setTimeout(type, 400);
}());


// for background changing
var sliding = document.querySelector('.bgimg');
var images = new Array(
        'static/Images/009.jpg',
        'static/Images/010.jpg',
        'static/Images/008.webp',
        'static/Images/007.jpg'
    );
var len = images.length;
var i = 0;

function slider(){
    if(i > len - 1){
        i = 0;
    }
    sliding.src = images[i];
    i ++;
    setTimeout('slider()', 3000);
}














