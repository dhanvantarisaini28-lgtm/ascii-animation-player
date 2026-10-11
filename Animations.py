"""
animations_basic.py
--------------------
Simple animations: Blinking Eyes, Swimming Fish, Grass in the Wind.
"""

import random

from renderer import render_frame


def animation_blinking_eyes():
    """A pair of ASCII eyes that periodically close and open.

    Two hand-drawn frames (open / closed) are stored in a list and we
    just alternate between them, holding the "open" state longer than
    the "closed" state so the blink reads as a quick flick rather than
    a slow fade.
    """
    eyes_open = r"""
        BLINKING EYES

           _____       _____
          /     \     /     \
         | O   O |   | O   O |
          \_____/     \_____/

    """
    eyes_closed = r"""
        BLINKING EYES

           _____       _____
          /     \     /     \
         |-------|   |-------|
          \_____/     \_____/

    """
    # Sequence of (frame, hold-time) pairs -- most frames are "open",
    # with a brief "closed" frame inserted every few cycles.
    frames = [
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_closed, 0.15),
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_closed, 0.15),
    ]
    for _ in range(4):  # play the whole blink cycle 4 times
        for frame, delay in frames:
            render_frame(frame, delay)


def animation_swimming_fish():
    """A fish made of text characters that swims left to right and back.

    The trick is simple string padding: we build a line that is
    `left_padding + fish_art + right content`, and change the amount
    of left padding each frame to slide the fish across the terminal.
    """
    fish_right = "><(((('>"
    fish_left = "<')))><"
    width = 60          # how wide our "pond" is
    water_line = "~" * width

    position = 0
    direction = 1  # 1 = moving right, -1 = moving left

    for _ in range(width * 2):  # swim across and back
        if direction == 1:
            fish_art = fish_right
        else:
            fish_art = fish_left

        padding = " " * position
        # Build the scene: water above, fish in the middle, water below
        scene = (
            "        SWIMMING FISH\n\n"
            f"{water_line}\n"
            f"{padding}{fish_art}\n"
            f"{water_line}\n"
        )
        render_frame(scene, 0.05)

        position += direction
        # Bounce off the edges of the pond
        if position >= width - len(fish_art):
            direction = -1
        elif position <= 0:
            direction = 1


def animation_grass_wind():
    """A field of grass that sways using randomly chosen lean characters.

    Each blade of grass is represented by one of three characters
    ('|', '/', '\\') representing "upright", "leaning right" and
    "leaning left". Every frame, we randomly nudge each blade's state
    a little so the whole field appears to ripple like wind blowing
    across it, rather than flickering with pure noise.
    """
    field_width = 50
    num_rows = 6

    # blade_state[i] tracks the current lean of blade i: -1, 0, or 1
    blade_state = [0] * field_width

    for _ in range(80):  # number of wind gusts to animate
        # Randomly nudge a handful of blades toward a lean direction,
        # and let neighboring blades drift toward similar states so
        # gusts look like they ripple across the field.
        gust_direction = random.choice([-1, 1])
        for i in range(field_width):
            if random.random() < 0.3:
                blade_state[i] = gust_direction
            elif random.random() < 0.1:
                blade_state[i] = 0

        char_map = {-1: "\\", 0: "|", 1: "/"}
        row = "".join(char_map[blade_state[i]] for i in range(field_width))

        scene_lines = ["   GRASS IN THE WIND\n"]
        # Draw several rows so it looks like a field, not a single line
        for r in range(num_rows):
            scene_lines.append(row)
        scene = "\n".join(scene_lines)

        render_frame(scene, 0.1)
