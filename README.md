# Hangman
A hangman game implemented in Python language



Hangman is a game where one player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, within a certain number of guesses. 

Here our second player is the computer which has a secret word in mind and the user is supposed to guess it.

The word to guess is represented by a row of dashes, representing each letter of the word.
If the player guesses a letter which exists in the word, the Python script writes it in all its correct positions and displays the word.
The player guessing the word may, at any time, attempt to guess the whole word. 
If the word is correct, the game is over and the user wins. 
Otherwise, if the guess is incorrect, the user loses a guess. 
A player is allowed at most 8 guesses per game.
If the user has used all his or her guesses, the game is over with the computer winning the game.

-----------------------------------------------------------------------------------------------------------
The project has been implemented in Python programming language using only two libraries - string and random.
