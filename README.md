# Invasion
A small alien invasion clone made in python using pygame. 
Based off Python Crash Course by Eric Matthes

Quick note: File paths for images may not be set correctly. 
* When running on VSCode use: `pygame.image.load("alien_invasion/images/<FILENAME.png>")`
* When running from terminal use: `pygame.image.load("images/<FILENAME.png>")`

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
