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
python ascii_animation_player.py
```

Then pick an option from the menu (1-12), or enter `0` to quit. Press `Ctrl+C` at any time during an animation to return to the menu.

## Project Structure

```
ascii_animation_player.py   # Main program: menu loop + all animation functions
README.md                   # This file
```

## Sample Output

```
<img width="262" height="140" alt="Screenshot 2026-09-30 093926" src="https://github.com/user-attachments/assets/4afacbf0-ed9c-4397-91bd-0a0613651683" />
<img width="221" height="140" alt="Screenshot 2026-09-30 093857" src="https://github.com/user-attachments/assets/b50268ec-2fd3-4c9a-8645-3f32d4934ca2" />


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

