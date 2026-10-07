import os
import time
import random
import sys
import math


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def render_frame(frame_text, delay):
    clear_screen()
    print(frame_text)
    time.sleep(delay)


def wait_for_enter(message="Press Enter to return to the menu..."):
    try:
        input(message)
    except KeyboardInterrupt:
        pass


def run_animation(func):
    try:
        func()
    except KeyboardInterrupt:
        print("\n(Animation interrupted.)")
    wait_for_enter()


# ---------------------------------------------------------
# 1. BLINKING EYES
# ---------------------------------------------------------

def animation_blinking_eyes():
    eyes_open = r"""
   O   O
     ^
  \___/
"""

    eyes_closed = r"""
   -   -
     ^
  \___/
"""

    frames = [
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_closed, 0.15),
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_open, 0.6),
        (eyes_closed, 0.15),
    ]

    for _ in range(4):
        for frame, delay in frames:
            render_frame(frame, delay)


# ---------------------------------------------------------
# 2. SWIMMING FISH
# ---------------------------------------------------------

def animation_swimming_fish():
    fish_right = "><(((('>"
    fish_left = "<')))>"
    width = 60
    water_line = "~" * width

    position = 0
    direction = 1

    for _ in range(width * 2):
        fish_art = fish_right if direction == 1 else fish_left

        padding = " " * position

        scene = (
            "        SWIMMING FISH\n\n"
            f"{water_line}\n"
            f"{padding}{fish_art}\n"
            f"{water_line}\n"
        )

        render_frame(scene, 0.05)

        position += direction

        if position >= width - len(fish_art):
            direction = -1
        elif position <= 0:
            direction = 1


# ---------------------------------------------------------
# 3. GRASS MOVING IN THE WIND
# ---------------------------------------------------------

def animation_grass_wind():

    field_width = 50
    num_rows = 6

    blade_state = [0] * field_width

    for _ in range(80):

        gust_direction = random.choice([-1, 1])

        for i in range(field_width):
            if random.random() < 0.3:
                blade_state[i] = gust_direction
            elif random.random() < 0.1:
                blade_state[i] = 0

        char_map = {
            -1: "\\",
            0: "|",
            1: "/"
        }

        row = "".join(
            char_map[blade_state[i]]
            for i in range(field_width)
        )

        scene_lines = ["   GRASS IN THE WIND\n"]

        for _ in range(num_rows):
            scene_lines.append(row)

        scene = "\n".join(scene_lines)

        render_frame(scene, 0.1)


# ---------------------------------------------------------
# 4. BOUNCING BALL
# ---------------------------------------------------------

def animation_bouncing_ball():

    width, height = 40, 12

    x, y = 5, 2
    dx, dy = 1, 1

    for _ in range(150):

        grid = [
            [" " for _ in range(width)]
            for _ in range(height)
        ]

        grid[y][x] = "O"

        border_top = "+" + "-" * width + "+"

        lines = [border_top]

        for row in grid:
            lines.append("|" + "".join(row) + "|")

        lines.append(border_top)

        scene = (
            "     BOUNCING BALL\n\n"
            + "\n".join(lines)
        )

        render_frame(scene, 0.03)

        x += dx
        y += dy

        if x <= 0 or x >= width - 1:
            dx *= -1

        if y <= 0 or y >= height - 1:
            dy *= -1


# ---------------------------------------------------------
# 5. LOADING SPINNER
# ---------------------------------------------------------

def animation_loading_spinner():

    spinner_frames = ["|", "/", "-", "\\"]

    for step in range(100):

        spin_char = spinner_frames[
            step % len(spinner_frames)
        ]

        percent = step + 1

        bar_filled = int(
            percent / 100 * 30
        )

        bar = (
            "#" * bar_filled
            + "-" * (30 - bar_filled)
        )

        scene = (
            "     LOADING SPINNER\n\n"
            f"    Loading {spin_char}\n"
            f"    [{bar}] {percent}%"
        )

        render_frame(scene, 0.05)


# ---------------------------------------------------------
# 6. TICKING CLOCK
# ---------------------------------------------------------

