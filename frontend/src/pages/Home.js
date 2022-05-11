import React from 'react'
import MiniAbout from '../components/MiniAbout/MiniAbout';
import MiniGallery from '../components/MiniGallery/MiniGallery';
import MiniEvents from '../components/MiniEvents/MiniEvents';

const Home = () => {
  return (
    <>
      <MiniAbout />
      <MiniGallery />
      <MiniEvents />
    </>
  )
}

export default Home