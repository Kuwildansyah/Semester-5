import React from 'react'
import Navbar from "./navbar";
import '../App.css';


function footer() {
  return (
    <footer>
    <div class="container-fluid">
      <div class="row">
        <div class="row h-100 footer-wrapper p-3 justify-content-center">
          <div class="col-md-3  d-flex justify-content-center">
            <img src={require("../pages/assets/logo_ilab.png")} alt="logo"  class="logo_foot2"/>
          </div>
          <div class="col-md-3  justify-content-center">
            <p class="my-1"><span class="fw-bold text-dark title fs-3" id="title">Services</span></p>
            <p class="my-1"><a href="#" class="fw-medium sub " id="sub">Email Marketing</a></p>
            <p  class="my-1"><a href="#" class="fw-medium sub " id="sub">Campaigns</a></p>
            <p class="my-1"><a href="#" class="fw-medium sub" id="sub">Branding</a></p>
            <p class="my-1"><a href="#" class="fw-medium sub" id="sub">Offline</a></p>
          </div>
          <div class="col-md-3  justify-content-center">
            <p class="my-1"><span class="fw-bold text-dark fs-3" id="title">About</span></p>
            <p class="my-1"><a href="#" class="fw-medium sub " id="sub">Our Story</a></p>
            <p class="my-1"><a href="#" class="fw-medium sub" id="sub">Benefits</a></p>
            <p class="my-1"><a href="#" class="fw-medium sub" id="sub">Team</a></p>
            <p class="my-1"><a href="#" class="fw-medium sub" id="sub">Careers</a></p>
          </div>
          <div class="col-md-3 ">
            <p><span class="fw-bold text-dark title fs-3" >Follow Us</span></p>
            <a href="#" class="sub d-block my-2">
              <img
                src={require("../pages/assets/logo-facebook.png")}
                alt="logo fb"
                width="15"
                height="20"
                class="mx-2"
                />
              Facebook
            </a>
            <a href="#" class="sub d-block my-2">
              <img
                src={require("../pages/assets/logo-twitter.png")}
                alt="logo twitter"
                width="20"
                height="20"
                class="mx-2"
              />Twitter
            </a>
            <a href="#" class="sub d-block my-2">
              <img
                src={require("../pages/assets/logo-instagram.png")}
                alt=" logo ig"
                width="19"
                height="19"
                class="mx-2"
              />Instagram
            </a>
          </div>
        </div>
        <div class="col-md-3 col-xs-12 d-flex justify-content-center">
          <p><span class="fw-light">Copyright 2022 Infinite Learning</span></p>
        </div>
      </div>
    </div>
  </footer>
  )
}

export default footer