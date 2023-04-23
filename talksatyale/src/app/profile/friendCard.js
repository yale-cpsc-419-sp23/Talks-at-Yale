import Image from 'next/image'
import styles from '../page.module.css'
import { FaMinus, FaPlus } from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";
import { FaTimes} from "react-icons/fa";

import React, { useState, useEffect, use } from 'react';

// Handles card clicked

export default function FriendCard({ user }) {
    // Add friend
    const handleAddFriend = async (email) => {
        try {
        const accessToken = localStorage.getItem('access_token');
        const headers = new Headers();
        if (accessToken) {
            headers.append('Authorization', `Bearer ${accessToken}`);
        }
        const response = await fetch(`http://localhost:8080/add_friend?email=${email}`, {
            method: 'POST',
            headers,
        });
        if (response.ok) {
            toast.success('Friend added successfully');
            // change the text of the button to Remove Friend
        } else {
            toast.error('Failed to add friend');
        }
        } catch (error) {
        console.log(error);
        toast.error('Failed to add friend');
        }
    };

  return (
    <div className={styles.friendCard}>
        <img className={styles.friendCardImage} alt={user.first_name} src={user.photo_link}/>
        <h2 className={styles.friendCardName}>{user.first_name} {user.last_name}</h2>
        <div className={styles.friendButtonContainer}>
            <button className={styles.friendCardButton} onClick={() => handleAddFriend(user.email)}>Add</button>
        </div>
    </div>


  )
}
