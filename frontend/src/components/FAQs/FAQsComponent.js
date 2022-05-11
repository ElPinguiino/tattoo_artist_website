import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { ContainerDiv, InnerDiv, MainContainer, OuterDiv, StyledDetails, StyledDiv, StyledP, StyledSection, StyledSpan, StyledSummary, Title } from './FAQsComponentElements';

const FAQsComponent = () => {
    const [faqs, setFaqs] = useState([])

    const getFaqs = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/faq')
        setFaqs(response.data)
        console.log('test')
    }
  
    useEffect(() => {
        getFaqs();
    }, [])
  
  return (
    <>
        <MainContainer>
            <StyledSection>
                <ContainerDiv>
                    <StyledDiv>
                        <Title>Frequently Asked Questions</Title>
                        <StyledP>The most common questions about how our business works and what
                                    can do for you.
                        </StyledP>
                    </StyledDiv>
                    <OuterDiv>
                    {faqs.map((faqs) => (
                        <InnerDiv key={faqs.id}>
                            <StyledDetails>
                                <StyledSummary>
                                {faqs.title}
                                </StyledSummary>
                                <StyledSpan>
                                {faqs.content}
                                </StyledSpan>
                            </StyledDetails>
                        </InnerDiv>
                    ))}
                    </OuterDiv>
                </ContainerDiv>
            </StyledSection>
        </MainContainer>
    </>
  )
}

export default FAQsComponent