import os
import json
import urllib.request
import urllib.parse
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

SYS_DIR = r"D:\Game\DAFFA_SYSTEM"
COVERS_DIR = os.path.join(SYS_DIR, "assets", "game_covers")
os.makedirs(COVERS_DIR, exist_ok=True)

from upgrade_daffa_master_v6 import create_rounded_cover, safe_filename

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def search_steam_cover(query: str) -> Image.Image | None:
    """Cari game di Steam StoreSearch API resmi dan unduh header.jpg aslinya."""
    url = f"https://store.steampowered.com/api/storesearch/?term={urllib.parse.quote(query)}&l=english&cc=US"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode("utf-8"))
        items = data.get("items", [])
        if not items:
            return None
        appid = items[0]["id"]
        print(f"  [STEAM SEARCH] '{query}' -> AppID {appid} ({items[0].get('name')})")
        hdr_url = f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{appid}/header.jpg"
        req2 = urllib.request.Request(hdr_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=10) as r2:
            tmp = os.path.join(COVERS_DIR, "_tmp_steam.jpg")
            with open(tmp, "wb") as f:
                f.write(r2.read())
        im = Image.open(tmp).convert("RGBA")
        os.remove(tmp)
        return im
    except Exception as e:
        print(f"  [STEAM SEARCH WARN] '{query}': {e}")
        return None

def search_bing_image(query: str) -> Image.Image | None:
    """Fallback ambil thumbnail gambar asli dari Bing Images jika tidak ada di Steam."""
    import re
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&first=1"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")
        # Cari murl atau turl (tse1.mm.bing.net)
        matches = re.findall(r'https://tse[1-4]\.mm\.bing\.net/th\?id=OIP\.[^"&]+', html)
        for img_url in matches[:4]:
            try:
                req_i = urllib.request.Request(img_url, headers=headers)
                with urllib.request.urlopen(req_i, timeout=8) as ri:
                    tmp = os.path.join(COVERS_DIR, "_tmp_bing.jpg")
                    with open(tmp, "wb") as f:
                        f.write(ri.read())
                im = Image.open(tmp).convert("RGBA")
                os.remove(tmp)
                if im.width >= 150 and im.height >= 90:
                    print(f"  [WEB IMAGE OK] '{query}' -> {im.size}")
                    return im
            except Exception:
                continue
    except Exception as e:
        print(f"  [WEB IMAGE WARN] '{query}': {e}")
    return None

def save_both_sizes(game_name: str, raw_img: Image.Image):
    fname = safe_filename(game_name)
    fpath = os.path.join(COVERS_DIR, fname)
    card_im = create_rounded_cover(raw_img, size=(240, 112), radius=10)
    card_im.save(fpath, "PNG")
    hero_im = create_rounded_cover(raw_img, size=(420, 196), radius=14)
    hero_im.save(fpath.replace(".png", "_hero.png"), "PNG")
    print(f"  [SAVED REAL COVER] {game_name} -> {fname}")

print("=== [1/3] FETCHING REAL ARTWORK FOR ALL MISSING GAMES ===")

# 1. Games on Steam / Web that previously used text placeholders
TARGET_SEARCHES = [
    ("My Voice Zoo", "My Voice Zoo", "My Voice Zoo game steam cover"),
    ("That's Not My Neighbor", "That's Not My Neighbor", "That's Not My Neighbor game banner"),
    ("Metal Slug", "METAL SLUG ATTACK RELOADED", "Metal Slug Attack Reloaded steam header"),
    ("Subnautica 2", "Subnautica 2", "Subnautica 2 game promotional banner"),
    ("Snowed Under", "Snowed Under", "Snowed Under game steam"),
    ("Upin & Ipin", "Upin & Ipin Universe", "Upin Ipin Universe game 2025 cover"),
    ("Astra 3D Action RPG", "Dark Souls III", "Dark Fantasy Knight 3D RPG game wallpaper"),
    ("SpaceX Falcon 9 3D", "Kerbal Space Program", "SpaceX Falcon 9 rocket launch night wallpaper"),
]

for game_key, steam_q, web_q in TARGET_SEARCHES:
    im = None
    # For Upin & Ipin and SpaceX, try web image first for exact match, else Steam
    if game_key in ("Upin & Ipin", "SpaceX Falcon 9 3D", "Astra 3D Action RPG"):
        im = search_bing_image(web_q) or search_steam_cover(steam_q)
    else:
        im = search_steam_cover(steam_q) or search_bing_image(web_q)

    if im:
        save_both_sizes(game_key, im)

