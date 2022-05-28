import styled from 'styled-components';
import { Link } from 'react-router-dom';
import tw from 'tailwind-styled-components';

// export const FooterContainer = styled.footer`
    
// `

// export const FooterWrap = styled.div`
//     padding: 48px 24px;
//     display: flex;
//     flex-direction: column;
//     justify-content: center;
//     align-items: center;
//     max-width: 1100px;
//     margin: auto;
// `

// export const SocialMedia = styled.section`
//     max-width: 1000px;
//     width: 100%;
// `

// export const SocialMediaWrap = styled.div`
//     display: flex;
//     justify-content: center;
//     align-items: center;
//     max-width: 1100px;
//     margin: 40px auto 0 auto;
//     @media screen and (max-width: 820px) {
//         flex-direction: column;
//     }
// `

// export const SocialLogo = styled(Link)`
//     color: #fff;
//     justify-self: start;
//     cursor: pointer;
//     text-decoration: none;
//     font-size: 1.5rem;
//     display: flex;
//     align-items: center;
//     margin-bottom: 16px;
//     font-weight: bold;
// `

// export const WebsiteRightsContainer = styled.div`
//     margin-top: 0.5rem;
// `

// export const WebsiteRights = styled.small`
//     color: #fff;
//     margin-bottom: 16px;
// `

// export const SocialIcons = styled.div`
//     display: flex;
//     justify-content: space-between;
//     align-items: center;
//     width: 240px;
//     margin-left: 1rem;
//     margin-right: 1rem;
// `

// export const SocialIconLink = styled.a`
//     color: #fff;
//     font-size: 36px;
// `




export const FooterContainer = tw.footer`
    
`

export const FooterWrap = tw.div`
    py-6
    px-24
    flex
    flex-col
    justify-center
    items-center
    max-w-screen-xl
    m-auto
`

export const SocialMedia = tw.section`
    max-w-screen-xl
    w-full
`

export const SocialMediaWrap = tw.div`
    flex
    justify-center
    items-center
    max-w-screen-xl
    margin: 40px auto 0 auto;
    mt-6
    mr-auto
    mb-0
    ml-auto

    md:flex-col
`

export const SocialLogo = styled(Link)`
    text-black
    justify-self-start
    cursor-pointers
    text-2xl
    flex
    items-center
    mb-4
    font-bold
`

export const WebsiteRightsContainer = tw.div`
    mt-2
`

export const WebsiteRights = tw.small`
    text-black
    mb-4
`
export const SocialIcons = tw.div`
    flex
    justify-between
    items-center
    w-60
    ml-4
    mr-4
`

export const SocialIconLink = tw.a`
    text-lisa-blue
    text-4xl
`