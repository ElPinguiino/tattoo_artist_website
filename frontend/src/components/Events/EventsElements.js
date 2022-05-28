import styled from 'styled-components';
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`
`

export const TitleContainer = tw.div`
    container
    mx-auto
    px-4
    
`

export const Title = tw.h2`
    text-lg
    text-black
`
export const EventsContainer = tw.div`
    justify-center
    align-center
    flex
    flex-wrap
`

export const EventCard = tw.div`
    h-80
    w-80
    p-6
    rounded-xl
    bg-rose-700/50
    my-2
    mx-2
`

export const EventDetails = tw.p`
    text-black
`