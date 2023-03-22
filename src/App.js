import React,{Component, useState, useEffect} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import {DailyChess} from './DailyChess.js';
import {TwoPlayerNormalChess} from './TwoPlayerNormalChess.js';
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
          <Route path='*' element={<OptionsPage/>}/>
        </Routes>
      </BrowserRouter>
    )
  }
}


export {App,A}
