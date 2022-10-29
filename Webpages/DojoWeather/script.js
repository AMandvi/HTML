

function convertTemp(element) {
    var tempType = element.value;
    var temperatures = document.querySelectorAll(".temp");
    for (var temperature of temperatures) {
        var tempInt = parseInt(temperature.innerText);
        if (tempType === "°F") {
            tempInt = Math.floor(tempInt * 9 / 5 + 32);
        } else {
            tempInt =  Math.floor((tempInt - 32) * 5 / 9)
        }
        temperature.innerText = tempInt + '°';
    }
}

function accept(){
    var divBox= document.querySelector("footer");
    divBox.remove();
}


// var todaymax = 24;
// var todaymin = 18;
// function convertTemp(element){
//     var tempType = element.value;
//     if (tempType === "°F") {
//         todaymax = Math.floor(todaymax * 9 / 5 + 32);
//         todaymin = Math.floor(todaymin * 9 / 5 + 32);
//     } else {
//         todaymax = Math.floor((todaymax - 32) * 5 / 9);
//         todaymin = Math.floor((todaymin - 32) * 5 / 9);
//     }
//     document.querySelector("#today_max_temp").innerText = todaymax + '°';
//     document.querySelector("#today_min_temp").innerText = todaymin + '°';
// }
