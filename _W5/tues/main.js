const getStatus = async (event) => {
    try {
        event.preventDefault();
        // // console.log(event);
        // // console.log("line 14: ");
        // // console.log(event.target);
        // let form = new FormData(event.target);
        // console.log("Form: ");
        // console.log(form);
        //let formData = Object.fromEntries(form);
        // console.log(typeof formData, console.log(formData));
        let response = await fetch(
            `https://cors-anywhere.herokuapp.com/https://http.dog/${event.target.dog.value}.jpg`
        );
        //console.log(response);
        let responseData = response.url;
        //console.log(responseData);
        let img = document.getElementById("dogImg");
        let name = document.getElementById("dogName");
        //name.innerText = responseData.name.toUpperCase();
        img.src = responseData;
        img.style.border = "5px yellow solid";
        img.style.borderRadius = "20px";
        img.style.height = "200px";
    } catch (err) {
        console.log(err.message);
    }
};
