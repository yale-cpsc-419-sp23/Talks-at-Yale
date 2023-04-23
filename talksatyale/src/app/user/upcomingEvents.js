"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import ProfileEventCard from './profileEventCard';

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function UpcomingEvents({events}) {
  console.log("Component but just page!");
    return (
      <div className={styles.upcomingEvents}>
        <h2>Upcoming Events</h2>
        <div className={styles.upcomingContainer}>
        {events.map((result) => (
          <ProfileEventCard key={result.id} event={result}/>
          ))}
        </div>
      </div>

    )
  }
