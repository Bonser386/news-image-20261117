"""Generate entry.png: one-image summary of world news, Tuesday 17 Nov 2026.
Deterministic, stdlib + Pillow only, run locally to build the repo image.
Sources (checked 18 Nov 2026): Just Security Early Edition 17 Nov 2026;
Hansen Intel / PBS NewsHour; NPR News Now 17 Nov; ASAS Press digest 17 Nov.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 244, 230)
INK = (24, 28, 44)
RED = (178, 34, 34)
NAVY = (18, 42, 86)
TEAL = (14, 110, 110)
GOLD = (184, 134, 11)
GREY = (90, 90, 96)

def font(size, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p, size)

def wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines

PANELS = [
    ("1  MIDDLE EAST", "IRAN FIRES DRONES AT US RADAR IN BAHRAIN",
     "Third Iranian strike on US targets in Bahrain in days. Bahrain says the drones were intercepted; no casualties or damage reported.", RED, "drone"),
    ("2  UKRAINE WAR", "UKRAINE HITS THE CRIMEA BRIDGE",
     "Kyiv says its strike severely damaged the Kerch Bridge to Crimea. Moscow hit bridges in Kyiv in reply.", NAVY, "bridge"),
    ("3  ASIA SUMMIT", "TRUMP IN ASIA FOR NUCLEAR TALKS",
     "Trump lands in Manila for ASEAN, then heads to Shenzhen for a Nov 19 trilateral with Xi Jinping and Putin on nuclear risk and Ukraine.", TEAL, "summit"),
    ("4  EUROPE", "ESTONIA TO SHUT ITS RUSSIAN BORDER",
     "All border crossings with Russia close from 1 Dec after Estonia blamed Moscow for a foiled arson plot on a drone plant.", GOLD, "border"),
    ("5  ASIA-PACIFIC", "JAPAN SCRAMBLES JETS ON RUSSIA",
     "Tokyo launches fighter jets and protests after two suspected Russian aircraft violate Japanese airspace.", NAVY, "jet"),
    ("6  YEMEN / SAUDI", "HOUTHIS STRIKE SAUDI OIL PIPELINE",
     "Houthis say they launched drones at Saudi Arabia's East-West oil pipeline as they push toward Aden.", RED, "pipe"),
]

def icon(d, kind, x, y, c):
    if kind == "drone":
        d.ellipse([x, y, x+54, y+30], outline=c, width=4)
        d.line([x+8, y+15, x-14, y+15], fill=c, width=4); d.line([x+46, y+15, x+68, y+15], fill=c, width=4)
        d.ellipse([x-22, y+8, x-6, y+22], outline=c, width=3); d.ellipse([x+60, y+8, x+76, y+22], outline=c, width=3)
        d.line([x+27, y+30, x+27, y+44], fill=c, width=3)
    elif kind == "bridge":
        d.arc([x, y-6, x+76, y+58], 180, 360, fill=c, width=5)
        for bx in (x+8, x+30, x+52):
            d.line([bx, y+26, bx, y+48], fill=c, width=3)
        d.line([x-4, y+48, x+80, y+48], fill=c, width=5)
    elif kind == "summit":
        for i, cx in enumerate((x+6, x+30, x+54)):
            d.ellipse([cx, y, cx+16, y+16], fill=c)
            d.polygon([(cx-2, y+20), (cx+18, y+20), (cx+8, y+48)], fill=c)
    elif kind == "border":
        d.rectangle([x, y+18, x+76, y+30], fill=c)
        d.line([x+10, y+30, x+10, y+50], fill=c, width=4); d.line([x+66, y+30, x+66, y+50], fill=c, width=4)
        d.line([x, y+50, x+76, y+50], fill=c, width=4)
    elif kind == "jet":
        d.polygon([(x, y+26), (x+76, y+14), (x+56, y+28), (x+76, y+42), (x, y+30)], fill=c)
    elif kind == "pipe":
        d.rectangle([x, y+14, x+76, y+30], fill=c)
        d.rectangle([x+18, y+30, x+30, y+50], fill=c); d.rectangle([x+48, y+30, x+60, y+50], fill=c)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
# Header
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((32, 22), "WORLD NEWS  •  IN ONE IMAGE", font=font(30, True), fill=(255, 255, 255))
d.text((32, 66), "TUESDAY 17 NOVEMBER 2026", font=font(44, True), fill=(255, 214, 90))
d.text((32, 118), "Six stories that defined the day", font=font(22), fill=(210, 220, 240))
d.rectangle([0, 148, W, 156], fill=RED)
# Panels 2 x 3
pw, ph, gx, gy = 480, 262, 16, 172
for i, (tag, head, body, col, kind) in enumerate(PANELS):
    x = gx + (i % 2) * (pw + 16)
    y = gy + (i // 2) * (ph + 16)
    d.rectangle([x, y, x+pw, y+ph], fill=(255, 255, 255), outline=(200, 190, 170), width=2)
    d.rectangle([x, y, x+pw, y+8], fill=col)
    d.text((x+18, y+20), tag, font=font(19, True), fill=col)
    icon(d, kind, x+pw-104, y+22, col)
    for j, line in enumerate(wrap(d, head, font(27, True), pw-36)):
        d.text((x+18, y+80+j*32), line, font=font(27, True), fill=INK)
    nlines = len(wrap(d, head, font(27, True), pw-36))
    for j, line in enumerate(wrap(d, body, font(20), pw-36)):
        d.text((x+18, y+86+nlines*32+j*26), line, font=font(20), fill=(52, 52, 58))
# Footer
d.rectangle([0, H-46, W, H], fill=NAVY)
d.text((32, H-36), "Sources: PBS NewsHour • Just Security • NPR — 17 Nov 2026", font=font(18), fill=(210, 220, 240))
img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
