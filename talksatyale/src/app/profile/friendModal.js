import styles from '../page.module.css';

import { FaBookmark } from 'react-icons/fa';
import { FaRegBookmark } from 'react-icons/fa';
import { FaTimes, FaPlus, FaMinus } from 'react-icons/fa';
import { FaCaretDown } from 'react-icons/fa';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import React, { useEffect, useState } from 'react';
import { userAgent } from 'next/server';
import { toast } from 'react-toastify';


export default function FriendModal({ onClose }) {
	// dropdown
	const [openSort, setOpenSort] = React.useState(false);
	const handleSort = () => {
		setOpenSort(!openSort);
	};

	// declare state variables
	const [searchTerm, setSearchTerm] = useState('');
	const [filterOption, setFilterOption] = useState('My Friends');
	const [searchResults, setSearchResults] = useState([]);

	// handle search input change
	const handleSearchInputChange = (event) => {
		setSearchTerm(event.target.value);
	  };


	// handle filter option selection
	const handleFilterOptionClick = (event) => {
		setFilterOption(event.target.value);
		setOpenSort(false);
	};

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


	const handleKeyDown = (event) => {
		console.log('key pressed');
	};
	// fetch search results from backend
	useEffect(() => {
		async function fetchSearchResults() {
		const accessToken = localStorage.getItem('access_token');
		const headers = new Headers();
		if (accessToken) {
		headers.append('Authorization', `Bearer ${accessToken}`);
		}
		  const url = `http://localhost:8080/search_people?search_term=${searchTerm}&filter_option=${filterOption}`;
		  const response = await fetch(url, { headers: headers });
		  const data = await response.json();
		  setSearchResults(data);
		}
		fetchSearchResults();
	  }, [searchTerm, filterOption]);

	return (
		<div className={styles.friendModal}>
			<div className={styles.friendModalContent}>
				<div className={styles.friendModalHeader}>
					<div className={styles.search}>
						<input
							className={styles.friendSearchBar}
							onKeyUp={handleKeyDown}
							placeholder="Search for friends..."
							onChange={handleSearchInputChange}
              				value={searchTerm}
						></input>
					</div>
					<div className={styles.friendDropContainer}>
						<button onClick={handleSort} className={styles.friendFilterList}>
							<div className={styles.textIconContainer}>
								{filterOption}{' '}
								<FaCaretDown size={20} style={{ marginLeft: '8px' }}/>
							</div>
						</button>
						{openSort ? (
							<ul className={styles.friendMenu}>
								<li className={styles.friendMenuItem} onClick={handleFilterOptionClick}>
									<button value="My Friends">My Friends</button>
								</li>
								<li className={styles.friendMenuItem} onClick={handleFilterOptionClick}>
									<button value="All People">All People</button>
								</li>
							</ul>
						) : null}
					</div>
					<div
						className={styles.friendModalClose}
						onClick={onClose}
					>
						<FaTimes />
					</div>
				</div>
				<div className={styles.friendListContainer}>
				{searchResults.map((user) => (
					<div key={user.id} className={styles.friendListItem}>
					<img src={user.photo_link} alt={user.name} className={styles.friendAvatar} />
					<div className={styles.friendDetails}>
					<div className={styles.friendName}>{user.first_name} {user.last_name}</div>
					<div className={styles.friendInfo}>{user.netid}</div>
					</div>
					<div className={styles.friendActions}>
					<button className={styles.friendActionButton}onClick={() => handleAddFriend(user.email)}>Add Friend</button>
					</div>
					</div>
				))}
				</div>
			</div>
		</div>
	);
}
