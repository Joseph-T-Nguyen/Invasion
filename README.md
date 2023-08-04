# Invasion
A small alien invasion clone made in python using pygame. 
Based off Python Crash Course by Eric Matthes

To run the game make sure you have python 3 installed, and install the pygame library:

`pip install pygame` to install globally, or `python3 -m pip install -U pygame --user` 

Navigate into the `alien_invasion` folder. We can run the game by the command: `py alien.py`

NOTE: 
* Game is incomplete - as it is, it will continually loop over and over

TODOs: 
* Add getters/setters for each class 
* Add "start game" and "quit game" buttons when running in full-screen mode
* Reorganise game.py - too many functions/"God object" 

BUGs:
* Alien fleet not dynamically readjusting when playing in fullscreen - revisit calculation
* Speed of entire game increases as you destroy more aliens.

Images:
* ship_old.png: https://www.flaticon.com/free-icon/rocket_293581. 64px by 64px
* ship.png: https://www.flaticon.com/free-icon/space_2790389. 64px by 64px
* alien.png: https://www.flaticon.com/free-icon/ufo_3489943. 64px by 64px
