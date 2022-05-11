import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { MainContainer, TitleContainer, Title, GalleryContainer, GalleryCard, StyledImage } from './MiniGalleryElements'


const MiniGallery = () => {
  const [recentImages, setRecentImages] = useState([])

  const getRecentImages = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/gallery_post')
      setRecentImages(response.data)
      console.log('test')
  }

  useEffect(() => {
      getRecentImages();
  }, [])

  return (
    <>
        <MainContainer>
            <TitleContainer>
                <Title>Recent Work</Title>
            </TitleContainer>
            <GalleryContainer>
            {recentImages.map((recentImages) => (
                <GalleryCard key={recentImages.id}>
                    <StyledImage src={recentImages.image}/>
                </GalleryCard>
                ))}
            </GalleryContainer>
        </MainContainer>
    </>
  )
}

export default MiniGallery




{/* <MainContainer>
            <TitleContainer>
                <Title>Recent Work</Title>
            </TitleContainer>
            <div class="carousel rounded-box">
            {recentImages.map((recentImages, index) => (
                <div class="carousel-item" key={index}>
                    <img src={recentImages.image} alt="caption" />
                </div>
                )
                )
            }
            </div> 
        </MainContainer> */}