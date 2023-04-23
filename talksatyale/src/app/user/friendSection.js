"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function FriendSection({friends}) {
    return (
      <div className={styles.friendSection}>
        <div className={styles.myFriends}>
          {friends?.map(friend => (
            <a href={`http://localhost:3000/user?net_id=${friend.netid}`} key={friend.netid}>
              <img className={styles.friendImages} src={friend.photo_link}/>
            </a>
          ))}
        </div>
      </div>

    )
  }
