#!/usr/bin/env python3
"""
main.py
-------
Entry point for the ASCII Art Animation Player.

Builds the main menu from MENU_OPTIONS, reads and validates the user's
choice, and dispatches to the matching animation function. This file
only handles the menu/control flow -- the animations themselves live in
the animations_*.py modules, and screen handling lives in renderer.py.
"""

import sys
import time

from renderer import clear_screen, run_animation
from animations_basic import (
    animation_blinking_eyes,
    animation_swimming_fish,
    animation_grass_wind,
)
from animations_motion import (
    animation_bouncing_ball,
    animation_loading_spinner,
    animation_bouncing_text,
)
from animations_random import (
    animation_rain,
    animation_fireworks,
    animation_starfield,
)
from animations_misc import (
    animation_ticking_clock,
    animation_countdown,
    animation_candle,
)

MENU_OPTIONS = [
    ("Blinking Eyes", animation_blinking_eyes),
    ("Swimming Fish", animation_swimming_fish),
    ("Grass Moving in the Wind", animation_grass_wind),
    ("Bouncing Ball", animation_bouncing_ball),
    ("Loading Spinner", animation_loading_spinner),
    ("Ticking Clock", animation_ticking_clock),
    ("Rain Falling", animation_rain),
    ("Fireworks", animation_fireworks),
    ("Bouncing Text (DVD-style)", animation_bouncing_text),
    ("Countdown Timer", animation_countdown),
    ("Starfield / Warp Speed", animation_starfield),
    ("Flickering Candle Flame", animation_candle),
]


def print_menu():
    clear_screen()
    print("=" * 40)
    print("   ASCII ART ANIMATION PLAYER")
    print("=" * 40)
    for idx, (name, _) in enumerate(MENU_OPTIONS, start=1):
        print(f"  {idx}. {name}")
    print("  0. Quit")
    print("=" * 40)


def parse_choice(raw, max_option):
    """Validate a raw menu input string and turn it into an int.

    Pulled out of main() as its own function so it can be tested in
    isolation (see test_validation.py) without needing to run the whole
    interactive menu loop.

    Returns the choice as an int if `raw` is a non-negative whole number
    between 0 and max_option (inclusive); otherwise returns None.
    """
    if not raw.isdigit():
        return None
    choice = int(raw)
    if 0 <= choice <= max_option:
        return choice
    return None


def main():
    while True:  # main menu loop -- keeps running until the user quits
        print_menu()
        raw_choice = input("Select an animation (0-{}): ".format(len(MENU_OPTIONS)))

        choice = parse_choice(raw_choice, len(MENU_OPTIONS))

        if choice is None:
            print("Please enter a valid number from the menu.")
            time.sleep(1)
            continue

        if choice == 0:
            clear_screen()
            print("Goodbye!")
            sys.exit(0)
        else:
            _, func = MENU_OPTIONS[choice - 1]
            run_animation(func)  # play the animation, then return here


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Goodbye!")
        sys.exit(0)
