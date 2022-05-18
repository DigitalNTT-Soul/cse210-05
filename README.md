# Jumper
"There are old skydivers and bold skydivers, but there are no old, bold skydivers." - Jeff Wuorio 

---
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. Guess the correct letters of the secret word before all of the lines of the parachute are cut!


## Getting Started
---

Make sure you have Python 3.10.4 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command.

```
python3 jumper
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hilo folder and click the "run" button.

There are some rules to this game and are listed as follows:

- The secret word is randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- The player guesses if the next one will be higher or lower.
- If the guess is incorrect, a line is cut on the player's parachute
- If the puzzle is solved the game is over. You landed safely on the ground!
- If the player has no more parachute, well, the game is over. Its a pretty long way to the ground...


The goal of the game is to guess the secret word before you run out of parachute.



## Project Structure
---
```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- game              (specific classes)
    +-- director.py     (director class script)
    +-- rules.py        (rules class script)
    +-- ui.py           (ui class script)
    +-- word_list.py    (word_list class script)
    +-- word_list.txt   (raw text file of words, for easy editing)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
Python 3.10.4

## Authors
---
* Dylan Ruppell (ruppelld@byui.edu) (github: DigitalNTT-Soul): Program design
* Austin Donovan (iskarr9g@gmail.com) (github: lskarr): ASCII Parachute Design, Parachute Class, Parachute guy function
* Matt Pellét (mattpellet@byui.edu) (github: m4j0rCSE): Word list, README
* Larry Brys (bry21010@byui.edu) (github: ljbrys)