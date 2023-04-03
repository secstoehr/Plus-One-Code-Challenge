# Plus-One-Code-Challenge
Author: Shannon Stoehr

Email: secstoehr@gmail.com

GitHub: https://github.com/secstoehr

This program allows a user to play tic tac toe against another person using the same terminal interface or the computer.

Users can play on square boards from 3x3 up to 10x10.

A win is considered a straight, uninterrupted line that spans the full length of the board in either a row, column, or diagonally from corner to opposite corner.

The program commands in the appropriate directory are:

~$ python3 SStoehr_TTT.py (test | play)

- The test option will run tests on the program.
- The play option will allow the user to play the game.

X always goes first.

To make a move, players will select a space using row,column as input (no spaces).

Rows and columns are numbered like a 2-dimensional array, so...

- The top left square is 0,0, and the rest of a 3x3 board would look like:

0,0 | 0,1 | 0,2

---+----+----

1,0 | 1,1 | 1,2

---+----+----

2,0 | 2,1 | 2,2

The player's board and opponent options will be chosen by the user before the game starts.

Currently the computer player is not very smart, it will play available spaces from left to right, top to bottom.

I hope to update the computer player in future work to allow the user to select computer difficulty options, with the current iteration as the "easy" difficulty.

Thanks for playing!
