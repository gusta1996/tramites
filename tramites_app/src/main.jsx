import React from 'react'
import ReactDOM from 'react-dom/client'
import 'semantic-ui-css/semantic.min.css'
import {Index} from "./Index";
import {Carrusel,Navbar} from "./componentes";


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <Navbar/>
      <Carrusel/>
      <Index />
  </React.StrictMode>
)
