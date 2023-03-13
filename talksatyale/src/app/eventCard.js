import Image from 'next/image'
import styles from './page.module.css'


export default function EventCard({ event }) {
  return (
    <div className={styles.cardContainer}>
        <div className={styles.cardLeft}>
            <h2 className={styles.cardDay}>THU</h2>
            <h2 className={styles.cardDate}>28</h2>
            <h2 className={styles.cardMonth}>FEB</h2>
        </div>
        <div className={styles.cardRight}>
            <h6 className={styles.cardDept}>COMPUTER SCIENCE</h6>
            <h2 className={styles.cardHeader}>{event[2]}</h2>
            {/* <p className={styles.cardDescription}>
            Machine learning systems are deployed in consequential domains such as education, employment, and credit, where decisions have profound effects on socioeconomic opportunity and life outcomes. High stakes decision settings present new statistical, algorithmic, and ethical challenges. In this talk, we examine the distributive impact of machine learning algorithms in societal contexts, and investigate the algorithmic and sociotechnical interventions that bring machine learning systems into alignment with societal values—equity and long-term welfare. First, we study the dynamic interactions between machine learning algorithms and populations, for the purpose of mitigating disparate impact in applications such as algorithmic lending and hiring. Next, we consider data-driven decision systems in competitive environments such as markets, and devise learning algorithms to ensure efficiency and allocative fairness. We end by outlining future directions for responsible machine learning in societal systems that bridge the gap between the optimization of predictive models and the evaluation of downstream decisions and impact.
            </p> */}
            <p className={styles.cardDescription}>{event[8]}</p>
            <p className={styles.cardLocation}>AKW 202 | {event[6]}</p>
        </div>
    </div>
    
  )
}
