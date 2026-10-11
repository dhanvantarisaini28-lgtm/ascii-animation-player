"""
renderer.py
-----------
Shared screen-handling helpers used by every animation.

Keeping this logic in one module means the clear-screen / print-frame /
sleep pattern, and the Ctrl+C safety net, only need to be written once
and are reused by all twelve animations.
"""

import os
import time


def clear_screen():
    """Clear the terminal. Uses 'cls' on Windows, 'clear' on Unix-like OSes."""
    os.system('cls' if os.name == 'nt' else 'clear')


def render_frame(frame_text, delay):
    """Clear the screen, print one frame, then pause briefly.

    This single function is the heartbeat of every animation: each loop
    iteration in an animation function calls this once per "tick".
    """
    clear_screen()
    print(frame_text)
    time.sleep(delay)


def wait_for_enter(message="Press Enter to return to the menu..."):
    """Pause until the user presses Enter, without crashing on Ctrl+C."""
    try:
        input(message)
    except KeyboardInterrupt:
        pass


def run_animation(func):
    """Wrapper that lets the user bail out of any animation with Ctrl+C
    and land safely back at the main menu, instead of killing the program.
    """
    try:
        func()
    except KeyboardInterrupt:
        print("\n(Animation interrupted.)")
    wait_for_enter()
