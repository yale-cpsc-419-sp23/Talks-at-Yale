import styles from './page.module.css'

import { FaBookmark } from "react-icons/fa";
import { FaRegBookmark } from "react-icons/fa";
import { faBookmark } from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";



export default function EventModal({ event }) {
    return (
    <div className={styles.modal}>
        <div className={styles.modalContent}>
            <div className={styles.modalHeader}>

                <FaRegBookmark size={40} className={styles.modalBookmark}/>
                <h2 className={styles.modalTitle}>{event[2]}</h2>
            </div>
            <div className={styles.modalBody}>
                body
            </div>
        

        </div>
    </div>
    )
}
