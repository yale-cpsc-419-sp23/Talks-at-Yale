'use client';

import Image from 'next/image';
import styles from './page.module.css';
import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import { FaCaretDown } from 'react-icons/fa';
import { FaTimes } from 'react-icons/fa';

export default function Header(props) {
	// toggling dropdowns
	// department dropdown
	const [openDept, setOpenDept] = React.useState(false);
	const handleDeptDrop = () => {
		// close other open filters
		setOpenDate(false);
		setOpenSort(false);

		setOpenDept(!openDept);
	};
	// date dropdowns
	const [openDate, setOpenDate] = React.useState(false);
	const handleDateDrop = () => {
		// close other open filters
		setOpenDept(false);
		setOpenSort(false);

		setOpenDate(!openDate);
	};
	// sort dropdown
	const [openSort, setOpenSort] = React.useState(false);
	const handleSortDrop = () => {
		// close other open filters
		setOpenDept(false);
		setOpenDate(false);

		setOpenSort(!openSort);
	};

	// handle department click
	const [selectedDept, setSelectedDept] = useState('All Departments');

	const handleDeptClick = (event) => {
		setSelectedDept(event.target.value);
		setOpenDept(false);
	};

	// declare a state variable to keep track of the selected date
	const [selectedDate, setSelectedDate] = useState('Upcoming');

	// handle click event on date option
	const handleDateClick = (event) => {
		setSelectedDate(event.target.value);
		setOpenDate(false);
	};

	// Handle sort click
	const [selectedSort, setSelectedSort] = useState('Date');
	const handleSortClick = (event) => {
		setSelectedSort(event.target.value);
		setOpenSort(false);
	};

	// Handle reset button
	const handleReset = () => {
		setOpenDept(false);
		setOpenDate(false);
		setOpenSort(false);
		setSelectedDept('All Departments');
		setSelectedDate('Upcoming');
		setSelectedSort('Date');
		setSearchTerm('');
	};

	const [data, setData] = useState([{}]);
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
			console.log(data);
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
			const accessToken = localStorage.getItem('access_token');
			const headers = new Headers();
			if (accessToken) {
				headers.append('Authorization', `Bearer ${accessToken}`);
			}
			const url = `http://localhost:8080/events/search?search_term=${searchTerm}&department=${encodeURIComponent(
				selectedDept
			)}&status=${encodeURIComponent(selectedDate)}&sort=${encodeURIComponent(
				selectedSort
			)}`;

			const response = await fetch(url, { headers: headers })
				.then((res) => res.json())
				.then((data) => {
					setData(data);
					setSearchResults(data);
					props.handleSearchResults(data);
				});
		}
		fetchResults();
	}, [searchTerm, selectedDept, selectedDate, selectedSort]);

	const handleKeyDown = (event) => {
		const value = event.target.value;
		setSearchTerm(value);
	};

	// Handles the login function
	function handlelogin() {
		try {
			const frontend_callback_url = `${window.location.origin}`;
			const login_url = `http://localhost:8080/login?frontend_callback=${encodeURIComponent(
				frontend_callback_url
			)}`;
			window.location.replace(login_url);
		} catch (error) {
			console.error('Error during login:', error);
		}
	}
	useEffect(() => {
		const accessToken = Cookies.get('access_token');
		console.log('Access Token from cookie:', accessToken);
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
					<h2 className={styles.title}>
						<a href="/">Talks at Yale</a>
					</h2>
					<div className={styles.search}>
						<input
							className={styles.searchBar}
							onKeyUp={handleKeyDown}
							placeholder="Search by title, department, topic, etc..."
						></input>
						<p className={styles.searchResults}>
							Showing {data.length} results.
						</p>
					</div>
				</div>
				<div className={styles.headerRight}>
					{loggedIn ? (
						<>
							<a href="http://localhost:3000/profile">
								<button className={styles.profileButton}>
									<h2>Profile</h2>
								</button>
							</a>
							<button
								className={styles.logInButton}
								onClick={handleLogout}
							>
								<h2>Log Out</h2>
							</button>
						</>
					) : (
						<button
							className={styles.logInButton}
							onClick={handlelogin}
						>
							<h2>Log In</h2>
						</button>
					)}
				</div>
			</div>
			<div className={styles.filters}>
				<div className={styles.dropContainer}>
					<button onClick={handleDeptDrop} className={styles.filterList}>
						<div className={styles.textIconContainer}>
							{selectedDept}{' '}
							<FaCaretDown size={20} style={{ marginLeft: '8px' }}/>
						</div>
						</button>
						{openDept ? (
							<ul className={styles.menu}>
								<li className={styles.menuItem}>
									<button onClick={handleDeptClick} value="All Departments"> All Departments</button>
								</li>
								{props.depts.map((dept) => (
									<li key={dept} className={styles.menuItem}>
										<button value={dept} onClick={handleDeptClick}>{dept}</button>
									</li>
								))}
							</ul>
						) : null}
				</div>
				<div className={styles.dropContainer}>
					<button onClick={handleDateDrop} className={styles.filterList}>
						<div className={styles.textIconContainer}>
							{selectedDate}{' '}
							<FaTimes size={15} style={{ marginLeft: '8px' }}/>
						</div>
					</button>
					{openDate ? (
						<ul className={styles.menu}>
							<li className={styles.menuItem} onClick={handleDateClick}>
								<button value="All Dates">All Dates</button>
							</li>
							<li className={styles.menuItem}>
								<button value="Upcoming" onClick={handleDateClick}>Upcoming</button>
							</li>
							<li className={styles.menuItem}>
								<button value="Past" onClick={handleDateClick}>Past</button>
							</li>
						</ul>
					) : null}
				</div>
				<div className={styles.orderContainer}>
					<p className={styles.orderBy}>Order By</p>
					<div className={styles.dropContainer}>
						<button onClick={handleSortDrop} className={styles.filterList}>
							<div className={styles.textIconContainer}>
								{selectedSort}
								<FaCaretDown size={20} style={{ marginLeft: '8px' }}/>
							</div>
						</button>
						{openSort ? (
							<ul className={styles.menu}>
								<li className={styles.menuItem}>
									<button value="Date" onClick={handleSortClick}>Date</button>
								</li>
								<li className={styles.menuItem}>
									<button value="Title" onClick={handleSortClick}>Title</button>
								</li>
								<li className={styles.menuItem}>
									<button value="Department" onClick={handleSortClick}>Department</button>
								</li>
							</ul>
						) : null}
					</div>
				</div>
				<button className={styles.resetButton} onClick={handleReset} >
					Reset
				</button>
		</div>
		</header>
	);
}
