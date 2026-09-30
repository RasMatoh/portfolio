"""Generate per-project preview images for project cards/case studies.
Clean, abstract, in the site's design language — replace with real
screenshots anytime by dropping static/img/projects/<id>.png.
Run: .tools/venv/Scripts/python.exe .tools/gen_previews.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import importlib.util

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "img" / "projects"
OUT.mkdir(exist_ok=True)

W, H = 1200, 630
BG = (11, 13, 18)
CARD = (20, 24, 38)
GRID = (34, 40, 54)
ACCENT = (94, 234, 212)
ACCENT_DIM = (94, 234, 212, 90)
TEXT_LO = (139, 147, 165)

spec = importlib.util.spec_from_file_location("portfolio_data", ROOT / "core" / "data.py")
data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data)

MONO = ROOT / "static" / "fonts" / "jbmono-400.woff2"


def font(size):
    try:
        return ImageFont.truetype(str(MONO), size)
    except OSError:
        return ImageFont.load_default()


def canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 72):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 72):
        d.line([(0, y), (W, y)], fill=GRID, width=1)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W // 2 - 340, -200, W // 2 + 340, 200], fill=30)
    img = Image.composite(Image.new("RGB", (W, H), ACCENT), img, glow)
    d = ImageDraw.Draw(img, "RGBA")
    return img, d


def motif_trading(d, seed):
    """Deterministic candlestick chart."""
    x = 120
    price = 380
    hi, lo = 150, 480
    for i in range(18):
        step = ((seed * 37 + i * 91) % 100) / 100
        body_h = 24 + int(step * 70)
        up = (seed + i) % 2 == 0
        o = price
        c = max(lo, min(hi, o - body_h if up else o + body_h))
        top, bot = min(o, c), max(o, c)
        wick_top = max(hi, top - 26)
        wick_bot = min(lo, bot + 26)
        color = (*ACCENT, 230) if up else (148, 163, 184, 160)
        d.line([(x + 18, wick_top), (x + 18, wick_bot)], fill=color, width=2)
        d.rectangle([x, top, x + 36, bot], fill=color)
        price = c
        x += 54
        if x > W - 120:
            break


def motif_ai(d, seed):
    """Layered neural-network nodes with connections."""
    layers = [[(300, 150), (300, 315), (300, 480)],
              [(560, 90), (560, 230), (560, 400), (560, 540)],
              [(820, 180), (820, 350), (820, 500)],
              [(1020, 300)]]
    for a in layers:
        for b in layers:
            if layers.index(b) == layers.index(a) + 1:
                for p in a:
                    for q in b:
                        d.line([p, q], fill=(94, 234, 212, 28), width=1)
    for li, layer in enumerate(layers):
        for p in layer:
            r = 10 if li < 3 else 16
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r],
                      fill=(20, 24, 38, 255), outline=(*ACCENT, 220), width=2)


def motif_security(d, seed):
    """Radar sweep with contacts."""
    cx, cy = W // 2, H // 2
    for r in (90, 170, 250):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(94, 234, 212, 60), width=2)
    d.line([(cx - 270, cy), (cx + 270, cy)], fill=(94, 234, 212, 40), width=1)
    d.line([(cx, cy - 270), (cx, cy + 270)], fill=(94, 234, 212, 40), width=1)
    sweep_end = (cx + int(250 * ((seed % 6) + 2) / 8 * 0.92), cy - int(250 * 0.82))
    d.line([(cx, cy), sweep_end], fill=(*ACCENT, 200), width=3)
    contacts = [(cx + 120, cy - 90), (cx - 150, cy + 70), (cx + 60, cy + 170), (cx - 80, cy - 180)]
    for i, (x, y) in enumerate(contacts):
        on = (seed + i) % 2 == 0
        d.ellipse([x - 7, y - 7, x + 7, y + 7],
                  fill=(*ACCENT, 235) if on else (148, 163, 184, 120))


def motif_web(d, seed):
    """Abstract browser chrome with content blocks."""
    d.rounded_rectangle([220, 120, 980, 510], radius=14, outline=(94, 234, 212, 190), width=3)
    d.line([(220, 190), (980, 190)], fill=(94, 234, 212, 190), width=3)
    for i, x in enumerate((252, 290, 328)):
        d.ellipse([x, 142, x + 22, 164], outline=(94, 234, 212, 160), width=2)
    d.rounded_rectangle([700, 136, 950, 170], radius=8, outline=(148, 163, 184, 120), width=2)
    d.rectangle([260, 230, 560, 268], fill=(94, 234, 212, 70))
    d.rectangle([260, 296, 620, 320], fill=(148, 163, 184, 60))
    d.rectangle([260, 336, 580, 360], fill=(148, 163, 184, 60))
    d.rounded_rectangle([660, 296, 940, 460], radius=10, outline=(94, 234, 212, 90), width=2)
    for row in range(3):
        for col in range(3):
            x, y = 700 + col * 76, 330 + row * 40
            d.rectangle([x, y, x + 56, y + 22], fill=(94, 234, 212, 45))


MOTIFS = {'trading': motif_trading, 'ai': motif_ai, 'ml': motif_ai,
          'security': motif_security, 'web': motif_web}


def seed_from(pid):
    return sum(ord(c) for c in pid)


for p in data.PROJECTS:
    img, d = canvas()
    motif = next((MOTIFS[c] for c in p['categories'] if c in MOTIFS), motif_web)
    motif(d, seed_from(p['id']))
    d.text((56, H - 72), f"~/projects/{p['id']}", font=font(24), fill=(*TEXT_LO, 220))
    img.save(OUT / f"{p['id']}.png", "PNG", optimize=True)
    print(f"{p['id']}.png")
