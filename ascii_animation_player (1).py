#!/usr/bin/env python3
"""
ASCII Art Animation Player
---------------------------
A menu-driven, terminal-only animation player.

Design notes:
- Each animation is a self-contained function.
- Frames are stored as strings (or generated procedurally) in lists/loops.
- The "movement" illusion is created by the classic loop:
      clear screen -> print a frame -> sleep -> repeat
- Only the standard library is used: os, time, random, sys.
- Every animation can be stopped early with Ctrl+C, which returns
  control to the main menu instead of crashing the program.
"""

import os
import time
import random
import sys

# --------------------------------------------------------------------------
# Screen helpers
# --------------------------------------------------------------------------

def clear_screen():
    """Clear the terminal. Uses 'cls' on Windows, 'clear' on Unix-like OSes."""
    os.system('cls' if os.name == 'nt' else 'clear')


def render_frame(frame_text, delay):
    """Clear the screen, print one frame, then pause briefly.

    This single function is the heartbeat of every animation below:
    each loop iteration calls this once per "tick" of the animation.
    """
    clear_screen()
    print(frame_text)
    time.sleep(delay)


def wait_for_enter(message="Press Enter to return to the menu..."):
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


# --------------------------------------------------------------------------
# 1. Blinking Eyes
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 2. Swimming Fish
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 3. Grass Moving in the Wind
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 4. Bouncing Ball
# --------------------------------------------------------------------------

def animation_bouncing_ball():
    """A ball that bounces inside a box, losing a bit of energy visually
    by simply reversing direction whenever it hits a wall or the floor.
    """
    width, height = 40, 12
    x, y = 5, 2
    dx, dy = 1, 1

    for _ in range(150):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        grid[y][x] = "O"

        border_top = "+" + "-" * width + "+"
        lines = [border_top]
        for row in grid:
            lines.append("|" + "".join(row) + "|")
        lines.append(border_top)

        scene = "     BOUNCING BALL\n\n" + "\n".join(lines)
        render_frame(scene, 0.03)

        x += dx
        y += dy
        if x <= 0 or x >= width - 1:
            dx *= -1
        if y <= 0 or y >= height - 1:
            dy *= -1


# --------------------------------------------------------------------------
# 5. Loading Spinner
# --------------------------------------------------------------------------

def animation_loading_spinner():
    """A classic rotating '|/-\\' spinner next to a progress percentage."""
    spinner_frames = ["|", "/", "-", "\\"]
    for step in range(100):
        spin_char = spinner_frames[step % len(spinner_frames)]
        percent = min(step + 1, 100)
        bar_filled = int(percent / 100 * 30)
        bar = "#" * bar_filled + "-" * (30 - bar_filled)
        scene = (
            "     LOADING SPINNER\n\n"
            f"    Loading {spin_char}\n"
            f"    [{bar}] {percent}%"
        )
        render_frame(scene, 0.05)


# --------------------------------------------------------------------------
# 6. Ticking Clock
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 7. Rain Falling
# --------------------------------------------------------------------------

def animation_rain():
    """Rain drops falling down the screen, each column independently
    tracking its own drop position using random start times.
    """
    width, height = 50, 15
    num_drops = 20

    # Each drop is [column, row]; start rows are randomized and negative
    # so drops enter the screen at staggered times.
    drops = [[random.randint(0, width - 1), random.randint(-height, 0)]
             for _ in range(num_drops)]

    for _ in range(100):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        for drop in drops:
            col, row = drop
            if 0 <= row < height:
                grid[row][col] = "|"
            drop[1] += 1
            if drop[1] >= height:
                drop[0] = random.randint(0, width - 1)
                drop[1] = random.randint(-5, 0)

        lines = ["".join(row) for row in grid]
        scene = "     RAIN FALLING\n\n" + "\n".join(lines)
        render_frame(scene, 0.08)


# --------------------------------------------------------------------------
# 8. Fireworks
# --------------------------------------------------------------------------

