import { useState } from "react";
import offLogo from "../icons/off.svg";
import onLogo from "../icons/on.svg";
import "./App.css";

function App() {
  const [sound, setSound] = useState(true);

  return (
    <>
      <h1>Toggle Sound!</h1>
      <div className="card">
        <img
          alt="Sound"
          className="svg"
          src={sound ? onLogo : offLogo}
          width="200"
          onClick={() => setSound(!sound)}
        />
      </div>
      <p>Click to toggle from On to Off over and over!</p>
    </>
  );
}
export default App;
