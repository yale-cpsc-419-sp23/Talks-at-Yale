import Image from 'next/image'
import styles from './page.module.css'
import Header from './header'


export default function Home() {
  return (
    <div className={styles.pageWrapper}>
      <Header />
      <main className={styles.main}>
        <div className={styles.description}>
        </div>
      </main>
    </div>
    
  )
}
