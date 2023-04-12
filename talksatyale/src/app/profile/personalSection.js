"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'


export default function PersonalSection() {
  
  
    return (
      <div className={styles.personalSection}>
        <div className={styles.rectangleBg}></div>
        <div className={styles.iconName}>
            <img className={styles.profileIcon} src="https://cdn-icons-png.flaticon.com/512/3940/3940403.png"/>
            <div className={styles.nameEmail}>
                <h2>Alan Weide</h2>
                <h4 className={styles.email}>alan.weide@yale.edu</h4>
            </div>
        </div>
    
      </div>
      
    )
  }
  