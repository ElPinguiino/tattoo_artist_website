import styled from 'styled-components';
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`
    py-6
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
    py-6
`

export const ArtistBio = tw.p`
    text-lg
`

