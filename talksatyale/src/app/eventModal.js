import styles from './page.module.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBookmark } from '@fortawesome/free-solid-svg-icons';

export default function EventModal() {
    return (
    <div className={styles.modal}>
        <div className={styles.modalContent}>
        <FontAwesomeIcon icon="fa-solid fa-bookmark" />

        </div>
    </div>
    )
}
