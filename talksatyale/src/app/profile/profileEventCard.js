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
    
    <div className={styles.profileCardContainer}>
      {isShown && (
        <EventModal event= {event}/>
      )}
        <h2 className={styles.profileCardTitle} onClick={handleCardClicked}>Dean’s Dialogue: Doing It All: Engineering, Entrepreneurship and University Engagement</h2>
        <p className={styles.profileCardDescription}>Join us for a conversation with Yale College Dean Pericles Lewis and Professor Anjelica Gonzalez on how basic science becomes impactful through a focus on human needs. Prof. Gonzalez is Associate Professor of Biomedical Engineering, Head of Davenport College, and Faculty Director at Tsai Center for Innovative Thinking at Yale. Her work focuses on engineering solutions for human diseases not addressed well in animal models. Prof. Gonzalez is co-founder of Aero Therapeutics, a company that develops respiratory devices for infants. PremieBreathe, a project based on human-centered design, is an outgrowth of her teaching and research. Attendees will have opportunities to ask questions. Refreshments will be provided at the conclusion of the event.</p>
        <p className={styles.profileCardDetails}>4:00pm to 5:30pm</p>
        <p className={styles.profileCardDetails}>Wednesday, March 29, 2023</p>
        <p className={styles.profileCardDetails}>Yale Schwarzman Center SC, Presidents' Room
168 Grove St
New Haven, CT 06511 </p>
    </div>
    
  )
}
