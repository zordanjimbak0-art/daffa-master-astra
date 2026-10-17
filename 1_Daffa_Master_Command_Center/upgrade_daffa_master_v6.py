import os
import sys
import shutil
import subprocess
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SYS_DIR = r"D:\Game\DAFFA_SYSTEM"
ASSETS_DIR = os.path.join(SYS_DIR, "assets")
COVERS_DIR = os.path.join(ASSETS_DIR, "game_covers")
GH_UI_DIR = os.path.join(ASSETS_DIR, "github_ui")

os.makedirs(COVERS_DIR, exist_ok=True)
os.makedirs(GH_UI_DIR, exist_ok=True)

print("=== [1/4] CLONING GITHUB UI THEMES & ICON ASSETS ===")
ctk_themes_dir = os.path.join(GH_UI_DIR, "CTkThemesPack")
if not os.path.exists(ctk_themes_dir):
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/a13xe/CTkThemesPack.git", ctk_themes_dir],
            check=True,
            timeout=30
        )
        print(f"  [OK] Cloned GitHub CTkThemesPack -> {ctk_themes_dir}")
    except Exception as e:
        print(f"  [WARN] CTkThemesPack clone note: {e}")
else:
    print(f"  [CACHED] CTkThemesPack -> {ctk_themes_dir}")

# Copy RPG / Game UI icons from our cloned Quick_3D_RPG GitHub repo into D:\Game\DAFFA_SYSTEM\assets\github_ui\icons
gh_rpg_icons = r"D:\Game\DAFFA_GAMES\rpg_3d\assets\icons"
dest_icons = os.path.join(GH_UI_DIR, "icons")
os.makedirs(dest_icons, exist_ok=True)
if os.path.exists(gh_rpg_icons):
    for f in os.listdir(gh_rpg_icons):
        if f.lower().endswith((".png", ".jpg")):
            shutil.copy2(os.path.join(gh_rpg_icons, f), os.path.join(dest_icons, f))
    print(f"  [OK] Copied {len(os.listdir(dest_icons))} GitHub UI icons into {dest_icons}")

print("\n=== [2/4] DOWNLOADING HD GAME BOX ART / COVERS (STEAM CDN & GITHUB) ===")
STEAM_APPIDS = {
    "Cookie Clicker": "1454400",
    "Stardew Valley": "413150",
    "Project Zomboid": "108600",
    "Subnautica 1": "264710",
    "Subnautica Below Zero": "848450",
    "Terraria": "105600",
    "MC Dungeons": "1672970",
    "SpongeBob": "1282150",
    "Soulmask": "2646460",
    "Quake Remaster": "2310",
    "Metal Slug": "2322360",
    "Naruto UNS 4": "349040",
    "Naruto Revolution": "272510",
    "Postal 2": "223470",
    "Serious Sam 2": "204340",
    "Serious Sam TFE": "41050",
    "Albion Online": "761890",
    "Kingdom Rush Vengeance": "1367550",
    "Plants vs Zombies": "3590",
    "Graveyard Keeper 2": "599140",
    "Bloons TD 5": "306020",
    "Kingdom Rush": "246420",
    "Kingdom Rush Frontiers": "458710",
    "Kingdom Rush Origins": "816340",
    "DREDGE": "1562430",
    "Savage Planet": "973810",
    "Blasphemous": "774361",
    "Blasphemous 2": "2114740",
    "Binding of Isaac: Repentance": "250900",
}

def safe_filename(name: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in name).strip("_") + ".png"

