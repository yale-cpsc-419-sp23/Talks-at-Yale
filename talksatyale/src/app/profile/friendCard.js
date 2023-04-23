import Image from 'next/image'
import styles from '../page.module.css'
import { FaMinus, FaPlus } from "react-icons/fa";
import { FaRegClock } from "react-icons/fa";
import { FaMapMarkerAlt } from "react-icons/fa";
import { FaTimes} from "react-icons/fa";
import { toast } from 'react-toastify';


import React, { useState, useEffect, use } from 'react';

// Handles card clicked

export default function FriendCard({ user, friends, setFriends }) {
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
			// create a copy of the friends state and add the new friend to the end
			const newFriends = [...friends, { email }];
			setFriends(newFriends);
			toast.success('Friend added successfully');
		  } else {
			toast.error('Failed to add friend');
		  }
		} catch (error) {
		  console.log(error);
		  toast.error('Failed to add friend');
		}
	  };


    // Remove friend
	const handleRemoveFriend = async (email) => {
		try {
		const accessToken = localStorage.getItem('access_token');
		const headers = new Headers();
		if (accessToken) {
			headers.append('Authorization', `Bearer ${accessToken}`);
		}
		const response = await fetch(`http://localhost:8080/remove_friend?email=${email}`, {
			method: 'POST',
			headers,
		});
		if (response.ok) {
			toast.success('Friend removed successfully');
		// update the friends array after removing the friend
			setFriends(prevFriends => prevFriends.filter(friend => friend.email !== email));
		} else {
			toast.error('Failed to remove friend');
		}
		} catch (error) {
		console.log(error);
		toast.error('Failed to remove friend');
		}
	};


  return (
    <div className={styles.friendCard}>
        <img className={styles.friendCardImage} alt={user.first_name} src={user.photo_link}/>
        <h2 className={styles.friendCardName}>{user.first_name} {user.last_name}</h2>
        <div className={styles.friendButtonContainer}>
            {friends.some(friend => friend.email === user.email) ? (
                <button className={styles.friendCardButton} onClick={() => handleRemoveFriend(user.email)}>Remove Friend</button>
            ) : (
                <button className={styles.friendCardButton} onClick={() => handleAddFriend(user.email)}>Add Friend</button>
            )}
        </div>

    </div>


  )
}
