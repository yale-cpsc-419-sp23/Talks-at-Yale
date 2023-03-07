import Image from 'next/image'
import styles from './page.module.css'


export default function Header() {
  return (
    <header className={styles.header}>
        <div className={styles.titleSearch}>
            <h1 className={styles.title}>Talks at Yale</h1>
            <input className={styles.searchBar} placeholder="Search by title, department, topic, etc."></input>

        </div>
        <button className={styles.logInButton}><h1>Log In</h1></button>
    </header>
  )
}
