"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'

const API_ENDPOINT = 'https://586e-2601-18b-8100-ef40-bcf2-3b57-699b-ed6a.ngrok.io';  // constant url, used to fetch data from backend

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
        const url = API_ENDPOINT + '/profile'
        const response = await fetch(url, {
          credentials: 'include',
          headers: headers,
        });
        const data = await response.json();
        console.log(data)
        setUser(data);
        console.log(user);
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
          <div className={styles.profileImageContainer}>
            <img className={styles.profileImage} src={user?.photo_link}/>

          </div>
            <div className={styles.nameEmail}>
              <h2>{user?.first_name} {user?.last_name}</h2>
              <h4 className={styles.email}>{user?.email}</h4>
            </div>
        </div>

      </div>

    )
  }
