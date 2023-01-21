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
            <div>1</div>
            <div>2</div>
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
            <div>4</div>
            <div>5</div>
            <div>6</div>
        </div>
    </div>
    )
};

export default ChessFrontEnd;