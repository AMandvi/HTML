var count= 3;
var countElement= document.querySelector("#count");

function increaseLikes(){
    count++;
    countElement.innerText= count + "like(s)";
    console.log(count);
}
