"use client";

import Image from 'next/image'
import styles from './page.module.css'
import React, { useState, useEffect, use } from 'react'
import Cookies from "js-cookie"
import { FaCaretDown } from "react-icons/fa";
import { FaTimes } from "react-icons/fa";

export default function Header(props) {


  // toggling dropdowns
  // department dropdown
  const [openDept, setOpenDept] = React.useState(false);
  const handleDeptDrop = () => {
    setOpenDept(!openDept);
  };
  // date dropdowns
  const [openDate, setOpenDate] = React.useState(false);
  const handleDateDrop = () => {
    setOpenDate(!openDate);
  };
  // sort dropdown
  const [openSort, setSort] = React.useState(false);
  const handleSortDrop = () => {
    setOpenSort(!openSort);
  };

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

  // fetching current events when new term entered
  useEffect(() => {
    async function fetchResults() {
      const response = await fetch(`http://localhost:8080/events/search?search_term=${searchTerm}`).then(
        res => res.json()
      ).then(
        data => {
          setData(data);
          setSearchResults(data);
          props.handleSearchResults(data);
        }
      )
    }
    fetchResults();
  }, [searchTerm]);

  const handleKeyDown = (event) => {
      const value = event.target.value;
      setSearchTerm(value);
  };

  // Handles the login function
  function handlelogin() {
    try {
      const frontend_callback_url = `${window.location.origin}`;
      const login_url = `http://localhost:8080/login?frontend_callback=${encodeURIComponent(frontend_callback_url)}`;
      window.location.replace(login_url);
    } catch (error) {
      console.error("Error during login:", error);
    }
  }
  useEffect(() => {
  const accessToken = Cookies.get('access_token');
  console.log("Access Token from cookie:", accessToken);
  if (accessToken) {
    localStorage.setItem('access_token', accessToken);
    checkLoginStatus();
    Cookies.remove('access_token');
  }
}, []);
useEffect(() => {
  checkLoginStatus();
}, []);



// Handles logout
async function handleLogout() {
  try {
    // Remove the access token from localStorage
    localStorage.removeItem('access_token');
    // Redirect to the backend /logout route
    const logout_url = 'http://localhost:8080/logout';
    const response = await fetch(logout_url, { credentials: 'include' });
    const data = await response.json();
    if (data.cas_logout_url) {
      setLoggedIn(false);
      setUsername('');
      // Redirect to the CAS logout page
      window.location.href = data.cas_logout_url;
    } else {
      // Handle the case when there's no CAS logout URL in the response
      console.error('Error during logout: CAS logout URL not provided');
    }
  } catch (error) {
    console.error('Error during logout:', error);
  }
}

  return (
    <header>
      <div className={styles.header}>
          <div className={styles.headerLeft}>
              <h2 className={styles.title}><a href="/">Talks at Yale</a></h2>
              <div className={styles.search}>
                  <input className={styles.searchBar} onKeyUp={handleKeyDown}
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
          
      </div>
      <div className={styles.filters}>
        <button onClick={handleDeptDrop}className={styles.filterList}>
          <div className={styles.textIconContainer}>Department <FaCaretDown size={20} style={{marginLeft:"8px"}}/></div>
        </button>
        { openDept ? (
          <ul className={styles.menu}>
            <li selected className={styles.menuItem}><button>All Departments</button></li>
            <li className={styles.menuItem}><button>ACCT- Accounting</button></li>
            <li className={styles.menuItem}><button>AFAM- African American Studies</button></li>
            <li className={styles.menuItem}><button>CPSC- Computer Science</button></li>
            <li className={styles.menuItem}><button>ENRG- Energy Studies</button></li>
            <li className={styles.menuItem}><button>MATH- Mathematics</button></li>
          </ul>
        ) : null}
        <button onClick={handleDateDrop} className={styles.filterList}>
          <div className={styles.textIconContainer}>Upcoming <FaTimes size={15} style={{marginLeft:"8px"}}/></div>
        </button>
        <button onClick={handleSortDrop}className={styles.filterList}>
          <div className={styles.textIconContainer}>Date <FaCaretDown size={20} style={{marginLeft:"8px"}}/></div>
        </button>
        <button className={styles.resetButton}>Reset</button>
      </div>
    </header>
  )
}