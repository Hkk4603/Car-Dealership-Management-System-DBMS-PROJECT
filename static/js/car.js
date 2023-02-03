const navbar = document.getElementById("nav-list");

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
    brandLogo.style.zIndex = 0; 
})

const accSec = document.getElementById("acc-section");
const acc = document.getElementById("account");
var flag = 0;
acc.addEventListener('click', (e) => {
    console.log('clicked');
    if (flag === 0) {
        accSec.style.animation = "accSecSlideDown 1s forwards";
        accSec.style.pointerEvents = "all";
        flag = 1;
    } else {
        accSec.style.animation = "accSecSlideUp 1s forwards";
        accSec.style.pointerEvents = "none";
        flag = 0;
    }
})



// Carousel
var imgContainer = document.getElementById("img-container"); 
var imgclass = document.getElementsByClassName("img");
var count = imgclass.length;
var index = 0; 

function goright(){
    if(index < count-1){
        index = index + 1; 
        imgContainer.style.transform = `translateX(calc(-800px * ${index}))`; 
    }else{
        index = 0; 
        imgContainer.style.transform = `translateX(calc(-800px * ${index}))`; 
    }
}

function goleft(){
    index = index - 1; 
    if(index > -1){
        imgContainer.style.transform = `translateX(calc(-800px * ${index}))`; 
    }else{
        index = count-1; 
        imgContainer.style.transform = `translateX(calc(-800px * ${index}))`; 
    }
}