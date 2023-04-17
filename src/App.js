import React,{Component} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import {DailyChess} from './DailyChess.js';
import {TwoPlayerNormalChess} from './TwoPlayerNormalChess.js';
import {OnePlayerNormalChess} from './OnePlayerNormalChess.js';
import {TwoPlayerHorde} from './TwoPlayerHorde.js';
import {OnePlayerHorde} from './OnePlayerHorde.js';
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

class App extends Component { //calls all the components and links all the buttons together
  render (){
    return (
      <BrowserRouter>
        <Routes>
          <Route path='/DailyChess' element={<DailyChess/>}/>
          <Route path='/TwoPlayerNormalChess' element={<TwoPlayerNormalChess/>}/>
          <Route path='/OnePlayerNormalChess' element={<OnePlayerNormalChess/>}/>
          <Route path='/TwoPlayerHorde' element={<TwoPlayerHorde/>}/>
          <Route path='/OnePlayerHorde' element={<OnePlayerHorde/>}/>
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


export default App;
