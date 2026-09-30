"""One-off asset pipeline: resize avatar, compress CV, generate og:image cards.
Run with: .tools/venv/Scripts/python.exe .tools/optimize_assets.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "static" / "img"
OG = IMG / "og"
OG.mkdir(exist_ok=True)

# ── 1. Resize the 357KB avatar to the size it renders at (96px, retina 2x) ──
src = Image.open(IMG / "profile.jpg").convert("RGB")
if src.width > 400:
    side = min(src.size)
    left = (src.width - side) // 2
    top = (src.height - side) // 2
    avatar = src.crop((left, top, left + side, top + side)).resize((400, 400), Image.LANCZOS)
    avatar.save(IMG / "profile.jpg", "JPEG", quality=85, optimize=True, progressive=True)
    print(f"avatar: {avatar.size}, saved")
else:
    print(f"avatar already sized: {src.size}, skipped")

# ── 2. Shared OG card background (1200x630, site palette, subtle grid) ──
W, H = 1200, 630
BG = (11, 13, 18)
CARD = (20, 24, 38)
GRID = (34, 40, 54)
ACCENT = (94, 234, 212)
TEXT_HI = (236, 238, 244)
TEXT_LO = (139, 147, 165)


def base_canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 72):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 72):
        d.line([(0, y), (W, y)], fill=GRID, width=1)
    # accent glow, top center
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W // 2 - 300, -180, W // 2 + 300, 180], fill=38)
    accent_layer = Image.new("RGB", (W, H), ACCENT)
    img = Image.composite(accent_layer, img, glow)
    d = ImageDraw.Draw(img)
    d.rectangle([56, 56, W - 56, H - 56], outline=GRID, width=2)
    return img, d


def font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        return ImageFont.load_default()


FONTS = ROOT / "static" / "fonts"
MONO = FONTS / "jbmono-400.woff2"
MONO_B = FONTS / "jbmono-600.woff2"
INTER = FONTS / "inter-400.woff2"
INTER_B = FONTS / "inter-600.woff2"

# ── 3. Site-wide card ──
img, d = base_canvas()
d.text((88, 150), "~/martin.dev", font=font(MONO_B, 34), fill=ACCENT)
d.text((88, 210), "Martin Kiuna", font=font(INTER_B, 64), fill=TEXT_HI)
d.text((88, 300), "Software Engineer", font=font(INTER_B, 40), fill=ACCENT)
d.text((88, 380), "ML-driven trading systems · autonomous threat detection",
       font=font(INTER, 26), fill=TEXT_LO)
d.text((88, 424), "Django & FastAPI backends", font=font(INTER, 26), fill=TEXT_LO)
d.text((88, 520), "Nairobi, Kenya · github.com/RasMatoh",
       font=font(MONO, 22), fill=TEXT_LO)
img.save(OG / "og-site.png", "PNG", optimize=True)
print("og-site.png written")

# ── 4. Per-project cards (import data.py directly — pure python, no Django) ──
import importlib.util
spec = importlib.util.spec_from_file_location("portfolio_data", ROOT / "core" / "data.py")
portfolio_data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(portfolio_data)

for p in portfolio_data.PROJECTS:
    img, d = base_canvas()
    d.text((88, 120), "~/martin.dev — case study", font=font(MONO_B, 26), fill=ACCENT)
    # word-wrap the title
    words, lines, cur = p["title"].split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if d.textlength(trial, font=font(INTER_B, 52)) > W - 200 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    lines.append(cur)
    y = 190
    for line in lines[:2]:
        d.text((88, y), line, font=font(INTER_B, 52), fill=TEXT_HI)
        y += 68
    # category + stack chips
    d.text((88, y + 30), " · ".join(p["categories"]).upper(),
           font=font(MONO_B, 24), fill=ACCENT)
    stack = "  ".join(p["stack"][:5])
    d.text((88, H - 150), stack, font=font(MONO, 24), fill=TEXT_LO)
    d.text((88, H - 105), p["impact"][:90], font=font(INTER, 22), fill=TEXT_LO)
    img.save(OG / f"{p['id']}.png", "PNG", optimize=True)
    print(f"{p['id']}.png written")
