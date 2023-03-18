"use client";

import Image from 'next/image'
import styles from './page.module.css'
import React, { useState, useEffect, use } from 'react'

export default function Header(props) {
  // store data and the search term
  const[data, setData] = useState([{}])


  const [searchTerm, setSearchTerm] = useState('');
  // const [searchResults, setSearchResults] = useState('');



   // store the search term
  // send search term back to parent (page) function
  useEffect(() => {
  async function fetchResults() {
      const response = await fetch(`http://127.0.0.1:5000/events/${searchTerm}`).then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          // setSearchResults(data)
          console.log(data)
          props.handleSearchResults(data);
        }
      )
    }
    fetchResults();
  }, [searchTerm]);


  // when enter key is pressed in search box,
  // call function to retrieve results based on search
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      const value = event.target.value;
      setSearchTerm(value);
      // Do something with the search term, such as calling a function
      console.log(`Search term entered: ${value}`);
    }
  };


    
    

  return (
    <header className={styles.header}>
        <div className={styles.headerLeft}>
            <h2 className={styles.title}>Talks at Yale</h2>
            <div className={styles.search}>
                <input className={styles.searchBar} onKeyDown={handleKeyDown}
                placeholder="Search by title, department, topic, etc..."></input>
                <p className={styles.searchResults}>Showing 20 results.</p>
            </div>
        </div>
        <div className={styles.headerRight}>
            <button className={styles.profileButton}><h2>My Profile</h2></button>
        </div>
    </header>
  )
}
