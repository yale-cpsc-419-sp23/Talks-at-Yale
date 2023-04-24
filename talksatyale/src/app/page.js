"use client";

import Image from 'next/image'
import styles from './page.module.css'
import './globals.css'
import Header from './header'
import EventCard from './eventCard'
import Landing from './landing/page'
import React, { useState, useEffect, use } from 'react'

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend
// const API_ENDPOINT = 'https://cpsc-419-group1.herokuapp.com';  // constant url, used to fetch data from backend

export default function Home() {

  // Keeping track of user status
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [loading, setLoading] = useState(true);

  // checking login status
  const checkLoginStatus = async () => {
    try {
      const headers = new Headers();
      const accessToken = localStorage.getItem('access_token');
      console.log('Access token:', accessToken);
      if (accessToken) {
        headers.append('Authorization', `Bearer ${accessToken}`);
      }

      const url = API_ENDPOINT + '/is_logged_in'
      const response = await fetch(url, {
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
    finally {
      setLoading(false); 
    }
  };

  useEffect(() => {
    checkLoginStatus();
  }, []);



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
         const url = API_ENDPOINT + '/events/departments'
         const response = await fetch(url).then(
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
           const url = API_ENDPOINT + '/events/events_status'
           const response = await fetch(url, {
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
         const url = API_ENDPOINT + '/events/search'
         const response = await fetch(url,
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

  if (loading) {
      return null; // don't render anything while loading
    } else if(loggedIn) {


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
