var textbox = document.getElementById("textbox");
var button = document.getElementById("button");

button.addEventListener("click", function(){
    localStorage.name = textbox.value;
});

document.write(localStorage.name);