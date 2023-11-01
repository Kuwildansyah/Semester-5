import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import hero from "../pages/assets/hero.jpg";
import '../App.css';

function beranda() {
  return (
    <div className="container-fluid">
      <div className="row">
      <div className="col-lg-12">
      <div class="row black">
        <img src={hero}  class="logo_foot" />
        <div class="content text-center justify-content-center " >
            <h1 class="text-light fw-bold">Selamat Datang</h1>
            <h3 class="text-light fw-light">Di website Praktikum<br/> Pemrograman Web</h3>
            <a class="btn btn-light text-dark text-center justify-content-center fw-bold my-4 learn">Learn More</a>
          </div>
        </div>
      </div>
      </div>
      </div> 
  )
}

export default beranda