# 🎮 Hangman Game - Python

A classic Hangman game built with Python, featuring word categories, difficulty levels, hints, and score tracking. Developed as part of the CodeAlpha Python Internship.

## ✨ Features

- **Word Categories**: Animals, Fruits, Countries
- **Difficulty Levels**: Easy (4-5 letters), Medium (6-7 letters), Hard (8+ letters)
- **Hint System**: Reveal one letter when stuck (2 hints/game)
- **Scoring**: Points for correct guesses, bonuses for remaining attempts
- **ASCII Art**: Visual hangman progression

## 🛠️ Tech Stack

- Python 3.x
- Built-in modules: `random`, `os`, `time`

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nagula-Lahari/CodeAlpha_HangmanGame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CodeAlpha_HangmanGame
   ```
3. Run the game:
   ```bash
   python hangman.py
   ```

## 🎯 How to Play

1. Select a word category and difficulty level
2. Guess letters one at a time
3. Use hints if needed (`type "hint"`)
4. Try to guess the word before the hangman is fully drawn!

## 📝 Code Structure

```
hangman.py
├── display_hangman()      # ASCII art generator
├── get_hint()            # Hint system logic
├── select_word()         # Word selection by category/difficulty
└── main_game_loop()      # Core gameplay
```

## 📊 Scoring System

| Action                | Points  |
|-----------------------|---------|
| Correct guess         | +5      |
| Using hint            | -5      |
| Winning (no hints)    | +20     |
| Remaining attempts    | +10 each|

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

## 📜 License

[MIT](LICENSE)

---

*Developed during the CodeAlpha Python Internship Program*  
[![CodeAlpha Badge](https://img.shields.io/badge/Internship-CodeAlpha-blue)](https://www.codealpha.tech)
```
