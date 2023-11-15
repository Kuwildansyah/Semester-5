import React from 'react';
import { BrowserRouter as Router,Routes, Route, Link,Switch, BrowserRouter } from 'react-router-dom';
import Contact from "../pages/contact";
import About from "../pages/about";
import Beranda from "../pages/beranda";
import logo_ilab from "../pages/assets/logo_ilab.png";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';


function navbar() {
  return (
<BrowserRouter>
<div class="header">
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-12">
    <nav class="main-header navbar navbar-expand navbar-white navbar-light bg-light ">
    <ul class="nav-links mx-4">
        <li class="nav-item">
            <img src={logo_ilab} class="logo" />
        </li>
    </ul>
  <ul class="nav-links nav-center">
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="#" class="btn btn-light text-dark fw-bold fs-6 ">
      <Link to="/home">Beranda</Link>
      </a>
      </li>
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="#" class="btn btn-light text-dark fw-bold  fs-6">
      <Link to="/about">Tentang</Link>
      </a>
      </li>
    <li class="nav-item fw-bold text-dark mx-4">
      <a href="#" class="btn btn-light text-dark fw-bold  fs-6">
      <Link to="/contact">contact</Link>
      </a>
      </li>
    </ul>
    <ul class="nav-links  nav-center ">    
    <li><a  class="btn btn-light text-dark fw-bold  fs-6">Sign Up</a></li>
    <li><a class="btn  btn-primary text-light fw-bold mx-5 fs-6">Login</a></li>
  </ul>
</nav>
</div>
</div>
</div>
</div>
  
</BrowserRouter>

  )
}

export default navbar