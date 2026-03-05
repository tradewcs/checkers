# Checkers

A Python implementation of the classic board game *Checkers* (also known as Draughts).

> **Work in Progress:** This project is actively being developed. Core game logic and mechanics are still under construction. Contributions and feedback are welcome!

## Features

- Player vs. player engine
- Board initialization and piece setup
- Support for basic moves and captures (coming soon)

## Current Status

The project currently includes the ability to initialize and display the game board. A sample starting position looks like:

```
. ○ . ○ . ○ . ○ 
○ . ○ . ○ . ○ . 
. ○ . ○ . ○ . ○ 
# . # . # . # . 
. # . # . # . # 
● . ● . ● . ● . 
. ● . ● . ● . ● 
● . ● . ● . ● . 
```

Pieces are represented as:

- `○` – light pieces (typically one player)
- `●` – dark pieces (the opposing player)
- `#` – dark squares where pieces may move
- `.` – empty light squares

## Getting Started

To run or experiment with the code:

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd checkers
   ```
2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # if requirements file exists
   ```
3. **Run the main program:**
   ```bash
   python main.py
   ```

## Contributing

This project is under active development. If you'd like to help, please open an issue or submit a pull request. Early contributions are especially valuable to shape the architecture and feature set.
