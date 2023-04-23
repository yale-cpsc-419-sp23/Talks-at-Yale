import styles from './page.module.css'

import { FaBookmark } from "react-icons/fa";
import { FaRegBookmark } from "react-icons/fa";
import { FaTimes, FaPlus, FaMinus } from "react-icons/fa";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import React, { useEffect, useState } from "react";



export default function EventModal({ event, onClose, favoriteEventIDs, setFavoriteEventIDs, isFavorited, setIsFavorited }) {

    const gcalEvent = () => {
        document.getElementById("gcal").href = "https://www.google.com/calendar/render?action=TEMPLATE&text=" + event.title + "&dates=" + event.iso + "&details=" + event.description + "&location=" + event.location + "&sf=true&output=xml";
        console.log(document.getElementById("gcal").href);
    }

    useEffect(() => {
      if(setIsFavorited){
        setIsFavorited(favoriteEventIDs?.includes(event.id));
      }
      }, [favoriteEventIDs, event.id]);

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


    return (
    <div className={styles.modal}>
        <div className={styles.modalContent}>
            <div className={styles.modalHeader}>
                {isFavorited ? (
                    <FaMinus size={25} className={styles.modalFaPlus} onClick={toggleFavorite} />
                ) : (
                    <FaPlus size={25} className={styles.modalFaPlus} onClick={toggleFavorite} />
                )}
                <h2 className={styles.modalTitle}>{event.title}</h2>
                <div className={styles.modalClose} onClick={onClose}>
                    <FaTimes />
                </div>

            </div>
            <div className={styles.modalSubHeader}>
                <h4 className={styles.modalDept}>{event.department}</h4>
                <h4 className={styles.addCalendar}>|</h4>
                <h4><a id = "gcal" href="" onClick={gcalEvent} className={styles.addCalendar} target="_blank"> add to Google Calendar</a></h4>
                <h4 className={styles.addCalendar}>|</h4>
                <h4><a id = "gcal" href={event.link} className={styles.addCalendar} target="_blank"> original event posting</a></h4>

            </div>
            <hr className={styles.hLine}></hr>

            <div className={styles.modalBody}>
                <p className={styles.modalDesc}>{event.description}</p>
            </div>

            <div className={styles.modalDetails}>
                <div className={styles.modalRow}>
                    <h4 className={styles.modalLabel}>Date</h4>
                    <h4 className={styles.modalDetail}>{event.long_date}</h4>
                </div>
                <div className={styles.modalRow}>
                    <h4 className={styles.modalLabel}>Time</h4>
                    <h4 className={styles.modalDetail}>{event.time}</h4>
                </div>
                <div className={styles.modalRow}>
                    <h4 className={styles.modalLabel}>Speaker</h4>
                    <h4 className={styles.modalDetail}>{event.speaker}</h4>
                </div>
                <div className={styles.modalRow}>
                    <h4 className={styles.modalLabel}>Location</h4>
                    <h4 className={styles.modalDetail}>{event.location}</h4>
                </div>
            </div>
            <hr className={styles.hLine}></hr>
            <h4 className={styles.modalFriends}>Inssia, Martin, Alan, and others have saved this event.</h4>


        </div>
    </div>
    )
}
