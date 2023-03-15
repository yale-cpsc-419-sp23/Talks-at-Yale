"use client";

import Image from 'next/image'
import styles from './page.module.css'
import Header from './header'
import EventCard from './eventCard'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'


export default function Home() {
  console.log("Component but just page!");

  // get search results from search term, passed from child (header)
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }


  const handleResponse = (response) => {
    if (Array.isArray(response[0]) !== true) {
      console.log("Redirecting to CAS login:", response[0]);
      window.location.href = response[0];
      console.log(response[0]);
      
    }
  }

  // calls the function to get events
  const[data, setData] = useState([{}])
  // useEffect(() => {
  //   async function fetchResults() {
  //     const response = await fetch(`http://127.0.0.1:5000/`).then(
  //       res => res.json()
  //     ).then(
  //       data => {
  //         setSearchResults(data);
  //         handleResponse(data); 
  //       }
  //     );
  
  //   }
  //   fetchResults();
  // }, []);
    useEffect(() => {
      axios.get('http://127.0.0.1:5000/').then((response) => {
        if (response.data.login_url) {
          // User is not authenticated, so redirect to CAS login page
          window.location.href = response.data.login_url;
        } else {
          // User is already authenticated, so display the search results
          setSearchResults(response.data.results);

          // console.log("Hello");

          // // handle redirect back to homepage after successful CAS authentication
          // if (data.redirect_url) {
          //   console.log("Redirecting back to homepage:", data.redirect_url);
          //   window.location.href = data.redirect_url;
          // }
        }
      });
    }, []);






  return (
    <div className={styles.pageWrapper}>
      <Header handleSearchResults={handleSearchResults}/>
      <main className={styles.main}>
        <div>
          {searchResults.map((result) => (
          <EventCard key={result.id} event={result} />
          ))}
 
        </div>
      </main>
    </div>
    
  )
}
