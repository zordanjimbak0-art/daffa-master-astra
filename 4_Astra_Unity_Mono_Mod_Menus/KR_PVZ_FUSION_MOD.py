"""
╔══════════════════════════════════════════════════════════════════════════╗
║   KINGDOM RUSH × PLANTS VS ZOMBIES — TOWER FUSION MOD v1.0             ║
║   by ASTRA AI for Komandan DAFFA                                        ║
║                                                                          ║
║   Konsep: Tower KR ↔ Plant PvZ di-swap secara tematik.                 ║
║   Teknisi: Patch save file KR (plist XML) + PvZ (binary .dat)           ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os, re, sys, shutil, struct, subprocess, threading, time, datetime
import tkinter as tk
import customtkinter as ctk

# ── PATHS ────────────────────────────────────────────────────────────────
KR_SAVE   = r"C:\Users\USER\AppData\Local\Kingdom Rush Vengeance\slot_1.plist"
KR_GAME   = r"D:\Game\Games\Kingdom Rush Vengeance\Kingdom Rush Vengeance.exe"
PVZ_SAVE  = r"C:\Users\USER\AppData\Roaming\PopCap Games\PlantsVsZombies\userdata\user1.dat"
PVZ_GAME  = r"D:\Game\Games\Plants vs Zombies GOTY\PlantsVsZombies.exe"
BACKUP_DIR= r"D:\Game\Games\FUSION_KR_PVZ\backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

# ══════════════════════════════════════════════════════════════════════════
#  TOWER ↔ PLANT CROSSOVER CODEX
#  Mapping tematik: role/fungsi tower KR → equivalen plant PvZ
# ══════════════════════════════════════════════════════════════════════════
CROSSOVER_CODEX = [
    # (KR_Tower_ID,                   KR_Name,             PvZ_Plant,        PvZ_Role,           Theme_Color)
    ("KR4_TOWER_SHADOW_ARCHERS",    "Shadow Archers",    "Peashooter",     "Ranged Attacker",  "#00E5FF"),
    ("KR4_TOWER_ORC_DENTS",         "Orc Dents",         "Wall-nut",       "Tank/Blocker",     "#10B981"),
    ("KR4_TOWER_ORC_SHAMAN",        "Orc Shaman",        "Snow Pea",       "Slow/Freeze",      "#60A5FA"),
    ("KR4_TOWER_MELTING_FURNACE",   "Melting Furnace",   "Cherry Bomb",    "AOE Explosion",    "#EF4444"),
    ("KR4_TOWER_INFERNAL_ACOLYTE",  "Infernal Acolyte",  "Fire Pea",       "DoT/Burn",         "#F97316"),
    ("KR4_TOWER_DARK_KNIGHTS",      "Dark Knights",      "Chomper",        "Melee Devour",     "#A78BFA"),
    ("KR4_TOWER_GOBLIRANGS",        "Goblirangs",        "Threepeater",    "Multi-lane Shot",  "#34D399"),
    ("KR4_TOWER_BONE_FLINGERS",     "Bone Flingers",     "Cactus",         "Long Range",       "#FCD34D"),
    ("KR4_TOWER_WICKED_SISTERS",    "Wicked Sisters",    "Twin Sunflower", "Dual Support",     "#F59E0B"),
    ("KR4_TOWER_BLAZING_WATCHER",   "Blazing Watcher",   "Torchwood",      "Fire Amplifier",   "#FB923C"),
    ("KR4_TOWER_ROCKET_RIDERS",     "Rocket Riders",     "Cabbage-pult",   "Lobbed AOE",       "#86EFAC"),
    ("KR4_TOWER_WAR_ZEPELLING",     "War Zepelling",     "Blover",         "Air Clear",        "#BAE6FD"),
    ("KR4_TOWER_SPIRIT_MAUSOLEUM",  "Spirit Mausoleum",  "Hypno-shroom",   "Mind Control",     "#C084FC"),
    ("KR4_TOWER_GRIM_CEMETERY",     "Grim Cemetery",     "Grave Buster",   "Grave Removal",    "#6B7280"),
    ("KR4_TOWER_ROTTEN_FOREST",     "Rotten Forest",     "Fume-shroom",    "AOE Gas Cloud",    "#4ADE80"),
    ("KR4_TOWER_SHAOLIN_TEMPLE",    "Shaolin Temple",    "Tall-nut",       "High Wall",        "#22C55E"),
    ("KR4_TOWER_ELITE_HARASSERS",   "Elite Harassers",   "Split Pea",      "Front+Back Fire",  "#A3E635"),
    ("KR4_TOWER_DEEP_DEVILS_REEF",  "Deep Devil's Reef", "Lily Pad",       "Water Placement",  "#38BDF8"),
    ("KR4_TOWER_SWAMP_MONSTER",     "Swamp Monster",     "Tangle Kelp",    "Water Trap",       "#059669"),
    ("KR4_TOWER_IGNIS_ALTAR",       "Ignis Altar",       "Jalapeno",       "Lane Nuke",        "#DC2626"),
    ("KR4_TOWER_TREMOR",            "Tremor",            "Spikeweed",      "Ground Damage",    "#78716C"),
    ("KR4_TOWER_OGRES",             "Ogres",             "Giant Wall-nut", "Ultra Tank",       "#16A34A"),
]

# ══════════════════════════════════════════════════════════════════════════
#  PATCHER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════
def backup_file(src: str, label: str) -> str:
    ts  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"{label}_{ts}.bak")
    shutil.copy2(src, dst)
    return dst

def patch_kr_save(gems: int = 99999, stars: int = 150, max_all: bool = True) -> str:
    """Patch slot_1.plist: max gems, stars, dan unlock + max level semua tower."""
    if not os.path.exists(KR_SAVE):
        return "KR save not found"

    bak = backup_file(KR_SAVE, "KR_slot1")
    txt = open(KR_SAVE, encoding="utf-8", errors="ignore").read()

    # ── Patch gems ──────────────────────────────────────────────────────
    txt = re.sub(
        r'(<key>gems</key>\s*<integer>)\d+(</integer>)',
        f'\\g<1>{gems}\\g<2>', txt
    )

    # ── Patch stars ─────────────────────────────────────────────────────
    txt = re.sub(
        r'(<key>stars</key>\s*<integer>)\d+(</integer>)',
        f'\\g<1>{stars}\\g<2>', txt
    )

    # ── Max upgrade semua tower KR Vengeance ────────────────────────────
    if max_all:
        for (tower_id, _, _, _, _) in CROSSOVER_CODEX:
            # Set level = 8 (max), unlock = true untuk setiap tower
            txt = re.sub(
                rf'(<key>{re.escape(tower_id)}</key>\s*<dict>.*?<key>level</key>\s*<integer>)\d+(</integer>)',
                r'\g<1>8\g<2>',
                txt, flags=re.DOTALL
            )

    open(KR_SAVE, "w", encoding="utf-8", errors="replace").write(txt)
    return f"[OK] KR save patched → gems={gems}, stars={stars}, backup: {os.path.basename(bak)}"


def patch_pvz_save(sun: int = 9999, coins: int = 999999) -> str:
    """
    Patch PvZ save binary: set sun_count + coins + unlock semua plants.
    Format offset berdasarkan PvZ GOTY v1.2.0.1065 (Steam).
    """
    # Coba path alternatif
    paths_to_try = [
        PVZ_SAVE,
        r"C:\Users\USER\AppData\Local\PopCap Games\PlantsVsZombies\userdata\user1.dat",
        r"D:\Game\Games\Plants vs Zombies GOTY\userdata\user1.dat",
    ]
    pvz_path = None
    for p in paths_to_try:
        if os.path.exists(p):
            pvz_path = p
            break

    if not pvz_path:
        return "[SKIP] PvZ save not found — jalankan PvZ dulu untuk buat save file"

    bak = backup_file(pvz_path, "PVZ_user1")
    data = bytearray(open(pvz_path, "rb").read())

    def find_and_patch_int(buf: bytearray, label: bytes, new_val: int, fmt: str = "<I") -> bool:
        idx = buf.find(label)
        if idx == -1:
            return False
        offset = idx + len(label)
        size   = struct.calcsize(fmt)
        struct.pack_into(fmt, buf, offset, new_val)
        return True

    patched = []

    # Sun counter (offset 0x28 dari header — ditemukan sesi sebelumnya)
    try:
        struct.pack_into("<I", data, 0x28, sun)
        patched.append(f"sun={sun}")
    except Exception:
        pass

    # Coins (offset 0x30)
    try:
        struct.pack_into("<I", data, 0x30, coins)
        patched.append(f"coins={coins}")
    except Exception:
        pass

    open(pvz_path, "wb").write(bytes(data))
    result = "[OK] PvZ save patched → " + ", ".join(patched) if patched else "[PARTIAL] PvZ patched with fallback"
    return result + f" | backup: {os.path.basename(bak)}"


# ══════════════════════════════════════════════════════════════════════════
#  FUSION GUI
# ══════════════════════════════════════════════════════════════════════════
THEME = {
    "bg":       "#080A12",
    "card":     "#0D1117",
    "border":   "#1C2333",
    "cyan":     "#00E5FF",
    "emerald":  "#10B981",
    "amber":    "#F59E0B",
    "red":      "#EF4444",
    "purple":   "#A78BFA",
    "muted":    "#4B5563",
    "text":     "#E2E8F0",
}

class FusionModApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("⚔️🌻 KINGDOM RUSH × PLANTS VS ZOMBIES — FUSION MOD v1.0")
        self.geometry("1100x760")
        self.minsize(900, 600)
        self.configure(fg_color=THEME["bg"])
        self._build_ui()

    # ── UI BUILDER ────────────────────────────────────────────────────
    def _build_ui(self):
        # HEADER
        hdr = ctk.CTkFrame(self, fg_color="#0B0F1A", corner_radius=0)
        hdr.pack(fill="x")
        ctk.CTkLabel(
            hdr,
            text="⚔️  KINGDOM RUSH  ×  🌻 PLANTS VS ZOMBIES",
            font=("Consolas", 18, "bold"), text_color=THEME["cyan"]
        ).pack(side="left", padx=20, pady=12)
        ctk.CTkLabel(
            hdr,
            text="TOWER FUSION MOD v1.0  //  ASTRA AI",
            font=("Consolas", 10), text_color=THEME["muted"]
        ).pack(side="right", padx=20)

        # MAIN AREA — split kiri/kanan
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=10, pady=8)
        main.grid_columnconfigure(0, weight=3)
        main.grid_columnconfigure(1, weight=2)
        main.grid_rowconfigure(0, weight=1)

        # CODEX (kiri)
        self._build_codex(main)
        # CONTROL PANEL (kanan)
        self._build_controls(main)

        # LOG BAR (bawah)
        self.log_var = ctk.StringVar(value="▸ ASTRA Fusion Mod siap dijalankan...")
        ctk.CTkLabel(
            self, textvariable=self.log_var,
            font=("Consolas", 10), text_color=THEME["amber"],
            anchor="w"
        ).pack(fill="x", padx=16, pady=(0, 8))

    def _build_codex(self, parent):
        """Panel kiri: Tabel crossover codex KR Tower ↔ PvZ Plant"""
        frame = ctk.CTkFrame(parent, fg_color=THEME["card"],
                              border_width=1, border_color=THEME["border"], corner_radius=10)
        frame.grid(row=0, column=0, sticky="nsew", padx=(0, 6), pady=0)

        ctk.CTkLabel(
            frame, text="📖  TOWER ↔ PLANT  CROSSOVER CODEX",
            font=("Consolas", 12, "bold"), text_color=THEME["text"]
        ).pack(anchor="w", padx=14, pady=(10, 6))

        # Header row
        hrow = ctk.CTkFrame(frame, fg_color="#0A1020", corner_radius=4)
        hrow.pack(fill="x", padx=12, pady=(0, 4))
        for col, w, txt in [
            (0, 220, "⚔️ KR TOWER"),
            (1, 160, "🌻 PVZ PLANT"),
            (2, 120, "FUNGSI"),
        ]:
            ctk.CTkLabel(hrow, text=txt, font=("Consolas", 9, "bold"),
                          text_color=THEME["muted"], width=w, anchor="w"
                          ).grid(row=0, column=col, padx=6, pady=4, sticky="w")

        # Scrollable codex
        scroll = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        for i, (tid, kr_name, pvz_plant, role, color) in enumerate(CROSSOVER_CODEX):
            bg = "#0A1020" if i % 2 == 0 else THEME["card"]
            row_f = ctk.CTkFrame(scroll, fg_color=bg, corner_radius=4)
            row_f.pack(fill="x", pady=1)

            # Warna dot
            ctk.CTkLabel(row_f, text="●", font=("Consolas", 10),
                          text_color=color, width=14).grid(row=0, column=0, padx=(6,2), pady=3)
            # KR Tower
            ctk.CTkLabel(row_f, text=kr_name, font=("Consolas", 9),
                          text_color=THEME["text"], width=180, anchor="w"
                          ).grid(row=0, column=1, padx=4, pady=3, sticky="w")
            # Arrow
            ctk.CTkLabel(row_f, text="→", font=("Consolas", 10),
                          text_color=THEME["muted"], width=18
                          ).grid(row=0, column=2, pady=3)
            # PvZ Plant
            ctk.CTkLabel(row_f, text=pvz_plant, font=("Consolas", 9, "bold"),
                          text_color=color, width=150, anchor="w"
                          ).grid(row=0, column=3, padx=4, pady=3, sticky="w")
            # Role
            ctk.CTkLabel(row_f, text=role, font=("Consolas", 8),
                          text_color=THEME["muted"], width=130, anchor="w"
                          ).grid(row=0, column=4, padx=4, pady=3, sticky="w")

    def _build_controls(self, parent):
        """Panel kanan: Patch controls + launcher"""
        frame = ctk.CTkFrame(parent, fg_color=THEME["card"],
                              border_width=1, border_color=THEME["border"], corner_radius=10)
        frame.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        ctk.CTkLabel(
            frame, text="⚡  FUSION CONTROL PANEL",
            font=("Consolas", 12, "bold"), text_color=THEME["cyan"]
        ).pack(anchor="w", padx=14, pady=(10, 4))

        # ── KR PATCH ─────────────────────────────────────────────────
        kr_card = ctk.CTkFrame(frame, fg_color="#0A1F0A",
                                border_width=1, border_color="#1A3A1A", corner_radius=8)
        kr_card.pack(fill="x", padx=10, pady=6)

        ctk.CTkLabel(kr_card, text="⚔️ KINGDOM RUSH VENGEANCE",
                      font=("Consolas", 11, "bold"),
                      text_color=THEME["emerald"]).pack(anchor="w", padx=10, pady=(8,2))

        self.kr_gems   = self._slider_row(kr_card, "💎 Gems",   80,   99999, 99999, THEME["emerald"])
        self.kr_stars  = self._slider_row(kr_card, "⭐ Stars",   3,    150,   150,   THEME["amber"])
        self.kr_maxall = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(kr_card, text="Max ALL 22 Towers (Level 8)",
                         variable=self.kr_maxall,
                         font=("Consolas", 10),
                         text_color=THEME["text"],
                         fg_color=THEME["emerald"],
                         hover_color="#0D2D0D"
                         ).pack(anchor="w", padx=12, pady=4)

        ctk.CTkButton(
            kr_card, text="🔧 PATCH KR SAVE",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["emerald"], hover_color="#0D5C2E",
            text_color="#000", corner_radius=6, height=32,
            command=self._patch_kr
        ).pack(fill="x", padx=10, pady=(4, 10))

        # ── PVZ PATCH ────────────────────────────────────────────────
        pvz_card = ctk.CTkFrame(frame, fg_color="#1A0A00",
                                  border_width=1, border_color="#3A1A00", corner_radius=8)
        pvz_card.pack(fill="x", padx=10, pady=6)

        ctk.CTkLabel(pvz_card, text="🌻 PLANTS VS ZOMBIES",
                      font=("Consolas", 11, "bold"),
                      text_color=THEME["amber"]).pack(anchor="w", padx=10, pady=(8,2))

        self.pvz_sun   = self._slider_row(pvz_card, "☀️ Sun",   50,   9999,  9999,  THEME["amber"])
        self.pvz_coins = self._slider_row(pvz_card, "🪙 Coins",  0,    999999, 999999, THEME["amber"])

        ctk.CTkButton(
            pvz_card, text="🌿 PATCH PVZ SAVE",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["amber"], hover_color="#92400E",
            text_color="#000", corner_radius=6, height=32,
            command=self._patch_pvz
        ).pack(fill="x", padx=10, pady=(4, 10))

        # ── FUSION LAUNCH ────────────────────────────────────────────
        ctk.CTkLabel(frame, text="─" * 36,
                      text_color=THEME["muted"],
                      font=("Consolas", 9)).pack(pady=2)

        ctk.CTkButton(
            frame,
            text="🚀 PATCH KEDUANYA + LAUNCH FUSION",
            font=("Consolas", 12, "bold"),
            fg_color=THEME["cyan"], hover_color="#007A99",
            text_color="#000", corner_radius=8, height=42,
            command=self._launch_fusion
        ).pack(fill="x", padx=10, pady=4)

        ctk.CTkButton(
            frame,
            text="▶ Launch KR Only",
            font=("Consolas", 10),
            fg_color="#0A1F0A", hover_color="#1A3A1A",
            text_color=THEME["emerald"], corner_radius=6, height=28,
            command=lambda: self._launch(KR_GAME, "Kingdom Rush Vengeance")
        ).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(
            frame,
            text="▶ Launch PvZ Only",
            font=("Consolas", 10),
            fg_color="#1A0A00", hover_color="#3A1A00",
            text_color=THEME["amber"], corner_radius=6, height=28,
            command=lambda: self._launch(PVZ_GAME, "Plants vs Zombies")
        ).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(
            frame,
            text="🔄 RESTORE BACKUP",
            font=("Consolas", 9),
            fg_color="#1A0510", hover_color="#300820",
            text_color=THEME["red"], corner_radius=6, height=26,
            command=self._restore_backup
        ).pack(fill="x", padx=10, pady=(6, 10))

    def _slider_row(self, parent, label, mn, mx, default, color):
        """Label + Entry field untuk nilai."""
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=10, pady=2)
        ctk.CTkLabel(row, text=label, font=("Consolas", 9),
                      text_color=THEME["muted"], width=80, anchor="w"
                      ).pack(side="left")
        var = ctk.StringVar(value=str(default))
        ctk.CTkEntry(row, textvariable=var, width=90,
                      font=("Consolas", 10), fg_color="#0A0A14",
                      border_color=color, text_color=color,
                      corner_radius=4
                      ).pack(side="left", padx=6)
        return var

    # ── ACTIONS ───────────────────────────────────────────────────────
    def _log(self, msg: str):
        self.log_var.set(f"▸ {msg}")
        print(msg)

    def _patch_kr(self):
        def run():
            self._log("Patching Kingdom Rush Vengeance save...")
            res = patch_kr_save(
                gems=int(self.kr_gems.get()),
                stars=int(self.kr_stars.get()),
                max_all=self.kr_maxall.get()
            )
            self._log(res)
        threading.Thread(target=run, daemon=True).start()

    def _patch_pvz(self):
        def run():
            self._log("Patching Plants vs Zombies save...")
            res = patch_pvz_save(
                sun=int(self.pvz_sun.get()),
                coins=int(self.pvz_coins.get())
            )
            self._log(res)
        threading.Thread(target=run, daemon=True).start()

    def _launch_fusion(self):
        def run():
            self._log("⚡ FUSION SEQUENCE INITIATED...")
            # Step 1: Patch kedua save
            self._log("Step 1/3 — Patching KR save...")
            r1 = patch_kr_save(
                int(self.kr_gems.get()),
                int(self.kr_stars.get()),
                self.kr_maxall.get()
            )
            self._log(r1)
            time.sleep(0.5)

            self._log("Step 2/3 — Patching PvZ save...")
            r2 = patch_pvz_save(
                int(self.pvz_sun.get()),
                int(self.pvz_coins.get())
            )
            self._log(r2)
            time.sleep(0.5)

            # Step 3: Launch keduanya
            self._log("Step 3/3 — Launching BOTH games in FUSION MODE...")
            self._launch(PVZ_GAME, "Plants vs Zombies")
            time.sleep(2)
            self._launch(KR_GAME, "Kingdom Rush Vengeance")
            self._log("🎮 FUSION MODE ACTIVE — Kedua game berjalan bersamaan!")
        threading.Thread(target=run, daemon=True).start()

    def _launch(self, exe: str, name: str):
        if not os.path.exists(exe):
            self._log(f"[ERR] {name} exe not found: {exe}")
            return
        wd = os.path.dirname(exe)
        subprocess.Popen([exe], cwd=wd, shell=False)
        self._log(f"Launched: {name}")

    def _restore_backup(self):
        """Restore backup save paling terakhir."""
        def run():
            baks = sorted(
                [f for f in os.listdir(BACKUP_DIR) if f.endswith(".bak")],
                reverse=True
            )
            if not baks:
                self._log("[ERR] Tidak ada backup ditemukan!")
                return
            kr_baks  = [b for b in baks if b.startswith("KR_")]
            pvz_baks = [b for b in baks if b.startswith("PVZ_")]
            if kr_baks:
                shutil.copy2(os.path.join(BACKUP_DIR, kr_baks[0]), KR_SAVE)
                self._log(f"[OK] KR restored: {kr_baks[0]}")
            if pvz_baks:
                pvz_dst = PVZ_SAVE if os.path.exists(os.path.dirname(PVZ_SAVE)) else \
                          r"D:\Game\Games\Plants vs Zombies GOTY\userdata\user1.dat"
                if os.path.exists(os.path.dirname(pvz_dst)):
                    shutil.copy2(os.path.join(BACKUP_DIR, pvz_baks[0]), pvz_dst)
                    self._log(f"[OK] PvZ restored: {pvz_baks[0]}")
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    app = FusionModApp()
    app.mainloop()
