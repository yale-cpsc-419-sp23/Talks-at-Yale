import Image from 'next/image'
import styles from './page.module.css'


export default function Header() {
  return (
    <header className={styles.header}>
        <div className={styles.headerLeft}>
            <h2 className={styles.title}>Talks at Yale</h2>
            <div className={styles.search}>
                <input className={styles.searchBar} placeholder="Search by title, department, topic, etc..."></input>
                <p className={styles.searchResults}>Showing 20 results.</p>

            </div>

        </div>
        <div className={styles.headerRight}>
            <button className={styles.logInButton}><h2>Log In</h2></button>
        </div>
    </header>
  )
}
