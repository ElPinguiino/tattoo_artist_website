import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { MainContainer, TitleContainer, Title, EventsContainer, EventCard, EventDetails} from './EventsElements';

const Events = () => {
    const [events, setEvents] = useState([])

    const getEvents = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/event')
        setEvents(response.data)
        console.log('test')
    }
  
    useEffect(() => {
        getEvents();
    }, [])
  
    return (
      <>
          <MainContainer>
              <TitleContainer>
                  <Title>Upcoming Events:</Title>
              </TitleContainer>
              <EventsContainer>
              {events.map((events) => (
                <EventCard key={events.id}>
                  <EventDetails>{events.title}</EventDetails>
                  <EventDetails>{events.dates}</EventDetails>
                  <EventDetails>{events.location}</EventDetails>
                </EventCard>
              ))}
              </EventsContainer>
          </MainContainer>
      </>
    )
  }

export default Events