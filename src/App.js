import React,{Component, useState, useEffect} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import {DailyChess} from './DailyChess.js';
import {TwoPlayerNormalChess} from './TwoPlayerNormalChess.js';
import {OnePlayerNormalChess} from './OnePlayerNormalChess.js';
import {TwoPlayerFischerRandomChess} from './TwoPlayerFischerRandomChess.js';
import {OnePlayerFischerRandomChess} from './OnePlayerFischerRandomChess.js';
import {TwoPlayerTranscendentalChess} from './TwoPlayerTranscendentalChess.js';
import {OnePlayerTranscendentalChess} from './OnePlayerTranscendentalChess.js';
import {TwoPlayerUpsideDownChess} from './TwoPlayerUpsideDownChess.js';
import {OnePlayerUpsideDownChess} from './OnePlayerUpsideDownChess.js';
import {TwoPlayerWeakChess} from './TwoPlayerWeakChess.js';
import {OnePlayerWeakChess} from './OnePlayerWeakChess.js';
import {TwoPlayerChargeOfTheLightBrigadeChess} from './TwoPlayerChargeOfTheLightBrigadeChess.js';
import {OnePlayerChargeOfTheLightBrigadeChess} from './OnePlayerChargeOfTheLightBrigadeChess.js';
import {TwoPlayerPeasantsRevoltChess} from './TwoPlayerPeasantsRevoltChess.js';
import {OnePlayerPeasantsRevoltChess} from './OnePlayerPeasantsRevoltChess.js';
import {TwoPlayerEndGameChess} from './TwoPlayerEndGameChess.js';
import {OnePlayerEndGameChess} from './OnePlayerEndGameChess.js';
import OptionsPage from './OptionsPage.js';


function A() {
  // usestate for setting a javascript
  // object for storing and using data
  const [data, setdata] = useState({
      Game: ""
  });

  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting a data from api
              setdata({
                  Game: data.Game
              });
          })
      );
  }, []);
  console.log(data.Game)
}

class App extends Component {
  render (){
    return (
      <BrowserRouter>
        <Routes>
          <Route path='/DailyChess' element={<DailyChess/>}/>
          <Route path='/TwoPlayerNormalChess' element={<TwoPlayerNormalChess/>}/>
          <Route path='/OnePlayerNormalChess' element={<OnePlayerNormalChess/>}/>
          <Route path='/TwoPlayerFischerRandomChess' element={<TwoPlayerFischerRandomChess/>}/>
          <Route path='/OnePlayerFischerRandomChess' element={<OnePlayerFischerRandomChess/>}/>
          <Route path='/TwoPlayerTranscendentalChess' element={<TwoPlayerTranscendentalChess/>}/>
          <Route path='/OnePlayerTranscendentalChess' element={<OnePlayerTranscendentalChess/>}/>
          <Route path='/TwoPlayerUpsideDownChess' element={<TwoPlayerUpsideDownChess/>}/>
          <Route path='/OnePlayerUpsideDownChess' element={<OnePlayerUpsideDownChess/>}/>
          <Route path='/TwoPlayerWeakChess' element={<TwoPlayerWeakChess/>}/>
          <Route path='/OnePlayerWeakChess' element={<OnePlayerWeakChess/>}/>
          <Route path='/TwoPlayerChargeOfTheLightBrigadeChess' element={<TwoPlayerChargeOfTheLightBrigadeChess/>}/>
          <Route path='/OnePlayerChargeOfTheLightBrigadeChess' element={<OnePlayerChargeOfTheLightBrigadeChess/>}/>
          <Route path='/TwoPlayerPeasantsRevoltChess' element={<TwoPlayerPeasantsRevoltChess/>}/>
          <Route path='/OnePlayerPeasantsRevoltChess' element={<OnePlayerPeasantsRevoltChess/>}/>
          <Route path='/TwoPlayerEndGameChess' element={<TwoPlayerEndGameChess/>}/>
          <Route path='/OnePlayerEndGameChess' element={<OnePlayerEndGameChess/>}/>
          <Route path='*' element={<OptionsPage/>}/>
        </Routes>
      </BrowserRouter>
    )
  }
}


export {App,A}
