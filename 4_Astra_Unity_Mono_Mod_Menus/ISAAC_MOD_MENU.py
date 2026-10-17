"""
ASTRA AI — The Binding of Isaac: Repentance MOD MENU v3.0
Engine   : Custom C++ + Native Lua Mod Engine (--luadebug un-sandboxed)
Features : Tabbed Interface, Virtual Console, Dead God Unlocker, God Mode, Stage Warp
Hotkeys  : ALT+1..9, ALT+0 Panic Reset (Strictly 60% Mechanical Keyboard Optimized)
Theme    : Dark Purple / Gold ASTRA Aesthetic (bg=#110022 card=#1A0033 acc=#9333EA)
Designed for: Komandan DAFFA
"""

import os, sys, time, threading, subprocess, ctypes, ctypes.wintypes as wt, winsound
import customtkinter as ctk
import psutil

GAME_DIR = r"D:\Game\Games\The.Binding.of.Isaac-Repentance-SteamRIP.com\The Binding of Isaac - Repentance"
GAME_EXE = os.path.join(GAME_DIR, "isaac-ng.exe")
PROC_NAME = "isaac-ng"

CMD_FILES = [
    os.path.join(GAME_DIR, "astra_cmd.txt"),
    os.path.join(os.environ.get("USERPROFILE", r"C:\Users\USER"), "Documents", "My Games", "Binding of Isaac Repentance+", "astra_cmd.txt"),
]

user32   = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Virtual key codes (Keyboard 60% friendly: ALT + Number row 0-9)
VK_ALT = 0x12
VK_1   = 0x31
VK_2   = 0x32
VK_3   = 0x33
VK_4   = 0x34
VK_5   = 0x35
VK_6   = 0x36
VK_7   = 0x37
VK_8   = 0x38
VK_9   = 0x39
VK_0   = 0x30

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

T = {
    "bg"    : "#0D001A",
    "card"  : "#17002E",
    "card2" : "#220042",
    "border": "#4C1D95",
    "acc"   : "#9333EA",
    "acc2"  : "#A855F7",
    "sec"   : "#6B21A8",
    "red"   : "#EF4444",
    "green" : "#10B981",
    "cyan"  : "#38BDF8",
    "gold"  : "#F59E0B",
    "main"  : "#F8FAFC",
    "muted" : "#94A3B8",
    "warn"  : "#F97316",
}

def _darken(hex_color: str, factor: float = 0.7) -> str:
    hex_color = hex_color.lstrip("#")
    r = max(0, int(int(hex_color[0:2], 16) * factor))
    g = max(0, int(int(hex_color[2:4], 16) * factor))
    b = max(0, int(int(hex_color[4:6], 16) * factor))
    return f"#{r:02X}{g:02X}{b:02X}"


class IsaacModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASTRA // THE BINDING OF ISAAC: REPENTANCE v3.0")
        self.geometry("540x800")
        self.minsize(500, 700)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.95)
        self.configure(fg_color=T["bg"])

        self._game_pid: int | None = None
        self._running = True

        # Toggle states per cheat (Default OFF)
        self._state = {
            "god_mode":    False,
            "inf_hp":      False,
            "inf_coins":   False,
            "inf_keys":    False,
            "inf_bombs":   False,
            "turbo_speed": False,
            "one_hit_ko":  False,
            "inf_charge":  False,
            "high_dmg":    False,
        }

        self._btn_refs = {}

        self._build_ui()
        threading.Thread(target=self._hotkey_thread, daemon=True).start()
        threading.Thread(target=self._process_watcher, daemon=True).start()

    def _build_ui(self):
        # Header Box
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10,
                            border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=12, pady=(10, 6))

        title_row = ctk.CTkFrame(hdr, fg_color="transparent")
        title_row.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(title_row, text="💀 BINDING OF ISAAC: REPENTANCE v3.0",
                     font=("Consolas", 14, "bold"), text_color=T["acc2"]).pack(side="left")
        ctk.CTkLabel(title_row, text="ASTRA PROTOCOL",
                     font=("Consolas", 9, "bold"), text_color=T["gold"]).pack(side="right")

        ctk.CTkLabel(hdr, text="Lua Engine Integration • Dead God Unlocker • Virtual Console (60% Keyboard)",
                     font=("Consolas", 8), text_color=T["muted"]).pack(anchor="w", padx=12, pady=(0, 4))

        sb = ctk.CTkFrame(hdr, fg_color="#0A0014", corner_radius=6)
        sb.pack(fill="x", padx=10, pady=(0, 4))
        self._dot = ctk.CTkLabel(sb, text="●", font=("Consolas", 12), text_color=T["red"])
        self._dot.pack(side="left", padx=(8, 4), pady=3)
        self._stat = ctk.CTkLabel(sb, text=f"Menunggu {PROC_NAME}.exe ...",
                                   font=("Consolas", 9, "bold"), text_color=T["muted"])
        self._stat.pack(side="left", pady=3)

        self._log = ctk.CTkLabel(hdr, text="STATUS: Standby — Siap Melayani Komandan DAFFA",
                                  font=("Consolas", 8), text_color=T["cyan"])
        self._log.pack(anchor="w", padx=12, pady=(0, 6))

        # Tabview
        self.tabview = ctk.CTkTabview(self, fg_color=T["card"],
                                      segmented_button_fg_color="#0A0014",
                                      segmented_button_selected_color=T["acc"],
                                      segmented_button_selected_hover_color=T["sec"],
                                      segmented_button_unselected_color="#140026",
                                      segmented_button_unselected_hover_color="#22003D",
                                      text_color=T["main"])
        self.tabview.pack(fill="both", expand=True, padx=12, pady=(0, 6))

        self.tab_cheats  = self.tabview.add("⚡ CHEAT & GOD")
        self.tab_unlock  = self.tabview.add("⭐ DEAD GOD & CHARS")
        self.tab_console = self.tabview.add("💻 VIRTUAL CONSOLE")
        self.tab_warp    = self.tabview.add("🗺️ STAGE WARP")

        self._build_tab_cheats()
        self._build_tab_unlock()
        self._build_tab_console()
        self._build_tab_warp()

        # Bottom Bar
        bot = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10, height=44)
        bot.pack(fill="x", padx=12, pady=(0, 10))

        ctk.CTkLabel(bot, text="Alpha:", font=("Consolas", 9),
                     text_color=T["muted"]).pack(side="left", padx=(10, 4), pady=8)
        sl = ctk.CTkSlider(bot, from_=0.3, to=1.0, number_of_steps=14, width=80,
                            command=lambda v: self.attributes("-alpha", float(v)))
        sl.set(0.95)
        sl.pack(side="left", pady=8)

        ctk.CTkButton(bot, text="🚨 PANIC RESET (ALT+0)", font=("Consolas", 9, "bold"),
                      fg_color=T["red"], hover_color=_darken(T["red"]),
                      text_color="#FFFFFF", width=140, height=28,
                      command=self._panic_reset).pack(side="left", padx=(12, 0), pady=8)

        ctk.CTkButton(bot, text="▶ LAUNCH (--luadebug)", font=("Consolas", 9, "bold"),
                      fg_color=T["acc"], hover_color=T["sec"],
                      text_color="#FFFFFF", width=150, height=28,
                      command=self._launch_game).pack(side="right", padx=10, pady=8)

    # ── TAB 1: CHEAT & GOD MODE ──────────────────────────────────────────────
    def _build_tab_cheats(self):
        sc = ctk.CTkScrollableFrame(self.tab_cheats, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=4, pady=4)

        cheats_info = [
            ("god_mode",    "⚔  GOD MODE (INVINCIBILITY)", "Kebal 100% dari semua luka (Damage Hook + Debug 3)", "ALT+1", T["green"]),
            ("inf_hp",      "💖 LOCK MAX HP (12 HEARTS)",  "Mengunci HP selalu penuh 12 hati merah (24 HP)",     "ALT+2", T["red"]),
            ("inf_coins",   "💰 LOCK 99 COINS",            "Koin terkunci maksimal di angka 99",                 "ALT+3", T["gold"]),
            ("inf_keys",    "🔑 LOCK 99 KEYS",             "Kunci pintu & peti terkunci maksimal 99",            "ALT+4", T["cyan"]),
            ("inf_bombs",   "💣 LOCK 99 BOMBS",            "Bom peledak tak terbatas selalu 99",                 "ALT+5", T["warn"]),
            ("turbo_speed", "⚡ TURBO SPEED 2.0 (MAX)",    "Kecepatan jalan Isaac maksimal cap 2.0",             "ALT+6", "#38BDF8"),
            ("one_hit_ko",  "💀 ONE-HIT KO ENEMIES",       "Musuh langsung musnah 1x sentuhan/tembakan",         "ALT+7", T["red"]),
            ("inf_charge",  "🔋 INFINITE ACTIVE CHARGE",   "Item aktif selalu penuh tanpa perlu charge (Debug 8)","KLIK",  T["acc2"]),
            ("high_dmg",    "💥 +40 DAMAGE BOOST",         "Tambahan +40 damage tembakan instan (Debug 4)",      "KLIK",  "#E11D48"),
        ]

        for key, label, desc, hk, col in cheats_info:
            self._cheat_card(sc, key, label, desc, hk, col)

        # Quick Actions Card
        qa_card = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                               border_color=T["border"], corner_radius=8)
        qa_card.pack(fill="x", padx=2, pady=(6, 2))
        ctk.CTkLabel(qa_card, text="⚡ INSTANT TACTICAL ACTIONS", font=("Consolas", 10, "bold"),
                     text_color=T["gold"]).pack(anchor="w", padx=10, pady=(6, 2))

        btn_row = ctk.CTkFrame(qa_card, fg_color="transparent")
        btn_row.pack(fill="x", padx=10, pady=(2, 8))

        ctk.CTkButton(btn_row, text="💀 KILL ROOM (ALT+9)", font=("Consolas", 9, "bold"),
                      fg_color=T["red"], hover_color=_darken(T["red"]), text_color="#FFFFFF",
                      height=28, command=lambda: self._send_cmd("kill_room")).pack(side="left", fill="x", expand=True, padx=(0, 4))

        ctk.CTkButton(btn_row, text="✨ GOD ITEMS COMBO (ALT+8)", font=("Consolas", 9, "bold"),
                      fg_color=T["gold"], hover_color=_darken(T["gold"]), text_color="#0A0014",
                      height=28, command=lambda: self._send_cmd("all_items")).pack(side="right", fill="x", expand=True, padx=(4, 0))

    def _cheat_card(self, parent, key: str, label: str, desc: str, hk: str, col: str):
        card = ctk.CTkFrame(parent, fg_color=T["card2"], border_width=1,
                             border_color=T["border"], corner_radius=8)
        card.pack(fill="x", padx=2, pady=3)

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=10, pady=5)

        ctk.CTkLabel(info, text=label, font=("Consolas", 10, "bold"),
                     text_color=T["main"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=desc, font=("Consolas", 8),
                     text_color=T["muted"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=f"HOTKEY: {hk}", font=("Consolas", 8, "bold"),
                     text_color=col, anchor="w").pack(anchor="w")

        btn = ctk.CTkButton(card, text="OFF", width=62, height=28,
                              font=("Consolas", 9, "bold"),
                              fg_color=_darken(col, 0.45),
                              hover_color=_darken(col, 0.6),
                              text_color=T["main"], corner_radius=6,
                              command=lambda k=key, c=col: self._toggle_cheat(k, c))
        btn.pack(side="right", padx=10, pady=8)
        self._btn_refs[key] = (btn, col)

    # ── TAB 2: DEAD GOD & ALL CHARACTERS ─────────────────────────────────────
    def _build_tab_unlock(self):
        sc = ctk.CTkScrollableFrame(self.tab_unlock, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=4, pady=4)

        # Big Dead God Unlock Banner
        dg_card = ctk.CTkFrame(sc, fg_color="#2A0845", border_width=2,
                               border_color=T["gold"], corner_radius=10)
        dg_card.pack(fill="x", padx=2, pady=6)

        ctk.CTkLabel(dg_card, text="🏆 DEAD GOD 1000000% UNLOCKER",
                     font=("Consolas", 13, "bold"), text_color=T["gold"]).pack(anchor="w", padx=14, pady=(10, 2))
        ctk.CTkLabel(dg_card, text="Membuka seluruh 637 Achievement, 716+ Item Collectibles, Secrets,\nSemua Ending, Tantangan, dan 34 Karakter Normal & Tainted permanen!",
                     font=("Consolas", 8), text_color="#E2E8F0", justify="left").pack(anchor="w", padx=14, pady=(0, 6))

        ctk.CTkButton(dg_card, text="⭐ BUKA SEMUA SEKARANG (DEAD GOD)",
                      font=("Consolas", 11, "bold"), fg_color=T["gold"],
                      hover_color=_darken(T["gold"]), text_color="#110022",
                      height=34, corner_radius=8,
                      command=lambda: self._send_cmd("unlock_all")).pack(fill="x", padx=14, pady=(4, 12))

        # Character Quick Selector
        char_card = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                                 border_color=T["border"], corner_radius=8)
        char_card.pack(fill="x", padx=2, pady=6)

        ctk.CTkLabel(char_card, text="🎭 WARP / GANTI 34 KARAKTER INSTAN",
                     font=("Consolas", 10, "bold"), text_color=T["cyan"]).pack(anchor="w", padx=12, pady=(8, 2))
        ctk.CTkLabel(char_card, text="Pilih karakter lalu klik tombol untuk restart run langsung sebagai karakter tersebut:",
                     font=("Consolas", 8), text_color=T["muted"]).pack(anchor="w", padx=12, pady=(0, 6))

        # 34 Characters List (Normal 0-18, Tainted 19-35)
        self._characters = [
            ("Isaac", 0),
            ("Magdalene", 1),
            ("Cain", 2),
            ("Judas", 3),
            ("??? (Blue Baby)", 4),
            ("Eve", 5),
            ("Samson", 6),
            ("Azazel", 7),
            ("Lazarus", 8),
            ("Eden", 9),
            ("The Lost (Holy Mantle)", 10),
            ("Lazarus II", 11),
            ("Black Judas", 12),
            ("Lilith", 13),
            ("Keeper", 14),
            ("Apollyon", 15),
            ("The Forgotten", 16),
            ("Bethany", 17),
            ("Jacob & Esau", 18),
            ("⭐ Tainted Isaac", 19),
            ("⭐ Tainted Magdalene", 20),
            ("⭐ Tainted Cain", 21),
            ("⭐ Tainted Judas", 22),
            ("⭐ Tainted ???", 23),
            ("⭐ Tainted Eve", 24),
            ("⭐ Tainted Samson", 25),
            ("⭐ Tainted Azazel", 26),
            ("⭐ Tainted Lazarus", 27),
            ("⭐ Tainted Eden", 28),
            ("⭐ Tainted Lost", 29),
            ("⭐ Tainted Lilith", 30),
            ("⭐ Tainted Keeper", 31),
            ("⭐ Tainted Apollyon", 32),
            ("⭐ Tainted Forgotten", 33),
            ("⭐ Tainted Bethany", 34),
            ("⭐ Tainted Jacob", 35),
        ]

        char_names = [f"{c[0]} (ID: {c[1]})" for c in self._characters]
        self._char_var = ctk.StringVar(value=char_names[0])

        self._char_menu = ctk.CTkOptionMenu(char_card, values=char_names,
                                            variable=self._char_var,
                                            fg_color="#0A0014",
                                            button_color=T["acc"],
                                            button_hover_color=T["sec"],
                                            font=("Consolas", 9),
                                            dropdown_font=("Consolas", 9))
        self._char_menu.pack(fill="x", padx=12, pady=4)

        ctk.CTkButton(char_card, text="▶ RESPAWN SEBAGAI KARAKTER TERPILIH",
                      font=("Consolas", 9, "bold"), fg_color=T["cyan"],
                      hover_color=_darken(T["cyan"]), text_color="#0A0014",
                      height=30, command=self._warp_character).pack(fill="x", padx=12, pady=(4, 10))

        # Quick Unlock Individual Groups
        other_card = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                                  border_color=T["border"], corner_radius=8)
        other_card.pack(fill="x", padx=2, pady=6)
        ctk.CTkLabel(other_card, text="📦 EXTRA UNLOCK SHORTCUTS",
                     font=("Consolas", 10, "bold"), text_color=T["gold"]).pack(anchor="w", padx=12, pady=(8, 4))

        extra_row = ctk.CTkFrame(other_card, fg_color="transparent")
        extra_row.pack(fill="x", padx=12, pady=(0, 10))

        ctk.CTkButton(extra_row, text="Buka The Lost (Holy Mantle)", font=("Consolas", 8, "bold"),
                      fg_color=T["sec"], hover_color=T["acc"], height=28,
                      command=lambda: self._send_cmd("cmd: achievement 245")).pack(side="left", fill="x", expand=True, padx=(0, 2))

        ctk.CTkButton(extra_row, text="Buka Death Certificate", font=("Consolas", 8, "bold"),
                      fg_color=T["sec"], hover_color=T["acc"], height=28,
                      command=lambda: self._send_cmd("cmd: achievement 628")).pack(side="right", fill="x", expand=True, padx=(2, 0))

    def _warp_character(self):
        sel_str = self._char_var.get()
        # Parse ID from string e.g. "Isaac (ID: 0)"
        try:
            char_id = int(sel_str.split("ID: ")[1].rstrip(")"))
            self._send_cmd(f"cmd: restart {char_id}")
            self._log.configure(text=f"RESPAWN: Karakter ID {char_id} ({sel_str.split(' (ID:')[0]})", text_color=T["cyan"])
        except Exception as e:
            self._log.configure(text=f"Error parse karakter: {e}", text_color=T["red"])

    # ── TAB 3: VIRTUAL CONSOLE (Tanpa Tilde ~ Untuk Keyboard 60%) ─────────────
    def _build_tab_console(self):
        sc = ctk.CTkScrollableFrame(self.tab_console, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=4, pady=4)

        # 60% Keyboard Info
        tip_card = ctk.CTkFrame(sc, fg_color="#240B3B", border_width=1,
                                border_color=T["acc"], corner_radius=8)
        tip_card.pack(fill="x", padx=2, pady=4)
        ctk.CTkLabel(tip_card, text="⌨ KONSOL LUA VIRTUAL (SOLUSI KEYBOARD 60%)",
                     font=("Consolas", 10, "bold"), text_color=T["gold"]).pack(anchor="w", padx=10, pady=(6, 2))
        ctk.CTkLabel(tip_card, text="Karena keyboard 60% tidak memiliki tombol tilde (~), Anda bisa mengetik\ndan mengirim perintah engine langsung dari sini secara real-time!",
                     font=("Consolas", 8), text_color="#E2E8F0", justify="left").pack(anchor="w", padx=10, pady=(0, 6))

        # Command Entry
        entry_frame = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                                  border_color=T["border"], corner_radius=8)
        entry_frame.pack(fill="x", padx=2, pady=6)

        ctk.CTkLabel(entry_frame, text="Ketik Perintah Native Engine:", font=("Consolas", 9, "bold"),
                     text_color=T["main"]).pack(anchor="w", padx=10, pady=(6, 2))

        input_row = ctk.CTkFrame(entry_frame, fg_color="transparent")
        input_row.pack(fill="x", padx=10, pady=(0, 8))

        self._cmd_entry = ctk.CTkEntry(input_row, placeholder_text="mis. giveitem c182, spawn 5.100.1, stage 13, debug 8...",
                                       font=("Consolas", 9), fg_color="#0A0014", border_color=T["border"])
        self._cmd_entry.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._cmd_entry.bind("<Return>", lambda e: self._send_custom_console())

        ctk.CTkButton(input_row, text="KIRIM", width=64, height=28,
                      font=("Consolas", 9, "bold"), fg_color=T["acc"],
                      hover_color=T["sec"], command=self._send_custom_console).pack(side="right")

        # 1-Click Popular S-Tier / God Items
        items_card = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                                  border_color=T["border"], corner_radius=8)
        items_card.pack(fill="x", padx=2, pady=6)
        ctk.CTkLabel(items_card, text="🎁 1-CLICK SPAWN GOD ITEMS (S-TIER)",
                     font=("Consolas", 10, "bold"), text_color=T["gold"]).pack(anchor="w", padx=10, pady=(8, 4))

        god_items = [
            ("💖 Sacred Heart", "c182", "Homing + Damage x2.3"),
            ("☀️ Godhead", "c331", "Aura Cahaya Mematikan"),
            ("🔥 Brimstone", "c118", "Mega Blood Laser"),
            ("⚡ Tech X", "c395", "Laser Ring Tembus Dinding"),
            ("👁️ Polyphemus", "c169", "Mega Damage Raksasa"),
            ("👶 C Section", "c678", "Homing Baby Fetus Tears"),
            ("🔄 R Key", "c636", "Reset Run Bawa Seluruh Item"),
            ("📜 Death Certificate", "c628", "Pilih Item Apapun di Game"),
            ("🍄 Mega Mush", "c625", "Tubuh Raksasa Kebal & Lindas"),
            ("🕊️ Holy Mantle", "c313", "Perisai Kebal 1x Per Room"),
            ("🌀 Psy Fly", "c580", "Lalat Pelindung Blokir Peluru"),
            ("🔪 Mom's Knife", "c114", "Pisau Putar Damage Ekstrem"),
        ]

        grid = ctk.CTkFrame(items_card, fg_color="transparent")
        grid.pack(fill="x", padx=8, pady=(0, 8))

        for idx, (name, item_code, desc) in enumerate(god_items):
            r = idx // 2
            c = idx % 2
            btn = ctk.CTkButton(grid, text=f"{name}\n({desc})", font=("Consolas", 8, "bold"),
                                fg_color="#20003D", hover_color=T["acc"], text_color=T["main"],
                                height=36, corner_radius=6,
                                command=lambda code=item_code, n=name: self._spawn_item(code, n))
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
            grid.grid_columnconfigure(c, weight=1)

    def _send_custom_console(self):
        text = self._cmd_entry.get().strip()
        if not text:
            return
        self._send_cmd(f"cmd: {text}")
        self._cmd_entry.delete(0, "end")

    def _spawn_item(self, item_code: str, item_name: str):
        self._send_cmd(f"cmd: giveitem {item_code}")
        self._log.configure(text=f"SPAWN ITEM: {item_name} ({item_code}) Diberikan!", text_color=T["green"])

    # ── TAB 4: STAGE WARP TELEPORT ───────────────────────────────────────────
    def _build_tab_warp(self):
        sc = ctk.CTkScrollableFrame(self.tab_warp, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=4, pady=4)

        info_card = ctk.CTkFrame(sc, fg_color=T["card2"], border_width=1,
                                 border_color=T["border"], corner_radius=8)
        info_card.pack(fill="x", padx=2, pady=4)
        ctk.CTkLabel(info_card, text="🗺️ TELEPORTASI LANTAI (STAGE WARP)",
                     font=("Consolas", 10, "bold"), text_color=T["cyan"]).pack(anchor="w", padx=10, pady=(6, 2))
        ctk.CTkLabel(info_card, text="Pindah langsung ke lantai manapun termasuk Bos Akhir Mother & The Beast:",
                     font=("Consolas", 8), text_color=T["muted"]).pack(anchor="w", padx=10, pady=(0, 6))

        stages = [
            ("Lantai 1: Basement / Cellar", "1", "Awal Permainan"),
            ("Lantai 2: Caves / Catacombs", "3", "Lantai Gua"),
            ("Lantai 3: Depths / Necropolis", "5", "Lantai Kedalaman"),
            ("Lantai 4: Womb / Utero (Mom)", "7", "Kandungan / Bos Mom"),
            ("Lantai 5: Sheol (Satan)", "9", "Neraka / Bos Satan"),
            ("Lantai 5: Cathedral (Isaac)", "10", "Katedral / Bos Isaac"),
            ("Lantai 6: Dark Room (The Lamb)", "11", "Kamar Gelap / Bos Lamb"),
            ("Lantai 6: The Chest (??? Blue Baby)", "11", "Peti / Bos Blue Baby"),
            ("⭐ The Void (Delirium)", "12", "Ruang Hampa / Bos Delirium"),
            ("⭐ Home (The Beast / True Ending)", "13", "Rumah Isaac / Bos The Beast"),
            ("Alt-Path: Downpour / Dross", "1a", "Lantai Air Repentance"),
            ("Alt-Path: Mines / Ashpit", "2a", "Lantai Tambang Repentance"),
            ("Alt-Path: Mausoleum / Gehenna", "3a", "Lantai Makam Repentance"),
            ("Alt-Path: Corpse (Mother Fight)", "4a", "Lantai Mayat / Bos Mother"),
        ]

        grid = ctk.CTkFrame(sc, fg_color="transparent")
        grid.pack(fill="x", padx=2, pady=4)

        for idx, (s_name, s_id, s_desc) in enumerate(stages):
            r = idx // 2
            c = idx % 2
            btn = ctk.CTkButton(grid, text=f"{s_name}\n[{s_desc}]",
                                font=("Consolas", 8, "bold"),
                                fg_color="#1E0038", hover_color=T["sec"], text_color=T["main"],
                                height=40, corner_radius=6,
                                command=lambda sid=s_id, sn=s_name: self._warp_stage(sid, sn))
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
            grid.grid_columnconfigure(c, weight=1)

    def _warp_stage(self, stage_id: str, stage_name: str):
        self._send_cmd(f"cmd: stage {stage_id}")
        self._log.configure(text=f"WARP STAGE: {stage_name} (stage {stage_id})", text_color=T["cyan"])

    # ── ENGINE IPC & TOGGLE LOGIC ────────────────────────────────────────────
    def _send_cmd(self, cmd_name: str):
        """Kirim perintah ke modul Lua via IPC command file"""
        try:
            for fpath in CMD_FILES:
                try:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(cmd_name + "\n")
                except Exception:
                    pass
            self._log.configure(text=f"ASTRA→ {cmd_name.upper()} DIKIRIM!", text_color=T["cyan"])
            winsound.Beep(1200, 50)
        except Exception as ex:
            self._log.configure(text=f"IPC ERR: {ex}", text_color=T["red"])

    def _toggle_cheat(self, key: str, col: str):
        self._state[key] = not self._state[key]
        active = self._state[key]
        btn, base_col = self._btn_refs[key]

        if active:
            btn.configure(text="ON ", fg_color=base_col, hover_color=_darken(base_col))
            self._send_cmd(f"{key}_on")
            self._log.configure(text=f"STATUS: {key.upper()} → ON [AKTIF]", text_color=T["green"])
            winsound.Beep(1200, 60)
        else:
            btn.configure(text="OFF", fg_color=_darken(base_col, 0.45), hover_color=_darken(base_col, 0.6))
            self._send_cmd(f"{key}_off")
            self._log.configure(text=f"STATUS: {key.upper()} → OFF [MATI]", text_color=T["muted"])
            winsound.Beep(700, 60)

    def _panic_reset(self):
        for key in list(self._state.keys()):
            if self._state[key]:
                self._state[key] = False
                if key in self._btn_refs:
                    btn, col = self._btn_refs[key]
                    btn.configure(text="OFF", fg_color=_darken(col, 0.45), hover_color=_darken(col, 0.6))

        self._send_cmd("panic_reset")
        self._log.configure(text="STATUS: PANIC RESET — Seluruh cheat OFF", text_color=T["warn"])
        winsound.Beep(400, 150)
        winsound.Beep(300, 150)

    def _process_watcher(self):
        while self._running:
            try:
                found = False
                for proc in psutil.process_iter(["name", "pid"]):
                    pname = (proc.info["name"] or "").lower()
                    if PROC_NAME.lower() in pname:
                        pid = proc.info["pid"]
                        if self._game_pid != pid:
                            self._game_pid = pid
                        found = True
                        break

                if found:
                    self.after(0, lambda: [
                        self._dot.configure(text_color=T["green"]),
                        self._stat.configure(
                            text=f"TERHUBUNG: {PROC_NAME} (PID {self._game_pid})",
                            text_color=T["green"])
                    ])
                else:
                    self._game_pid = None
                    self.after(0, lambda: [
                        self._dot.configure(text_color=T["red"]),
                        self._stat.configure(
                            text=f"Menunggu {PROC_NAME}.exe ...", text_color=T["muted"])
                    ])
            except Exception:
                pass
            time.sleep(0.5)

    def _hotkey_thread(self):
        key_map = {
            VK_1: "god_mode",
            VK_2: "inf_hp",
            VK_3: "inf_coins",
            VK_4: "inf_keys",
            VK_5: "inf_bombs",
            VK_6: "turbo_speed",
            VK_7: "one_hit_ko",
        }
        prev = {k: False for k in key_map}
        prev[VK_0] = False
        prev[VK_8] = False
        prev[VK_9] = False

        while self._running:
            try:
                alt_down = (user32.GetAsyncKeyState(VK_ALT) & 0x8000) != 0
                if alt_down:
                    for vk, key in key_map.items():
                        pressed = (user32.GetAsyncKeyState(vk) & 0x8000) != 0
                        if pressed and not prev[vk]:
                            col = self._btn_refs[key][1]
                            self.after(0, lambda k=key, c=col: self._toggle_cheat(k, c))
                            time.sleep(0.2)
                        prev[vk] = pressed

                    # ALT + 8 : God Items Combo
                    p8 = (user32.GetAsyncKeyState(VK_8) & 0x8000) != 0
                    if p8 and not prev[VK_8]:
                        self.after(0, lambda: self._send_cmd("all_items"))
                        time.sleep(0.25)
                    prev[VK_8] = p8

                    # ALT + 9 : Kill Room
                    p9 = (user32.GetAsyncKeyState(VK_9) & 0x8000) != 0
                    if p9 and not prev[VK_9]:
                        self.after(0, lambda: self._send_cmd("kill_room"))
                        time.sleep(0.25)
                    prev[VK_9] = p9

                    # ALT + 0 : Panic Reset
                    p0 = (user32.GetAsyncKeyState(VK_0) & 0x8000) != 0
                    if p0 and not prev[VK_0]:
                        self.after(0, self._panic_reset)
                        time.sleep(0.25)
                    prev[VK_0] = p0
                else:
                    for k in prev:
                        prev[k] = False
            except Exception:
                pass
            time.sleep(0.04)

    def _launch_game(self):
        if os.path.exists(GAME_EXE):
            try:
                proc = subprocess.Popen([GAME_EXE, "--luadebug"], cwd=GAME_DIR)
                self._log.configure(text=f"Meluncurkan {PROC_NAME} (PID {proc.pid})...", text_color=T["green"])
                winsound.Beep(1000, 80)
            except Exception as e:
                self._log.configure(text=f"Launch error: {e}", text_color=T["red"])
        else:
            self._log.configure(text="isaac-ng.exe tidak ditemukan!", text_color=T["red"])
            winsound.Beep(300, 300)

    def on_closing(self):
        self._running = False
        self._panic_reset()
        self.destroy()


if __name__ == "__main__":
    app = IsaacModMenu()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