def animation_ticking_clock():

    positions = [
        (0, -2),
        (1, -2),
        (2, -1),
        (2, 0),
        (2, 1),
        (1, 2),
        (0, 2),
        (-1, 2),
        (-2, 1),
        (-2, 0),
        (-2, -1),
        (-1, -2)
    ]

    def build_face(hand_index):

        size = 5

        grid = [
            [" " for _ in range(size * 2 + 1)]
            for _ in range(size * 2 + 1)
        ]

        center = size

        # Clock marks
        for i in range(12):
            dx, dy = positions[i]
            grid[
                center + dy
            ][
                center + dx
            ] = "*"

        # Clock hand
        hdx, hdy = positions[hand_index]

        grid[center][center] = "+"

        grid[
            center + hdy // 2
        ][
            center + hdx // 2
        ] = "o"

        lines = [
            "".join(row)
            for row in grid
        ]

        return "\n".join(lines)

    for tick in range(36):

        hand_index = tick % 12

        face = build_face(hand_index)

        scene = (
            "     TICKING CLOCK\n\n"
            + face
            + f"\n\n      Tick {tick + 1}"
        )

        render_frame(scene, 0.2)


# ---------------------------------------------------------
# 7. RAIN FALLING
# ---------------------------------------------------------

def animation_rain():

    width, height = 50, 15
    num_drops = 20

    drops = [
        [
            random.randint(0, width - 1),
            random.randint(-height, 0)
        ]
        for _ in range(num_drops)
    ]

    for _ in range(100):

        grid = [
            [" " for _ in range(width)]
            for _ in range(height)
        ]

        for drop in drops:

            col, row = drop

            if 0 <= row < height:
                grid[row][col] = "|"

            drop[1] += 1

            if drop[1] >= height:
                drop[0] = random.randint(
                    0, width - 1
                )

                drop[1] = random.randint(-5, 0)

        lines = [
            "".join(row)
            for row in grid
        ]

        scene = (
            "     RAIN FALLING\n\n"
            + "\n".join(lines)
        )

        render_frame(scene, 0.08)


# ---------------------------------------------------------
# 8. FIREWORKS
# ---------------------------------------------------------

def animation_fireworks():

    width, height = 40, 16

    for _ in range(4):

        center_x = random.randint(
            10, width - 10
        )

        peak_y = random.randint(3, 6)

        # Rocket going upward
        for row in range(
            height - 1,
            peak_y,
            -1
        ):

            grid = [
                [" " for _ in range(width)]
                for _ in range(height)
            ]

            grid[row][center_x] = "|"

            lines = [
                "".join(r)
                for r in grid
            ]

            scene = (
                "     FIREWORKS\n\n"
                + "\n".join(lines)
            )

            render_frame(scene, 0.03)

        # Explosion
        for radius in range(1, 6):

            grid = [
                [" " for _ in range(width)]
                for _ in range(height)
            ]

            for angle in range(0, 360, 30):

                rad = math.radians(angle)

                px = (
                    center_x
                    + int(
                        radius
                        * math.cos(rad)
                    )
                )

                py = (
                    peak_y
                    + int(
                        radius
                        * math.sin(rad)
                        / 2
                    )
                )

                if (
                    0 <= px < width
                    and 0 <= py < height
                ):
                    grid[py][px] = random.choice(
                        ["*", "+", "."]
                    )

            lines = [
                "".join(r)
                for r in grid
            ]

            scene = (
                "     FIREWORKS\n\n"
                + "\n".join(lines)
            )

            render_frame(scene, 0.1)


# ---------------------------------------------------------
# 9. BOUNCING TEXT
# ---------------------------------------------------------

def animation_bouncing_text():

    label = "PYTHON"

    width, height = 60, 18

    x, y = 5, 5
    dx, dy = 1, 1

    styles = [
        "[ {} ]",
        "< {} >",
        "( {} )",
        "{{ {} }}"
    ]

    style_index = 0

    for _ in range(150):

        grid = [
            [" " for _ in range(width)]
            for _ in range(height)
        ]

        text = styles[
            style_index
        ].format(label)

        for i, ch in enumerate(text):

            if 0 <= x + i < width:
                grid[y][x + i] = ch

        lines = [
            "".join(row)
            for row in grid
        ]

        scene = (
            "   BOUNCING TEXT\n\n"
            + "\n".join(lines)
        )

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
            style_index = (
                style_index + 1
            ) % len(styles)


