"use client";

import styles from '../page.module.css';
import React, { useState, useEffect, use } from 'react';
import axios from 'axios';
import ProfileHeader from './profileHeader';
import PersonalSection from './personalSection';
import FriendSection from './friendSection';
import UpcomingEvents from './upcomingEvents';
import Landing from '../landing/page';

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function Profile() {
    // Keeping track of user status
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [loading, setLoading] = useState(true);

  // user details
  const [friends, setFriends] = useState([]);
  const [profile, setProfile] = useState([]);
  const [events, setEvents] = useState([])

  // getting user details
  const [refresh, setRefresh] = useState(false);

  useEffect(() => {
    async function getDetails() {
      try {
        const params = new URLSearchParams(window.location.search);
        const netid = params.get('net_id');
        const url = `${API_ENDPOINT}/user_details?net_id=${netid}`;
        const response = await fetch(url);
        const data = await response.json();
        setFriends(data.friends);
        setProfile(data.profile)
        setEvents(data.events)
        console.log('Friends: ', data);
      } catch (error) {
        console.error('Error finding friends:', error);
      }
    }
    getDetails();
  }, [refresh]);

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



  // Handles the login function
  function handlelogin() {
    try {
      const frontend_callback_url = `${window.location.origin}`;
      const login_url = API_ENDPOINT + `/sign_in?frontend_callback=${encodeURIComponent(frontend_callback_url)}`;
      window.location.replace(login_url);
    } catch (error) {
      console.error("Error during login:", error);
    }
  }

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
    if (loading) {
      return null; // don't render anything while loading
    } else if(loggedIn) {


    return (
      <div className={styles.pageWrapper}>
        <ProfileHeader/>
        <main className={styles.profileMain}>
          <div className={styles.profileTop}>
            <PersonalSection profile={profile}/>
            <FriendSection friends={friends}/>
          </div>
          <div className={styles.profileBottom}>
            <UpcomingEvents events={events}/>

          </div>
          <div>
            <a href="http://localhost:3000/profile">
              <button className={styles.profileLogOut}>
                <h2>Back to Profile</h2>
              </button>
            </a>

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