def animation_fireworks():
    """A simple firework: a '|' rises, then explodes into a ring of '*'
    particles that expand outward and fade after a few frames.
    """
    width, height = 40, 16

    for burst in range(4):
        center_x = random.randint(10, width - 10)
        peak_y = random.randint(3, 6)

        # Rising phase: a single trail character climbs upward
        for row in range(height - 1, peak_y, -1):
            grid = [[" " for _ in range(width)] for _ in range(height)]
            grid[row][center_x] = "|"
            lines = ["".join(r) for r in grid]
            scene = "     FIREWORKS\n\n" + "\n".join(lines)
            render_frame(scene, 0.03)

        # Explosion phase: a ring of particles expands outward
        for radius in range(1, 6):
            grid = [[" " for _ in range(width)] for _ in range(height)]
            for angle in range(0, 360, 30):
                import math
                rad = math.radians(angle)
                px = center_x + int(radius * math.cos(rad))
                py = peak_y + int(radius * math.sin(rad) / 2)
                if 0 <= px < width and 0 <= py < height:
                    grid[py][px] = random.choice(["*", "+", "."])
            lines = ["".join(r) for r in grid]
            scene = "     FIREWORKS\n\n" + "\n".join(lines)
            render_frame(scene, 0.1)


# --------------------------------------------------------------------------
# 9. Bouncing "DVD Logo" Text
# --------------------------------------------------------------------------

def animation_bouncing_text():
    """Classic bouncing-logo effect, but with a text label instead of a
    logo image -- bounces diagonally around the screen, changing
    "color" (represented by swapping brackets) each time it hits a wall.
    """
    label = "PYTHON"
    width, height = 60, 18
    x, y = 5, 5
    dx, dy = 1, 1
    styles = ["[ {} ]", "< {} >", "( {} )", "{{ {} }}"]
    style_index = 0

    for _ in range(150):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        text = styles[style_index].format(label)
        for i, ch in enumerate(text):
            if 0 <= x + i < width:
                grid[y][x + i] = ch

        lines = ["".join(row) for row in grid]
        scene = "   BOUNCING TEXT\n\n" + "\n".join(lines)
        render_frame(scene, 0.04)

        x += dx
        y += dy
        hit_wall = False
        if x <= 0 or x + len(text) >= width:
            dx *= -1
            hit_wall = True
        if y <= 0 or y >= height - 1:
            dy *= -1
            hit_wall = True
        if hit_wall:
            style_index = (style_index + 1) % len(styles)


# --------------------------------------------------------------------------
# 10. Progress Bar Countdown
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 11. Starfield (warp-speed effect)
# --------------------------------------------------------------------------

def animation_starfield():
    """Stars that appear to fly toward the viewer: each star has a
    column and a "distance" that shrinks each frame, so it drifts and
    accelerates toward the center-ish, mimicking a warp/star-trek effect.
    """
    width, height = 60, 18
    num_stars = 40

    stars = []
    for _ in range(num_stars):
        stars.append({
            "col": random.randint(0, width - 1),
            "row": random.randint(0, height - 1),
            "speed": random.choice([1, 1, 2]),
        })

    chars_by_speed = {1: ".", 2: "*"}

    for _ in range(120):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        for star in stars:
            col, row = star["col"], star["row"]
            if 0 <= row < height and 0 <= col < width:
                grid[row][col] = chars_by_speed.get(star["speed"], ".")
            star["col"] -= star["speed"]
            if star["col"] < 0:
                star["col"] = width - 1
                star["row"] = random.randint(0, height - 1)

        lines = ["".join(row) for row in grid]
        scene = "     STARFIELD\n\n" + "\n".join(lines)
        render_frame(scene, 0.05)


# --------------------------------------------------------------------------
# 12. Flickering Candle Flame
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# Main Menu
# --------------------------------------------------------------------------

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
    print(f"  0. Quit")
    print("=" * 40)


def main():
    while True:  # main menu loop -- keeps running until the user quits
        print_menu()
        choice = input("Select an animation (0-{}): ".format(len(MENU_OPTIONS)))

        # Validate input: must be a number within the valid menu range
        if not choice.isdigit():
            print("Please enter a valid number.")
            time.sleep(1)
            continue

        choice = int(choice)

        if choice == 0:
            clear_screen()
            print("Goodbye!")
            sys.exit(0)
        elif 1 <= choice <= len(MENU_OPTIONS):
            _, func = MENU_OPTIONS[choice - 1]
            run_animation(func)  # play the animation, then return here
        else:
            print("Invalid choice. Please pick a number from the menu.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Goodbye!")
        sys.exit(0)
