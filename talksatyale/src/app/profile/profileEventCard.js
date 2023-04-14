import Image from 'next/image'
import styles from '../page.module.css'
import { FaMinus, FaPlus } from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";
import { FaTimes} from "react-icons/fa";

import EventModal from '../eventModal';
import React, { useState, useEffect, use } from 'react';

// Handles card clicked


export default function ProfileEventCard({ event,  onRemoveFavoriteEvent}) {

  const [isShown, setIsShown] = useState(false);

  const handleCardClicked = event => {

    try {
        setIsShown(true);
        console.log("Card clicked!");
      } catch (error) {
        console.error('Error when card clicked:', error);
      }

  };

  const removeEvent = async (eventID) => {
    try {
      const response = await fetch(`http://localhost:8080/events/remove_favorite?event_id=${eventID}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });
      if (!response.ok) {
        throw new Error('Error removing event from favorites');
      }
      console.log('Event removed from favorites!');
      onRemoveFavoriteEvent(eventID);
    } catch (error) {
      console.error('Error removing event from favorites:', error);
    }
  };

  // const favoriteEvent = event => {
  //   try {
  //     console.log("Item favorited!");
  //   } catch (error) {
  //     console.error('Error when favoriting:', error);
  //   }
  // }
  const closeModal = () => {
    setIsShown(false);
  };

  return (
    <div className={styles.profileCardContainer}>
      {isShown && (
        <EventModal event= {event} onClose={closeModal}/>
      )}
      <div className={styles.closeIcon} onClick={() => removeEvent(event.id)}>
                    <FaMinus />
                </div>
        <h2 className={styles.profileCardTitle} onClick={handleCardClicked}>{event.title}</h2>
        <p className={styles.profileCardDescription}>{event.description}</p>
        <p className={styles.profileCardDetails}>{event.time}</p>
        <p className={styles.profileCardDetails}>{event.date}</p>
        <p className={styles.profileCardDetails}>{event.location}</p>
    </div>

  )
}
