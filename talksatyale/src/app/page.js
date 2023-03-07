import Image from 'next/image'
import styles from './page.module.css'
import Header from './header'
import EventCard from './eventCard'


export default function Home() {
  return (
    <div className={styles.pageWrapper}>
      <Header />
      <main className={styles.main}>
        <div>
          <EventCard />
        </div>
      </main>
    </div>
    
  )
}
