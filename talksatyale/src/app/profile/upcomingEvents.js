"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import ProfileEventCard from './profileEventCard';

const API_ENDPOINT = 'https://586e-2601-18b-8100-ef40-bcf2-3b57-699b-ed6a.ngrok.io';  // constant url, used to fetch data from backend

export default function UpcomingEvents({props}) {
  console.log("Component but just page!");

  // get search results from search term, passed from child (header)
  const[data, setData] = useState([{}])
  const [events, setEvents] = useState([]);
  const handleFavoriteResults = (results) => {
    setEvents(results);
  }

  useEffect(() => {
    async function fetchFavoriteEvents() {
      try {
        const url = API_ENDPOINT + '/events/favorite_events';
        const response = await fetch(url, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        const data = await response.json();
        setEvents(data);
        console.log(data);
      } catch (error) {
        console.error('Error fetching favorite events:', error);
      }
    }
    fetchFavoriteEvents();
  }, []);

  const removeFavoriteEvent = (eventId) => {
    setEvents(events.filter((event) => event.id !== eventId));
  };

    return (
      <div className={styles.upcomingEvents}>
        <h2>Upcoming Events</h2>
        <div className={styles.upcomingContainer}>
        {events.map((result) => (
          <ProfileEventCard key={result.id} event={result} onRemoveFavoriteEvent={removeFavoriteEvent}/>
          ))}
        </div>
      </div>

    )
  }
