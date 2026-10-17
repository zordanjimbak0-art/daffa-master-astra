GAME_EXE = r"D:\Game\Games\Subnautica-Below-Zero-SteamRIP.com\Subnautica Below Zero\SubnauticaZero.exe"
PROC     = "SubnauticaZero"
"""
================================================================================
ASTRA AI - SUBNAUTICA: BELOW ZERO DUAL-ENGINE MOD MENU v2.0
Engineered for Komandan DAFFA // AMD RX 580 // 60% Keyboard Optimized
DUAL-ENGINE ARCHITECTURE:
  1. ENGINE 1 (NATIVE SAVE PATCHER): 100% Crash-Proof Native Engine God Mode,
     Infinite Oxygen, Free Crafting, Unlock Blueprints, Zero Freezing, Docile Leviathans.
  2. ENGINE 2 (HARDWARE SCANCODE CONSOLE): Real-time live commands via Shift+Enter
     (Spawn Seatruck, Prawn Suit, Day/Night, Speed 2.5x, Resource Spawner).
No F1-F12 / Tilde / Numpad needed: 100% GUI Buttons + ALT+1..9 Hotkeys
================================================================================
"""

import os
import sys
import time
import json
import threading
import ctypes
import ctypes.wintypes as wt
import winsound
import customtkinter as ctk
import psutil

# ----------------- WIN32 API & SENDINPUT STRUCTURES (64-BIT EXACT) -----------------
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wt.LONG),
        ("dy", wt.LONG),
        ("mouseData", wt.DWORD),
        ("dwFlags", wt.DWORD),
        ("time", wt.DWORD),
        ("dwExtraInfo", ctypes.c_size_t)
    ]

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wt.WORD),
        ("wScan", wt.WORD),
        ("dwFlags", wt.DWORD),
        ("time", wt.DWORD),
        ("dwExtraInfo", ctypes.c_size_t)
    ]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wt.DWORD),
        ("wParamL", wt.WORD),
        ("wParamH", wt.WORD)
    ]

class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT)
    ]

class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wt.DWORD),
        ("u", INPUT_UNION)
    ]

INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

SCAN_LSHIFT = 0x2A
SCAN_RETURN = 0x1C

# Virtual Keys for 60% Keyboard (ALT + 1..0)
VK_MENU = 0x12
VK_0 = 0x30
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_6 = 0x36
VK_7 = 0x37
VK_8 = 0x38
VK_9 = 0x39
VK_N = 0x4E
VK_B = 0x42

# ----------------- UI THEME -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

THEME = {
    "bg_main": "#080D1A",
    "bg_card": "#10182B",
    "bg_card_hover": "#17233E",
    "border": "#1E2F52",
    "accent_cyan": "#00E5FF",
    "accent_emerald": "#10B981",
    "accent_amber": "#F59E0B",
    "accent_red": "#EF4444",
    "accent_purple": "#A855F7",
    "accent_blue": "#3B82F6",
    "text_main": "#F8FAFC",
    "text_muted": "#94A3B8"
}

# ----------------- SAVE PATH RESOLVER -----------------
def get_save_paths():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_dir, "Subnautica Below Zero", "SNAppData", "SavedGames"),
        os.path.join(base_dir, "SNAppData", "SavedGames"),
        r"D:\Game\Games\Subnautica-Below-Zero-SteamRIP.com\Subnautica Below Zero\SNAppData\SavedGames"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

class SubnauticaDualEngineModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("⚡ ASTRA // SUBNAUTICA: BELOW ZERO DUAL-ENGINE MOD MENU v3.0")
        self.geometry("520x780")
        self.minsize(480, 680)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.95)
        self.configure(fg_color=THEME["bg_main"])

        # State Variables
        self.game_pid = None
        self.game_hwnd = None
        self.save_dir = get_save_paths()
        self.active_slot = "slot0000"

        # Live Cheat Toggle States
        self.state_god = False
        self.state_oxygen = False
        self.state_craft = False
        self.state_fastbuild = False
        self.state_speed = False

        # 686-Item Master Catalog State
        self.all_items = self.load_catalog_items()
        self.displayed_items_limit = 50
        self.current_filtered_items = []

        self.setup_ui()
        self.start_background_worker()

    def load_catalog_items(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidates = [
            os.path.join(base_dir, "subnautica_bz_items.json"),
            r"D:\Game\Games\Subnautica-Below-Zero-SteamRIP.com\subnautica_bz_items.json"
        ]
        for p in candidates:
            if os.path.exists(p):
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        return json.load(f)
                except Exception:
                    pass
        return []

    def setup_ui(self):
        # 1. Header Card
        header = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=10, border_width=1, border_color=THEME["border"])
        header.pack(fill="x", padx=12, pady=(10, 6))

        title_lbl = ctk.CTkLabel(
            header,
            text="❄️ SUBNAUTICA: BELOW ZERO // ASTRA v2.0",
            font=("Consolas", 14, "bold"),
            text_color=THEME["accent_cyan"]
        )
        title_lbl.pack(anchor="w", padx=12, pady=(8, 2))

        sub_lbl = ctk.CTkLabel(
            header,
            text="DUAL-ENGINE SYSTEM // 60% KEYBOARD OPTIMIZED // KOMANDAN DAFFA",
            font=("Consolas", 9, "bold"),
            text_color=THEME["text_muted"]
        )
        sub_lbl.pack(anchor="w", padx=12, pady=(0, 6))

        # Status Bar
        status_box = ctk.CTkFrame(header, fg_color="#080C16", corner_radius=6)
        status_box.pack(fill="x", padx=10, pady=(0, 8))

        self.status_dot = ctk.CTkLabel(status_box, text="●", font=("Consolas", 12), text_color=THEME["accent_red"])
        self.status_dot.pack(side="left", padx=(8, 4), pady=3)

        self.status_text = ctk.CTkLabel(
            status_box,
            text="WAITING FOR SubnauticaZero.exe...",
            font=("Consolas", 10, "bold"),
            text_color=THEME["text_muted"]
        )
        self.status_text.pack(side="left", pady=3)

        self.save_status_lbl = ctk.CTkLabel(
            status_box,
            text="SAVE: CHECKING...",
            font=("Consolas", 9),
            text_color=THEME["accent_cyan"]
        )
        self.save_status_lbl.pack(side="right", padx=8, pady=3)

        # 2. Tabview
        self.tabs = ctk.CTkTabview(
            self,
            fg_color=THEME["bg_card"],
            segmented_button_fg_color="#080C16",
            segmented_button_selected_color=THEME["accent_blue"],
            segmented_button_unselected_color="#10182B",
            corner_radius=10
        )
        self.tabs.pack(fill="both", expand=True, padx=12, pady=(0, 8))

        tab_save = self.tabs.add("⚡ 1-KLIK ENGINE SAVE")
        tab_live = self.tabs.add("🎮 LIVE CONSOLE")
        tab_spawn = self.tabs.add("🎒 RESEP & ITEM")

        self.setup_save_engine_tab(tab_save)
        self.setup_live_console_tab(tab_live)
        self.setup_item_spawner_tab(tab_spawn)

        # 3. Bottom Controls
        bottom_box = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=10, height=36)
        bottom_box.pack(fill="x", padx=12, pady=(0, 10))

        op_lbl = ctk.CTkLabel(bottom_box, text="Transparansi:", font=("Consolas", 9), text_color=THEME["text_muted"])
        op_lbl.pack(side="left", padx=(10, 4), pady=6)

        op_slider = ctk.CTkSlider(bottom_box, from_=0.4, to=1.0, number_of_steps=12, width=100, command=self.change_opacity)
        op_slider.set(0.95)
        op_slider.pack(side="left", pady=6)

        launch_btn = ctk.CTkButton(
            bottom_box,
            text="▶ JALANKAN GAME",
            font=("Consolas", 10, "bold"),
            fg_color=THEME["accent_cyan"],
            text_color="#080D1A",
            hover_color="#00B4D8",
            width=110,
            height=26,
            command=self.launch_game
        )
        launch_btn.pack(side="right", padx=10, pady=6)

    # ----------------- TAB 1: SAVE ENGINE PATCHER -----------------
    def setup_save_engine_tab(self, parent):
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=2, pady=2)

        info_box = ctk.CTkFrame(scroll, fg_color="#0A1122", corner_radius=6, border_width=1, border_color="#1E2F52")
        info_box.pack(fill="x", pady=(2, 8))
        desc = (
            "💡 ENGINE INJECTOR LANGSUNG MERUBAH GAME ENGINE RULES DI SAVE GAME!\n"
            "• 100% Berfungsi tanpa butuh konsol, tanpa lag, kebal total!\n"
            "• Saat game di-load/dilanjutkan, cheat langsung aktif selamanya!"
        )
        ctk.CTkLabel(info_box, text=desc, font=("Consolas", 9), text_color="#38BDF8", justify="left").pack(padx=8, pady=6, anchor="w")

        # Master Buttons
        btn_all_on = ctk.CTkButton(
            scroll,
            text="⚡ AKTIFKAN NATIVE GOD MODE & UNLIMITED TOTAL",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["accent_emerald"],
            hover_color="#059669",
            text_color="#080D1A",
            height=34,
            command=self.apply_engine_all_cheats
        )
        btn_all_on.pack(fill="x", pady=4)

        btn_reset = ctk.CTkButton(
            scroll,
            text="🔄 KEMBALIKAN KE MODE NORMAL (RESET SAVE)",
            font=("Consolas", 10, "bold"),
            fg_color="#334155",
            hover_color="#475569",
            text_color=THEME["text_main"],
            height=28,
            command=self.reset_engine_to_normal
        )
        btn_reset.pack(fill="x", pady=2)

        # Checkboxes for Custom Rules
        ctk.CTkLabel(scroll, text="PILIHAN CHEAT SPESIFIK:", font=("Consolas", 10, "bold"), text_color=THEME["accent_amber"]).pack(anchor="w", pady=(8, 4))

        self.sw_god = self.create_switch(scroll, "🛡️ Kebal Total (Zero Damage dari Apapun)", True)
        self.sw_oxygen = self.create_switch(scroll, "🫁 Oksigen Abadi (O2 Never Depletes)", True)
        self.sw_craft = self.create_switch(scroll, "🛠️ Free Crafting (Bahan Gratis / No Cost)", True)
        self.sw_tech = self.create_switch(scroll, "🔓 Buka Semua Blueprint & Resep", True)
        self.sw_power = self.create_switch(scroll, "⚡ Daya Baterai & Base Abadi (No Power Required)", True)
        self.sw_freeze = self.create_switch(scroll, "❄️ Kebal Dingin (No Freezing / Hypothermia)", True)
        self.sw_hunger = self.create_switch(scroll, "🍖 Bebas Lapar & Bebas Haus", True)
        self.sw_crush = self.create_switch(scroll, "⚓ Kendaraan Kebal Tekanan Air (No Crush Damage)", True)
        self.sw_docile = self.create_switch(scroll, "🦈 Leviathan & Predator Jinak (Zero Aggression)", True)

        apply_custom_btn = ctk.CTkButton(
            scroll,
            text="💾 TERAPKAN PILIHAN KE SAVE GAME",
            font=("Consolas", 10, "bold"),
            fg_color=THEME["accent_blue"],
            hover_color="#2563EB",
            text_color="#FFFFFF",
            height=30,
            command=self.apply_engine_custom_cheats
        )
        apply_custom_btn.pack(fill="x", pady=(8, 4))

    def create_switch(self, parent, text, default_val):
        sw = ctk.CTkSwitch(
            parent,
            text=text,
            font=("Consolas", 10),
            text_color=THEME["text_main"],
            progress_color=THEME["accent_cyan"]
        )
        if default_val:
            sw.select()
        sw.pack(anchor="w", pady=3, padx=4)
        return sw

    # ----------------- TAB 2: LIVE CONSOLE INJECTOR -----------------
    def setup_live_console_tab(self, parent):
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=2, pady=2)

        info_box = ctk.CTkFrame(scroll, fg_color="#0A1122", corner_radius=6, border_width=1, border_color="#1E2F52")
        info_box.pack(fill="x", pady=(2, 6))
        desc = (
            "⌨️ LIVE CONSOLE (SHIFT + ENTER AUTO-INJECTOR):\n"
            "• Tekan Hotkey saat di dalam game, ATAU klik tombol [APPLY] di sini!\n"
            "• Dioptimalkan untuk Keyboard 60% (ALT+1 s/d ALT+0)."
        )
        ctk.CTkLabel(info_box, text=desc, font=("Consolas", 9), text_color="#38BDF8", justify="left").pack(padx=8, pady=4, anchor="w")

        # Toggles
        self.btn_god = self.create_cheat_toggle(scroll, "🛡️ GOD MODE (KEBAL)", "ALT+1", self.toggle_god)
        self.btn_oxygen = self.create_cheat_toggle(scroll, "🫁 INFINITE OXYGEN (O2)", "ALT+2", self.toggle_oxygen)
        self.btn_craft = self.create_cheat_toggle(scroll, "🛠️ FREE CRAFTING (NO COST)", "ALT+3", self.toggle_craft)
        self.btn_fastbuild = self.create_cheat_toggle(scroll, "🏗️ FAST BUILD (INSTAN)", "ALT+4", self.toggle_fastbuild)
        self.btn_speed = self.create_cheat_toggle(scroll, "⚡ SUPER SPEED (2.5x)", "ALT+5", self.toggle_speed)

        # Action Buttons
        self.create_action_btn(scroll, "☀️ SIANG TERANG (DAY)", "ALT+6", THEME["accent_amber"], self.cmd_day)
        self.create_action_btn(scroll, "🌙 MALAM HARI (NIGHT)", "ALT+N", THEME["accent_purple"], self.cmd_night)
        self.create_action_btn(scroll, "🚀 SPAWN SEATRUCK (KAPAL SELAM)", "ALT+7", THEME["accent_cyan"], self.cmd_spawn_seatruck)
        self.create_action_btn(scroll, "🤖 SPAWN PRAWN SUIT (ROBOT MECHA)", "ALT+8", THEME["accent_emerald"], self.cmd_spawn_exosuit)
        self.create_action_btn(scroll, "🔓 BUKA SEMUA BLUEPRINT", "ALT+B", THEME["accent_cyan"], self.cmd_unlock_all)
        self.create_action_btn(scroll, "🚨 PANIC / RESET NORMAL", "ALT+0", THEME["accent_red"], self.cmd_panic_reset)

    # ----------------- TAB 3: RESEP & ITEM SPAWNER (686 ITEMS) -----------------
    def setup_item_spawner_tab(self, parent):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=2, pady=2)

        # 1. Quick Presets Card
        preset_card = ctk.CTkFrame(container, fg_color="#0A1122", corner_radius=8, border_width=1, border_color="#1E2F52")
        preset_card.pack(fill="x", pady=(2, 6))

        ctk.CTkLabel(preset_card, text="⚡ PAKET CEPAT POPULER (1-KLIK):",
                     font=("Consolas", 9, "bold"), text_color=THEME["accent_cyan"]).pack(anchor="w", padx=8, pady=(4, 2))

        row1 = ctk.CTkFrame(preset_card, fg_color="transparent")
        row1.pack(fill="x", padx=6, pady=(0, 4))

        ctk.CTkButton(row1, text="💎 Starter Mineral (+5)", font=("Consolas", 8, "bold"),
                      fg_color=THEME["accent_cyan"], text_color="#080D1A", hover_color="#00B4D8", height=24,
                      command=lambda: self.send_compound_command("item titanium 5; item copper 5; item diamond 5")).pack(side="left", fill="x", expand=True, padx=2)

        ctk.CTkButton(row1, text="🤿 Complete Diving Pack", font=("Consolas", 8, "bold"),
                      fg_color=THEME["accent_blue"], text_color="#FFFFFF", hover_color="#2563EB", height=24,
                      command=lambda: self.send_compound_command("item highcapacitytank; item swimchargefins; item rebreather; item heatblade")).pack(side="left", fill="x", expand=True, padx=2)

        ctk.CTkButton(row1, text="❄️ Cold Suit Full Set", font=("Consolas", 8, "bold"),
                      fg_color=THEME["accent_purple"], text_color="#FFFFFF", hover_color="#9333EA", height=24,
                      command=lambda: self.send_compound_command("item coldsuitsuit; item coldsuitgloves; item coldsuithelmet")).pack(side="left", fill="x", expand=True, padx=2)

        row2 = ctk.CTkFrame(preset_card, fg_color="transparent")
        row2.pack(fill="x", padx=6, pady=(0, 6))

        ctk.CTkButton(row2, text="⚡ 5x Ion Cube + Ion Battery", font=("Consolas", 8, "bold"),
                      fg_color=THEME["accent_amber"], text_color="#080D1A", hover_color="#D97706", height=24,
                      command=lambda: self.send_compound_command("item precursorioncrystal 5; item precursorionbattery 2")).pack(side="left", fill="x", expand=True, padx=2)

        ctk.CTkButton(row2, text="🚀 All Seatruck Modules Pack", font=("Consolas", 8, "bold"),
                      fg_color=THEME["accent_emerald"], text_color="#080D1A", hover_color="#059669", height=24,
                      command=lambda: self.send_compound_command("item seatruck; item seatruckaquariummodule; item seatruckfabricatormodule; item seatrucksleepermodule; item seatruckstoragemodule; item seatruckteleportationmodule; item seatruckdockingmodule")).pack(side="left", fill="x", expand=True, padx=2)

        # 2. Search & Controls Bar
        ctrl_card = ctk.CTkFrame(container, fg_color=THEME["bg_card"], corner_radius=8, border_width=1, border_color=THEME["border"])
        ctrl_card.pack(fill="x", pady=(0, 6))

        # Search Bar
        search_row = ctk.CTkFrame(ctrl_card, fg_color="transparent")
        search_row.pack(fill="x", padx=8, pady=(6, 4))

        self.search_entry = ctk.CTkEntry(
            search_row,
            placeholder_text="🔍 Cari nama atau ID item (mis: diamond, seatruck, ion, cold)...",
            font=("Consolas", 9),
            fg_color="#080D1A",
            border_color=THEME["border"]
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 4))
        self.search_entry.bind("<KeyRelease>", lambda e: self.filter_items())

        ctk.CTkButton(
            search_row, text="RESET", width=50, height=26, font=("Consolas", 8, "bold"),
            fg_color="#334155", hover_color="#475569", command=self.reset_search
        ).pack(side="right")

        # Filter & Options Row
        filter_row = ctk.CTkFrame(ctrl_card, fg_color="transparent")
        filter_row.pack(fill="x", padx=8, pady=(0, 6))

        # Categories Dropdown
        categories = [
            f"Semua Kategori ({len(self.all_items)})",
            "Material Mentah & Mineral",
            "Bahan Fabrikasi & Elektronik",
            "Alat & Peralatan",
            "Pakaian & Baju Dingin",
            "Kendaraan & Modul Seatruck",
            "Bagian Pangkalan (Base)",
            "Interior & Dekorasi",
            "Fauna & Hewan Laut",
            "Telur Makhluk (Eggs)",
            "Tanaman, Benih & Konsumsi",
            "Alien & Komponen Alan",
            "Lain-lain (Misc)"
        ]
        self.cat_var = ctk.StringVar(value=categories[0])
        self.cat_menu = ctk.CTkOptionMenu(
            filter_row,
            values=categories,
            variable=self.cat_var,
            command=lambda v: self.filter_items(),
            font=("Consolas", 8),
            dropdown_font=("Consolas", 8),
            fg_color="#080D1A",
            button_color=THEME["accent_blue"],
            width=180,
            height=26
        )
        self.cat_menu.pack(side="left", padx=(0, 4))

        # Quantity Selector
        ctk.CTkLabel(filter_row, text="Jml:", font=("Consolas", 9), text_color=THEME["text_muted"]).pack(side="left", padx=(4, 2))
        self.qty_var = ctk.StringVar(value="1")
        self.qty_menu = ctk.CTkOptionMenu(
            filter_row,
            values=["1", "5", "10", "25", "50"],
            variable=self.qty_var,
            font=("Consolas", 8),
            dropdown_font=("Consolas", 8),
            fg_color="#080D1A",
            button_color="#334155",
            width=55,
            height=26
        )
        self.qty_menu.pack(side="left", padx=(0, 4))

        # Mode Selector
        self.mode_var = ctk.StringVar(value="Inventori")
        self.mode_seg = ctk.CTkSegmentedButton(
            filter_row,
            values=["Inventori", "Di Depan"],
            variable=self.mode_var,
            font=("Consolas", 8, "bold"),
            selected_color=THEME["accent_cyan"],
            selected_hover_color="#00B4D8",
            unselected_color="#080D1A",
            height=26
        )
        self.mode_seg.pack(side="right")

        # 3. Status Bar Count
        self.count_lbl = ctk.CTkLabel(
            container,
            text=f"Menampilkan 0 dari {len(self.all_items)} item katalog",
            font=("Consolas", 8),
            text_color=THEME["accent_cyan"]
        )
        self.count_lbl.pack(anchor="w", padx=6, pady=(0, 2))

        # 4. Scrollable Frame for Items
        self.item_scroll = ctk.CTkScrollableFrame(container, fg_color="transparent")
        self.item_scroll.pack(fill="both", expand=True, padx=2, pady=(0, 2))

        # Initial render
        self.filter_items()

    def reset_search(self):
        self.search_entry.delete(0, "end")
        self.cat_var.set(f"Semua Kategori ({len(self.all_items)})")
        self.filter_items()

    def filter_items(self):
        query = self.search_entry.get().strip().lower()
        selected_cat = self.cat_var.get()

        filtered = []
        for item in self.all_items:
            # Check category
            if not selected_cat.startswith("Semua Kategori") and item.get("category") != selected_cat:
                continue
            # Check search text
            if query:
                if query not in item["name"].lower() and query not in item["id"].lower():
                    continue
            filtered.append(item)

        self.current_filtered_items = filtered
        self.displayed_items_limit = 50
        self.render_items_list()

    def render_items_list(self):
        for widget in self.item_scroll.winfo_children():
            widget.destroy()

        total = len(self.current_filtered_items)
        shown = min(self.displayed_items_limit, total)
        self.count_lbl.configure(text=f"Menampilkan {shown} dari {total} item ditemukan (Katalog: {len(self.all_items)} Item)")

        for item in self.current_filtered_items[:shown]:
            self.create_catalog_item_card(self.item_scroll, item)

        if shown < total:
            more_btn = ctk.CTkButton(
                self.item_scroll,
                text=f"▼ TAMPILKAN 50 ITEM BERIKUTNYA (SISA {total - shown})...",
                font=("Consolas", 9, "bold"),
                fg_color="#1E293B",
                hover_color=THEME["accent_blue"],
                height=28,
                command=self.load_more_items
            )
            more_btn.pack(fill="x", pady=6, padx=4)

    def load_more_items(self):
        self.displayed_items_limit += 50
        self.render_items_list()

    def create_catalog_item_card(self, parent, item):
        name = item["name"]
        sid = item["id"]
        cat = item.get("category", "General")

        box = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_width=1, border_color=THEME["border"], corner_radius=6)
        box.pack(fill="x", pady=2, padx=2)

        info = ctk.CTkFrame(box, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=8, pady=4)

        title_lbl = ctk.CTkLabel(info, text=name, font=("Consolas", 9, "bold"), text_color=THEME["text_main"], anchor="w")
        title_lbl.pack(anchor="w")

        meta_lbl = ctk.CTkLabel(info, text=f"[{cat}] ID: {sid}", font=("Consolas", 8), text_color=THEME["text_muted"], anchor="w")
        meta_lbl.pack(anchor="w")

        btn = ctk.CTkButton(
            box,
            text="+SPAWN",
            width=64,
            height=24,
            font=("Consolas", 9, "bold"),
            fg_color=THEME["accent_cyan"],
            hover_color="#00B4D8",
            text_color="#080D1A",
            corner_radius=4,
            command=lambda i_id=sid, i_name=name: self.spawn_catalog_item(i_id, i_name)
        )
        btn.pack(side="right", padx=6, pady=4)

    def spawn_catalog_item(self, item_id, item_name):
        qty = self.qty_var.get()
        mode = self.mode_var.get()
        prefix = "item" if mode == "Inventori" else "spawn"
        cmd = f"{prefix} {item_id} {qty}"
        self.send_game_command(cmd)
        self.status_text.configure(text=f"SPAWN: {item_name} x{qty} ({prefix})", text_color=THEME["accent_emerald"])

    def create_cheat_toggle(self, parent, title, hotkey, command):
        box = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_width=1, border_color=THEME["border"], corner_radius=8)
        box.pack(fill="x", padx=2, pady=3)

        info = ctk.CTkFrame(box, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=8, pady=6)

        lbl = ctk.CTkLabel(info, text=title, font=("Consolas", 10, "bold"), text_color=THEME["text_main"], anchor="w")
        lbl.pack(anchor="w")

        hk_badge = ctk.CTkLabel(info, text=f"HOTKEY: {hotkey}", font=("Consolas", 9), text_color=THEME["accent_cyan"], anchor="w")
        hk_badge.pack(anchor="w")

        btn = ctk.CTkButton(
            box,
            text="OFF",
            width=54,
            height=26,
            font=("Consolas", 10, "bold"),
            fg_color="#1E293B",
            hover_color="#334155",
            text_color=THEME["text_muted"],
            corner_radius=6,
            command=command
        )
        btn.pack(side="right", padx=8, pady=6)
        return btn

    def create_action_btn(self, parent, title, hotkey, color, command):
        box = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_width=1, border_color=THEME["border"], corner_radius=8)
        box.pack(fill="x", padx=2, pady=3)

        info = ctk.CTkFrame(box, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=8, pady=5)

        lbl = ctk.CTkLabel(info, text=title, font=("Consolas", 10, "bold"), text_color=THEME["text_main"], anchor="w")
        lbl.pack(anchor="w")

        hk_badge = ctk.CTkLabel(info, text=f"TRIGGER: {hotkey}", font=("Consolas", 9), text_color=color, anchor="w")
        hk_badge.pack(anchor="w")

        btn = ctk.CTkButton(
            box,
            text="APPLY",
            width=54,
            height=24,
            font=("Consolas", 9, "bold"),
            fg_color=color,
            hover_color="#334155",
            text_color="#080D1A" if color != THEME["accent_red"] else "#FFFFFF",
            corner_radius=6,
            command=command
        )
        btn.pack(side="right", padx=8, pady=5)

    def change_opacity(self, val):
        self.attributes("-alpha", float(val))

    # ==================== ENGINE 1: SAVE PATCHER IMPLEMENTATION ====================
    def get_gameinfo_path(self):
        if not self.save_dir:
            self.save_dir = get_save_paths()
        if not self.save_dir or not os.path.exists(self.save_dir):
            return None
        slot_path = os.path.join(self.save_dir, self.active_slot, "gameinfo.json")
        if os.path.exists(slot_path):
            return slot_path
        # Search first available slot
        for entry in os.listdir(self.save_dir):
            p = os.path.join(self.save_dir, entry, "gameinfo.json")
            if os.path.exists(p):
                self.active_slot = entry
                return p
        return None

    def read_save_gameinfo(self):
        p = self.get_gameinfo_path()
        if not p or not os.path.exists(p):
            return None, "File save tidak ditemukan!"
        try:
            with open(p, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            return data, p
        except Exception as e:
            return None, str(e)

    def write_save_gameinfo(self, data, path):
        try:
            # Backup original first
            bak = path + ".bak_astra"
            if not os.path.exists(bak):
                with open(path, "rb") as src, open(bak, "wb") as dst:
                    dst.write(src.read())
            # Save patched json with utf-8-sig
            with open(path, "w", encoding="utf-8-sig") as f:
                json.dump(data, f, ensure_ascii=False)
            return True, "Sukses!"
        except Exception as e:
            return False, str(e)

    def apply_engine_all_cheats(self):
        data, path = self.read_save_gameinfo()
        if not data:
            self.status_text.configure(text=f"SAVE ERROR: {path}", text_color=THEME["accent_red"])
            winsound.Beep(600, 200)
            return

        opts = data.setdefault("gameOptions", {})
        opts["playerDamageTakenModifier"] = 0.0
        opts["oxygenDepletes"] = False
        opts["craftingRequiresResources"] = False
        opts["techRequiresUnlocking"] = False
        opts["technologyRequiresPower"] = False
        opts["bodyTemperatureDecreases"] = False
        opts["hunger"] = False
        opts["thirst"] = False
        opts["vehicleWaterPressureDamage"] = False
        opts["baseWaterPressureDamage"] = False
        opts["creatureAggressionModifier"] = 0.0

        ok, msg = self.write_save_gameinfo(data, path)
        if ok:
            winsound.Beep(1800, 150)
            winsound.Beep(2400, 200)
            self.save_status_lbl.configure(text=f"{self.active_slot}: NATIVE GOD MODE ON!", text_color=THEME["accent_emerald"])
        else:
            self.save_status_lbl.configure(text=f"ERROR: {msg}", text_color=THEME["accent_red"])

    def apply_engine_custom_cheats(self):
        data, path = self.read_save_gameinfo()
        if not data:
            self.status_text.configure(text=f"SAVE ERROR: {path}", text_color=THEME["accent_red"])
            return

        opts = data.setdefault("gameOptions", {})
        opts["playerDamageTakenModifier"] = 0.0 if self.sw_god.get() else 1.0
        opts["oxygenDepletes"] = not self.sw_oxygen.get()
        opts["craftingRequiresResources"] = not self.sw_craft.get()
        opts["techRequiresUnlocking"] = not self.sw_tech.get()
        opts["technologyRequiresPower"] = not self.sw_power.get()
        opts["bodyTemperatureDecreases"] = not self.sw_freeze.get()
        opts["hunger"] = not self.sw_hunger.get()
        opts["thirst"] = not self.sw_hunger.get()
        opts["vehicleWaterPressureDamage"] = not self.sw_crush.get()
        opts["creatureAggressionModifier"] = 0.0 if self.sw_docile.get() else 1.0

        ok, msg = self.write_save_gameinfo(data, path)
        if ok:
            winsound.Beep(1600, 150)
            self.save_status_lbl.configure(text=f"{self.active_slot}: CUSTOM RULES SAVED!", text_color=THEME["accent_cyan"])
        else:
            self.save_status_lbl.configure(text=f"ERROR: {msg}", text_color=THEME["accent_red"])

    def reset_engine_to_normal(self):
        data, path = self.read_save_gameinfo()
        if not data:
            return

        bak = path + ".bak_astra"
        if os.path.exists(bak):
            try:
                with open(bak, "rb") as src, open(path, "wb") as dst:
                    dst.write(src.read())
                winsound.Beep(1000, 150)
                self.save_status_lbl.configure(text=f"{self.active_slot}: RESTORED FROM BACKUP!", text_color=THEME["text_muted"])
                return
            except Exception:
                pass

        # Fallback reset manually
        opts = data.setdefault("gameOptions", {})
        opts["playerDamageTakenModifier"] = 1.0
        opts["oxygenDepletes"] = True
        opts["craftingRequiresResources"] = True
        opts["techRequiresUnlocking"] = True
        opts["technologyRequiresPower"] = True
        opts["bodyTemperatureDecreases"] = True
        opts["hunger"] = True
        opts["thirst"] = True
        opts["vehicleWaterPressureDamage"] = True
        opts["creatureAggressionModifier"] = 1.0

        ok, _ = self.write_save_gameinfo(data, path)
        if ok:
            winsound.Beep(800, 150)
            self.save_status_lbl.configure(text=f"{self.active_slot}: RESET TO DEFAULT", text_color=THEME["text_muted"])

    # ==================== ENGINE 2: LIVE CONSOLE INJECTOR ====================
    def send_scancode_key(self, scan, is_down=True):
        flags = KEYEVENTF_SCANCODE
        if not is_down:
            flags |= KEYEVENTF_KEYUP
        inp = INPUT()
        inp.type = INPUT_KEYBOARD
        inp.u.ki = KEYBDINPUT(0, scan, flags, 0, 0)
        user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    def send_unicode_char(self, ch):
        inp = INPUT()
        inp.type = INPUT_KEYBOARD
        inp.u.ki = KEYBDINPUT(0, ord(ch), KEYEVENTF_UNICODE, 0, 0)
        user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))
        inp.u.ki = KEYBDINPUT(0, ord(ch), KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, 0)
        user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    def focus_game_window(self):
        """Bawa game ke foreground jika dipanggil dari klik tombol GUI"""
        hwnd = self.find_game_window()
        if hwnd:
            try:
                cur_thread = kernel32.GetCurrentThreadId()
                game_thread = user32.GetWindowThreadProcessId(hwnd, None)
                user32.AttachThreadInput(cur_thread, game_thread, True)
                user32.ShowWindow(hwnd, 9) # SW_RESTORE
                user32.SetForegroundWindow(hwnd)
                user32.BringWindowToTop(hwnd)
                user32.AttachThreadInput(cur_thread, game_thread, False)
                time.sleep(0.12)
            except Exception:
                pass

    def send_game_command(self, cmd_text):
        """Kirim perintah konsol via Shift+Enter dan hardware scan codes"""
        # Guard: Pastikan game sedang berjalan dan memiliki jendela aktif
        hwnd = self.find_game_window()
        if not hwnd and not self.game_pid:
            self.status_text.configure(text="GAME TIDAK AKTIF! Jalankan Subnautica dahulu.", text_color=THEME["accent_red"])
            winsound.Beep(500, 150)
            return

        winsound.Beep(1200, 50)
        # 1. Pastikan jendela game aktif jika diklik via GUI
        self.focus_game_window()

        # 2. Buka Console via Shift + Enter (Scan Code 0x2A + 0x1C)
        self.send_scancode_key(SCAN_LSHIFT, True)
        time.sleep(0.02)
        self.send_scancode_key(SCAN_RETURN, True)
        time.sleep(0.04)
        self.send_scancode_key(SCAN_RETURN, False)
        time.sleep(0.02)
        self.send_scancode_key(SCAN_LSHIFT, False)

        # 3. Tunggu animasi slide console Subnautica
        time.sleep(0.35)

        # 4. Ketik teks perintah
        for ch in cmd_text:
            self.send_unicode_char(ch)
            time.sleep(0.015)

        time.sleep(0.06)

        # 5. Eksekusi Enter
        self.send_scancode_key(SCAN_RETURN, True)
        time.sleep(0.04)
        self.send_scancode_key(SCAN_RETURN, False)

    def send_compound_command(self, compound_cmd):
        for cmd in compound_cmd.split(";"):
            c = cmd.strip()
            if c:
                self.send_game_command(c)
                time.sleep(0.2)

    def find_game_window(self):
        # 1. Cek dari PID yang terdeteksi
        if self.game_pid:
            found = []
            WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_int, wt.HWND, wt.LPARAM)
            def enum_cb(h, _):
                if user32.IsWindowVisible(h):
                    p = wt.DWORD()
                    user32.GetWindowThreadProcessId(h, ctypes.byref(p))
                    if p.value == self.game_pid:
                        found.append(h)
                return 1
            user32.EnumWindows(WNDENUMPROC(enum_cb), 0)
            if found:
                return found[0]

        # 2. Cek Nama Window Standar
        h = user32.FindWindowW(None, "Subnautica Below Zero")
        if h: return h
        h = user32.FindWindowW("UnityWndClass", None)
        if h: return h
        return 0

    # ----------------- TOGGLES -----------------
    def toggle_god(self):
        self.state_god = not self.state_god
        if self.state_god:
            self.send_game_command("nodamage")
            self.btn_god.configure(text="ON", fg_color=THEME["accent_emerald"], text_color="#080D1A")
            winsound.Beep(1400, 100)
        else:
            self.send_game_command("nodamage")
            self.btn_god.configure(text="OFF", fg_color="#1E293B", text_color=THEME["text_muted"])
            winsound.Beep(800, 100)

    def toggle_oxygen(self):
        self.state_oxygen = not self.state_oxygen
        if self.state_oxygen:
            self.send_game_command("oxygen")
            self.btn_oxygen.configure(text="ON", fg_color=THEME["accent_cyan"], text_color="#080D1A")
            winsound.Beep(1400, 100)
        else:
            self.send_game_command("oxygen")
            self.btn_oxygen.configure(text="OFF", fg_color="#1E293B", text_color=THEME["text_muted"])
            winsound.Beep(800, 100)

    def toggle_craft(self):
        self.state_craft = not self.state_craft
        if self.state_craft:
            self.send_game_command("nocost")
            self.btn_craft.configure(text="ON", fg_color=THEME["accent_amber"], text_color="#080D1A")
            winsound.Beep(1400, 100)
        else:
            self.send_game_command("nocost")
            self.btn_craft.configure(text="OFF", fg_color="#1E293B", text_color=THEME["text_muted"])
            winsound.Beep(800, 100)

    def toggle_fastbuild(self):
        self.state_fastbuild = not self.state_fastbuild
        if self.state_fastbuild:
            self.send_game_command("fastbuild")
            self.btn_fastbuild.configure(text="ON", fg_color=THEME["accent_purple"], text_color="#FFFFFF")
            winsound.Beep(1400, 100)
        else:
            self.send_game_command("fastbuild")
            self.btn_fastbuild.configure(text="OFF", fg_color="#1E293B", text_color=THEME["text_muted"])
            winsound.Beep(800, 100)

    def toggle_speed(self):
        self.state_speed = not self.state_speed
        if self.state_speed:
            self.send_game_command("speed 2.5")
            self.btn_speed.configure(text="ON", fg_color=THEME["accent_cyan"], text_color="#080D1A")
            winsound.Beep(1400, 100)
        else:
            self.send_game_command("speed 1.0")
            self.btn_speed.configure(text="OFF", fg_color="#1E293B", text_color=THEME["text_muted"])
            winsound.Beep(800, 100)

    # ----------------- ACTION METHODS -----------------
    def cmd_day(self):
        self.send_game_command("day")

    def cmd_night(self):
        self.send_game_command("night")

    def cmd_spawn_seatruck(self):
        self.send_game_command("spawn seatruck")

    def cmd_spawn_exosuit(self):
        self.send_game_command("spawn exosuit")

    def cmd_unlock_all(self):
        self.send_game_command("unlockall")

    def cmd_panic_reset(self):
        self.send_game_command("speed 1.0")
        if self.state_god: self.toggle_god()
        if self.state_oxygen: self.toggle_oxygen()
        if self.state_craft: self.toggle_craft()
        if self.state_fastbuild: self.toggle_fastbuild()
        winsound.Beep(600, 250)

    def launch_game(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        game_dir = os.path.join(base_dir, "Subnautica Below Zero")
        game_path = os.path.join(game_dir, "SubnauticaZero.exe")
        if os.path.exists(game_path):
            try:
                import subprocess
                subprocess.Popen([game_path], cwd=game_dir)
                winsound.Beep(1000, 80)
            except Exception:
                os.startfile(game_path)

    # ----------------- BACKGROUND WORKER & 60% KEYBOARD HOTKEYS -----------------
    def start_background_worker(self):
        t = threading.Thread(target=self.hotkey_and_monitor_loop, daemon=True)
        t.start()

    def hotkey_and_monitor_loop(self):
        while True:
            try:
                # 1. Deteksi Proses Game
                running = False
                for p in psutil.process_iter(['name', 'pid']):
                    pname = p.info['name']
                    if pname and 'subnauticazero' in pname.lower():
                        self.game_pid = p.info['pid']
                        running = True
                        break

                if running:
                    self.status_dot.configure(text_color=THEME["accent_emerald"])
                    self.status_text.configure(text=f"CONNECTED: SubnauticaZero (PID {self.game_pid})", text_color=THEME["accent_emerald"])
                else:
                    self.game_pid = None
                    self.status_dot.configure(text_color=THEME["accent_red"])
                    self.status_text.configure(text="WAITING FOR SubnauticaZero.exe...", text_color=THEME["text_muted"])

                # 2. Cek Status Save Slot
                save_p = self.get_gameinfo_path()
                if save_p:
                    self.save_status_lbl.configure(text=f"SAVE: {self.active_slot} (READY)", text_color=THEME["accent_cyan"])
                else:
                    self.save_status_lbl.configure(text="SAVE: NOT FOUND", text_color=THEME["text_muted"])

                # 3. Global Hotkey Scanner (Khusus Keyboard 60% tanpa F1-F12)
                alt_down = (user32.GetAsyncKeyState(VK_MENU) & 0x8000) != 0
                if alt_down:
                    if user32.GetAsyncKeyState(VK_1) & 0x8000:
                        self.toggle_god()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_2) & 0x8000:
                        self.toggle_oxygen()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_3) & 0x8000:
                        self.toggle_craft()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_4) & 0x8000:
                        self.toggle_fastbuild()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_5) & 0x8000:
                        self.toggle_speed()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_6) & 0x8000:
                        self.cmd_day()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_7) & 0x8000:
                        self.cmd_spawn_seatruck()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_8) & 0x8000:
                        self.cmd_spawn_exosuit()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_9) & 0x8000:
                        self.send_compound_command("item titanium 5; item copper 5; item diamond 5")
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_B) & 0x8000:
                        self.cmd_unlock_all()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_N) & 0x8000:
                        self.cmd_night()
                        time.sleep(0.35)
                    elif user32.GetAsyncKeyState(VK_0) & 0x8000:
                        self.cmd_panic_reset()
                        time.sleep(0.35)

            except Exception:
                pass
            time.sleep(0.08)

if __name__ == "__main__":
    app = SubnauticaDualEngineModMenu()
    app.mainloop()

