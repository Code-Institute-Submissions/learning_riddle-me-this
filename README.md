# Riddle-me-this

This repo contains a solution code for the milestone project of the *Practical Pyton* module.
https://riddle-me--this.herokuapp.com/

## UX
Minimal interface to allow the following features.

## Features
- create a username 
- button to start getting riddles
- riddle page in which you can type the answer and submit
- if the answer is wrong the app will tell you and you can try again
- more than one player can use the riddle-me-this at the same time
- leaderboard page with your rank, when more than one user, and the points achieved

## Features left to implement
Some styling on the different web pages.
System that stores the riddle in which the user is and don't allow the user to skip a riddle without being unnoticed.
System to record when a user decides to skip a riddle.
Update punctuation system to include when a user skips a riddle.

## Technologies used
- Python version 3 with following main modules: Flask, Requests and unittest 
- Github to store repository
- Github to deplay project

## Testing
Manual testing for most common user functionality.
Automatic testing for some of the functions used in the app, see below:
  - The index.html page is rendered when GET request is executed
  - Returns the username when POST request is executed in the index.html page
  - Usernames are added correctly and are unique
  - The riddle.html is rendered when GET request is executed
  - The read_riddles function reads a sample of riddles correctly
  - The app redirects the user to the Leaderboard when all riddles are completed
  - The leaderboard.html page is rendered when GET request is executed
  - The Score is updated correctly when we add two incorrect and one correct answer
 
