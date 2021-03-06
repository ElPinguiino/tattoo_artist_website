import styled from 'styled-components';
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`

`

export const ContentContainer = tw.div`
    container
    mx-auto
    px-4
    flex
    flex-wrap
`

export const ArtistPictureContainer = tw.div`
    lg:flex-1
`

export const ArtistPicture = tw.img`
    rounded-lg
    object-cover
    h-150
    w-300
`

export const ArtistBioContainer = tw.div`
    lg:flex-1
`

export const ArtistBio = tw.p`
    text-lg
    line-clamp-10
    text-black
`

export const StyledButton = tw.button`
    focus:outline-none
    text-white
    bg-lisa-yellow
    font-medium
    rounded-lg
    text-sm
    px-5 
    py-2.5
    mb-2
`