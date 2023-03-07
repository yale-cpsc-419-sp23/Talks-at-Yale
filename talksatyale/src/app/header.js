import Image from 'next/image'
import styles from './page.module.css'


export default function Header() {
  return (
    <header className={styles.header}>
        <div className={styles.titleSearch}>
            <h2 className={styles.title}>Talks at Yale</h2>
            <input className={styles.searchBar} placeholder="Search by title, department, topic, etc..."></input>

        </div>
        <button className={styles.logInButton}><h2>Log In</h2></button>
    </header>
  )
}
