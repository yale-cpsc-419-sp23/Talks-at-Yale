"use client";

import Image from 'next/image'
import styles from './page.module.css'
import React, { useState, useEffect, use } from 'react'
import Cookies from "js-cookie"

export default function Header(props) {

  const[data, setData] = useState([{}])


  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState('');

  // Keeping track of user status
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  // checking login status
  const checkLoginStatus = async () => {
    try {
      const headers = new Headers();
      const accessToken = localStorage.getItem('access_token');
      console.log(accessToken);
      if (accessToken) {
        headers.append('Authorization', `Bearer ${accessToken}`);
      }

      const response = await fetch('http://127.0.0.1:5000/is_logged_in', {
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
  // fetching current events when new term entered (not connected to new backend)
  useEffect(() => {
    async function fetchResults() {
      const response = await fetch(`http://127.0.0.1:5000/events/${searchTerm}`).then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          setSearchResults(data)
          console.log(data)
          props.handleSearchResults(data);
        }
      )
    }
    fetchResults();
  }, [searchTerm]);

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      const value = event.target.value;
      setSearchTerm(value);
      // Do something with the search term, such as calling a function
      console.log(`Search term entered: ${value}`);
    }
  };

  // Handles the login function
  function handlelogin() {
    try {
      const frontend_callback_url = `${window.location.origin}`;
      const login_url = `http://127.0.01:5000/login?frontend_callback=${encodeURIComponent(frontend_callback_url)}`;
      window.location.href = login_url;
    } catch (error) {
      console.error("Error during login:", error);
    }
  }
  useEffect(() => {
  const accessToken = Cookies.get('access_token');
  if (accessToken) {
    localStorage.setItem('access_token', accessToken);
    // Cookies.remove('access_token');
  }
  checkLoginStatus();
}, []);


// Handles logout
async function handleLogout() {
  try {
    // Remove the access token from localStorage
    localStorage.removeItem('access_token');
    // Redirect to the backend /logout route
    const logout_url = 'http://127.0.01:5000/logout';
    const response = await fetch(logout_url, { credentials: 'include' });
    const data = await response.json();
    if (!data.logged_in) {
      setLoggedIn(false);
      setUsername('');

      // Redirect to the CAS logout page
      window.location.href = data.cas_logout_url;
    }
  } catch (error) {
    console.error('Error during logout:', error);
  }
}


  return (
    <header className={styles.header}>
        <div className={styles.headerLeft}>
            <h2 className={styles.title}><a href="/">Talks at Yale</a></h2>
            <div className={styles.search}>
                <input className={styles.searchBar} onKeyDown={handleKeyDown}
                placeholder="Search by title, department, topic, etc..."></input>
                <p className={styles.searchResults}>Showing 20 results.</p>
            </div>
        </div>
        <div className={styles.headerRight}>
      {loggedIn ? (
          <button className={styles.profileButton} onClick={handleLogout}>
            <h2>Log Out</h2>
          </button>
      ) : (
        <button className={styles.profileButton} onClick={handlelogin}>
          <h2>Log In</h2>
        </button>
      )}
    </div>
    </header>
  )
}
