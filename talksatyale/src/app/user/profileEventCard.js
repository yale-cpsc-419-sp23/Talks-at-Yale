import Image from 'next/image'
import styles from '../page.module.css'
import { FaMinus, FaPlus } from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";
import { FaTimes} from "react-icons/fa";

import EventModal from '../eventModal';
import React, { useState, useEffect, use } from 'react';

// Handles card clicked

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function ProfileEventCard({ event }) {

  const [isShown, setIsShown] = useState(false);

  const handleCardClicked = event => {

    try {
        setIsShown(true);
        console.log("Card clicked!");
      } catch (error) {
        console.error('Error when card clicked:', error);
      }

  };

  const closeModal = () => {
    setIsShown(false);
  };

  return (
    <div className={styles.profileCardContainer}>
      {isShown && (
        <EventModal event= {event} onClose={closeModal}/>
      )}
        <h2 className={styles.profileCardTitle} onClick={handleCardClicked}>{event.title}</h2>
        <p className={styles.profileCardDescription}>{event.description}</p>
        <p className={styles.profileCardDetails}>{event.time}</p>
        <p className={styles.profileCardDetails}>{event.date}</p>
        <p className={styles.profileCardDetails}>{event.location}</p>
    </div>

  )
}
