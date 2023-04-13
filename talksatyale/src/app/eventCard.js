import Image from 'next/image'
import styles from './page.module.css'
import { FaPlus, FaMinus} from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";
import { FaTimes } from 'react-icons/fa';

import EventModal from './eventModal';
import React, { useState, useEffect, use } from 'react';

// Handles card clicked



export default function EventCard({ event, favoriteEventIDs, setFavoriteEventIDs}) {


  const [isShown, setIsShown] = useState(false);
  const [isFavorited, setIsFavorited] = useState(false);


  const handleCardClicked = event => {

    try {
        setIsShown(true);
        console.log("Card clicked!");
      } catch (error) {
        console.error('Error when card clicked:', error);
      }

  };

  const toggleFavorite = async () => {
    try {
      if (isFavorited) {
        const response = await fetch(`http://localhost:8080/events/remove_favorite?event_id=${event.id}`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        if (!response.ok) {
          throw new Error('Error removing event from favorites');
        }
        console.log('Event removed from favorites!');
        setIsFavorited(false);
        setFavoriteEventIDs(favoriteEventIDs.filter(id => id !== event.id));
      } else {
        const response = await fetch(`http://localhost:8080/events/add_favorite?event_id=${event.id}`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        if (!response.ok) {
          throw new Error('Error adding event to favorites');
        }
        console.log('Event added to favorites!');
        setIsFavorited(true);
        setFavoriteEventIDs([...favoriteEventIDs, event.id]);
      }
    } catch (error) {
      console.error('Error toggling favorite:', error);
    }
  };

  const closeModal = () => {
    console.log("Modal closed");
    setIsShown(false);
  };


  useEffect(() => {
    setIsFavorited(favoriteEventIDs?.includes(event.id));
  }, [favoriteEventIDs, event.id]);

  return (
    <div className={styles.cardContainer}>
      {isShown && (
        <EventModal event= {event} onClose={closeModal} />
      )}
        <div className={styles.cardLeft}>
            <h2 className={styles.cardDay}>{event.formatted_date.week_day}</h2>
            <h2 className={styles.cardDate}>{event.formatted_date.exact_date}</h2>
            <h2 className={styles.cardMonth}>{event.formatted_date.month}</h2>
        </div>
        <div className={styles.cardRight}>
          {isFavorited ? (
            <FaMinus className={styles.cardFaPlus} onClick={toggleFavorite} />
          ) : (
            <FaPlus className={styles.cardFaPlus} onClick={toggleFavorite} />
          )}
            <h6 className={styles.cardDept}>{event.department}</h6>
            <h2 className={styles.cardTitle} onClick={handleCardClicked}>{event.title}</h2>
            <p className={styles.cardDescription}>{event.description}</p>
            <p className={styles.cardLocation}><FaRegClock size={18} className={styles.smallIcons}/> {event.time} | <FaMapMarkerAlt size={18} className={styles.smallIcons}/> {event.location} </p>
        </div>
    </div>

  )
}
