
import React, { useEffect, useState } from 'react'
import axios from 'axios';
import Masonry from 'react-masonry-css';
import { PostContainer, PostImage } from './MasonryElements'

const MasonryLayout = () => {
  const [images, setImages] = useState([]);

  const getImages = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/gallery_post')
        setImages(response.data)
    }
  
  useEffect(() => {
      getImages();
  }, [])

  const breakpointColumnsObj = {
    default: 4,
    3000: 6,
    2000: 5,
    1200: 3,
    1000: 2,
    500: 1,
  };

  return (
    <>
        <Masonry
          className="flex animate-slide-fwd"
          breakpointCols={breakpointColumnsObj}
        >
        {images.map((images) => (
        <PostContainer key={images.id}>
          <PostImage
            
            className="w-max"
            src={images.image}
          />
        </PostContainer>
        ))}
        </Masonry>
    </>
  )
}

export default MasonryLayout