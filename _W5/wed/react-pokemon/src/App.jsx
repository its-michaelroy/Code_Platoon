import axios from "axios";
// import { useState } from "react";
import "./App.css";

function App() {
    let pokemonImg =
        "" ||
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png";

    const getPokemonImg = async () => {
        const randomNumber = Math.floor(Math.random() * 250);
        const response = await axios.get(
            `https://pokeapi.co/api/v2/pokemon/${randomNumber}`
        );
        //Filter if same type as random pokemon add to array
        let pokemonArray = [];

        //Find the type of pokemon
        const responseType = response.data.types[0].type.name;
        // console.log(responseType);
        while (pokemonArray.length < 5) {
            let randomNumber2 = Math.floor(Math.random() * 150) + 1;

            const response2 = await axios.get(
                `https://pokeapi.co/api/v2/pokemon/${randomNumber2}`
            );

            if (responseType === response2.data.types[0].type.name) {
                let responseImg2 = response2.data.sprites.front_default;
                pokemonArray.push(responseImg2);
            }
        }
        // console.log(pokemonArray);

        for (let i = 0; i < pokemonArray.length; i++) {
            document.getElementById(`newPokemon${[i + 1]}`).src =
                pokemonArray[i];
        }

        let responseImg = response.data.sprites.front_default;
        pokemonImg = responseImg;
        document.getElementById("newPokemon6").src = pokemonImg;
    };

    return (
        <>
            <h1>Pokemon React</h1>
            <div className="card">
                <img id="newPokemon1" src={pokemonImg} />
                <img id="newPokemon2" src={pokemonImg} />
                <img id="newPokemon3" src={pokemonImg} />
                <img id="newPokemon4" src={pokemonImg} />
                <img id="newPokemon5" src={pokemonImg} />
                <img id="newPokemon6" src={pokemonImg} />
                <button onClick={() => getPokemonImg()}>Random Pokemon</button>
                <p>Click the button above ^ to select a random Pokemon!</p>
            </div>
        </>
    );
}

export default App;
