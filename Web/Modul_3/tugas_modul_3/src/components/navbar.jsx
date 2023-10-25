import React from 'react';
import { BrowserRouter as Router,Routes, Route, Link,Switch, BrowserRouter } from 'react-router-dom';
import Contact from "../pages/contact";
import About from "../pages/about";
import Beranda from "../pages/beranda";



function navbar() {
  return (
<BrowserRouter>
    
    <nav class="main-header navbar navbar-expand navbar-white navbar-light bg-light fixed-top">
    <ul class="nav-links mx-4">
        <li class="nav-item">
            <img src="Assets/logo-ilab.png " class="logo" />
        </li>
    </ul>
  <ul class="nav-links nav-center">
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="" class="btn btn-light text-dark fw-bold fs-6 ">
      <Link to="/">Beranda</Link>
      </a>
      </li>
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="#" class="btn btn-light text-dark fw-bold  fs-6"></a>
      <Link to="/about">Tentang</Link>
      </li>
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="#" class="btn btn-light text-dark fw-bold  fs-6"></a>
      <Link to="/contact">contact</Link>
      </li>
    </ul>
    <ul class="nav-links  nav-center">    
    <li><a  class="btn btn-light text-dark fw-bold  fs-6">Sign Up</a></li>
    <li><a class="btn  btn-primary text-light fw-bold mx-5 fs-6">Login</a></li>
  </ul>
</nav>
  <Routes>
  <Route  path="/home" element={<Beranda />} ></Route>
      <Route  path="/contact" element={<Contact />} ></Route>
      <Route  path="/about" element={<About />} ></Route>
  </Routes>
</BrowserRouter>

  )
}

export default navbar