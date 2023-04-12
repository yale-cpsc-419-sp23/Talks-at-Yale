"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import ProfileEventCard from './profileEventCard';


export default function UpcomingEvents({props}) {
  console.log("Component but just page!");

  // get search results from search term, passed from child (header)
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }
 
  

  const[data, setData] = useState([{}])






  // calls the function to get events
  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    const headers = new Headers();
    if (accessToken) {
      headers.append('Authorization', `Bearer ${accessToken}`);
    }
    async function fetchResults() {
      const response = await fetch(`http://localhost:8080/events/`,
      {headers: headers,}
      ).then(
        res => res.json()
      ).then(
        data => {
          setSearchResults(data);
        }
      );

    }
    fetchResults();
  }, []);


  
  
    return (
      <div className={styles.upcomingEvents}>
        <h2>Upcoming Events</h2>
        <div className={styles.upcomingContainer}>
          <ProfileEventCard/>
          <ProfileEventCard/>
          <ProfileEventCard/>
          <ProfileEventCard/>
          <ProfileEventCard/>
        </div>
        {/* {searchResults.map((result) => (
          <ProfileEventCard key={result.id} event={result}/>
          ))} */}

      </div>
      
    )
  }
  