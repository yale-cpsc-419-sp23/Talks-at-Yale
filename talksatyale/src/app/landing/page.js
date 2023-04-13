"use client";
import Cookies from "js-cookie";

import styles from './landing.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'


export default function Landing() {
  // Handles the login function
  function handlelogin() {
    try {
      const frontend_callback_url = `${window.location.origin}`;
      const login_url = `http://localhost:8080/login?frontend_callback=${encodeURIComponent(frontend_callback_url)}`;
      window.location.replace(login_url);
    } catch (error) {
      console.error("Error during login:", error);
    }
  }
  useEffect(() => {
  const accessToken = Cookies.get('access_token');
  console.log("Access Token from cookie:", accessToken);
  if (accessToken) {
    localStorage.setItem('access_token', accessToken);
    Cookies.remove('access_token');
  }
}, []);
  
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
          <button className={styles.logInButton} onClick={handlelogin}><h2>Log In</h2></button>
            
        </main>
      </div>
      
    )
  }
  