import React from 'react'
import { useForm } from "react-hook-form";
import { MainContainer, StyledForm, FormDiv, FormHeading, StyledInput, RelativeDiv, StyledOuterDiv, StyledDualInputDiv, StyledLabel, StyledInputDiv, StyledTextAreaLabel, StyledTextArea } from './FormElements';

const ConsultForm = () => {
  return (
    <>
      <MainContainer>
        <StyledForm>
          <FormDiv>
            <FormHeading>Consultation Form</FormHeading>
            <StyledOuterDiv>
              <StyledDualInputDiv>
                <RelativeDiv>
                  <StyledInput type="text" id="consultation-form-firstname" placeholder="First Name"/>
                </RelativeDiv>
              </StyledDualInputDiv>
              <StyledDualInputDiv>
                <RelativeDiv>
                <StyledInput type="text" id="consultation-form-lastname" placeholder="Last Name"/>
                </RelativeDiv>
              </StyledDualInputDiv>
              <StyledInputDiv>
                <StyledInput type="email" id="consultation-form-email" placeholder="whatisyouremail@email.com"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledInput type="number" id="consultation-form-number" placeholder="Phone Number"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledInput type="button"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="consultation-form-tattoo-size" placeholder="How big do you want the tattoo?"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="consultation-form-tattoo-placement" placeholder="Detail where you want the tattoo placed"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="consultation-form-tattoo-concept" placeholder="Explain your tattoo concept if you would like to"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledLabel>Image Refrences:</StyledLabel>
                <StyledInput type="file"/>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="consultation-form-existing-tattoos" placeholder="Are there any existing tattoos that we will need to workaround?"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledLabel>Existing Tattoos to Workaround:</StyledLabel>
                <StyledInput type="file"/>
              </StyledInputDiv>
              <StyledInputDiv>
                  <StyledInput type="text" id="consultation-form-preferred-days" placeholder="What days work best for you for an appointment"></StyledInput>
              </StyledInputDiv>
              <StyledInputDiv>
                  <StyledInput type="text" id="consultation-form-preferred-time-of-day" placeholder="Explain your tattoo concept if you would like to"></StyledInput>
              </StyledInputDiv>
              <StyledInputDiv>
                <StyledTextAreaLabel>
                  <StyledTextArea id="consultation-form-additional-comments" placeholder="Please enter any other relavent information"></StyledTextArea>
                </StyledTextAreaLabel>
              </StyledInputDiv>
            </StyledOuterDiv>
          </FormDiv>
        </StyledForm>
      </MainContainer>
    </>
  )
}

export default ConsultForm