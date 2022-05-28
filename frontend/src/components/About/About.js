import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { MainContainer, ContentContainer, ArtistPictureContainer, ArtistPicture, ArtistBioContainer, ArtistBio } from '../About/AboutElements'

const About = () => {
  const [artistInfo, setArtistInfo] = useState([]);

  const getArtistInfo = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/artist_info')
        setArtistInfo(response.data)
        console.log(response.data)
    }
  
  useEffect(() => {
      getArtistInfo();
  }, [])

  return (
    <>
        <MainContainer>
        <div key={artistInfo.id}>
        {artistInfo.map((artistInfo) => (
          <ContentContainer>
          <ArtistPictureContainer>
            <ArtistPicture src={artistInfo.image} />
          </ArtistPictureContainer>
          <ArtistBioContainer>
            <ArtistBio >{artistInfo.bio}</ArtistBio>
          </ArtistBioContainer>
        </ContentContainer>
        ))}
        </div>
      </MainContainer>
    </>
  )
}

export default About