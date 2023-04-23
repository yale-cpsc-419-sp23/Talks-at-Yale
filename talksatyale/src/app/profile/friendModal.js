import styles from '../page.module.css';

import { FaBookmark } from 'react-icons/fa';
import { FaRegBookmark } from 'react-icons/fa';
import { FaTimes, FaPlus, FaMinus } from 'react-icons/fa';
import { FaCaretDown } from 'react-icons/fa';

import FriendCard from './friendCard';

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
	const [friends, setFriends] = useState([]);

	// handle search input change
	const handleSearchInputChange = (event) => {
		setSearchTerm(event.target.value);
	  };


	// handle filter option selection
	const handleFilterOptionClick = (event) => {
		setFilterOption(event.target.value);
		setOpenSort(false);
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

	// fetch friends
	useEffect(() => {
		async function getFriends() {
		const accessToken = localStorage.getItem('access_token');
		const headers = new Headers();
		if (accessToken) {
		headers.append('Authorization', `Bearer ${accessToken}`);
		}
		  const url = `http://localhost:8080/list_friends`;
		  const response = await fetch(url, { headers: headers });
		  const data = await response.json();
		  setFriends(data);
		}
		getFriends();
	  }, []);

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
						<FriendCard user={user}/>
				))}
				</div>
			</div>
		</div>
	);
}
