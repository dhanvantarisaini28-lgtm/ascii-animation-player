"""
animations_random.py
---------------------
Procedural animations driven mainly by the `random` module: Rain Falling,
Fireworks, Starfield.
"""

import math
import random

from renderer import render_frame


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
                rad = math.radians(angle)
                px = center_x + int(radius * math.cos(rad))
                py = peak_y + int(radius * math.sin(rad) / 2)
                if 0 <= px < width and 0 <= py < height:
                    grid[py][px] = random.choice(["*", "+", "."])
            lines = ["".join(r) for r in grid]
            scene = "     FIREWORKS\n\n" + "\n".join(lines)
            render_frame(scene, 0.1)


def animation_starfield():
    """Stars that appear to fly toward the viewer: each star has a
    column and a "distance" that shrinks each frame, so it drifts and
    accelerates across the screen, mimicking a warp/star-trek effect.
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
