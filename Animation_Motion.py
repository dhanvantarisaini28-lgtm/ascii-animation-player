"""
animations_motion.py
---------------------
Animations built around moving an object frame by frame: Bouncing Ball,
Loading Spinner, Bouncing Text.
"""

from renderer import render_frame


def animation_bouncing_ball():
    """A ball that bounces inside a box, simply reversing direction
    whenever it hits a wall or the floor.
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
