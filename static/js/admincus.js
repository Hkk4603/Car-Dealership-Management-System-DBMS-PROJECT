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


var add = document.getElementById("addBtn");
var addCon = document.getElementById("addFormContainer"); 
add.addEventListener('click', (e)=>{
    addCon.style.display = "flex";
})

var del = document.getElementById("delBtn");
var delCon = document.getElementById("delFormContainer"); 
del.addEventListener('click', (e)=>{
    delCon.style.display = "flex";
})

var update = document.getElementById("updateBtn");
var updateCon = document.getElementById("updateFormContainer"); 
update.addEventListener('click', (e)=>{
    updateCon.style.display = "flex";
})


var clsBtns = document.getElementsByClassName("cls-wht"); 
var operatorCon = document.getElementsByClassName("operator-forms-container");
for(let i = 0; i < clsBtns.length; i++ ){
    clsBtns[i].addEventListener('click', (e)=>{
        operatorCon[i].style.display = "none"; 
    })
}