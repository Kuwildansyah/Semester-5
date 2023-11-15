import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router,Routes, Route, Link,Switch, BrowserRouter } from 'react-router-dom';
import Navbar from "./components/navbar";
import Footer from "./components/footer";
import Contact from "./pages/contact";
import About from "./pages/about";
import Beranda from "./pages/beranda";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div>
  <Navbar /> 
<BrowserRouter>
    <Routes>
      <Route index element={<Beranda />} ></Route>
      <Route  path="/home" element={<Beranda />} ></Route>
      <Route  path="/contact" element={<Contact />} ></Route>
      <Route  path="/about" element={<About />} ></Route>
    </Routes>
</BrowserRouter>
<Footer />

</div>

   
  );
}

export default App;
