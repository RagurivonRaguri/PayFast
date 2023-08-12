import React, {useState, useEffect} from 'react';
import {Switch, Route} from 'react-router-dom'
import Login from './components/Login'
import Header from './components/Header'
import Profile from './components/Profile'
import Sales from './components/Sales'
import LandingPage from './components/LandingPage';
import Dashboard from './components/Dashboard/Dashboard';
import AddProduct from './components/Dashboard/AddProduct';
import RemoveProduct from './components/Dashboard/RemoveProduct';
import ViewSuppliers from './components/Dashboard/ViewSuppliers';
import PatchProduct from './components/Dashboard/PatchProduct';
import AddManager from './components/Dashboard/AddManager';
import AddCashier from './components/Dashboard/AddCashier';
import SalesHistory from './components/Dashboard/SalesHistory';
import Signup from './components/Signup';


function App() {
  const [products, setProducts] = useState([])
  useEffect(()=>{
    fetch('/products').then(r => r.json()).then(data => setProducts(data))
  },[]) 
  
  return (
    <div className="App">

      <Header/>

      <Switch>
      <Route path='/profile'>
      <Profile/>
      </Route>
      <Route path='/sales'>
      <Sales products={products} />
      </Route>
      <Route path='/dashboard'>
      <Dashboard/>
      </Route>
      <Route path='/add-product'>
      <AddProduct/>
      </Route>
      <Route path='/add-manager'>
      <AddManager />
      </Route>
      <Route path='/add-cashier'>
      <AddCashier />
      </Route>
      <Route path='/sales-history'>
      <SalesHistory />
      </Route>
      <Route path='/remove-product'>
      <RemoveProduct products={products}/>
      </Route>
      <Route path='/patch-product'>
      <PatchProduct products={products}/>
      </Route>
      <Route path='/view-suppliers'>
      <ViewSuppliers />
      </Route>
      <Route path='/login'>
      <Login/>
      </Route>
      <Route path='/signup'>
      <Signup/>
      </Route>
      <Route>
      <LandingPage exact path='/'/>
      </Route>
      </Switch>

    </div>
  );
}

export default App;
