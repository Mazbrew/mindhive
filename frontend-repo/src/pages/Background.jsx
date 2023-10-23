import squirrel from "../assets/squirrel.gif"
import forg from "../assets/forg.gif"

import "../styles/Background.css"

export default function Background(){

    return(
        <div id="BackgroundContainer">
            <img id="Squirrel"src={squirrel} alt="" />
            <img id="Forg" src={forg} alt="" />
        </div>
    )
}