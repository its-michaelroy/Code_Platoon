function roll() {
    //history[row] = []; // create the list before we add to it

    console.log(length);
    //for (i = 0; i < 5; i++) {
    random_num = Math.ceil(length * Math.random());
    //console.log(p, r, i);
    //history[row][i] = r;
    document.images[i].src = "die" + random_num + ".gif"; //changed the value for all images on roll function activation
    // t.value = t.value + r + "\t"; // ----  display the value of the dice in the text area
    //}
    // t.value = t.value + "\n";
    // row++;
}
//Grabs value, adds item to the list, and clears input field
function add_List_item() {
    let new_item = document.getElementById("item").value;
    if (new_item != "" && new_item != " ") {
        document.getElementById("todo").innerHTML +=
            `<li onclick="StrikeThrough(event)">${new_item}</li>`;
        document.getElementById("item").value = "";
    }
}

function StrikeThrough(event) {
    let list_item = event.target;

    if (list_item.style.textDecoration === "line-through") {
        list_item.style.textDecoration = "none";
    } else {
        list_item.style.textDecoration = "line-through";
    }
}
roll();
