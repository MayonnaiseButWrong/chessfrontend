import React,{Component, useState, useEffect} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import {ChessFrontEnd} from './Chess.js';
import OptionsPage from './OptionsPage.js';



class App extends Component {
  render (){
    return (
      <BrowserRouter>
        <Routes>
          <Route path='/ChessGame' element={<ChessFrontEnd/>}/>
          <Route path='*' element={<OptionsPage/>}/>
        </Routes>
      </BrowserRouter>
    )
  }
}


export default App;
