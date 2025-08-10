"""
Enhanced Hangman Game for CodeAlpha Internship
Features:
- Word categories (Animals, Fruits, Countries)
- Difficulty levels (Easy, Medium, Hard)
- Hint system
- Score tracking
- Improved ASCII art
- Comprehensive input validation
"""

import random
from collections import defaultdict

# Word database by category and difficulty
WORDS = {
    'animals': {
        'easy': ['cat', 'dog', 'fish', 'bird', 'frog'],
        'medium': ['tiger', 'zebra', 'panda', 'hippo', 'koala'],
        'hard': ['chameleon', 'kangaroo', 'rhinoceros', 'platypus', 'peacock']
    },
    'fruits': {
        'easy': ['apple', 'pear', 'kiwi', 'grape', 'mango'],
        'medium': ['banana', 'orange', 'cherry', 'peach', 'melon'],
        'hard': ['pomegranate', 'dragonfruit', 'persimmon', 'boysenberry', 'starfruit']
    },
    'countries': {
        'easy': ['usa', 'uk', 'canada', 'japan', 'italy'],
        'medium': ['brazil', 'germany', 'russia', 'france', 'spain'],
        'hard': ['azerbaijan', 'kazakhstan', 'mozambique', 'turkmenistan', 'kyrgyzstan']
    }
}

# Enhanced ASCII art for hangman
HANGMAN_ART = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

def select_category():
    """Let player select a word category"""
    print("\nSelect a category:")
    for i, category in enumerate(WORDS.keys(), 1):
        print(f"{i}. {category.capitalize()}")
    
    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(WORDS):
                return list(WORDS.keys())[choice-1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def select_difficulty():
    """Let player select difficulty level"""
    print("\nSelect difficulty:")
    print("1. Easy (4-5 letters)")
    print("2. Medium (6-7 letters)")
    print("3. Hard (8+ letters)")
    
    while True:
        try:
            choice = int(input("Enter difficulty level (1-3): "))
            if 1 <= choice <= 3:
                return ['easy', 'medium', 'hard'][choice-1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def get_hint(secret_word, guessed_letters):
    """Provide a hint by revealing an unrevealed letter"""
    unrevealed = [letter for letter in secret_word if letter not in guessed_letters]
    if unrevealed:
        return random.choice(unrevealed)
    return None

def display_game_state(secret_word, guessed_letters, incorrect_guesses, attempts_left, score, hints_remaining):
    """Display current game state"""
    print(HANGMAN_ART[len(incorrect_guesses)])
    print(f"\nCategory: {category.capitalize()} | Difficulty: {difficulty.capitalize()}")
    print(f"Score: {score} | Hints remaining: {hints_remaining}")
    print(f"\nWord: {' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses) if incorrect_guesses else 'None'}")
    print(f"Attempts left: {attempts_left}")

def hangman_game():
    """Main game function"""
    global category, difficulty
    
    # Game setup
    category = select_category()
    difficulty = select_difficulty()
    secret_word = random.choice(WORDS[category][difficulty]).lower()
    guessed_letters = set()
    incorrect_guesses = set()
    attempts_left = 6
    hints_remaining = 2
    score = 0
    hint_used = False
    
    print("\nWelcome to Enhanced Hangman!")
    print(f"Guess the {difficulty} {category} word. You have {attempts_left} attempts.")
    print("Type 'hint' for a hint (2 available per game)")
    
    while attempts_left > 0:
        display_game_state(secret_word, guessed_letters, incorrect_guesses, attempts_left, score, hints_remaining)
        
        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            score += attempts_left * 10  # Bonus points for remaining attempts
            if not hint_used:
                score += 20  # Bonus for no hints used
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print(f"Your final score: {score}")
            return score
        
        # Get player input
        while True:
            guess = input("\nGuess a letter (or 'hint'): ").lower()
            
            if guess == 'hint':
                if hints_remaining > 0:
                    hint = get_hint(secret_word, guessed_letters)
                    if hint:
                        hints_remaining -= 1
                        hint_used = True
                        score -= 5  # Small penalty for using hint
                        print(f"Hint: The word contains the letter '{hint}'")
                        break
                    else:
                        print("No more letters to reveal!")
                else:
                    print("No hints remaining!")
                continue
            
            if len(guess) != 1:
                print("Please enter a single letter.")
                continue
            
            if not guess.isalpha():
                print("Please enter a valid letter (a-z).")
                continue
            
            if guess in guessed_letters or guess in incorrect_guesses:
                print("You've already guessed that letter.")
                continue
            
            break  # Valid input
        
        # Process guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
            score += 5  # Points for correct guess
        else:
            incorrect_guesses.add(guess)
            attempts_left -= 1
            print(f"Incorrect! {attempts_left} attempts remaining.")
    
    # Game over
    print(HANGMAN_ART[6])  # Full hangman
    print(f"\nGame over! The word was: {secret_word}")
    print(f"Your final score: {score}")
    return score

def main():
    """Main program loop with score tracking"""
    total_score = 0
    games_played = 0
    
    print("=== ENHANCED HANGMAN GAME ===")
    print("Features: Categories | Difficulty Levels | Hints | Scoring")
    
    while True:
        game_score = hangman_game()
        total_score += game_score
        games_played += 1
        
        # Game statistics
        print(f"\nGames Played: {games_played} | Total Score: {total_score}")
        print(f"Average Score: {total_score/games_played:.1f}")
        
        # Play again prompt
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Statistics:")
            print(f"Total Games: {games_played}")
            print(f"Total Score: {total_score}")
            print(f"Average Score: {total_score/games_played:.1f}")
            break

if __name__ == "__main__":
    main()