import React from 'react';
import { FaFacebook, FaInstagram, FaYoutube, FaLinkedin, FaDiscord, FaTwitch } from 'react-icons/fa';
import { FooterContainer, FooterWrap, FooterLinksContainer, FooterLinksWrapper, FooterLinkItems, FooterLinkTitle, FooterLink, SocialMedia, SocialMediaWrap, WebsiteRightsContainer, WebsiteRights, SocialIcons, SocialIconLink } from './FooterElements';

const Footer = () => {
    return (
        <FooterContainer>
            <FooterWrap>
                <SocialMedia>
                    <SocialMediaWrap>
                            <SocialIcons>
                                <SocialIconLink href="https://www.facebook.com/slundtattoosandart/" target="_blank" aria-label='Facebook'>
                                    <FaFacebook />
                                </SocialIconLink>
                                <SocialIconLink href="https://www.instagram.com/zee.l.1991/?hl=en" target="_blank" aria-label='Instagram'>
                                    <FaInstagram />
                                </SocialIconLink>
                                <SocialIconLink href="https://www.youtube.com/channel/UCDnP-XXi6GE43NSb1xeEX-Q" target="_blank" aria-label='Youtube'>
                                    <FaYoutube />
                                </SocialIconLink>
                                <SocialIconLink href="https://www.linkedin.com/company/juan-of-a-kind-kitchen" target="_blank" aria-label='Linkedin'>
                                    <FaLinkedin />
                                </SocialIconLink>
                                <SocialIconLink href="https://www.linkedin.com/company/juan-of-a-kind-kitchen" target="_blank" aria-label='Linkedin'>
                                    <FaDiscord />
                                </SocialIconLink>
                                <SocialIconLink href="https://www.linkedin.com/company/juan-of-a-kind-kitchen" target="_blank" aria-label='Linkedin'>
                                    <FaTwitch />
                                </SocialIconLink>
                            </SocialIcons>
                    </SocialMediaWrap>
                </SocialMedia>
                <WebsiteRightsContainer>
                    <WebsiteRights>Stephanie Johnson Tattooing © {new Date().getFullYear()}</WebsiteRights>
                </WebsiteRightsContainer>
            </FooterWrap>
        </FooterContainer>
    )
}

export default Footer;