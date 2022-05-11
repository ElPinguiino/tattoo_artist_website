import styled from 'styled-components'
import tw from 'tailwind-styled-components';

export const MainContainer = tw.div`
    mt-12
    mx-auto
    flex
    justify-center
`

export const StyledForm = tw.form`
    flex
    w-full
    max-w-sm
    space-x-3
    
`

export const FormDiv = tw.div`
    w-full
    max-w-2xl
    px-5
    py-10
    m-auto
    mt-10
    bg-white
    rounded-lg
    shadow
    dark:bg-clip-padding backdrop-filter backdrop-blur-xl bg-opacity-20
`

export const StyledOuterDiv = tw.div`
    grid
    max-w-xl
    grid-cols-2
    gap-4
    m-auto
`

export const FormHeading = tw.div`
    mb-6
    text-3xl
    font-light
    text-center
    text-gray-800
    dark:text-black
`

export const StyledInputDiv = tw.div`
    col-span-2
`

export const StyledDualInputDiv = tw.div`
    col-span-2 lg:col-span-1
`

export const RelativeDiv = tw.div`
    relative
`

export const StyledInput = tw.input`
    appearance-none
    block
    w-full
    bg-gray-200
    text-gray-700
    border
    border-gray-200
    rounded
    py-3
    px-4
    mb-3
    leading-tight
    focus:outline-none
    focus:bg-white
    focus:border-gray-500
`

export const StyledTextAreaLabel = tw.label`
    text-gray-700
`

export const StyledTextArea = tw.textarea`
flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 rounded-lg text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent
`

export const StyledLabel = tw.label`
    block
    uppercase
    tracking-wide
    tex-700
    text-xs
    font-bold
    mb-2
`