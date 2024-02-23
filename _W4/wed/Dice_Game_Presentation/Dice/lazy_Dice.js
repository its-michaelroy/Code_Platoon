let todoItems = [];

function roll() {
    let random_number = Math.ceil(todoItems.length * Math.random());
    document.getElementById("dice").src = "images/die" + random_number + ".gif";
    setTimeout(function () {
        msg_alert(random_number);
    }, 250);
}

function msg_alert(random_number) {
    alert(
        `Looks like you'll have to do number ${random_number} on the todo list!`
    );
    alert("YA BUM!");
}
//Grabs value, adds item to the list, and clears input field
function add_List_Item() {
    let new_Item = document.getElementById("item").value;
    if (new_Item != "" && new_Item != " ") {
        document.getElementById(
            "todo"
        ).innerHTML += `<li onclick="StrikeThrough(event)">${new_Item}</li>`;
        document.getElementById("item").value = "";
        todoItems.push("item");
    }
}

function StrikeThrough(event) {
    let list_Item = event.target;

    if (list_Item.style.textDecoration === "line-through") {
        list_Item.style.textDecoration = "none";
    } else {
        list_Item.style.textDecoration = "line-through";
    }
}