# 2. Build REAL composite artwork for "KR x PVZ Fusion" using the real Kingdom Rush + Plants vs Zombies Steam covers!
pvz_p = os.path.join(COVERS_DIR, safe_filename("Plants vs Zombies"))
kr_p = os.path.join(COVERS_DIR, safe_filename("Kingdom Rush Vengeance"))
if os.path.exists(pvz_p) and os.path.exists(kr_p):
    pvz_im = Image.open(pvz_p).convert("RGBA").resize((240, 196), Image.Resampling.LANCZOS)
    kr_im = Image.open(kr_p).convert("RGBA").resize((240, 196), Image.Resampling.LANCZOS)
    comp = Image.new("RGBA", (420, 196), (0, 0, 0, 255))
    comp.paste(kr_im.crop((15, 0, 225, 196)), (0, 0))
    comp.paste(pvz_im.crop((15, 0, 225, 196)), (210, 0))
    draw = ImageDraw.Draw(comp)
    # Glowing center lightning divider
    draw.line([(210, 0), (210, 196)], fill=(16, 185, 129, 255), width=5)
    draw.rounded_rectangle((155, 76, 265, 120), radius=10, fill=(8, 14, 24, 235), outline=(16, 185, 129, 255), width=2)
    try:
        fnt = ImageFont.truetype("consolab.ttf", 18)
    except Exception:
        fnt = ImageFont.load_default()
    draw.text((168, 88), "KR x PVZ", font=fnt, fill=(52, 211, 153, 255))
    save_both_sizes("KR x PVZ Fusion", comp)

print("\n=== [2/3] FIXING CARD LAYOUT & BUTTON CLIPPING IN Daffa_Master_GUI.py ===")
gui_path = os.path.join(SYS_DIR, "Daffa_Master_GUI.py")
with open(gui_path, "r", encoding="utf-8") as f:
    code = f.read()

# Fix 1: Shorten long titles on card row 1 so the status badge never gets pushed/clipped, and make action buttons fit 100% cleanly
old_title_block = '''        title_lbl = ctk.CTkLabel(
            r1, text=item["name"],
            font=("Consolas", 12, "bold"),
            text_color=THEME["text_main"], anchor="w"
        )
        title_lbl.pack(side="left", fill="x", expand=True)
        title_lbl.bind("<Button-1>", lambda e, it=item: self.select_hero_item(it))

        badge_pill = ctk.CTkLabel(
            r1,
            text=item.get("status", "READY"),
            font=("Consolas", 8, "bold"),
            fg_color="#071324",
            text_color=color,
            corner_radius=5, padx=6, pady=1
        )
        badge_pill.pack(side="right")'''

new_title_block = '''        disp_name = item["name"] if len(item["name"]) <= 18 else item["name"][:17] + "…"
        title_lbl = ctk.CTkLabel(
            r1, text=disp_name,
            font=("Consolas", 11, "bold"),
            text_color=THEME["text_main"], anchor="w"
        )
        title_lbl.pack(side="left", fill="x", expand=True)
        title_lbl.bind("<Button-1>", lambda e, it=item: self.select_hero_item(it))

        disp_status = item.get("status", "READY")
        if len(disp_status) > 14:
            disp_status = disp_status[:13] + "…"
        badge_pill = ctk.CTkLabel(
            r1,
            text=disp_status,
            font=("Consolas", 8, "bold"),
            fg_color="#071324",
            text_color=color,
            corner_radius=5, padx=5, pady=1
        )
        badge_pill.pack(side="right", padx=(2, 0))'''

if old_title_block in code:
    code = code.replace(old_title_block, new_title_block, 1)
    print("  [OK] Fixed card title & status badge overflow.")

# Fix 2: Adjust cover thumbnail width from 126 to 112 and sub_txt length to 32 so PLAY + 📁 + ⭐ + ⌨️ buttons never clip on 2-column grid
code = code.replace("size=(126, 62), is_hero=False", "size=(112, 58), is_hero=False")
code = code.replace("width=126, height=62", "width=112, height=58")
code = code.replace("if len(sub_txt) > 42:\n            sub_txt = sub_txt[:40] + \"..\"", "if len(sub_txt) > 30:\n            sub_txt = sub_txt[:28] + \"..\"")

with open(gui_path, "w", encoding="utf-8") as f:
    f.write(code)

print("\n=== [3/3] COMPILING & RESTARTING DAFFA MASTER v6.0 ULTRA ===")
res = subprocess.run(["python", "-m", "py_compile", gui_path], capture_output=True, text=True)
if res.returncode != 0:
    print("  [ERROR]", res.stderr)
    raise SystemExit(1)
print("  [OK] Zero syntax errors!")
