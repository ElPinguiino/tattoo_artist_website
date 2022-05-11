import React from 'react'
import { MainContainer, ContentContainer, ArtistPictureContainer, ArtistPicture, ArtistBioContainer, ArtistBio } from './MiniAboutElements';
import image from '../../assets/images/stephaniejohnson.png';

const MiniAbout = () => {
  return (
    <>
      <MainContainer>
        <ContentContainer>
          <ArtistPictureContainer>
            <ArtistPicture src={image} />
          </ArtistPictureContainer>
          <ArtistBioContainer>
            <ArtistBio>Hello fuckers, what it do? My name is Stephanie Johnson. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</ArtistBio>
          </ArtistBioContainer>
        </ContentContainer>
      </MainContainer>
    </>
  )
}

export default MiniAbout