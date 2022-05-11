import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { MainContainer, TitleContainer, Title, EventsContainer, EventCard, EventDetails} from './MiniEventsElements';

const MiniEvents = () => {
  const [recentEvents, setRecentEvents] = useState([])

  const getRecentEvents = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/event')
      setRecentEvents(response.data)
      console.log('test')
  }

  useEffect(() => {
      getRecentEvents();
  }, [])

  return (
    <>
        <MainContainer>
            <TitleContainer>
                <Title>Upcoming Events:</Title>
            </TitleContainer>
            <EventsContainer>
            {recentEvents.map((recentEvents) => (
              <EventCard key={recentEvents.id}>
                <EventDetails>{recentEvents.title}</EventDetails>
                <EventDetails>{recentEvents.dates}</EventDetails>
                <EventDetails>{recentEvents.location}</EventDetails>
              </EventCard>
            ))}
            </EventsContainer>
        </MainContainer>
    </>
  )
}

export default MiniEvents