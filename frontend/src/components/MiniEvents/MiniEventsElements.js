import styled from 'styled-components';
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`
    mt-12
    py-4
    px-4
`

export const TitleContainer = tw.div`
    container
    mx-auto
`

export const Title = tw.h2`
    text-2xl
    text-black
`
export const EventsContainer = tw.div`
    justify-center
    align-center
    flex
    overflow-auto
    whitespace-nowrap
`

export const EventCard = tw.div`
    h-80
    min-w-80
    p-4
    rounded-xl
    bg-lisa-green/70
    my-2
    mx-2
`

export const EventDetails = tw.p`
    text-black
`