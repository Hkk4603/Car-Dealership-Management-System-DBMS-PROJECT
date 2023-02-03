var popularContainer = document.getElementById("popular-container");
var popular = document.getElementById("popular");
var cards = document.querySelectorAll(".card");
var cardsClasses = [];  
var count = 0;

console.log(cards); 

function addCardAnimation(){
    if(count == 0){
        count = count + 1; 
    }else{
        return;
    }
    cards.forEach(e => {
        cardsClasses.push(e.id);
    })

    console.log(cardsClasses); 
    // cardsClasses = ["card1", "card2", "card3"]; 
    cardsClasses.forEach(e => {
        var card = document.getElementById(e); 
        card.style.animation = "popUpCards 0.5s forwards";
        // card.style.animationDelay = "1s"
        card.style.pointerEvents = "all"; 
    })
}

var scrollpos = window.scrollY; 
var wh = window.innerHeight+300;
window.addEventListener('scroll', () => {
    if (this.window.scrollY > wh) {
        addCardAnimation();
    }
});

var powContainer = document.getElementById("pow-container"); 
var powImg = document.getElementById("pow-img"); 
var hero = document.getElementById("hero"); 
var navbar = document.getElementById("navbar"); 
powImg.addEventListener('click',(e) => {
    powImg.style.animation = "powerUp 1s infinite";
    // powContainer.style.animation = "bgClear 1s forwards"; 
    setTimeout(()=>{
        powContainer.style.display = "none"; 
        hero.style.pointerEvents = "all"; 
        navbar.style.pointerEvents = "all"; 
    }, 1000);
    var audio = new Audio("./poweron-track-cut.mp3");
    audio.play(); 
});


const ham = document.getElementById("ham-btn");
const cls = document.getElementById("close-btn");
const navList = document.getElementById("nav-list"); 
const brandLogo = document.getElementById("brand-logo");

ham.addEventListener('click', (e) => {
    navList.style.animation = "slideDown 1.5s forwards"; 
    ham.style.opacity = 0; 
    ham.style.pointerEvents = "none"; 
    cls.style.pointerEvents = "all"; 
    cls.style.opacity = 1;  
    brandLogo.style.zIndex = -1; 
})

cls.addEventListener('click', (e) => {
    navList.style.animation = "slideUp 1.5s forwards"; 
    ham.style.opacity = 1; 
    cls.style.opacity = 0; 
    cls.style.pointerEvents = "none"; 
    ham.style.pointerEvents = "all"; 
    brandLogo.style.zIndex = 3; 
})

const accSec = document.getElementById("acc-section"); 
const acc = document.getElementById("account"); 
var flag = 0; 
acc.addEventListener('click', (e) =>{
    console.log('clicked'); 
    if(flag === 0){
        accSec.style.animation = "accSecSlideDown 1s forwards"; 
        accSec.style.pointerEvents = "all"; 
        flag = 1; 
    }else{
        accSec.style.animation = "accSecSlideUp 1s forwards"; 
        accSec.style.pointerEvents = "none"; 
        flag = 0;
    }
})