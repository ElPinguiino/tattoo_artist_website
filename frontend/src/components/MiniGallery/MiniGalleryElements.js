import styled from 'styled-components';
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`
    mt-12
    py-6
`

export const TitleContainer = tw.div`
    container
    mx-auto
    px-4
    
`

export const Title = tw.h2`
    text-lg
`
export const GalleryContainer = tw.div`
    justify-center
    align-center
    flex
    carousel
    rounded-box
`

export const GalleryCard = tw.div`
    carousel-item
    h-64
    w-64
`

export const StyledImage = tw.img`

`

// &:hover{
//     -webkit-transform: scale(1.2);
//     -ms-transform: scale(1.2);
//     transform: scale(1.2);
//     transition: 1s ease;
// }