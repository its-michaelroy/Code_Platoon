console.log("HELLO WHISKEY PLATOON!");
// Your function(s) should go here that will interact with the webpage or DOM
let guess = document.getElementById("guess");
let submit = document.getElementById("submit");
let message = document.getElementById("message");
let randomNumber = Math.floor(Math.random() * 100) + 1;
let guesses = document.getElementById("guesses");
let tries = 0;
let resetButton = document.getElementById("reset");

submit.addEventListener("click", function () {
    if (guess.value > randomNumber) {
        message.innerHTML = "Your guess is too high!";
    } else if (guess.value < randomNumber) {
        message.innerHTML = "Your guess is too low!";
    } else {
        message.innerHTML =
            "Congratulations! You guessed the correct number in " +
            tries +
            " tries!";
    }
    tries += 1;
    guesses.innerHTML += `On guess ${tries}, User input ${guess.value}<br>`;
});

resetButton.addEventListener("click", function () {
    location.reload();
});
