import styles from '../page.module.css'

import { FaBookmark } from "react-icons/fa";
import { FaRegBookmark } from "react-icons/fa";
import { FaTimes, FaPlus, FaMinus } from "react-icons/fa";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import React, { useEffect, useState } from "react";



export default function FriendModal({ onClose }) {
  // dropdown
  const [openSort, setOpenSort] = React.useState(false);
  const handleSort = () => {
    setOpenSort(!openSort);
  };

  // declare a state variable to keep track of the selected date
const [selectedSort, setSelectedSort] = useState('My Friends');

// handle click event on date option
const handleSortClick = (event) => {
  setSelectedSort(event.target.value);
  setOpenSort(false);
};

  const handleKeyDown = (event) => {
    console.log("key pressed");
    };

    return (
    <div className={styles.friendModal}>
      <div className={styles.friendModalContent}>
        <div className={styles.friendModalHeader}>
          <div className={styles.search}>
            <input className={styles.friendSearchBar} onKeyUp={handleKeyDown}
            placeholder="Search for friends..."></input>
          </div>

          {/* fheijfw */}
          <button onClick={handleSort} className={styles.filterList}>
            <div className={styles.textIconContainer}>{selectedSort} <FaTimes size={15} style={{marginLeft:"8px"}}/></div>
          </button>
          { openSort ? (
            <ul className={styles.menu}>
              <li className={styles.menuItem} onClick={handleSortClick}><button value="My Friends">My Friends</button></li>
              <li className={styles.menuItem} onClick={handleSortClick}><button value="All People">All People</button></li>
            </ul>
          ) : null}

          {/* jieow */}
          <div className={styles.friendModalClose} onClick={onClose}>
              <FaTimes />
          </div>
        </div>

      </div>
 
    </div>
    )
}
