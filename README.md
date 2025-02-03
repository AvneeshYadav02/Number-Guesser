# Guess the Number Game

A simple Python game where the player tries to guess a randomly generated number between 1 and 100. The game gives feedback on whether the guess is too high or too low, and the player has a limited number of attempts based on their chosen difficulty level.

## Game Features

- **Difficulty Levels**: 
  - 1: 2 lives (for experienced players)
  - 2: 5 lives (for intermediate players)
  - 3: 10 lives (for beginners)

- **Feedback on Guess**:
  - "Too Low" or "Too High" when the guess is far from the number.
  - "Low" or "High" when the guess is close to the number but not correct.
  - "YOU GUESSED IT 👏👏👏👏 !!" when the guess is correct.

## How to Play

1. Choose your difficulty level by typing:
   - `1` for 2 lives
   - `2` for 5 lives
   - `3` for 10 lives
2. Guess the number between 1 and 100.
3. Receive feedback on your guess and adjust accordingly.
4. If you guess the number correctly, you win the game!
5. If you run out of lives, the game ends, and you are shown the correct number.

## How to Run the Game

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Run the Python script in your terminal:

   ```bash
   python3 guess_the_number.py
