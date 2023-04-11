import Image from 'next/image'
import styles from '../page.module.css'
import { FaPlus } from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";

import EventModal from '../eventModal';
import React, { useState, useEffect, use } from 'react';

// Handles card clicked



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

  const favoriteEvent = event => {
    try {
      console.log("Item favorited!");
    } catch (error) {
      console.error('Error when favoriting:', error);
    }
  }

  return (
    
    <div className={styles.cardContainer}>
      {isShown && (
        <EventModal event= {event}/>
      )}
        <div className={styles.cardLeft}>
            <h2 className={styles.cardDay}>{event.formatted_date.week_day}</h2>
            <h2 className={styles.cardDate}>{event.formatted_date.exact_date}</h2>
            <h2 className={styles.cardMonth}>{event.formatted_date.month}</h2>
        </div>
        <div className={styles.cardRight}>
            <FaPlus className={styles.cardFaPlus} onClick={favoriteEvent}/>
            <h6 className={styles.cardDept}>{event.department}</h6>
            <h2 className={styles.cardTitle} onClick={handleCardClicked}>{event.title}</h2>
            <p className={styles.cardDescription}>{event.description}</p>
            <p className={styles.cardLocation}><FaRegClock size={18} className={styles.smallIcons}/> {event.time} | <FaMapMarkerAlt size={18} className={styles.smallIcons}/> {event.location} </p>
        </div>
    </div>
    
  )
}
