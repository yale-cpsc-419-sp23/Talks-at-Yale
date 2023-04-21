"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import FriendModal from './friendModal';

export default function FriendSection() {

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
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
            <a href="https://google.com"><img className={styles.friendImages} src='https://yalestudentphotos.s3.amazonaws.com/9067bb5899168ad2a0f4f4c2d98abfda.jpg'/></a>
        </div>
        <button className={styles.friendButton} onClick={openFriend}>
            <h2>Manage Friends</h2>
        </button>


      </div>

    )
  }
