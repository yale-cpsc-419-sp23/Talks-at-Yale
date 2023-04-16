"use client";

import Image from 'next/image'
import styles from './page.module.css'
import './globals.css'
import Header from './header'
import EventCard from './eventCard'
import Landing from './landing/page'
import React, { useState, useEffect, use } from 'react'


export default function Home() {

  // Keeping track of user status
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  // checking login status
  const checkLoginStatus = async () => {
    try {
      const headers = new Headers();
      const accessToken = localStorage.getItem('access_token');
      console.log('Access token:', accessToken);
      if (accessToken) {
        headers.append('Authorization', `Bearer ${accessToken}`);
      }

      const response = await fetch('http://localhost:8080/is_logged_in', {
        credentials: 'include',
        headers: headers,
      });
      const data = await response.json();
      console.log(data)
      if (data.logged_in) {
        setLoggedIn(true);
        setUsername(data.username);
      } else {
        setLoggedIn(false);
        setUsername('');
  
      }

    } catch (error) {
      console.error('Error checking login status:', error);
    }
  };

  useEffect(() => {
    checkLoginStatus();
  }, []);



 

  if(loggedIn) {

     // get search results from search term, passed from child (header)
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }

  // get departments from backend
  const [depts, setDepts] = useState([]);

  const [favoriteEventIDs, setFavoriteEventIDs] = useState([]);


  const[data, setData] = useState([{}])

  useEffect(() => {

    async function fetchDepts() {
      console.log('Fetching departments')
      const response = await fetch(`http://localhost:8080/events/departments`).then(
        res => res.json()
      ).then(
        data => {
          setDepts(data);
          console.log('Dept data:', data);
        }
      );

    }
    fetchDepts();
  }, []);

  // Getfavorited ids

  useEffect(() => {
    const fetchFavoriteEventIDs = async () => {
      try {
        const response = await fetch(`http://localhost:8080/events/events_status`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        const data = await response.json();
        setFavoriteEventIDs(data.IDS);
      } catch (error) {
        console.error('Error fetching favorite event IDs:', error);
      }
    };

    fetchFavoriteEventIDs();
  }, []);



  // calls the function to get events
  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    const headers = new Headers();
    if (accessToken) {
      headers.append('Authorization', `Bearer ${accessToken}`);
    }
    async function fetchResults() {
      const response = await fetch(`http://localhost:8080/events/search`,
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
    
      <div className={styles.pageWrapper}>
        <Header handleSearchResults={handleSearchResults} depts={depts}/>
        <main className={styles.main}>
          <div>
            {searchResults.map((result) => (
            <EventCard key={result.id} event={result} favoriteEventIDs={favoriteEventIDs} setFavoriteEventIDs={setFavoriteEventIDs} />
            ))}
  
          </div>
        </main>
      </div>
  
    )
  

  }
  else {
    return (
      <Landing />
    )
  }
  }
