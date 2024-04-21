# Word Guess

Word Guess is a Python terminal game which runs in a mock terminal on Heroku. Users score points by correctly guessing the hidden random word. 

[Here is the live version of my project.](https://mwbark-word-guess-07e0e1567ada.herokuapp.com/)

## How to Play

A random word is generated and displayed as empty blank spaces.

Users can then guess the word outright or guess individual letters within the word.

Correct letter guesses update the empty blank spaces at the correct letter’s positions in the word.

Letter guesses and incorrect word guesses cost 1 life point.

Life points equal to the length of the random word are generated for each new word (e.g. 5 points for a 5-letter word).

Users have to guess the word before their life points reach 0, at which point a new game will start.

A successful word guess scores the user 1 point. 

## Features

### Existing features

- Random word generation
- Word checker
  - checks random words only contain english alphabet characters
- Empty letter space generation
- User letter or word guess input
- Guess validator
  - checks user word guess length is equal to the length of the random word
  - checks whether the user's guess contains only lowercase English alphabet characters
- Letter guess updater
  - successful letter guesses are added to the empty letter spaces
  - unsuccessful guesses are added to a 'doesn't contain' list
- Life points
- Current score and high score

### Future Features

- Difficulty levels
- Word scramble game option - where the random words are scrambled instead of hidden
- Word of the day 
- User classes to keep track of player info

## Data Model

## Testing

I have manually tested this project by doing the following:

## Bugs

### Solved Bugs

- 'doesn't contain' list didn't reset on successful word guess as i forgot to add 'doesnt_contain = []' in the correct place.

### Unfixed Bugs

- No bugs remaining.

## Deployment

This project was deployed using a mock terminal in Heroku.

- Steps for deployment:
  - Create new Heroku app
  - Add config vars in Heroku settings
  - Set the buildbacks to 'Python' and 'NodeJS' in that order
  - Link the Heroku app to the repository
  - Click on 'Deploy'

## Credits

-  vaibhavsingh97 for the imports [here]()
-  Wordnik for the generate words. Link below.

[<img src="assets/images/wordnik_badge_b1.png">](https://wordnik.com/)
