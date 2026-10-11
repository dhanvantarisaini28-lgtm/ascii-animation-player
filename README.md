# ASCII Art Animation Player

A menu-driven, terminal-based animation player written in pure Python. It creates the illusion of movement using nothing but `os`, `time`, and `random` from the standard library — no external graphics libraries required.

## Features

- Simple numbered menu with 12 animations + Quit option
- Runs entirely in the terminal (Windows, macOS, Linux)
- No external dependencies — standard library only
- Graceful handling of invalid input and Ctrl+C interrupts

### Animations included

1. Blinking Eyes
2. Swimming Fish
3. Grass Moving in the Wind
4. Bouncing Ball
5. Loading Spinner
6. Ticking Clock
7. Rain Falling
8. Fireworks
9. Bouncing Text (DVD-style)
10. Countdown Timer
11. Starfield / Warp Speed
12. Flickering Candle Flame

## Requirements

- Python 3.x (no additional packages needed)

## How to Run

```bash
python main.py
```

Then pick an option from the menu (1-12), or enter `0` to quit. Press `Ctrl+C` at any time during an animation to return to the menu.

## Instructions for Testing

A small unit test suite covers the menu input-validation logic (`parse_choice` in `main.py`):

```bash
python -m unittest test_validation.py -v
```

These tests also run fine with `pytest` if you have it installed.

## Project Structure

```
main.py                 # Entry point: menu loop, input validation, dispatch
renderer.py              # Shared screen helpers (clear_screen, render_frame, wait_for_enter, run_animation)
animations_basic.py      # Blinking Eyes, Swimming Fish, Grass in the Wind
animations_motion.py     # Bouncing Ball, Loading Spinner, Bouncing Text
animations_random.py     # Rain Falling, Fireworks, Starfield
animations_misc.py       # Ticking Clock, Countdown Timer, Candle Flame
test_validation.py       # Unit tests for input validation
README.md                # This file
statement.md             # Problem statement, scope, target users, features
```

## Sample Output

```
(Paste a sample run of the program here, e.g. the main menu or a frame from an animation)
```

## Tech Stack

- Python 3
- Standard library modules: `os`, `time`, `random`, `sys`

## Author

Dhanvantari Saini

## Course Info

Built for: Introduction to Problem Solving and Programming (CSE1021)
Faculty: Dr. Siddharth Singh Chouhan

## License

This project is for educational purposes.
