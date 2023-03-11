"use client";

import Image from 'next/image'
import styles from './page.module.css'
import Header from './header'
import EventCard from './eventCard'
import React, { useState, useEffect, use } from 'react'


export default function Home() {
  const [searchResults, setSearchResults] = useState([]);
  const handleSearchResults = (results) => {
    console.log(results);
    setSearchResults(results);
  }
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
