import os
import shutil
import subprocess
from upgrade_daffa_master_v6 import generate_cyber_cover, COVERS_DIR, safe_filename

SYS_DIR = r"D:\Game\DAFFA_SYSTEM"
GUI_PATH = os.path.join(SYS_DIR, "Daffa_Master_GUI.py")
BAK_PATH = os.path.join(SYS_DIR, "Daffa_Master_GUI.py.bak_v5")

# Ensure Metal Slug cover exists
ms_path = os.path.join(COVERS_DIR, safe_filename("Metal Slug"))
if not os.path.exists(ms_path):
    generate_cyber_cover("Metal Slug", "RUN & GUN ARCADE • MOD", "#F59E0B", size=(240, 112)).save(ms_path, "PNG")
    generate_cyber_cover("Metal Slug", "RUN & GUN ARCADE • MOD", "#F59E0B", size=(420, 196)).save(ms_path.replace(".png", "_hero.png"), "PNG")
    print("[OK] Generated Metal_Slug.png cover art")

if os.path.exists(GUI_PATH) and not os.path.exists(BAK_PATH):
    shutil.copy2(GUI_PATH, BAK_PATH)
    print(f"[BACKUP] Saved {BAK_PATH}")

with open(GUI_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update window title & version badge to v6.0 ULTRA (ROG / STEAM EDITION)
code = code.replace(
    'self.title("⚔️ DAFFA MASTER COMMAND CENTER v5.0 // ASTRA AI PROTOCOL")',
    'self.title("⚔️ DAFFA MASTER COMMAND CENTER v6.0 ULTRA // STEAM & ROG ARMOURY EDITION")'
)
code = code.replace(
    'text="ASTRA CORE v5.0"',
    'text="v6.0 ULTRA // GITHUB EDITION"'
)

# 2. Add Live GitHub Theme Switcher pill in setup_header right next to war_room_pill
if "self.theme_pill =" not in code and "self.war_room_pill.pack(side=\"left\", padx=4)" in code:
    theme_btn_code = '''        self.war_room_pill.pack(side="left", padx=4)

        # Live GitHub Theme Switcher Pill
        self.theme_pill = ctk.CTkButton(
            self.hud_box,
            text="🎨 THEME: CYBER",
            font=("Consolas", 11, "bold"),
            fg_color="#1E1B4B",
            hover_color="#312E81",
            text_color="#A855F7",
            corner_radius=6,
            width=125,
            height=28,
            command=self.cycle_github_theme
        )
        self.theme_pill.pack(side="left", padx=4)'''
    code = code.replace('        self.war_room_pill.pack(side="left", padx=4)', theme_btn_code, 1)

# 3. Replace setup_center_panel, populate_cards, and create_game_card with the new v6.0 Hero Banner + HD Cover Art Cards
start_marker = "    # ==================== CENTER PANEL"
end_marker = "    # ==================== RIGHT COMMAND CENTER ===================="

assert start_marker in code and end_marker in code, "Markers not found in Daffa_Master_GUI.py"

new_center_and_cards = '''    # ==================== CENTER PANEL (v6.0 STEAM / ROG HERO EDITION) ====================
    def cycle_github_theme(self):
        """Ganti tema palet UI secara live dari koleksi GitHub CTkThemesPack."""
        presets = [
            ("CYBER",   "#080C14", "#0E1524", "#111A2E", "#00E5FF"),
            ("CRIMSON", "#120609", "#1C0A10", "#281018", "#EF4444"),
            ("NEON",    "#0D0718", "#160C28", "#21133B", "#A855F7"),
            ("MATRIX",  "#05120C", "#0A1F15", "#102E20", "#10B981"),
        ]
        idx = (getattr(self, "_gh_theme_idx", 0) + 1) % len(presets)
        self._gh_theme_idx = idx
        t_name, bg_m, bg_p, bg_c, acc = presets[idx]
        THEME["bg_main"] = bg_m
        THEME["bg_panel"] = bg_p
        THEME["bg_card"] = bg_c
        THEME["accent_cyan"] = acc

        try:
            self.configure(fg_color=bg_m)
            self.header_frame.configure(fg_color=bg_p, border_color=acc)
            self.sidebar.configure(fg_color=bg_p, border_color=acc)
            self.center_panel.configure(fg_color=bg_p, border_color=acc)
            self.cmd_panel.configure(fg_color=bg_p, border_color=acc)
            self.bottom_bar.configure(fg_color=bg_p, border_color=acc)
            self.hero_frame.configure(border_color=acc)
            self.theme_pill.configure(text=f"🎨 THEME: {t_name}", text_color=acc)
            self.show_toast(f"🎨 GITHUB THEME: {t_name}", f"Palet warna diupdate ke {t_name} Mode!", color=acc, duration=2000)
        except Exception:
            pass

    def _safe_cover_filename(self, name: str) -> str:
        return "".join(c if c.isalnum() else "_" for c in name).strip("_") + ".png"

    def _get_cover_image(self, item: dict, size=(126, 62), is_hero=False):
        from PIL import Image
        if not hasattr(self, "_cover_cache"):
            self._cover_cache = {}
        key = (item["name"], size, is_hero)
        if key in self._cover_cache:
            return self._cover_cache[key]

        covers_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "game_covers")
        base_fn = self._safe_cover_filename(item["name"])
        hero_fn = base_fn.replace(".png", "_hero.png")
        target_path = os.path.join(covers_dir, hero_fn if is_hero else base_fn)
        if not os.path.exists(target_path):
            target_path = os.path.join(covers_dir, base_fn)

        if not os.path.exists(target_path):
            try:
                from upgrade_daffa_master_v6 import generate_cyber_cover
                os.makedirs(covers_dir, exist_ok=True)
                im_gen = generate_cyber_cover(item["name"], item.get("genre", "ASTRA MODULE"), item.get("color", "#00E5FF"), size=(240, 112))
                im_gen.save(target_path, "PNG")
            except Exception:
                return None

        try:
            pil_im = Image.open(target_path).convert("RGBA")
            ctk_im = ctk.CTkImage(light_image=pil_im, dark_image=pil_im, size=size)
            self._cover_cache[key] = ctk_im
            return ctk_im
        except Exception:
            return None

    def select_hero_item(self, item: dict):
        """Update Hero Showcase Banner di bagian atas katalog saat game dipilih."""
        self.selected_hero_item = item
        if not hasattr(self, "hero_frame") or not self.hero_frame.winfo_exists():
            return
        color = item.get("color", THEME["accent_cyan"])
        self.hero_frame.configure(border_color=color)

        hero_img = self._get_cover_image(item, size=(216, 100), is_hero=True)
        if hero_img:
            self.hero_cover_lbl.configure(image=hero_img, text="")
        else:
            self.hero_cover_lbl.configure(image=None, text=item.get("icon", "🎮"))

        self.hero_title_lbl.configure(text=f"{item.get('icon', '🎮')}  {item['name'].upper()}", text_color=THEME["text_main"])
        self.hero_status_pill.configure(text=item.get("status", "READY"), text_color=color)
        self.hero_genre_lbl.configure(
            text=f"🎯 {item.get('genre', 'Game')}   •   📂 {item.get('category', 'MODS')}   •   ⏱️ Dimainkan: {self._last_played_str(item['name'])}"
        )

        hks = item.get("hotkeys", [])
        if isinstance(hks, dict):
            hk_list = [f"{k}: {v}" for k, v in hks.items()]
        else:
            hk_list = list(hks)
        hk_preview = "   |   ".join(hk_list[:3]) if hk_list else "Siap dijalankan dengan optimasi penuh ASTRA AI."
        self.hero_hk_lbl.configure(text=f"⚡ Fitur & Hotkey: {hk_preview}")

        self.hero_play_btn.configure(
            fg_color=color,
            hover_color=THEME["accent_emerald"],
            command=lambda it=item: self.launch_item(it)
        )
        self.hero_hk_btn.configure(command=lambda it=item: self.show_hotkey_guide(it))
        self.hero_folder_btn.configure(command=lambda it=item: self.open_item_folder(it))

    def setup_center_panel(self):
        # ── 1. FEATURED HERO SHOWCASE BANNER (STEAM / ROG STYLE) ──
        self.hero_frame = ctk.CTkFrame(
            self.center_panel,
            fg_color="#0B1322",
            corner_radius=12,
            border_width=2,
            border_color=THEME["accent_cyan"],
            height=122
        )
        self.hero_frame.pack(fill="x", padx=14, pady=(12, 6))
        self.hero_frame.pack_propagate(False)

        self.hero_cover_lbl = ctk.CTkLabel(
            self.hero_frame,
            text="",
            width=216,
            height=100,
            fg_color="#070C16",
            corner_radius=10
        )
        self.hero_cover_lbl.pack(side="left", padx=(12, 14), pady=10)

        hero_mid = ctk.CTkFrame(self.hero_frame, fg_color="transparent")
        hero_mid.pack(side="left", fill="both", expand=True, pady=10)

        top_title_row = ctk.CTkFrame(hero_mid, fg_color="transparent")
        top_title_row.pack(fill="x")

        self.hero_title_lbl = ctk.CTkLabel(
            top_title_row,
            text="🦁  MY VOICE ZOO",
            font=("Consolas", 16, "bold"),
            text_color=THEME["text_main"],
            anchor="w"
        )
        self.hero_title_lbl.pack(side="left")

        self.hero_status_pill = ctk.CTkLabel(
            top_title_row,
            text="⚡ ASTRA MOD MENU",
            font=("Consolas", 9, "bold"),
            fg_color="#051C2C",
            text_color=THEME["accent_cyan"],
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.hero_status_pill.pack(side="left", padx=10)

        self.hero_genre_lbl = ctk.CTkLabel(
            hero_mid,
            text="🎯 Voice Zoo Tycoon   •   📂 MODS",
            font=("Consolas", 10, "bold"),
            text_color=THEME["accent_cyan"],
            anchor="w"
        )
        self.hero_genre_lbl.pack(fill="x", pady=(3, 2))

        self.hero_hk_lbl = ctk.CTkLabel(
            hero_mid,
            text="⚡ Fitur & Hotkey: ALT+1 +1M Gold | ALT+2 999M Gold | ALT+4 Unlock 30 Hewan | ALT+8 God Save",
            font=("Consolas", 9),
            text_color=THEME["text_muted"],
            anchor="w"
        )
        self.hero_hk_lbl.pack(fill="x", pady=(2, 0))

        hero_right = ctk.CTkFrame(self.hero_frame, fg_color="transparent")
        hero_right.pack(side="right", padx=14, pady=10)

        self.hero_play_btn = ctk.CTkButton(
            hero_right,
            text="🚀 PLAY + INJECT MOD",
            font=("Consolas", 12, "bold"),
            fg_color=THEME["accent_cyan"],
            hover_color=THEME["accent_emerald"],
            text_color="#040B14",
            corner_radius=8,
            width=185,
            height=38
        )
        self.hero_play_btn.pack(pady=(2, 6))

        hero_sub_btns = ctk.CTkFrame(hero_right, fg_color="transparent")
        hero_sub_btns.pack(fill="x")

        self.hero_hk_btn = ctk.CTkButton(
            hero_sub_btns,
            text="⌨️ HOTKEYS",
            font=("Consolas", 10, "bold"),
            fg_color="#162238",
            hover_color="#233554",
            text_color=THEME["accent_amber"],
            corner_radius=6,
            width=110,
            height=28
        )
        self.hero_hk_btn.pack(side="left", padx=(0, 5))

        self.hero_folder_btn = ctk.CTkButton(
            hero_sub_btns,
            text="📁 FOLDER",
            font=("Consolas", 10, "bold"),
            fg_color="#162238",
            hover_color="#233554",
            text_color=THEME["text_main"],
            corner_radius=6,
            width=70,
            height=28
        )
        self.hero_folder_btn.pack(side="left")

        # ── 2. SUB-HEADER & FILTER / SORT BAR ──
        self.center_top = ctk.CTkFrame(self.center_panel, fg_color="transparent", height=40)
        self.center_top.pack(fill="x", padx=16, pady=(2, 2))

        self._draw_pixel_art_header()

        self.section_title = ctk.CTkLabel(
            self.center_top,
            text=f"KATALOG SEMUA GAME ({len(GAMES_LIST)})",
            font=("Consolas", 13, "bold"),
            text_color=THEME["text_main"]
        )
        self.section_title.pack(side="left", padx=(6, 0))

        self.count_badge = ctk.CTkLabel(
            self.center_top,
            text=f"{len(GAMES_LIST)} ITEM",
            font=("Consolas", 10, "bold"),
            fg_color=THEME["bg_card"],
            text_color=THEME["accent_cyan"],
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.count_badge.pack(side="left", padx=10)

        ctrl_bar = ctk.CTkFrame(self.center_panel, fg_color="transparent", height=32)
        ctrl_bar.pack(fill="x", padx=14, pady=(0, 4))

        cats = [
            ("ALL",     "⬜ SEMUA",     THEME["accent_cyan"],    "#00354D"),
            ("MODS",    "🟢 MODS",      THEME["accent_emerald"], "#0A1F0A"),
            ("TRAINER", "🟣 TRAINER",   THEME["accent_purple"],  "#14050A"),
            ("CONSOLE", "🟠 CONSOLE",   THEME["accent_amber"],   "#1A0A00"),
            ("TOOLS",   "⚪ TOOLS",     THEME["text_muted"],     "#0D0D1A"),
        ]
        for cat_key, label, fg, bg in cats:
            is_active = (cat_key == self.filter_cat)
            btn = ctk.CTkButton(
                ctrl_bar, text=label,
                font=("Consolas", 9, "bold"),
                fg_color=fg if is_active else "#162032",
                text_color=THEME["text_dark"] if is_active else THEME["text_muted"],
                hover_color=bg, corner_radius=6, height=24, width=78,
                command=lambda c=cat_key: self.set_filter_cat(c)
            )
            btn.pack(side="left", padx=2, pady=2)
            self._cat_btns[cat_key] = btn

        sort_opts = [
            ("fav",     "⭐ Favorit"),
            ("recent",  "⏱️ Terakhir"),
            ("genre",   "🎯 Genre"),
            ("az",      "🔤 A-Z"),
            ("default", "Default"),
        ]
        for mode, label in sort_opts:
            ctk.CTkButton(
                ctrl_bar, text=label,
                font=("Consolas", 8, "bold"),
                fg_color="#162032", hover_color="#263552",
                text_color=THEME["text_muted"],
                corner_radius=5, height=22, width=64,
                command=lambda m=mode: self.set_sort(m)
            ).pack(side="right", padx=2)

        self.cards_scroll = ctk.CTkScrollableFrame(
            self.center_panel,
            fg_color="transparent",
            corner_radius=8
        )
        self.cards_scroll.pack(fill="both", expand=True, padx=10, pady=(0, 8))

        default_hero = next((g for g in GAMES_LIST if g["name"] == "My Voice Zoo"), GAMES_LIST[0])
        self.select_hero_item(default_hero)

        self.populate_cards(self._apply_sort_filter(list(GAMES_LIST)))

    def _draw_pixel_art_header(self):
        import tkinter as tk
        PIXEL = 2
        C  = "#00E5FF"
        D  = "#007A99"
        BG = THEME["bg_panel"]
        ART = [
            "0000011111111100000",
            "0001111111111111000",
            "0011111111111111100",
            "0111111111111111110",
            "1111001111111001111",
            "1110001111111000111",
            "1111001111111001111",
            "1111111110111111111",
            "1111111000011111111",
            "1111111110111111111",
            "1111111111111111111",
            "0111100111110011110",
            "0011100111110011100",
            "0001111111111111000",
            "0000111111111110000",
            "0000001111111000000",
        ]
        W = len(ART[0]) * PIXEL
        H = len(ART)    * PIXEL
        canvas = tk.Canvas(self.center_top, width=W, height=H, bg=BG, highlightthickness=0, bd=0)
        canvas.pack(side="left", padx=(0, 4))
        for row_i, row in enumerate(ART):
            for col_i, px in enumerate(row):
                if px != "0":
                    x0, y0 = col_i * PIXEL, row_i * PIXEL
                    canvas.create_rectangle(x0, y0, x0 + PIXEL, y0 + PIXEL, fill=C if px == "1" else D, outline="")
        self._pixel_canvas = canvas
        self._pulse_pixel_art()

    def _pulse_pixel_art(self):
        if not hasattr(self, "_pixel_canvas") or not self._pixel_canvas.winfo_exists():
            return
        colors = ["#00E5FF", "#00CDE6", "#00B8CC", "#00CDE6", "#00E5FF"]
        idx = getattr(self, "_pulse_idx", 0)
        col = colors[idx % len(colors)]
        try:
            for item in self._pixel_canvas.find_all():
                self._pixel_canvas.itemconfig(item, fill=col)
        except Exception:
            return
        self._pulse_idx = (idx + 1) % len(colors)
        self.after(1600, self._pulse_pixel_art)

    def populate_cards(self, items):
        for widget in self.cards_scroll.winfo_children():
            widget.destroy()

        self.card_widgets.clear()
        self.indicator_labels.clear()

        self.cards_scroll.grid_columnconfigure(0, weight=1)
        self.cards_scroll.grid_columnconfigure(1, weight=1)

        row, col = 0, 0
        for item in items:
            card = self.create_game_card(item, row, col)
            self.card_widgets.append((item, card))
            col += 1
            if col > 1:
                col = 0
                row += 1

        self.count_badge.configure(text=f"{len(items)} ITEM")

    def create_game_card(self, item, row, col):
        color  = item.get("color", THEME["accent_cyan"])
        icon   = item.get("icon",  "🎮")
        genre  = item.get("genre", "")
        cat    = item.get("category", "")
        is_fav = item["name"] in self.favorites

        card = ctk.CTkFrame(
            self.cards_scroll,
            fg_color="#111A2E",
            border_width=1,
            border_color=THEME["accent_amber"] if is_fav else "#22324F",
            corner_radius=12
        )
        card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=8, pady=8)

        # 1. Left HD Cover Art Thumbnail (126x62)
        cov_img = self._get_cover_image(item, size=(126, 62), is_hero=False)
        if cov_img:
            cov_lbl = ctk.CTkLabel(body, text="", image=cov_img, width=126, height=62, corner_radius=8)
        else:
            cov_lbl = ctk.CTkLabel(body, text=icon, font=("Segoe UI Emoji", 24), width=126, height=62,
                                   fg_color="#090F1C", corner_radius=8, text_color=color)
        cov_lbl.pack(side="left", padx=(2, 10), pady=2)
        cov_lbl.bind("<Button-1>", lambda e, it=item: self.select_hero_item(it))

        # 2. Right Content Area
        right_box = ctk.CTkFrame(body, fg_color="transparent")
        right_box.pack(side="left", fill="both", expand=True)

        # Row 1: Status Dot + Game Title + Status Pill
        r1 = ctk.CTkFrame(right_box, fg_color="transparent")
        r1.pack(fill="x")

        status_dot = ctk.CTkLabel(r1, text="●", font=("Consolas", 11), text_color="#4B5563")
        status_dot.pack(side="left", padx=(0, 4))
        self.indicator_labels[item["name"]] = status_dot

        title_lbl = ctk.CTkLabel(
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
        badge_pill.pack(side="right")

        # Row 2: Genre + Hotkey Snippet
        r2 = ctk.CTkFrame(right_box, fg_color="transparent")
        r2.pack(fill="x", pady=(2, 4))

        hotkeys = item.get("hotkeys", [])
        snippet_txt = hotkeys[0] if isinstance(hotkeys, list) and hotkeys else (
            list(hotkeys.keys())[0] if isinstance(hotkeys, dict) and hotkeys else genre
        )
        sub_txt = f"{genre} • {snippet_txt}" if genre else snippet_txt
        if len(sub_txt) > 42:
            sub_txt = sub_txt[:40] + ".."

        sub_lbl = ctk.CTkLabel(
            r2, text=sub_txt,
            font=("Consolas", 9),
            text_color=THEME["text_muted"], anchor="w"
        )
        sub_lbl.pack(side="left", fill="x", expand=True)

        # Row 3: Action Buttons
        btn_row = ctk.CTkFrame(right_box, fg_color="transparent")
        btn_row.pack(fill="x")

        launch_btn = ctk.CTkButton(
            btn_row,
            text="▶ PLAY",
            font=("Consolas", 10, "bold"),
            fg_color=color,
            hover_color=THEME["accent_emerald"],
            text_color="#050A14",
            corner_radius=6,
            height=26,
            command=lambda it=item: (self.select_hero_item(it), self.launch_item(it))
        )
        launch_btn.pack(side="left", expand=True, fill="x", padx=(0, 4))

        folder_btn = ctk.CTkButton(
            btn_row,
            text="📁",
            font=("Consolas", 10),
            fg_color="#1B2842",
            hover_color="#2C4068",
            text_color=THEME["text_main"],
            corner_radius=6,
            width=28,
            height=26,
            command=lambda it=item: self.open_item_folder(it)
        )
        folder_btn.pack(side="left", padx=1)

        fav_btn = ctk.CTkButton(
            btn_row,
            text="⭐" if is_fav else "☆",
            font=("Consolas", 11),
            fg_color="#1B2842",
            hover_color="#2C4068",
            text_color=THEME["accent_amber"] if is_fav else THEME["text_muted"],
            corner_radius=6,
            width=28,
            height=26
        )
        fav_btn.configure(command=lambda n=item["name"], b=fav_btn: self.toggle_favorite(n, b))
        fav_btn.pack(side="left", padx=1)
        self._fav_btns[item["name"]] = fav_btn

        if hotkeys:
            hk_btn = ctk.CTkButton(
                btn_row,
                text="⌨️",
                font=("Consolas", 10),
                fg_color="#1B2842",
                hover_color="#2C4068",
                text_color=THEME["accent_amber"],
                corner_radius=6,
                width=28,
                height=26,
                command=lambda it=item: (self.select_hero_item(it), self.show_hotkey_guide(it))
            )
            hk_btn.pack(side="left", padx=(1, 0))

        def _on_enter(e, c=card, col_hex=color, it=item):
            try:
                c.configure(border_color=col_hex, fg_color="#16233D")
            except Exception:
                pass

        def _on_leave(e, c=card, n=item["name"]):
            try:
                fav_now = n in self.favorites
                c.configure(border_color=THEME["accent_amber"] if fav_now else "#22324F", fg_color="#111A2E")
            except Exception:
                pass

        card.bind("<Enter>", _on_enter)
        card.bind("<Leave>", _on_leave)
        body.bind("<Enter>", _on_enter)
        body.bind("<Button-1>", lambda e, it=item: self.select_hero_item(it))

        return card

'''

s_idx = code.index(start_marker)
e_idx = code.index(end_marker)
code = code[:s_idx] + new_center_and_cards + code[e_idx:]

with open(GUI_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Upgraded Daffa_Master_GUI.py to v6.0 ULTRA (Hero Showcase + HD Cover Art Cards + GitHub Themes)!")
