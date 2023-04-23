"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import FriendModal from './friendModal';

const API_ENDPOINT = 'https://dynamic-peony-fc31a3.netlify.app';  // constant url, used to fetch data from backend

export default function FriendSection() {

    const [friends, setFriends] = useState([]);

    const getFriends = async () => {
      try {
        const url = API_ENDPOINT + '/list_friends';
        const response = await fetch(url);
        const data = await response.json();
        setFriends(data);
      }
      
      catch (error) {
        console.error("Error during login:", error);
      }
    };

    useEffect(() => {
      getFriends();
    }, []);

    const [isShown, setIsShown] = useState(false);
  
  
    const openFriend = event => {
  
      try {
          setIsShown(true);
          console.log("Manage friend clicked!");
        } catch (error) {
          console.error('Error when card clicked:', error);
        }
  
    };
    const closeModal = () => {
        setIsShown(false);
      };

    return (
      <div className={styles.friendSection}>
        {isShown && (
        <FriendModal event= {event} onClose={closeModal}/>
            )}
        <div className={styles.myFriends}>
          {friends.map(friend => (
            <a href={`https://example.com/profile/${friend.id}`} key={friend.id}>
              <img className={styles.friendImages} src={friend.profile_picture}/>
            </a>
          ))}
            {/* <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a> */}
        </div>
        <button className={styles.friendButton} onClick={openFriend}>
            <h2>Manage Friends</h2>
        </button>


      </div>

    )
  }
