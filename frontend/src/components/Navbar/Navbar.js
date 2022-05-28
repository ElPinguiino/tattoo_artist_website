import React, {useState} from 'react'
import { StyledButton, StyledAnchor, StyledListItem, StyledDiv, StyledUL, StyledSVG} from './NavbarElements';

const Navbar = () => {

    const [showNavbar, setShowNavbar] = useState(false)

    return (
        <>
            {showNavbar ? (
              <StyledButton
                onClick={() => setShowNavbar(!showNavbar)}
              >
                x
              </StyledButton>
            ) : (
              <StyledSVG
                onClick={() => setShowNavbar(!showNavbar)}
                fill="#E6007E"
                viewBox="0 0 100 80"
                width="40"
                height="40"
              >
                <rect width="100" height="10"></rect>
                <rect y="30" width="100" height="10"></rect>
                <rect y="60" width="100" height="10"></rect>
              </StyledSVG>
            )}
            <div
              className={`top-0 right-0 w-[80vw] bg-gradient-to-r from-lisa-pink via-lisa-orange via-lisa-yellow via-lisa-green to-lisa-blue p-10 pl-20 text-white fixed h-full z-40  ease-in-out duration-300 ${
                showNavbar ? "translate-x-0 " : "translate-x-full"
              }`}
            >
              <StyledUL>
                  <StyledListItem>
                      <StyledAnchor href="/">Home</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/gallery">Gallery</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/about">About</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/contact">Contact</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/merch">Merch</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/events">Events</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/consultation">Consultation</StyledAnchor>
                  </StyledListItem>
                  <StyledListItem>
                      <StyledAnchor href="/faqs">FAQs</StyledAnchor>
                  </StyledListItem>
              </StyledUL>
            </div>

        </>
    )
}

export default Navbar