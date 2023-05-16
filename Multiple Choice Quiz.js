var questions = [
    {
        prompt: "What color is the sky?\n(a) blue,\n(b) green,\n(c) red",
        answer: "a"
    },
    {
        prompt: "What color is the grass?\n(a) blue,\n(b) green,\n(c) red",
        answer: "b"
    },
    {
        prompt: "What color is the stop sign?\n(a) blue,\n(b) green,\n(c) red",
        answer: "c"
    }
];

var score = 0;

for(var i=0; i < questions.length; i++){
    response = window.prompt(questions[i].prompt);
    if(response == questions[i].answer){
        score++;
        alert("Correct");
    } else {
        alert("Wrong");
    }
}

alert("You got " + score + "/" + questions.length + " correct.");