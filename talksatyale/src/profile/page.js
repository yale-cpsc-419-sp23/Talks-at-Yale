"use client";

import styles from './profile.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import EventCard from '../eventCard'


export default function Login() {
  
  
    return (
      <div className={styles.pageWrapper}>
        <main>
          <h1 className={styles.title}>Talks at Yale</h1>
          <h2 className={styles.subtitle}>Never miss out on an event.</h2>
          <div className={styles.listContainer}>
            <div className={styles.rectangle}></div>
            <div className={styles.bulletContainer}>
              <h2 className={styles.bullets}>View events you don’t want to miss</h2>
              <h2 className={styles.bullets}>Save your favorite events to your profile and GCal</h2>
              <h2 className={styles.bullets}>Send event feedback directly to organizers</h2>
              <h2 className={styles.bullets}>Explore events by department, topic, date, and more</h2>
            </div>
          </div>
          <button className={styles.logInButton}><h2>Log In</h2></button>
            
        </main>
      </div>
      
    )
  }
  