# ---------------------------------------------------------
# 10. COUNTDOWN TIMER
# ---------------------------------------------------------

def animation_countdown():

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
            "#  ##  #  #  ",
            "#   #  #  #  ",
            " ####  ####  ",
        ],
    }

    for key in [
        "5",
        "4",
        "3",
        "2",
        "1",
        "GO"
    ]:

        art_lines = digit_art[key]

        scene = (
            "     COUNTDOWN\n\n"
            + "\n".join(art_lines)
        )

        render_frame(scene, 0.8)


# ---------------------------------------------------------
# 11. STARFIELD
# ---------------------------------------------------------

def animation_starfield():

    width, height = 60, 18
    num_stars = 40

    stars = []

    for _ in range(num_stars):

        stars.append({
            "col": random.randint(
                0, width - 1
            ),

            "row": random.randint(
                0, height - 1
            ),

            "speed": random.choice(
                [1, 1, 2]
            ),
        })

    chars_by_speed = {
        1: ".",
        2: "*"
    }

    for _ in range(120):

        grid = [
            [" " for _ in range(width)]
            for _ in range(height)
        ]

        for star in stars:

            col = star["col"]
            row = star["row"]

            if (
                0 <= row < height
                and 0 <= col < width
            ):
                grid[row][col] = (
                    chars_by_speed.get(
                        star["speed"],
                        "."
                    )
                )

            star["col"] -= star["speed"]

            if star["col"] < 0:

                star["col"] = width - 1

                star["row"] = random.randint(
                    0, height - 1
                )

        lines = [
            "".join(row)
            for row in grid
        ]

        scene = (
            "     STARFIELD\n\n"
            + "\n".join(lines)
        )

        render_frame(scene, 0.05)


# ---------------------------------------------------------
# 12. FLICKERING CANDLE
# ---------------------------------------------------------

def animation_candle():

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

        flame = random.choice(
            flame_shapes
        )

        scene_lines = (
            ["      CANDLE FLAME\n", flame]
            + candle_body
        )

        scene = "\n".join(scene_lines)

        render_frame(scene, 0.15)


# ---------------------------------------------------------
# MENU
# ---------------------------------------------------------

MENU_OPTIONS = [

    (
        "Blinking Eyes",
        animation_blinking_eyes
    ),

    (
        "Swimming Fish",
        animation_swimming_fish
    ),

    (
        "Grass Moving in the Wind",
        animation_grass_wind
    ),

    (
        "Bouncing Ball",
        animation_bouncing_ball
    ),

    (
        "Loading Spinner",
        animation_loading_spinner
    ),

    (
        "Ticking Clock",
        animation_ticking_clock
    ),

    (
        "Rain Falling",
        animation_rain
    ),

    (
        "Fireworks",
        animation_fireworks
    ),

    (
        "Bouncing Text (DVD-style)",
        animation_bouncing_text
    ),

    (
        "Countdown Timer",
        animation_countdown
    ),

    (
        "Starfield / Warp Speed",
        animation_starfield
    ),

    (
        "Flickering Candle Flame",
        animation_candle
    ),
]


# ---------------------------------------------------------
# PRINT MENU
# ---------------------------------------------------------

def print_menu():

    clear_screen()

    print("=" * 40)
    print("   ASCII ART ANIMATION PLAYER")
    print("=" * 40)

    for idx, (name, _) in enumerate(
        MENU_OPTIONS,
        start=1
    ):
        print(f"  {idx}. {name}")

    print("  0. Quit")
    print("=" * 40)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    while True:

        print_menu()

        choice = input(
            f"Select an animation "
            f"(0-{len(MENU_OPTIONS)}): "
        ).strip()

        if not choice.isdigit():

            print("Please enter a valid number.")
            time.sleep(1)
            continue

        choice = int(choice)

        if choice == 0:

            clear_screen()
            print("Goodbye!")
            sys.exit(0)

        if 1 <= choice <= len(MENU_OPTIONS):

            _, func = MENU_OPTIONS[
                choice - 1
            ]

            run_animation(func)

        else:

            print(
                "Invalid choice. "
                "Please pick a number from the menu."
            )

            time.sleep(1)


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        clear_screen()
        print("Goodbye!")
        sys.exit(0)
