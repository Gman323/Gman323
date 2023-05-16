var secretWord = "lucky";
var response;
var entryCount = 0;
var entryLimit = 3;
var error = false;

while(response != secretWord && !error){
    if(entryCount < entryLimit){
        response = window.prompt("Enter guess: ");
        entryCount++;
    } else {
        error = true;
    }
}

if(error){
    alert("Locked out");
} else {
    alert("Welcome");
}