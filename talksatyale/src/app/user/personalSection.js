"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function PersonalSection(props) {
  const {profile} = props;

    return (
      <div className={styles.personalSection}>
        <div className={styles.rectangleBg}></div>
        <div className={styles.iconName}>
          <div className={styles.profileImageContainer}>
            <img className={styles.profileImage} src={profile?.photo_link}/>

          </div>
            <div className={styles.nameEmail}>
              <h2>{profile?.first_name} {profile?.last_name}</h2>
              <h4 className={styles.email}>{profile?.email}</h4>
            </div>
        </div>
      </div>

    )
  }
