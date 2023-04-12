"use client";

import styles from '../page.module.css';
import React, { useState, useEffect, use } from 'react';
import axios from 'axios';
import ProfileHeader from './profileHeader';
import PersonalSection from './personalSection';
import RightColumn from './rightColumn';
import UpcomingEvents from './upcomingEvents';



export default function Profile() {
  
  
    return (
      <div className={styles.pageWrapper}>
        <ProfileHeader/>
        <main className={styles.profileMain}>
          <div className={styles.profileLeft}>
            <PersonalSection/>
            <UpcomingEvents/>
          </div>
          <div className={styles.profileRight}>
            <RightColumn/>
          </div>
        </main>
      </div>
      
    )
  }
  