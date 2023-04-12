"use client";

import Image from 'next/image'
import styles from './page.module.css'
import './globals.css'
import Header from './header'
import EventCard from './eventCard'
import React, { useState, useEffect, use } from 'react'


export default function Home() {

  // get search results from search term, passed from child (header)
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }

  // get departments from backend
  const [depts, setDepts] = useState([]);


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
          <EventCard key={result.id} event={result}/>
          ))}

        </div>
      </main>
    </div>

  )
}
