"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'


export default function PersonalSection() {

  const [user, setUser] = useState(null);

  useEffect(() => {
    async function fetchProfile() {
      try {
        const headers = new Headers();
        const accessToken = localStorage.getItem('access_token');
        console.log('Access token:', accessToken);
        if (accessToken) {
          headers.append('Authorization', `Bearer ${accessToken}`);
        }
        const response = await fetch('http://localhost:8080/profile', {
          credentials: 'include',
          headers: headers,
        });
        const data = await response.json();
        console.log(data)
        setUser(data);
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    }
    fetchProfile();
  }, []);

    return (
      <div className={styles.personalSection}>
        <div className={styles.rectangleBg}></div>
        <div className={styles.iconName}>
            <img className={styles.profileIcon} src={user?.photo_link}/>
            <div className={styles.nameEmail}>
              <h2>{user?.first_name} {user?.last_name}</h2>
              <h4 className={styles.email}>{user?.email}</h4>
            </div>
        </div>

      </div>

    )
  }
