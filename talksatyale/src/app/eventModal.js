import styles from './page.module.css'

import { FaBookmark } from "react-icons/fa";
import { FaRegBookmark } from "react-icons/fa";
import { FaTimes } from "react-icons/fa";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";



export default function EventModal({ event, onClose }) {
    return (
    <div className={styles.modal}>
        <div className={styles.modalContent}>
            <div className={styles.modalHeader}>
                <FaRegBookmark size={40} className={styles.modalBookmark}/>
                <div className={styles.modalDetails}>
                    <h2 className={styles.modalTitle}>{event.title}</h2>
                </div>
                <div className={styles.modalClose} onClick={onClose}>
                    <FaTimes />
                </div>

            </div>
            <div className={styles.modalSubHeader}>
                <h3>{event.department}</h3>
                <h3><a href="https://calendar.google.com" className={styles.addCalendar}>Add to Google Calendar</a></h3>

            </div>

            <div className={styles.modalBody}>
                {event.description}
            </div>
            <div>
                {event.bio}
            </div>
            <div>
                {event.speaker}
            </div>
            <div>
                {event.speaker_title}
            </div>
            <div>
                {event.location}
            </div>
            <div>
                {event.date}
            </div>
            <div>
                {event.time}
            </div>

        </div>
    </div>
    )
}
