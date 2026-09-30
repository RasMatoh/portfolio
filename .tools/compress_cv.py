"""Compress the CV by re-rasterizing pages at moderate DPI.
Target: well under 300KB from the original 4MB.
Run: .tools/venv/Scripts/python.exe .tools/compress_cv.py
"""
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
CV = ROOT / "static" / "img" / "martin-kiuna-cv.pdf"
BACKUP = CV.with_suffix(".orig.pdf")

if not BACKUP.exists():
    BACKUP.write_bytes(CV.read_bytes())

src = pymupdf.open(BACKUP)
out = pymupdf.open()

DPI = 110  # sharp for screen reading; ~4x lighter than the original embeds
for page in src:
    pix = page.get_pixmap(dpi=DPI)
    jpeg = pix.tobytes("jpeg", jpg_quality=72)
    page_rect = page.rect
    new_page = out.new_page(width=page_rect.width, height=page_rect.height)
    new_page.insert_image(new_page.rect, stream=jpeg)

out.save(str(CV), garbage=4, deflate=True)
print(f"pages: {src.page_count} -> {out.page_count}")
print(f"{BACKUP.name}: {BACKUP.stat().st_size / 1024:.0f} KB -> {CV.stat().st_size / 1024:.0f} KB")
src.close()
out.close()
