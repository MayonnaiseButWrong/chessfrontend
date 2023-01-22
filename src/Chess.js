import './Chess.css'
import {Link} from 'react-router-dom'
import {choice} from './OptionsPage.js';

//<Link to='/'><button onClick='ChessFrontEnd(2,1)'> Quit / New game</button></Link>

const startingLayout = [
    [],
    [],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    [],
    []
    ];

const ChessFrontEnd = () => {
    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div class="grid-container1">
            <div class= 'boarderleft'></div>
            <div class='chessboard'>
                <div class="grid-container2">
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                    <div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div><div>11</div>
                </div>
            </div>

            <div class='last-moves'>
                <h2 class='last-moves-header'>Last Moves</h2>
                <p class='last-moves-text'>efwasdf</p>
            </div>

            <div class='black-pieces-taken'>
                <h2 class='black-pieces-taken-header'>Black Pieces Taken</h2>
                <p class='black-pieces-taken-text'>dfbgdfvyjh</p>
            </div>

            <div class='white-pieces-taken'>
                <h2 class='white-pieces-taken-header'>White Pieces</h2>
                <p class='white-pieces-taken-text'>sghnyjukyjt</p>
            </div>

            <div class='selet-move-button'>
                <button>select move</button>
            </div>

            <div class= 'boarderright'></div>
            
            <div class= 'disclaimer'>
                <p class='disclaimer-text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
            </div>
        </div>
    </div>
    );
};

export default ChessFrontEnd;