function heartChange() {
    let heart = document.getElementById("heart")
    heart.classList.toggle("fa-solid")
}

let Allhearts=document.getElementsByClassName("heart")

for(let i in Allhearts) {
    Allhearts[i].addEventListener("click",function(){
    Allhearts[i].classList.toggle("fa-solid")
})}