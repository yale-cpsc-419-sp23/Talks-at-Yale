"use client";

import Image from 'next/image'
import styles from '../page.module.css'
import React, { useState, useEffect} from 'react'
import Cookies from "js-cookie"
import { FaCaretDown } from "react-icons/fa";
import { FaTimes } from "react-icons/fa";

const API_ENDPOINT = 'https://cpsc-419-group1.herokuapp.com';  // constant url, used to fetch data from backend

export default function ProfilHeader() {



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
  };



  // Handles the login function
  function handlelogin() {
    try {
      const frontend_callback_url = `${window.location.origin}`;
      const login_url = API_ENDPOINT + `/login?frontend_callback=${encodeURIComponent(frontend_callback_url)}`;
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
    const logout_url = API_ENDPOINT + '/logout';
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
            
          </div>

      </div>
    </header>
  )
}