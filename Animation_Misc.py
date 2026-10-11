"""
animations_misc.py
-------------------
The remaining animations: Ticking Clock, Countdown Timer, Flickering
Candle Flame.
"""

import random

from renderer import render_frame


def animation_ticking_clock():
    """A simple analog-style clock face where the 'hand' rotates through
    12 positions, one tick per frame, using a dictionary that maps each
    hour position to a pre-drawn face.
    """
    # Map hand position (0-11, like clock hours) to the character used
    # at each of the 12 positions around a text clock face.
    positions = [
        (0, -2), (1, -2), (2, -1), (2, 0), (2, 1), (1, 2),
        (0, 2), (-1, 2), (-2, 1), (-2, 0), (-2, -1), (-1, -2)
    ]

    def build_face(hand_index):
        size = 5
        grid = [[" " for _ in range(size * 2 + 1)] for _ in range(size * 2 + 1)]
        center = size
        for i in range(12):
            dx, dy = positions[i]
            grid[center + dy][center + dx] = "*"
        # draw the hand from center toward the current hour position
        hdx, hdy = positions[hand_index]
        grid[center][center] = "+"
        grid[center + hdy // 2][center + hdx // 2] = "o"
        lines = ["".join(row) for row in grid]
        return "\n".join(lines)

    for tick in range(36):  # three full sweeps around the clock
        hand_index = tick % 12
        face = build_face(hand_index)
        scene = "     TICKING CLOCK\n\n" + face + f"\n\n      Tick {tick + 1}"
        render_frame(scene, 0.2)


def animation_countdown():
    """A large ASCII countdown from 5 to 'GO!' using a dictionary that
    maps each digit/word to its multi-line ASCII-art block.
    """
    digit_art = {
        "5": [
            " ##### ",
            " #     ",
            " ##### ",
            "     # ",
            " ##### ",
        ],
        "4": [
            " #   # ",
            " #   # ",
            " ##### ",
            "     # ",
            "     # ",
        ],
        "3": [
            " ##### ",
            "     # ",
            "  #### ",
            "     # ",
            " ##### ",
        ],
        "2": [
            " ##### ",
            "     # ",
            " ##### ",
            " #     ",
            " ##### ",
        ],
        "1": [
            "   #   ",
            "  ##   ",
            "   #   ",
            "   #   ",
            " ##### ",
        ],
        "GO": [
            " ####  ####  ",
            "#    # #  #  ",
            "#  ## #  #  ",
            "#   # #  #  ",
            " ####  ####  ",
        ],
    }

    for key in ["5", "4", "3", "2", "1", "GO"]:
        art_lines = digit_art[key]
        scene = "     COUNTDOWN\n\n" + "\n".join(art_lines)
        render_frame(scene, 0.8)


def animation_candle():
    """A candle whose flame randomly picks between a few flame shapes
    each frame to simulate a natural flicker.
    """
    flame_shapes = [
        "  (  )  ",
        "  ( )   ",
        "   ( )  ",
        "  (())  ",
        "   ()   ",
    ]
    candle_body = [
        "  |  |  ",
        "  |  |  ",
        "  |  |  ",
        " ______ ",
    ]

    for _ in range(80):
        flame = random.choice(flame_shapes)
        scene_lines = ["      CANDLE FLAME\n", flame] + candle_body
        scene = "\n".join(scene_lines)
        render_frame(scene, 0.15)