def create_rounded_cover(img: Image.Image, size=(240, 112), radius=12, border_col=None) -> Image.Image:
    img = img.convert("RGBA")
    # Center crop to aspect ratio
    target_w, target_h = size
    src_w, src_h = img.size
    scale = max(target_w / src_w, target_h / src_h)
    nw, nh = int(src_w * scale), int(src_h * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - target_w) // 2
    top = (nh - target_h) // 2
    img = img.crop((left, top, left + target_w, top + target_h))

    # Add subtle bottom dark vignette for contrast
    overlay = Image.new("RGBA", size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(target_h // 2, target_h):
        alpha = int(150 * ((y - target_h // 2) / (target_h // 2)))
        odraw.line([(0, y), (target_w, y)], fill=(6, 10, 18, alpha))
    img = Image.alpha_composite(img, overlay)

    # Rounded mask
    mask = Image.new("L", size, 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle((0, 0, target_w - 1, target_h - 1), radius=radius, fill=255)

    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)

    if border_col:
        bdraw = ImageDraw.Draw(out)
        bdraw.rounded_rectangle((0, 0, target_w - 1, target_h - 1), radius=radius, outline=border_col, width=2)
    return out

def generate_cyber_cover(title: str, subtitle: str, accent_hex: str, size=(240, 112)) -> Image.Image:
    w, h = size
    accent_hex = accent_hex.lstrip("#")
    ar, ag, ab = int(accent_hex[0:2], 16), int(accent_hex[2:4], 16), int(accent_hex[4:6], 16)

    img = Image.new("RGBA", size, (10, 16, 28, 255))
    draw = ImageDraw.Draw(img)

    # Gradient & cyber grid
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(8 + ar * 0.28 * (1 - t))
        g = int(14 + ag * 0.28 * (1 - t))
        b = int(26 + ab * 0.28 * (1 - t))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    for gx in range(0, w, 24):
        draw.line([(gx, 0), (gx, h)], fill=(ar, ag, ab, 28), width=1)
    for gy in range(0, h, 24):
        draw.line([(0, gy), (w, gy)], fill=(ar, ag, ab, 28), width=1)

    # Glowing diagonal cyber stripes
    draw.polygon([(w - 70, 0), (w, 0), (w, 70)], fill=(ar, ag, ab, 65))
    draw.line([(0, h - 3), (w, h - 3)], fill=(ar, ag, ab, 220), width=3)

    try:
        f_title = ImageFont.truetype("consolab.ttf", 18)
        f_sub = ImageFont.truetype("consola.ttf", 11)
    except Exception:
        f_title = ImageFont.load_default()
        f_sub = ImageFont.load_default()

    # Title text with shadow
    short_title = title[:20].upper()
    draw.text((15, 34), short_title, font=f_title, fill=(0, 0, 0, 220))
    draw.text((14, 33), short_title, font=f_title, fill=(248, 250, 252, 255))

    draw.text((14, 58), subtitle[:28].upper(), font=f_sub, fill=(ar, ag, ab, 255))
    draw.text((14, 12), "ASTRA // EDITION", font=f_sub, fill=(148, 163, 184, 200))

    return create_rounded_cover(img, size=size, radius=10, border_col=(ar, ag, ab, 180))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for game_name, appid in STEAM_APPIDS.items():
    fname = safe_filename(game_name)
    fpath = os.path.join(COVERS_DIR, fname)
    if not os.path.exists(fpath):
        url = f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{appid}/header.jpg"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw_path = fpath + ".raw.jpg"
                with open(raw_path, "wb") as f:
                    f.write(resp.read())
            im = Image.open(raw_path)
            rounded = create_rounded_cover(im, size=(240, 112), radius=10)
            rounded.save(fpath, "PNG")
            # Also save a large hero banner version (460x215)
            hero = create_rounded_cover(im, size=(420, 196), radius=14)
            hero.save(fpath.replace(".png", "_hero.png"), "PNG")
            os.remove(raw_path)
            print(f"  [STEAM ART OK] {game_name} -> {fname}")
        except Exception as e:
            print(f"  [FALLBACK ART] {game_name}: {e}")

# Custom / Non-Steam / Special Games Cover Art
CUSTOM_GAMES = [
    ("My Voice Zoo", "VOICE ZOO TYCOON • MOD", "#00E5FF"),
    ("Astra 3D Action RPG", "FIRST-PERSON PBR RPG", "#A855F7"),
    ("SpaceX Falcon 9 3D", "ORBITAL TELEMETRY SIM", "#F59E0B"),
    ("Subnautica 2", "UNREAL ENGINE 5 • MOD", "#00E5FF"),
    ("Upin & Ipin", "3D OPEN WORLD • UE4SS", "#38BDF8"),
    ("Snowed Under", "PUZZLE PLATFORMER", "#38BDF8"),
    ("That's Not My Neighbor", "AUTOPILOT RADAR MOD", "#F59E0B"),
    ("KR x PVZ Fusion", "TOWER DEFENSE FUSION", "#10B981"),
]

for gname, gsub, gcol in CUSTOM_GAMES:
    fname = safe_filename(gname)
    fpath = os.path.join(COVERS_DIR, fname)
    if not os.path.exists(fpath):
        im = generate_cyber_cover(gname, gsub, gcol, size=(240, 112))
        im.save(fpath, "PNG")
        im_hero = generate_cyber_cover(gname, gsub, gcol, size=(420, 196))
        im_hero.save(fpath.replace(".png", "_hero.png"), "PNG")
        print(f"  [CUSTOM ART OK] {gname} -> {fname}")

print("\n=== [3/4] COVER ASSETS READY ===")
