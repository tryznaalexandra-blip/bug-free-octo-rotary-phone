#!/usr/bin/env python3
"""Render MagicFuse email hero PNG with exact on-image copy."""
from __future__ import annotations

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 400

# Brand / reference palette
BG = (26, 26, 26)  # #1A1A1A
LAVENDER = (184, 194, 240)  # #B8C2F0 — accent headline
WHITE = (255, 255, 255)
CYAN_RING = (0, 174, 239)  # #00AEEF
BLUE_BOLT = (0, 85, 255)  # #0055FF
GRAY_TAG = (176, 176, 176)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load_font(path: str, size: int):
    return ImageFont.truetype(path, size)


def draw_lightning(draw: ImageDraw.ImageDraw, cx: int, cy: int, scale: float = 1.0) -> None:
    """Simple bolt matching SVG proportions, filled BLUE_BOLT."""
    s = scale
    pts = [
        (cx + 12 * s, cy + 0 * s),
        (cx + 2 * s, cy + 14 * s),
        (cx + 10 * s, cy + 14 * s),
        (cx + 6 * s, cy + 26 * s),
        (cx + 22 * s, cy + 10 * s),
        (cx + 14 * s, cy + 10 * s),
    ]
    draw.polygon(pts, fill=BLUE_BOLT)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line: list[str] = []
    for w in words:
        trial = " ".join(line + [w])
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Logo row
    draw_lightning(draw, 46, 38, scale=1.15)
    f_logo = load_font(FONT_BOLD, 26)
    draw.text((82, 34), "magicfuse", font=f_logo, fill=WHITE)
    f_tag = load_font(FONT_REG, 12)
    draw.text((82, 64), "Powered by TechMagic", font=f_tag, fill=GRAY_TAG)

    # Main heading (exact strings)
    y_head = 118
    f_head = load_font(FONT_BOLD, 44)
    x = 48
    s1 = "SALESFORCE"
    s2 = " ROADMAP"  # leading space before ROADMAP for spacing
    draw.text((x, y_head), s1, font=f_head, fill=LAVENDER)
    bb = draw.textbbox((x, y_head), s1, font=f_head)
    x_rm = bb[2] + 6
    draw.text((x_rm, y_head), s2.strip(), font=f_head, fill=WHITE)

    # Subhead — word wrap within content column (leave room for circle)
    sub = "Five shifts we see on healthy Salesforce programs"
    f_sub = load_font(FONT_REG, 23)
    max_text_w = 700
    lines = wrap_text(draw, sub, f_sub, max_text_w)
    y_sub = y_head + 58
    lh = int((draw.textbbox((0, 0), "Ag", font=f_sub)[3] - draw.textbbox((0, 0), "Ag", font=f_sub)[1]) * 1.25)
    for ln in lines:
        draw.text((48, y_sub), ln, font=f_sub, fill=WHITE)
        y_sub += lh

    # Decorative circle (right) — lavender fill, cyan stroke
    cx, cy = W - 205, H // 2
    r = 165
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=LAVENDER, outline=CYAN_RING, width=7)

    # Minimal “editorial” pencil across circle (nod to reference)
    py = cy + 25
    draw.rounded_rectangle((cx - 95, py, cx + 85, py + 10), radius=3, fill=(244, 208, 63))
    draw.rounded_rectangle((cx + 85, py - 2, cx + 96, py + 12), radius=2, fill=(248, 180, 196))

    out = "/workspace/magicfuse-email1-hero-banner-text.png"
    img.save(out, "PNG", optimize=True)
    print(out)


if __name__ == "__main__":
    main()
