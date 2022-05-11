import React, {useState} from 'react';
import './App.css';
import Home from './pages/Home';
import Gallery from './pages/Gallery';
import About from './pages/About';
import Contact from './pages/Contact';
import Merch from './pages/Merch';
import Events from './pages/Events';
import Consultation from './pages/Consultation';
import FAQs from './pages/FAQs';
import Header from './components/Header/Header';

import { 
  BrowserRouter,
  Routes, 
  Route 
} from 'react-router-dom';

import Navbar from './components/Navbar/Navbar';
import Footer from './components/Footer/Footer';

function App() {

  return (
    <>
      <BrowserRouter>
        <Header />
        <div className="flex flex-col items-center justify-center min-h-0 py-2">
            <Navbar />
        </div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/gallery" element={<Gallery />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/merch" element={<Merch />} />
            <Route path="/events" element={<Events />} />
            <Route path="/consultation" element={<Consultation />} />
            <Route path="/faqs" element={<FAQs />} />
          </Routes>
          <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
