import React from 'react'
import { useForm } from "react-hook-form";
import { MainContainer, StyledForm, FormDiv, FormHeading, StyledInput, RelativeDiv, StyledOuterDiv, StyledDualInputDiv, StyledLabel, StyledInputDiv, StyledTextAreaLabel, StyledTextArea } from './FormElements';

const ContactForm = () => {
  return (
    <MainContainer>
        <StyledForm>
          <FormDiv>
            <FormHeading>Contact Form</FormHeading>
            <StyledOuterDiv>
                <StyledInputDiv>
                <StyledInput type="text" id="contact-form-fullname" placeholder="Full Name"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledInput type="email" id="contact-form-email" placeholder="whatisyouremail@email.com"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledInput type="number" id="contact-form-number" placeholder="Phone Number"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="contact-form-tattoo-size" placeholder="What can I help you with?"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
            </StyledOuterDiv>
          </FormDiv>
        </StyledForm>
      </MainContainer>
  )
}

export default ContactForm