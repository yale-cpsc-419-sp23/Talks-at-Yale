"use client";

import Image from 'next/image'
import styles from './page.module.css'
import './globals.css'
import Header from './header'
import EventCard from './eventCard'
import React, { useState, useEffect, use } from 'react'


export default function Home() {
  console.log("Component but just page!");

  // get search results from search term, passed from child (header)
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }


  // calls the function to get events
  const[data, setData] = useState([{}])
  useEffect(() => {
    async function fetchResults() {
      const response = await fetch(`http://localhost:8080/`).then(
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
