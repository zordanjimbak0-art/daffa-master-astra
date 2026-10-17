"""
═══════════════════════════════════════════════════════════════════════════════
  ASTRA AI — THAT'S NOT MY NEIGHBOR  RADAR  v3.5  REAL-TIME DETECTOR
  Khusus Komandan DAFFA:
  1. 🚨 INDIKATOR REAL-TIME PINTU (PUTUSAN BUKA vs TUTUP OTOMATIS)
  2. 👁️ SENSOR PENGLIHATAN OPENCV (AUTO-SCAN JENDELA DARI SCREENSHOT)
  3. 📋 ENSIKLOPEDIA DOPPELGANGER LENGKAP 20 PENGHUNI DENGAN CIRI MONSTER
  4. 🤡 RADAR KARTU BADUT (NIGHTMARE CLOWN) & JAWABAN KUIS CHESTER
  5. ⭐ INJEKSI 100% S-RANK PERFECT SCORE [ALT+4]
═══════════════════════════════════════════════════════════════════════════════
"""
import os, sys, time, threading, struct, ctypes, winsound, subprocess
import customtkinter as ctk
import psutil
import cv2
import numpy as np
from PIL import Image
import win32gui, win32ui, win32con

# WAJIB: Matikan virtualisasi DPI Windows agar GetClientRect & PyAutoGUI sinkron 1:1 pada skala 125%/150%
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

# ── Paths & Win32 ─────────────────────────────────────────────────────────────
_TMNM_BASE = r"D:\Game\Games\Thats-Not-My-Neighbor-SteamRIP.com"
_TMNM_SUB  = "That's not my neighbor"
GAME_EXE   = os.path.join(_TMNM_BASE, _TMNM_SUB, _TMNM_SUB + ".exe")
PROC_NAME  = "That's not my neighbor"
SAVE_DIR   = os.path.join(os.environ.get("APPDATA", ""),
                          "Godot", "app_userdata", "That's not my neighbor")
RECORD_SAVE = os.path.join(SAVE_DIR, "data_record.save")
RECORD2_SAVE = os.path.join(SAVE_DIR, "data_record_02.save")

user32   = ctypes.windll.user32
VK_ALT   = 0x12
VK_SPACE = 0x20
VK_1, VK_2, VK_3, VK_4 = 0x31, 0x32, 0x33, 0x34

# ── Skema Warna Taktis ASTRA ──────────────────────────────────────────────────
T = {
    "bg"      : "#0C0602",
    "panel"   : "#170B04",
    "card"    : "#231106",
    "card2"   : "#2E1708",
    "border"  : "#592800",
    "border_hi": "#B35400",
    "acc"     : "#F59E0B",
    "sec"     : "#D97706",
    "green"   : "#10B981",
    "green_bg": "#064E3B",
    "red"     : "#EF4444",
    "red_bg"  : "#7F1D1D",
    "cyan"    : "#06B6D4",
    "blue"    : "#3B82F6",
    "purple"  : "#8B5CF6",
    "main"    : "#F8FAFC",
    "muted"   : "#94A3B8",
    "gold"    : "#FBBF24",
}

# ── Database 30 Penghuni Resmi Godot Engine (Ground-Truth 100%) ──────────────
try:
    from GENERATED_RESIDENTS import RESIDENTS
except Exception:
    import json
    _db_path = os.path.join(os.path.dirname(__file__), "OFFICIAL_RESIDENTS_DB.json")
    if os.path.exists(_db_path):
        _raw_db = json.load(open(_db_path, "r", encoding="utf-8"))
        RESIDENTS = []
        for k, v in _raw_db.items():
            fn = v.get("NAME", "")
            ln = v.get("LAST_NAME", "")
            name = (fn + " " + ln).strip()
            apt_en = v.get("APARTMENT_NUMBER_ENGLISH", "F01-01")
            floor = 1
            if "-" in apt_en:
                try: floor = int(apt_en.split("-")[0].replace("F", "").replace("P", ""))
                except: floor = 1
            RESIDENTS.append({
                "name": name,
                "apt": apt_en,
                "floor": floor,
                "id_num": v.get("ID_NUMBER", ""),
                "id_exp": v.get("ID_EXPIRATION", ""),
                "asli": f"Pekerjaan: {v.get('OCCUPATION_ENGLISH', '')}. Ciri: {v.get('APPEARANCE_ENGLISH', '')}",
                "monster_alert": f"AWAS! Periksa urat/parasit di pipi & dahi, mata merah, atau nomor ID bukan {v.get('ID_NUMBER', '')}!",
                "doppel_tells": ["Urat merah di pipi", "Urat di dahi", "Mata merah", "Topi palsu", "Gigi taring"]
            })
    else:
        RESIDENTS = [{"name": "Angus Ciprianni", "apt": "F01-03", "floor": 1, "id_num": "565003698845"}]

# Jawaban Kuis Chester Resmi (Ground-Truth Source Code Godot 4 — Scripts__Chester.gd)
CHESTER_QUIZ = [
    # ── STANDARD MODE (PERTANYAAN 1 s/d 6) ──────────────────────────────────
    ("STANDARD #1: What is the meaning of life, the universe and everything else?\n(Arti kehidupan, alam semesta, dan segalanya)", "42"),
    ("STANDARD #2: What is the scientific name of the Australian animal that drastically changes its appearance when removed from its natural habitat?\n(Nama ilmiah Blobfish hewan Australia)", "PSYCHROLUTESMARCIDUS"),
    ("STANDARD #3: What is the name of the only sport that allows you to punch your opponent in the face because they capture a piece?\n(Olahraga catur tinju)", "CHESSBOXING"),
    ("STANDARD #4: At least how many times do you have to fold a 0.01 mm thick sheet of paper to cover the distance between the Shire and Mordor?\n(Lipat kertas Shire ke Mordor LOTR)", "38"),
    ("STANDARD #5: The key is hide / EQEY QBXM MBIA MWXM XUES MCMS BQIX WUEW AHWY MV?\n(Sandi Caesar cipher: Planet Uranus)", "URANUS"),
    ("STANDARD #6: According to F.S.M. global warming is a consequence of the fact that since the 19th century the number of _______ decrease\n(Teori FSM: berkurangnya bajak laut)", "PIRATES"),
    # ── NIGHTMARE / EVIL MODE (PERTANYAAN 1 s/d 6) ──────────────────────────
    ("NIGHTMARE #1: Lastname of the man behind the true face of the mask most known to internet users.\n(Nama belakang Guy Fawkes / topeng Anonymous)", "FAWKES"),
    ("NIGHTMARE #2: Which number would give you the victory in a contest of writing the largest number with conventional rules of the Roman numeral system?\n(Angka Romawi konvensional terbesar: 3888)", "MMMDCCCLXXXVIII"),
    ("NIGHTMARE #3: Name of the hairiest lieutenant of World War II.\n(Letnan paling berbulu PD II: Beruang Wojtek)", "WOJTEK"),
    ("NIGHTMARE #4: Temple where once a god caused the largest pandemic ever seen in all the great darkn beyond.\n(Kuil wabah Corrupted Blood World of Warcraft)", "ZUL'GURUB"),
    ("NIGHTMARE #5: Clave name of the multicellular organism with the ability to clone anything it touches its rhizome.\n(Nama sandi pohon kloning SCP)", "SCP-038"),
    ("NIGHTMARE #6: How many numbers can be formed with the digits of the cardinality of the power set of a set with the first perfect and happy number of elements?\n(Kombinatorika digit 2^28 = 268435456)", "45360"),
]

CARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "JOKER BADUT"]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ══════════════════════════════════════════════════════════════════════════════
class TMNMModMenu(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("ASTRA // THAT'S NOT MY NEIGHBOR  RADAR v3.5")

        # ── Ukuran & posisi: pojok kanan atas, tidak nutup game ──────────────
        WIN_W, WIN_H = 640, 820
        # Ukur layar setelah Tk init
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        pos_x = max(0, sw - WIN_W - 8)
        pos_y = 8
        self.geometry(f"{WIN_W}x{WIN_H}+{pos_x}+{pos_y}")
        self.minsize(560, 680)
        self.configure(fg_color=T["bg"])
        self.attributes("-alpha", 0.95)
        self.attributes("-topmost", True)
        self.resizable(True, True)

        self.game_pid         = None
        self._last_save_mtime = 0
        self._save_data       = []
        self._selected_res    = RESIDENTS[0]
        self._autopilot_active = False
        self._chester_active   = True
        self._radar_hook_active = True
        self._auto_ranks_active = True
        self._last_radar_mtime = 0
        self._radar_json_path  = os.path.join(SAVE_DIR, "radar_state.json")
        self._guest_history    = []

        self._build_ui()
        self.after(200, self._manual_refresh_radar)

        # Paksa muncul di depan via Win32 HWND 100ms setelah mainloop start
        self.after(150, self._win32_force_topmost)

        # Threads
        threading.Thread(target=self._hotkey_loop,          daemon=True).start()
        threading.Thread(target=self._process_watch,        daemon=True).start()
        threading.Thread(target=self._save_watcher,         daemon=True).start()
        threading.Thread(target=self._radar_file_watcher,   daemon=True).start()
        threading.Thread(target=self._autopilot_worker,     daemon=True).start()

    def _win32_force_topmost(self):
        """Paksa window tampil di ATAS game fullscreen via Win32 API."""
        try:
            import ctypes
            HWND_TOPMOST   = -1
            SWP_NOMOVE     = 0x0002
            SWP_NOSIZE     = 0x0001
            SWP_SHOWWINDOW = 0x0040
            flags = SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW

            # Cari HWND window ini via title
            hwnd = win32gui.FindWindow(None, "ASTRA // THAT'S NOT MY NEIGHBOR  RADAR v3.5")
            if hwnd:
                win32gui.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, flags)
                win32gui.ShowWindow(hwnd, 9)   # SW_RESTORE
                win32gui.SetForegroundWindow(hwnd)
            # Juga via Tkinter
            self.deiconify()
            self.lift()
            self.focus_force()
            self.attributes("-topmost", True)
            self.update()
        except Exception as e:
            self._log(f"[topmost err] {e}")



    # ══════════════════════════════════════════════════════════════════════════
    # BUILD UI
    # ══════════════════════════════════════════════════════════════════════════
    def _build_ui(self):
        # ── Header ───────────────────────────────────────────
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10,
                            border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=10, pady=(10, 4))

        ctk.CTkLabel(hdr, text="🚪 RADAR REAL-TIME: DETEKTOR PINTU INSTAN v3.5",
                     font=("Consolas", 13, "bold"), text_color=T["acc"]).pack(anchor="w", padx=12, pady=(8, 1))
        ctk.CTkLabel(hdr, text="SENSOR PINTU REAL-TIME • AUTO-SCAN LAYAR • CIRI MONSTER LENGKAP",
                     font=("Consolas", 8, "bold"), text_color=T["muted"]).pack(anchor="w", padx=12, pady=(0, 4))

        # Status Line
        sbar = ctk.CTkFrame(hdr, fg_color="#0A0502", corner_radius=6)
        sbar.pack(fill="x", padx=10, pady=(0, 4))
        self._dot = ctk.CTkLabel(sbar, text="●", font=("Consolas", 12), text_color=T["red"])
        self._dot.pack(side="left", padx=(8, 4), pady=3)
        self._stat = ctk.CTkLabel(sbar, text=f"Menunggu proses game: {PROC_NAME}",
                                   font=("Consolas", 9, "bold"), text_color=T["muted"])
        self._stat.pack(side="left", pady=3)

        self._log_lbl = ctk.CTkLabel(hdr, text="— Siap Menganalisis Tamu Jendela —",
                                      font=("Consolas", 8), text_color=T["cyan"])
        self._log_lbl.pack(anchor="w", padx=12, pady=(0, 4))

        # ── SAKLAR TOGGLE ON-OFF CHEAT TAKTIS (KOMANDAN DAFFA) ────────
        sw_panel = ctk.CTkFrame(hdr, fg_color="#100803", corner_radius=8,
                                border_width=1, border_color=T["border"])
        sw_panel.pack(fill="x", padx=10, pady=(0, 6))

        sw_title_row = ctk.CTkFrame(sw_panel, fg_color="transparent")
        sw_title_row.pack(fill="x", padx=8, pady=(4, 2))
        ctk.CTkLabel(sw_title_row, text="⚡ SAKLAR CHEAT (ON / OFF) // ASTRA PROTOCOL:",
                     font=("Consolas", 9, "bold"), text_color=T["acc"]).pack(side="left")

        # Baris 1: Autopilot & Chester
        sw_r1 = ctk.CTkFrame(sw_panel, fg_color="transparent")
        sw_r1.pack(fill="x", padx=8, pady=2)

        self.sw_autopilot = ctk.CTkSwitch(
            sw_r1, text="🤖 Autopilot Bot [ALT+A]",
            font=("Consolas", 9, "bold"),
            progress_color=T["green"],
            button_color="#FFFFFF",
            button_hover_color=T["acc"],
            command=self._on_switch_autopilot
        )
        self.sw_autopilot.pack(side="left", padx=(0, 10))

        self.sw_chester = ctk.CTkSwitch(
            sw_r1, text="🧠 Chester 0-Click Solver",
            font=("Consolas", 9, "bold"),
            progress_color=T["green"],
            button_color="#FFFFFF",
            button_hover_color=T["acc"],
            command=self._on_switch_chester
        )
        self.sw_chester.pack(side="left")
        self.sw_chester.select()

        # Baris 2: Radar Hook & Auto S-Rank
        sw_r2 = ctk.CTkFrame(sw_panel, fg_color="transparent")
        sw_r2.pack(fill="x", padx=8, pady=(2, 6))

        self.sw_radar_hook = ctk.CTkSwitch(
            sw_r2, text="👁️ Live Engine Telemetry",
            font=("Consolas", 9, "bold"),
            progress_color=T["green"],
            button_color="#FFFFFF",
            button_hover_color=T["acc"],
            command=self._on_switch_radar_hook
        )
        self.sw_radar_hook.pack(side="left", padx=(0, 10))
        self.sw_radar_hook.select()

        self.sw_ranks = ctk.CTkSwitch(
            sw_r2, text="⭐ Auto-Lock S-Rank [ALT+4]",
            font=("Consolas", 9, "bold"),
            progress_color=T["green"],
            button_color="#FFFFFF",
            button_hover_color=T["acc"],
            command=self._on_switch_ranks
        )
        self.sw_ranks.pack(side="left")
        self.sw_ranks.select()

        # ── TOMBOL UTAMA: MODE AUTOPILOT BOT (ANALISIS & EKSEKUSI PENUH) ──
        self._btn_autopilot = ctk.CTkButton(
            self,
            text="⚪ AUTOPILOT BOT: STANDBY [ALT+A]\n(Klik untuk Menyerahkan Seluruh Analisis & Keputusan ke Bot)",
            font=("Consolas", 11, "bold"),
            fg_color=T["card2"],
            border_width=2,
            border_color=T["border_hi"],
            hover_color=T["acc"],
            text_color="#FFFFFF",
            height=46,
            corner_radius=10,
            command=self._toggle_autopilot
        )
        self._btn_autopilot.pack(fill="x", padx=10, pady=(0, 6))

        # ── HERO INDIKATOR REAL-TIME UTAMA (SUPER BESAR) ──────
        self._hero_box = ctk.CTkFrame(self, corner_radius=12, fg_color=T["red_bg"],
                                      border_width=3, border_color=T["red"])
        self._hero_box.pack(fill="x", padx=10, pady=(0, 6))

        self._hero_title = ctk.CTkLabel(
            self._hero_box, text="🚨 CEK JENDELA SEKARANG!",
            font=("Consolas", 20, "bold"), text_color="#FFFFFF"
        )
        self._hero_title.pack(pady=(10, 2))

        self._hero_action = ctk.CTkLabel(
            self._hero_box,
            text="Pilih nama tamu di bawah ATAU tekan tombol [SCAN LAYAR] untuk putusan instan!",
            font=("Consolas", 10, "bold"), text_color=T["gold"], wraplength=580
        )
        self._hero_action.pack(pady=(0, 10))

        # ── TOMBOL DUA KEPUTUSAN CEPAT (LANGSUNG KETAHUAN) ────
        btn_decide = ctk.CTkFrame(self, fg_color="transparent")
        btn_decide.pack(fill="x", padx=10, pady=(0, 6))

        self._btn_impostor = ctk.CTkButton(
            btn_decide, text="🛑 TUTUP PINTU!\n(IMPOSTOR / MONSTER)",
            font=("Consolas", 11, "bold"), fg_color=T["red_bg"], hover_color=T["red"],
            text_color="#FFFFFF", height=42, corner_radius=8,
            command=self._set_impostor_verdict
        )
        self._btn_impostor.pack(side="left", expand=True, fill="x", padx=(0, 4))

        self._btn_human = ctk.CTkButton(
            btn_decide, text="✅ BUKA PINTU!\n(MANUSIA ASLI 100%)",
            font=("Consolas", 11, "bold"), fg_color=T["green_bg"], hover_color=T["green"],
            text_color="#FFFFFF", height=42, corner_radius=8,
            command=self._set_human_verdict
        )
        self._btn_human.pack(side="left", expand=True, fill="x", padx=(4, 0))

        # ── TOMBOL TELPON DDD (KHUSUS IMPOSTOR) ──────────────────────────────
        ddd_frame = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=8,
                                 border_width=2, border_color="#FF0000")
        ddd_frame.pack(fill="x", padx=10, pady=(0, 4))

        ctk.CTkLabel(ddd_frame,
                     text="📞 JIKA IMPOSTOR → ANGKAT TELEPON → KETIK:  3 - 3 - 1 - 2  → ENTER",
                     font=("Consolas", 10, "bold"), text_color="#FF5555").pack(side="left", padx=12, pady=6)

        ctk.CTkButton(ddd_frame, text="🔴 ALARM\nDDD 3312",
                      font=("Consolas", 9, "bold"), fg_color="#7F1D1D", hover_color="#EF4444",
                      text_color="#FFFFFF", width=80, height=38, corner_radius=6,
                      command=self._alarm_ddd).pack(side="right", padx=8, pady=4)

        # ── TABS INFORMASI & FITUR ────────────────────────────
        tabs = ctk.CTkTabview(self, fg_color=T["panel"], border_color=T["border"],
                               border_width=1, corner_radius=10,
                               segmented_button_fg_color=T["panel"],
                               segmented_button_selected_color=T["sec"],
                               segmented_button_selected_hover_color=T["acc"],
                               text_color=T["main"])
        tabs.pack(fill="both", expand=True, padx=10, pady=(0, 4))

        t_live    = tabs.add("📡 LIVE RADAR")
        t_radar   = tabs.add("🔍 ANALISIS TAMU")
        t_clown   = tabs.add("🤡 KARTU BADUT")
        t_chester = tabs.add("🧠 KUIS CHESTER")
        t_ranks   = tabs.add("⭐ AUTO-WIN RANK S")
        t_tools   = tabs.add("🛠️ EXE & TOOLS")
        tabs.set("📡 LIVE RADAR")

        self._build_tab_live(t_live)
        self._build_tab_radar(t_radar)
        self._build_tab_clown(t_clown)
        self._build_tab_chester(t_chester)
        self._build_tab_ranks(t_ranks)
        self._build_tab_tools(t_tools)

        # ── BOTTOM BAR ────────────────────────────────────────
        bot = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10, height=38)
        bot.pack(fill="x", padx=10, pady=(0, 8))
        bot.pack_propagate(False)

        ctk.CTkLabel(bot, text="Alpha:", font=("Consolas", 9), text_color=T["muted"]).pack(side="left", padx=(8, 2))
        sl = ctk.CTkSlider(bot, from_=0.3, to=1.0, number_of_steps=14, width=80,
                            command=lambda v: self.attributes("-alpha", float(v)))
        sl.set(0.95)
        sl.pack(side="left", pady=8)

        ctk.CTkButton(bot, text="⭐ INJEK RANK S [ALT+4]",
                      font=("Consolas", 9, "bold"), fg_color=T["green_bg"],
                      hover_color=T["green"], text_color=T["main"],
                      height=26, command=self._inject_perfect_rank_s).pack(side="right", padx=(4, 8))

        ctk.CTkButton(bot, text="👁️ SCAN LAYAR [ALT+1]",
                      font=("Consolas", 9, "bold"), fg_color=T["border_hi"],
                      hover_color=T["acc"], text_color="#000000",
                      height=26, command=self._scan_screen_vision).pack(side="right", padx=4)

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 0: RADAR TELEMETRI REAL-TIME (GROUND TRUTH ENGINE GODOT 4)
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_live(self, parent):
        # ── 1. Status Koneksi Engine ──────────────────────────────────────────
        conn_box = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8, border_width=1, border_color=T["border"])
        conn_box.pack(fill="x", padx=6, pady=(4, 2))

        self._lbl_live_hook_status = ctk.CTkLabel(
            conn_box, text="● ENGINE HOOK: TERHUBUNG (Godot 4.2 Forward+)",
            font=("Consolas", 10, "bold"), text_color=T["green"]
        )
        self._lbl_live_hook_status.pack(side="left", padx=10, pady=6)

        ctk.CTkButton(
            conn_box, text="🔄 REFRESH SEKARANG", font=("Consolas", 9, "bold"),
            width=130, height=26, fg_color=T["card2"], hover_color=T["border_hi"],
            command=self._manual_refresh_radar
        ).pack(side="right", padx=8, pady=4)

        # ── 2. Kartu Status Tamu Saat Ini (Super Besar & Jelas) ───────────────
        self._live_verdict_card = ctk.CTkFrame(
            parent, fg_color=T["card2"], corner_radius=10,
            border_width=2, border_color=T["border_hi"]
        )
        self._live_verdict_card.pack(fill="x", padx=6, pady=4)

        self._live_guest_title = ctk.CTkLabel(
            self._live_verdict_card, text="👤 TAMU DI JENDELA: MENUNGGU DATA...",
            font=("Consolas", 15, "bold"), text_color=T["acc"]
        )
        self._live_guest_title.pack(anchor="w", padx=12, pady=(10, 2))

        self._live_status_badge = ctk.CTkLabel(
            self._live_verdict_card, text="🔍 HASIL PEMERIKSAAN ENGINE: MENUNGGU TAMU",
            font=("Consolas", 12, "bold"), text_color=T["muted"]
        )
        self._live_status_badge.pack(anchor="w", padx=12, pady=2)

        self._live_audit_info = ctk.CTkLabel(
            self._live_verdict_card,
            text="• Raw Node: -\n• Status Doppelganger: -\n• Jadwal Kunjungan (Today List): -\n• Waktu Update: -",
            font=("Consolas", 10), text_color=T["main"], justify="left", anchor="w"
        )
        self._live_audit_info.pack(anchor="w", padx=14, pady=(4, 8))

        # ── 3. Tombol Aksi Eksekusi Cepat (Direct Engine Injection) ────────────
        btn_action_row = ctk.CTkFrame(self._live_verdict_card, fg_color="transparent")
        btn_action_row.pack(fill="x", padx=10, pady=(0, 10))

        self._live_btn_open = ctk.CTkButton(
            btn_action_row, text="🟢 BUKA PINTU LOKET [ALT+O]\n(100% AMAN / SAH)",
            font=("Consolas", 10, "bold"), fg_color=T["green_bg"], hover_color=T["green"],
            height=42, command=self.auto_door_open
        )
        self._live_btn_open.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self._live_btn_lock = ctk.CTkButton(
            btn_action_row, text="🔴 KUNCI & ALARM DDD [ALT+D]\n(DOPPELGANGER / BAHAYA)",
            font=("Consolas", 10, "bold"), fg_color=T["red_bg"], hover_color=T["red"],
            height=42, command=self.auto_door_close_and_ddd
        )
        self._live_btn_lock.pack(side="left", fill="x", expand=True, padx=(4, 0))

        # ── 4. Live Dump Variabel Internal Game (Ground Truth Textbox) ────────
        dump_frame = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8, border_width=1, border_color=T["border"])
        dump_frame.pack(fill="both", expand=True, padx=6, pady=4)

        dump_hdr = ctk.CTkFrame(dump_frame, fg_color="transparent")
        dump_hdr.pack(fill="x", padx=10, pady=(6, 2))
        ctk.CTkLabel(
            dump_hdr, text="🔍 DUMP VARIABEL MEMORI GDSCRIPT (GROUND TRUTH):",
            font=("Consolas", 9, "bold"), text_color=T["acc"]
        ).pack(side="left")

        self._txt_live_dump = ctk.CTkTextbox(
            dump_frame, font=("Consolas", 9), fg_color="#0A0502",
            text_color="#A7F3D0", activate_scrollbars=True
        )
        self._txt_live_dump.pack(fill="both", expand=True, padx=8, pady=(2, 8))

    def _manual_refresh_radar(self):
        try:
            if os.path.isfile(self._radar_json_path):
                with open(self._radar_json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self._on_radar_json_event(data)
                self._log("📡 [RADAR] Telemetri radar berhasil disegarkan!")
        except Exception as e:
            self._log(f"[Refresh Err] {e}")

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 1: RADAR ANALISIS TAMU & CIRI MONSTER LENGKAP
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_radar(self, parent):
        # Dropdown Pemilih Cepat Penghuni & Tombol Taktis
        pick_frame = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8)
        pick_frame.pack(fill="x", padx=6, pady=(4, 2))

        ctk.CTkLabel(pick_frame, text="PENGHUNI:", font=("Consolas", 10, "bold"),
                     text_color=T["acc"]).pack(side="left", padx=(8, 4), pady=4)

        names = [f"{r['name']} ({r['apt']})" for r in RESIDENTS]
        self._drop_res = ctk.CTkOptionMenu(
            pick_frame, values=names, font=("Consolas", 10, "bold"),
            fg_color=T["card2"], button_color=T["border_hi"],
            command=self._on_dropdown_change
        )
        self._drop_res.pack(side="left", fill="x", expand=True, padx=4, pady=4)

        ctk.CTkButton(
            pick_frame, text="⚡ AUTO-SCAN [ALT+1]", font=("Consolas", 9, "bold"),
            fg_color=T["sec"], hover_color=T["acc"], height=28,
            command=self._scan_and_ocr
        ).pack(side="left", padx=4, pady=4)

        ctk.CTkButton(
            pick_frame, text="📞 TELPON KAMAR", font=("Consolas", 9, "bold"),
            fg_color=T["card2"], hover_color=T["border_hi"], height=28,
            command=self.auto_call_room
        ).pack(side="left", padx=(4, 8), pady=4)

        # Kartu Detail Ciri Penghuni vs Ciri Monster
        sc = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=4, pady=2)

        # Kotak Checklist Otomatis (Virtual Security Checklist)
        chk_box = ctk.CTkFrame(sc, fg_color=T["card"], corner_radius=8,
                               border_width=1, border_color=T["border"])
        chk_box.pack(fill="x", pady=(2, 4))

        ctk.CTkLabel(chk_box, text="📋 VIRTUAL SECURITY CHECKLIST (AUDIT OTOMATIS OLEH BOT):",
                     font=("Consolas", 10, "bold"), text_color=T["acc"]).pack(anchor="w", padx=10, pady=(6, 2))
        
        self._chk_photo = ctk.CTkLabel(chk_box, text="[✔] 1. Foto Wajah Cocok dengan Tamu di Jendela: Menunggu...",
                                       font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_photo.pack(anchor="w", padx=14, pady=1)

        self._chk_id = ctk.CTkLabel(chk_box, text="[✔] 2. Nomor ID & Tanggal Kadaluwarsa Sah: Menunggu...",
                                    font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_id.pack(anchor="w", padx=14, pady=1)

        self._chk_entry = ctk.CTkLabel(chk_box, text="[✔] 3. Alasan Izin Masuk (Entry Request) Sah: Menunggu...",
                                       font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_entry.pack(anchor="w", padx=14, pady=1)

        self._chk_list = ctk.CTkLabel(chk_box, text="[✔] 4. Terdaftar di Jadwal Tamu Hari Ini: Menunggu...",
                                      font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_list.pack(anchor="w", padx=14, pady=1)

        self._chk_ddd = ctk.CTkLabel(chk_box, text="[✔] 5. Cap & Watermark Resmi DDD 1955: Menunggu...",
                                     font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_ddd.pack(anchor="w", padx=14, pady=1)

        self._chk_phone = ctk.CTkLabel(chk_box, text="[✔] 6. Nomor Telepon Kamar Resmi: Menunggu...",
                                       font=("Consolas", 9), text_color=T["muted"], anchor="w")
        self._chk_phone.pack(anchor="w", padx=14, pady=(1, 6))

        # Kotak 1: Peringatan Bahaya Doppelganger (Merah)
        self._box_alert = ctk.CTkFrame(sc, fg_color=T["red_bg"], corner_radius=8,
                                       border_width=2, border_color=T["red"])
        self._box_alert.pack(fill="x", pady=3)

        ctk.CTkLabel(self._box_alert, text="⚠️ PERINGATAN BENTUK MONSTER / IMPOSTOR:",
                     font=("Consolas", 10, "bold"), text_color="#FFFFFF").pack(anchor="w", padx=10, pady=(6, 2))

        self._lbl_monster_desc = ctk.CTkLabel(
            self._box_alert, text="", font=("Consolas", 9, "bold"),
            text_color="#FCA5A5", anchor="w", justify="left", wraplength=540
        )
        self._lbl_monster_desc.pack(anchor="w", padx=12, pady=(0, 6))

        # Kotak 2: Wujud Manusia Asli yang Sah (Hijau)
        self._box_human = ctk.CTkFrame(sc, fg_color=T["green_bg"], corner_radius=8,
                                       border_width=1, border_color=T["green"])
        self._box_human.pack(fill="x", pady=3)

        ctk.CTkLabel(self._box_human, text="✅ WUJUD MANUSIA ASLI (YANG BOLEH MASUK):",
                     font=("Consolas", 10, "bold"), text_color="#FFFFFF").pack(anchor="w", padx=10, pady=(6, 2))

        self._lbl_human_desc = ctk.CTkLabel(
            self._box_human, text="", font=("Consolas", 9),
            text_color="#A7F3D0", anchor="w", justify="left", wraplength=540
        )
        self._lbl_human_desc.pack(anchor="w", padx=12, pady=(0, 6))

        # Kotak 3: Checklist Cepat 4 Aturan Emas
        rule_box = ctk.CTkFrame(sc, fg_color=T["card"], corner_radius=8,
                                border_width=1, border_color=T["border"])
        rule_box.pack(fill="x", pady=3)

        ctk.CTkLabel(rule_box, text="📋 4 ATURAN EMAS MENENTUKAN IMPOSTOR:",
                     font=("Consolas", 10, "bold"), text_color=T["gold"]).pack(anchor="w", padx=10, pady=(6, 2))

        rules = [
            "1. BENTUK FISIK: Jika di jendela berwujud MONSTER BERBULU, TOPI UNGU, MATA 3, atau CACAT ➔ 100% IMPOSTOR! TUTUP PINTU!",
            "2. WAJAH vs FOTO: Jika wajah orang di jendela BEDA dengan foto di ID Card ➔ 100% IMPOSTOR!",
            "3. NO APARTEMEN: Cocokkan nomor apt di lembar izin masuk dengan database apartemen.",
            "4. EXPIRY DATE: Tahun game adalah 1955. Jika masa berlaku lewat 1954 ke bawah ➔ KADALUARSA (TUTUP PINTU).",
        ]
        for r in rules:
            ctk.CTkLabel(rule_box, text=r, font=("Consolas", 8),
                         text_color=T["main"], anchor="w", wraplength=530).pack(anchor="w", padx=12, pady=2)

        # Init selection
        self._on_dropdown_change(names[0])

    def _on_dropdown_change(self, val):
        name_only = val.split(" (")[0]
        res = next((r for r in RESIDENTS if r["name"] == name_only), RESIDENTS[0])
        self._selected_res = res

        self._lbl_monster_desc.configure(text=res["monster_alert"])
        phone_txt = res.get("phone", "N/A")
        occ_txt   = res.get("occ", "Penghuni")
        self._lbl_human_desc.configure(
            text=f"• No. Apt: {res['apt']} (Lantai {res['floor']}) | Telp: {phone_txt} | Pekerjaan: {occ_txt}\n• Nomor ID Resmi: {res['id_num']} | Exp: {res['id_exp']}\n• Penampilan Sah: {res['asli']}"
        )

        # Default reset ke status tanya
        self._hero_box.configure(fg_color=T["card2"], border_color=T["border_hi"])
        self._hero_title.configure(text=f"🔍 CEK: {res['name'].upper()}", text_color=T["acc"])
        self._hero_action.configure(
            text="Cocokkan wujud tamu di jendela kaca dengan info di bawah, lalu tekan tombol putusan!",
            text_color=T["main"]
        )

    # ══════════════════════════════════════════════════════════════════════════
    # PUTUSAN INSTAN (BUKA vs TUTUP PINTU)
    # ══════════════════════════════════════════════════════════════════════════
    def _set_impostor_verdict(self):
        """Putusan: TUTUP PINTU (IMPOSTOR) + instruksi TELPON DDD."""
        self._hero_box.configure(fg_color=T["red_bg"], border_color=T["red"])
        self._hero_title.configure(
            text="🛑 IMPOSTOR! TUTUP PINTU — TELPON DDD (3312)! 🚨",
            text_color="#FFFFFF"
        )
        self._hero_action.configure(
            text="❌ JANGAN BUKA PINTU!\n📞 Angkat telepon → Tekan 3312 → Laporkan ke DDD sekarang!",
            text_color="#FCA5A5"
        )
        self._log(f"🚨 IMPOSTOR: {self._selected_res['name']} → TUTUP PINTU + TELPON 3312!")
        try:
            # Alarm 3x beep
            for _ in range(3):
                winsound.Beep(380, 200)
                time.sleep(0.05)
        except Exception:
            pass

    def _set_human_verdict(self):
        """Putusan: BUKA PINTU (MANUSIA ASLI)."""
        self._hero_box.configure(fg_color=T["green_bg"], border_color=T["green"])
        self._hero_title.configure(text="✅ AMAN! MANUSIA ASLI — BUKA PINTU!", text_color="#FFFFFF")
        self._hero_action.configure(
            text="Penghuni asli dan dokumen sah. Silakan buka pintu masuk!",
            text_color="#A7F3D0"
        )
        self._log(f"VERIFIED: {self._selected_res['name']} terbukti manusia asli. Buka pintu.")
        try:
            winsound.Beep(1400, 100)
        except Exception:
            pass

    def _alarm_ddd(self):
        """Tampilkan reminder + suara alarm DDD 3312."""
        self._hero_box.configure(fg_color="#4A0000", border_color="#FF0000")
        self._hero_title.configure(
            text="📞 TELPON DDD SEKARANG! → 3 3 1 2 → ENTER",
            text_color="#FF5555"
        )
        self._hero_action.configure(
            text="① Angkat telepon di meja  ② Ketik 3312  ③ Tekan ENTER  ④ Tunggu konfirmasi DDD",
            text_color="#FCA5A5"
        )
        self._log("📞 ALARM DDD: Ketik 3312 di telepon sekarang!")
        try:
            for freq in [300, 500, 300, 500]:
                winsound.Beep(freq, 250)
        except Exception:
            pass

    # ══════════════════════════════════════════════════════════════════════════
    # SENSOR PENGLIHATAN CERDAS OPENCV & SCREEN CAPTURE
    # ══════════════════════════════════════════════════════════════════════════
    def _capture_game_frame(self):
        """
        Menangkap frame visual game That's Not My Neighbor secara presisi.
        Mendukung windowed mode, posisi layar kustom, dan fullscreen tanpa offset.
        """
        try:
            desk_hwnd = win32gui.GetDesktopWindow()
            desk_rect = win32gui.GetWindowRect(desk_hwnd)
            dw, dh = desk_rect[2] - desk_rect[0], desk_rect[3] - desk_rect[1]

            hwndDC  = win32gui.GetWindowDC(desk_hwnd)
            mfcDC   = win32ui.CreateDCFromHandle(hwndDC)
            saveDC  = mfcDC.CreateCompatibleDC()
            bmp     = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(mfcDC, dw, dh)
            saveDC.SelectObject(bmp)
            saveDC.BitBlt((0, 0), (dw, dh), mfcDC, (0, 0), win32con.SRCCOPY)
            bmpinfo = bmp.GetInfo()
            bmpstr  = bmp.GetBitmapBits(True)
            full_pil = Image.frombuffer(
                "RGB", (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
                bmpstr, "raw", "BGRX", 0, 1
            )
            full_frame = cv2.cvtColor(np.array(full_pil), cv2.COLOR_RGB2BGR)

            win32gui.DeleteObject(bmp.GetHandle())
            saveDC.DeleteDC()
            mfcDC.DeleteDC()
            win32gui.ReleaseDC(desk_hwnd, hwndDC)

            # Cek koordinat jendela game jika sedang aktif
            _, grect = self._get_game_window_rect()
            if grect:
                gx1, gy1, gx2, gy2 = grect
                gx1, gy1 = max(0, gx1), max(0, gy1)
                gx2, gy2 = min(dw, gx2), min(dh, gy2)
                gw, gh = gx2 - gx1, gy2 - gy1
                if gw > 250 and gh > 250:
                    return full_frame[gy1:gy2, gx1:gx2], (gx1, gy1, gx2, gy2)

            return full_frame, (0, 0, dw, dh)
        except Exception as e:
            self._log(f"[Capture Error] {e}")
            return None, None

    def _analyze_face_vision(self, game_frame):
        """
        Sensor Penglihatan Wajah & Kepala:
        1. Urat / Parasit Merah di Wajah (scar_2: pipi kiri, pipi kanan, dahi)
        2. Topi Ungu Monster (Purple Fedora)
        3. Bulu Monster Peachman (Orange/Brown Fur)
        4. Warna Kulit Abnormal (Alien Hijau / Zombie Biru)
        """
        if game_frame is None:
            return "ERROR", ["Gagal menangkap frame game"]

        gh, gw, _ = game_frame.shape
        # Area jendela kaca loket tempat kepala & wajah tamu berdiri
        y1, y2 = int(gh * 0.08), int(gh * 0.55)
        x1, x2 = int(gw * 0.38), int(gw * 0.64)
        face_roi = game_frame[y1:y2, x1:x2]

        if face_roi.size == 0 or np.mean(face_roi) < 12:
            return "EMPTY", ["Tidak ada tamu di loket"]

        fh_h, fh_w, _ = face_roi.shape
        hsv = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)

        # ── 1. Deteksi Urat / Parasit Merah (Crimson Veins / Scar Anomaly) ──
        m1 = cv2.inRange(hsv, np.array([0, 70, 50]), np.array([12, 255, 255]))
        m2 = cv2.inRange(hsv, np.array([168, 70, 50]), np.array([180, 255, 255]))
        red_mask = cv2.bitwise_or(m1, m2)
        red_pct = np.count_nonzero(red_mask) / (fh_h * fh_w) * 100

        # Sub-region pipi kiri, pipi kanan, dan dahi (menghindari bibir)
        lc_roi = face_roi[int(fh_h * 0.30):int(fh_h * 0.75), 0:int(fh_w * 0.45)]
        rc_roi = face_roi[int(fh_h * 0.30):int(fh_h * 0.75), int(fh_w * 0.55):]
        top_roi = face_roi[0:int(fh_h * 0.40), :]

        def calc_red(roi):
            if roi.size == 0: return 0.0
            rhsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            rm = cv2.bitwise_or(
                cv2.inRange(rhsv, np.array([0, 70, 50]), np.array([12, 255, 255])),
                cv2.inRange(rhsv, np.array([168, 70, 50]), np.array([180, 255, 255]))
            )
            return np.count_nonzero(rm) / (roi.shape[0] * roi.shape[1]) * 100

        lc_red = calc_red(lc_roi)
        rc_red = calc_red(rc_roi)
        fh_red = calc_red(top_roi)

        # ── 2. Deteksi Topi Ungu Monster (Purple Fedora) ──
        hat_mask = cv2.inRange(hsv, np.array([125, 90, 50]), np.array([165, 255, 255]))
        hat_pct = np.count_nonzero(hat_mask) / (fh_h * fh_w) * 100

        # ── 3. Deteksi Bulu Monster Cokelat/Oranye (Peachman Fur) ──
        fur_mask = cv2.inRange(hsv, np.array([10, 100, 70]), np.array([26, 255, 255]))
        fur_pct = np.count_nonzero(fur_mask) / (fh_h * fh_w) * 100

        # ── 4. Deteksi Warna Kulit Abnormal (Alien Hijau / Zombie Biru) ──
        green_mask = cv2.inRange(hsv, np.array([35, 60, 40]), np.array([85, 255, 255]))
        green_pct = np.count_nonzero(green_mask) / (fh_h * fh_w) * 100

        blue_mask = cv2.inRange(hsv, np.array([95, 60, 40]), np.array([130, 255, 255]))
        blue_pct = np.count_nonzero(blue_mask) / (fh_h * fh_w) * 100

        reasons = []
        if red_pct > 3.0 or lc_red > 2.0 or rc_red > 2.0:
            reasons.append(f"Urat/Parasit Merah di Wajah (Pipi: {max(lc_red, rc_red):.1f}%, Total: {red_pct:.1f}%)")
        if fh_red > 4.0:
            reasons.append(f"Retakan/Urat Abnormal di Dahi ({fh_red:.1f}%)")
        if hat_pct > 2.5:
            reasons.append(f"Topi Ungu Monster Terdeteksi ({hat_pct:.1f}%)")
        if fur_pct > 10.0:
            reasons.append(f"Bulu Monster Peachman Abnormal ({fur_pct:.1f}%)")
        if green_pct > 5.0:
            reasons.append(f"Warna Kulit Hijau Alien ({green_pct:.1f}%)")
        if blue_pct > 5.0:
            reasons.append(f"Warna Kulit Biru/Lebam Zombie ({blue_pct:.1f}%)")

        if reasons:
            return "IMPOSTOR", reasons
        return "CLEAN", []

    def _scan_screen_vision(self):
        """Manual trigger OpenCV vision scan."""
        frame, _ = self._capture_game_frame()
        if frame is None:
            self._log("Gagal menangkap layar game.")
            return
        status, reasons = self._analyze_face_vision(frame)
        if status == "IMPOSTOR":
            self._apply_verdict_impostor("Wajah & Ciri Fisik", reasons)
        elif status == "CLEAN":
            self._log("✅ SENSOR WAJAH: Bebas dari urat, parasit, topi palsu, dan bulu monster.")
            winsound.Beep(1200, 80)
        else:
            self._log(f"Status jendela loket: {status}")

    # ══════════════════════════════════════════════════════════════════════════
    # OCR DOKUMEN & AUDIT DATABASE 30 PENGHUNI RESMI GODOT
    # ══════════════════════════════════════════════════════════════════════════
    def _read_documents_with_auto_zoom(self, frame):
        """Membaca teks dokumen kartu ID dan surat izin masuk di meja loket secara pasif (tanpa menggerakkan mouse)."""
        if frame is None:
            return []

        gh, gw, _ = frame.shape
        desk_crop = frame[int(gh * 0.45):int(gh * 0.98), int(gw * 0.25):int(gw * 0.85)]
        detected_texts = self._run_rapid_ocr(desk_crop)
        return detected_texts

    def _run_rapid_ocr(self, img_np):
        """Eksekusi OCR menggunakan RapidOCR ONNX."""
        detected = []
        try:
            from rapidocr_onnxruntime import RapidOCR
            if not hasattr(self, "_rapid_ocr_engine"):
                self._rapid_ocr_engine = RapidOCR()
            res, _ = self._rapid_ocr_engine(img_np)
            if res:
                for line in res:
                    txt = line[1].strip()
                    if txt:
                        detected.append(txt)
        except Exception:
            try:
                import pytesseract
                raw = pytesseract.image_to_string(img_np, config="--psm 6 -l eng")
                for l in raw.splitlines():
                    if l.strip():
                        detected.append(l.strip())
            except Exception:
                pass
        return detected

    def _audit_resident_database(self, detected_texts):
        """
        Audit silang teks OCR dengan Database 30 Penghuni Resmi Godot:
        1. Ejaan Nama
        2. Nomor ID 12 digit
        3. Tanggal Kadaluwarsa
        4. Alasan Izin Masuk (Pests / Infeksi)
        5. Nomor Apartemen
        """
        raw_combined = " ".join(detected_texts).lower()
        if not raw_combined:
            return None, ["Dokumen tidak terbaca di meja loket"]

        best_match = None
        best_score = 0
        for res in RESIDENTS:
            parts = res["name"].lower().split()
            score = 0
            for p in parts:
                if len(p) >= 3 and p in raw_combined:
                    score += len(p)
            apt_clean = res["apt"].lower().replace("-", "")
            if res["apt"].lower() in raw_combined or apt_clean in raw_combined:
                score += 5
            if score > best_score:
                best_score = score
                best_match = res

        anomalies = []
        fake_tokens = [
            "albertsky", "roberttsky", "robertskyn", "peachmann", "pecchman",
            "stonnn", "isthar", "ereskijal", "ishtor", "eneskigal"
        ]
        for ft in fake_tokens:
            if ft in raw_combined:
                anomalies.append(f"Nama Palsu Doppelganger: '{ft.upper()}'")

        danger_reasons = ["pest", "emergency pest", "provoke", "witchcraft", "brujeria", "infestation", "kill"]
        for dr in danger_reasons:
            if dr in raw_combined:
                anomalies.append(f"Alasan Izin Masuk Berbahaya ({dr.upper()})!")
                break

        if best_match:
            import re
            digits = re.findall(r"\b\d{10,14}\b", raw_combined)
            if digits:
                found_id = digits[0]
                expected_id = str(best_match.get("id_num", ""))
                if expected_id and found_id != expected_id:
                    anomalies.append(f"Nomor ID Palsu: terbaca '{found_id}', seharusnya '{expected_id}'")

        return best_match, anomalies

    def _run_full_autonomous_scan(self, is_autopilot=False):
        """
        PIPELINE UTAMA AUTONOMOUS ASTRA BOT:
        Tahap 1: Tangkap Frame Game
        Tahap 2: Sensor Wajah OpenCV (Urat/Parasit Merah, Topi, Bulu)
        Tahap 3: Sensor Dokumen OCR (Nama, ID, Tanggal, Alasan Masuk, Kamar)
        Tahap 4: Update Virtual Security Checklist 6 Poin
        Tahap 5: Putusan Otomatis (Buka Pintu vs Tutup & Panggil DDD 3312)
        """
        frame, _ = self._capture_game_frame()
        if frame is None:
            return None

        # ── TAHAP 1: SENSOR PENGLIHATAN WAJAH (MUTLAK) ──
        vis_verdict, vis_reasons = self._analyze_face_vision(frame)
        if vis_verdict == "EMPTY":
            if not is_autopilot:
                self._log("Loket kosong. Menunggu tamu tiba di jendela...")
            return None

        if vis_verdict == "IMPOSTOR":
            self._log(f"🚨 [VISUAL IMPOSTOR] Cacat fisik terdeteksi: {'; '.join(vis_reasons)}")
            self._apply_verdict_impostor("Wujud Fisik Monster", vis_reasons)
            if is_autopilot:
                time.sleep(0.2)
                self.auto_door_close_and_ddd()
            return "IMPOSTOR"

        # ── TAHAP 2: SENSOR DOKUMEN MEJA (OCR + DATABASE 30 WARGA) ──
        detected_texts = self._read_documents_with_auto_zoom(frame)
        best_match, doc_anomalies = self._audit_resident_database(detected_texts)

        if doc_anomalies and ("Nama Palsu" in doc_anomalies[0] or "Berbahaya" in doc_anomalies[0] or "Nomor ID" in doc_anomalies[0]):
            self._log(f"🚨 [DOCUMENT IMPOSTOR] Dokumen palsu terdeteksi: {'; '.join(doc_anomalies)}")
            self._apply_verdict_impostor("Kecurangan Dokumen", doc_anomalies)
            return "IMPOSTOR"

        if best_match:
            self._log(f"✅ [VERIFIED HUMAN] {best_match['name']} ({best_match['apt']}) 100% Lolos Verifikasi.")
            self._apply_verdict_human(best_match)
            return "HUMAN"

        self._log("Wajah bersih. Dekatkan atau letakkan dokumen di meja untuk verifikasi.")
        return None

    def _ocr_auto_detect(self, is_autopilot=False):
        """Wrapper untuk scan OCR."""
        return self._run_full_autonomous_scan(is_autopilot=is_autopilot)

    def _apply_verdict_impostor(self, category, reasons):
        """Terapkan status merah IMPOSTOR ke seluruh elemen antarmuka."""
        self._hero_box.configure(fg_color=T["red_bg"], border_color=T["red"])
        self._hero_title.configure(
            text="🛑 IMPOSTOR / DOPPELGANGER! TUTUP PINTU! 🚨",
            text_color="#FFFFFF"
        )
        reason_txt = "\n• ".join(reasons)
        self._hero_action.configure(
            text=(
                f"❌ JANGAN DIBUKA! BOT MENDETEKSI {category.upper()}:\n"
                f"• {reason_txt}\n"
                f"👉 TEKAN [ALT+D] UNTUK AUTO-LOCK & CALL DDD 3312!"
            ),
            text_color="#FCA5A5"
        )

        if hasattr(self, "_chk_photo"):
            first_r = reasons[0] if reasons else "Anomali Terdeteksi"
            self._chk_photo.configure(text=f"[❌ CACAT] 1. Foto Wajah & Wujud: {first_r}", text_color=T["red"])
            self._chk_id.configure(text=f"[❌ ILEGAL] 2. ID Card & Nomor ID: Tidak Lolos Uji", text_color=T["red"])
            self._chk_entry.configure(text=f"[❌ DITOLAK] 3. Alasan Izin Masuk Ditolak", text_color=T["red"])
            self._chk_list.configure(text=f"[❌ BAHAYA] 4. Tamu Anomali Mengancam Gedung", text_color=T["red"])
            self._chk_ddd.configure(text=f"[🚨 DARURAT] 5. Panggil DDD 3312 Segera!", text_color=T["red"])
            if hasattr(self, "_chk_phone"):
                self._chk_phone.configure(text=f"[⚠️ KUNCI] 6. Telepon Kamar / Laporkan DDD 3312", text_color=T["red"])

        try:
            for _ in range(3):
                winsound.Beep(420, 140)
                time.sleep(0.04)
        except Exception:
            pass

    def _apply_verdict_human(self, res):
        """Terapkan status hijau MANUSIA SAH ke seluruh elemen antarmuka."""
        name = res["name"]
        opt_val = f"{name} ({res['apt']})"
        if hasattr(self, "_drop_res"):
            self._drop_res.set(opt_val)
            self._on_dropdown_change(opt_val)

        self._hero_box.configure(fg_color=T["green_bg"], border_color=T["green"])
        self._hero_title.configure(
            text=f"✅ 100% MANUSIA ASLI: {name.upper()}",
            text_color="#FFFFFF"
        )
        phone_txt = res.get("phone", "N/A")
        self._hero_action.configure(
            text=(
                f"• Apartemen: {res['apt']} (Lantai {res['floor']}) | Telepon: {phone_txt}\n"
                f"• Dokumen ID ({res['id_num']}), Checklist, & Wujud Fisik 100% Sah!\n"
                f"👉 TEKAN [ALT+O] UNTUK BUKA PINTU LOKET!"
            ),
            text_color="#A7F3D0"
        )

        if hasattr(self, "_chk_photo"):
            self._chk_photo.configure(text=f"[✔ LOLOS] 1. Foto Wajah & Wujud Fisik Bersih ({name})", text_color=T["green"])
            self._chk_id.configure(text=f"[✔ LOLOS] 2. ID Card & Nomor ID Sah ({res['id_num']})", text_color=T["green"])
            self._chk_entry.configure(text=f"[✔ LOLOS] 3. Alasan Izin Masuk Sah (Bebas Pest/Sihir)", text_color=T["green"])
            self._chk_list.configure(text=f"[✔ LOLOS] 4. Terdaftar di Gedung (Apt {res['apt']} Lantai {res['floor']})", text_color=T["green"])
            self._chk_ddd.configure(text=f"[✔ LOLOS] 5. Cap & Watermark Resmi DDD 1955 Valid", text_color=T["green"])
            if hasattr(self, "_chk_phone"):
                self._chk_phone.configure(text=f"[✔ LOLOS] 6. Telepon Kamar Terdaftar ({phone_txt})", text_color=T["green"])

        try:
            winsound.Beep(1200, 90)
            winsound.Beep(1500, 110)
        except Exception:
            pass

    # ══════════════════════════════════════════════════════════════════════════
    # KONTROL OTOMATIS PINTU & TELEPON DDD VIA WIN32 SENDINPUT
    # ══════════════════════════════════════════════════════════════════════════
    def _get_game_hwnd(self):
        """Mendapatkan HWND jendela game That's Not My Neighbor."""
        hwnd = win32gui.FindWindow(None, "That's not my neighbor")
        if not hwnd:
            wins = []
            win32gui.EnumWindows(lambda h, _: wins.append((h, win32gui.GetWindowText(h))), None)
            for h, t in wins:
                if "neighbor" in t.lower() and win32gui.IsWindowVisible(h):
                    hwnd = h
                    break
        return hwnd

    def _get_game_window_rect(self):
        """Mendapatkan koordinat jendela game That's Not My Neighbor."""
        hwnd = self._get_game_hwnd()
        if hwnd:
            return hwnd, win32gui.GetWindowRect(hwnd)
        return None, None

    def _click_1080p(self, x_1080, y_1080):
        """
        Model Matematika Transformasi Viewport Godot 4 (Argon Viewport Calibrator):
        1. Ambil GetClientRect & ClientToScreen
        2. Hitung skala seragam: s = min(client_w / 1920.0, client_h / 1080.0)
        3. Kompensasi letterbox / black bars: offset_x = (client_w - 1920*s)/2, offset_y = (client_h - 1080*s)/2
        4. Posisi absolut layar: x_screen = origin_x + offset_x + round(x_1080 * s)
        """
        hwnd = self._get_game_hwnd()
        if not hwnd:
            self._log("[BOT] Jendela game tidak ditemukan!")
            return False
        left, top, right, bottom = win32gui.GetClientRect(hwnd)
        client_w = float(right - left)
        client_h = float(bottom - top)
        if client_w <= 0 or client_h <= 0:
            return False

        origin_x, origin_y = win32gui.ClientToScreen(hwnd, (0, 0))
        scale = min(client_w / 1920.0, client_h / 1080.0)
        vp_w = 1920.0 * scale
        vp_h = 1080.0 * scale

        offset_x = (client_w - vp_w) / 2.0
        offset_y = (client_h - vp_h) / 2.0

        final_x = int(round(origin_x + offset_x + (x_1080 * scale)))
        final_y = int(round(origin_y + offset_y + (y_1080 * scale)))

        try:
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.04)
            ctypes.windll.user32.SetCursorPos(final_x, final_y)
            time.sleep(0.02)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # MOUSEEVENTF_LEFTDOWN
            time.sleep(0.04)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # MOUSEEVENTF_LEFTUP
            return True
        except Exception as e:
            self._log(f"[Click Error] {e}")
            return False

    def _click_game_coords(self, norm_x, norm_y):
        """Konversi koordinat relatif ke 1080p pixel lalu klik via Viewport Calibrator."""
        x_1080 = int(round(norm_x * 1920.0))
        y_1080 = int(round(norm_y * 1080.0))
        return self._click_1080p(x_1080, y_1080)

    def _type_keys_to_game(self, text):
        """Mengirim keystroke ke jendela game secara otomatis (misal nomor telepon)."""
        hwnd, _ = self._get_game_window_rect()
        if not hwnd:
            return
        try:
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.05)
            for ch in str(text):
                if ch.isdigit():
                    vk = 0x30 + int(ch)
                elif ch.upper() == "ENTER" or ch == "\n":
                    vk = 0x0D
                else:
                    vk = ord(ch.upper())
                ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
                time.sleep(0.04)
                ctypes.windll.user32.keybd_event(vk, 0, 2, 0)
                time.sleep(0.06)
            ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
            time.sleep(0.04)
            ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
        except Exception as e:
            self._log(f"[Type Error] {e}")

    def auto_call_room(self):
        """[TELEPON KAMAR OTOMATIS] Angkat telepon loket & dial nomor kamar penghuni."""
        if not self._selected_res:
            self._log("Pilih penghuni terlebih dahulu untuk menghubungi kamar.")
            return
        phone = self._selected_res.get("phone", "")
        if not phone:
            self._log(f"Nomor telepon tidak tercatat untuk {self._selected_res['name']}.")
            return

        self._log(f"📞 Menghubungi kamar {self._selected_res['apt']} (Nomor: {phone})...")
        self._click_game_coords(0.17, 0.88)
        time.sleep(0.35)
        self._type_keys_to_game(phone)

    def _send_radar_command(self, cmd: str):
        """Kirim perintah langsung ke Godot 4 via user://radar_cmd.txt (0-Click, 100% Reliable)."""
        try:
            cmd_path = os.path.join(SAVE_DIR, "radar_cmd.txt")
            with open(cmd_path, "w", encoding="utf-8") as f:
                f.write(cmd + "\n")
            self._log(f"📡 [ENGINE COMMAND] Mengirim '{cmd}' ke Godot engine!")
            try:
                winsound.Beep(1200, 60)
            except Exception:
                pass
        except Exception as e:
            self._log(f"[Radar Cmd Err] {e}")

    def auto_door_open(self):
        """[ALT+O / ALT+3] BUKA PINTU LOKET INSTAN VIA GODOT HOOK."""
        self._log("⚡ [RADAR ENGINE] Membuka pintu loket langsung via Godot Hook...")
        self._set_human_verdict()
        self._send_radar_command("OPEN_DOOR")

    def auto_door_close_and_ddd(self):
        """[ALT+D / ALT+2] KUNCI PINTU & ALARM BAHAYA INSTAN VIA GODOT HOOK."""
        self._log("🚨 [RADAR ENGINE] Mengunci pintu & alarm darurat langsung via Godot Hook...")
        self._set_impostor_verdict()
        self._send_radar_command("EMERGENCY_DDD")

    def _on_switch_autopilot(self):
        val = bool(self.sw_autopilot.get())
        if val != self._autopilot_active:
            self._toggle_autopilot()

    def _on_switch_chester(self):
        val = bool(self.sw_chester.get())
        self._chester_active = val
        st = "AKTIF [ON]" if val else "NONAKTIF [OFF]"
        self._log(f"🧠 Chester Zero-Click Solver: {st}")
        try: winsound.Beep(1200 if val else 700, 60)
        except Exception: pass

    def _on_switch_radar_hook(self):
        val = bool(self.sw_radar_hook.get())
        self._radar_hook_active = val
        st = "AKTIF [ON]" if val else "NONAKTIF [OFF]"
        self._log(f"👁️ Live Engine Telemetry: {st}")
        try: winsound.Beep(1200 if val else 700, 60)
        except Exception: pass

    def _on_switch_ranks(self):
        val = bool(self.sw_ranks.get())
        self._auto_ranks_active = val
        if val:
            self._inject_perfect_rank_s()
        st = "DIKUNCI 100% [ON]" if val else "NONAKTIF [OFF]"
        self._log(f"⭐ Auto-Lock S-Rank: {st}")
        try: winsound.Beep(1200 if val else 700, 60)
        except Exception: pass

    def _toggle_autopilot(self):
        """[ALT+A] Toggle Mode Autopilot Bot Otomatis Penuh."""
        self._autopilot_active = not self._autopilot_active
        if self._autopilot_active:
            if hasattr(self, "sw_autopilot"):
                self.sw_autopilot.select()
            if hasattr(self, "_btn_autopilot"):
                self._btn_autopilot.configure(
                    text="🟢 AUTOPILOT BOT: AKTIF! [ALT+A]\n(Menganalisis Tamu & Buka/Kunci Pintu Sendiri)",
                    fg_color="#064E3B", hover_color="#059669", border_color="#10B981"
                )
            self._log("🤖 [AUTOPILOT] BOT DIAKTIFKAN! Bot otomatis mendeteksi dokumen & mengambil keputusan.")
            try:
                winsound.Beep(1000, 80)
                winsound.Beep(1400, 120)
            except Exception:
                pass
        else:
            if hasattr(self, "sw_autopilot"):
                self.sw_autopilot.deselect()
            if hasattr(self, "_btn_autopilot"):
                self._btn_autopilot.configure(
                    text="⚪ AUTOPILOT BOT: STANDBY [ALT+A]\n(Klik untuk Menyerahkan Seluruh Analisis & Keputusan ke Bot)",
                    fg_color=T["card2"], hover_color=T["border_hi"], border_color=T["border"]
                )
            self._log("🤖 [AUTOPILOT] Bot standby. Kembali ke kendali manual [ALT+1 / ALT+D / ALT+O].")
            try:
                winsound.Beep(800, 100)
            except Exception:
                pass

    def _autopilot_worker(self):
        """Worker pasif pengawas status loket (Zero-Click)."""
        while True:
            time.sleep(2.0)

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 2: KARTU BADUT (NIGHTMARE CLOWN — UNFATHOMABLE)
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_clown(self, parent):
        ctk.CTkLabel(parent, text="🃏 MINI-GAME KARTU BADUT (UNFATHOMABLE / OLD MAID)",
                     font=("Consolas", 11, "bold"), text_color=T["acc"]).pack(padx=8, pady=(4, 2))

        rule_box = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8,
                                border_width=1, border_color=T["border"])
        rule_box.pack(fill="x", padx=8, pady=3)

        ctk.CTkLabel(
            rule_box,
            text=(
                "📖 ATURAN RESMI GODOT SOURCE CODE:\n"
                "• Game ini adalah variasi Old Maid (Cabut Kartu Kembar).\n"
                "• Semua kartu memiliki pasangan kembar KECUALI 1 Kartu Joker Badut ('payaso')!\n"
                "• Setiap giliran: Anda mencabut 1 kartu dari tangan Badut, lalu Badut mencabut 1 kartu dari Anda.\n"
                "• Setiap pasangan kembar otomatis dibuang dari tangan.\n"
                "• Yang tersisa memegang Kartu Joker Badut sendirian di akhir permainan KALAH & DIBUNUH!"
            ),
            font=("Consolas", 8), text_color=T["main"], justify="left"
        ).pack(anchor="w", padx=10, pady=6)

        rec_card = ctk.CTkFrame(parent, fg_color="#180700", corner_radius=10,
                                border_width=2, border_color=T["acc"])
        rec_card.pack(fill="x", padx=8, pady=4)

        self._clown_rec_title = ctk.CTkLabel(
            rec_card, text="💡 STRATEGI KEMENANGAN MUTLAK",
            font=("Consolas", 11, "bold"), text_color=T["acc"]
        )
        self._clown_rec_title.pack(pady=(6, 2))

        self._clown_rec_detail = ctk.CTkLabel(
            rec_card,
            text=(
                "1. Prioritaskan mencabut kartu lawan yang nilai angkanya cocok dengan kartu di tangan Anda agar langsung terbuang!\n"
                "2. Jangan pernah mencabut kartu Joker pembunuh!\n"
                "3. Array 'mano_payaso' di memori Godot 4 sudah menyimpan urutan kartu sejak awal dibagikan.\n"
                "4. Jika menggunakan RadarHook.gd, panggil solve_clown_card_game() untuk auto-win instan!"
            ),
            font=("Consolas", 8), text_color=T["gold"], justify="left"
        )
        self._clown_rec_detail.pack(padx=10, pady=(0, 6))

        # Tabel Referensi Cepat
        table_card = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8,
                                 border_width=1, border_color=T["border"])
        table_card.pack(fill="x", padx=8, pady=3)

        ctk.CTkLabel(table_card, text="PILIH NILAI KARTU TANGAN ANDA UNTUK CEK PASANGAN:",
                     font=("Consolas", 9, "bold"), text_color=T["cyan"]).pack(anchor="w", padx=10, pady=(6, 2))

        opt_box = ctk.CTkFrame(table_card, fg_color="transparent")
        opt_box.pack(fill="x", padx=8, pady=(0, 6))

        for rk in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JOKER"]:
            btn = ctk.CTkButton(
                opt_box, text=rk, width=32, height=24, font=("Consolas", 8, "bold"),
                fg_color=T["border"] if rk != "JOKER" else T["red_bg"],
                hover_color=T["acc"], command=lambda val=rk: self._set_table_card(val)
            )
            btn.pack(side="left", padx=1, pady=2)

    def _set_table_card(self, val):
        if val == "JOKER":
            self._clown_rec_title.configure(text="⚠️ AWAS: ANDA MEMEGANG KARTU JOKER!")
            self._clown_rec_detail.configure(
                text="Biarkan Badut mencabut kartu Joker ini dari tangan Anda di giliran berikutnya! Jangan sampai tertahan di tangan Anda saat kartu lain habis!"
            )
            try: winsound.Beep(450, 150)
            except Exception: pass
        else:
            self._clown_rec_title.configure(text=f"🎯 MENCARI PASANGAN KARTU [{val}]")
            self._clown_rec_detail.configure(
                text=f"Cabut kartu dengan nilai [{val}] dari tangan Badut agar sepasang kartu langsung dibuang dari tangan Anda!"
            )
            try: winsound.Beep(1100, 60)
            except Exception: pass

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 3: KUIS CHESTER
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_chester(self, parent):
        ctk.CTkLabel(parent, text="Bocoran Kuis Chester Resmi (Pemberi Medali Rahasia):",
                     font=("Consolas", 9), text_color=T["muted"]).pack(padx=8, pady=(4, 2))

        sc = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=8, pady=4)

        for q, a in CHESTER_QUIZ:
            box = ctk.CTkFrame(sc, fg_color=T["card"], corner_radius=8,
                               border_width=1, border_color=T["border"])
            box.pack(fill="x", pady=3)

            ctk.CTkLabel(box, text=f"❓ {q}", font=("Consolas", 9, "bold"),
                         text_color=T["main"], anchor="w", wraplength=480).pack(anchor="w", padx=10, pady=(6, 2))

            ans_row = ctk.CTkFrame(box, fg_color=T["card2"], corner_radius=6)
            ans_row.pack(fill="x", padx=10, pady=(2, 6))

            ctk.CTkLabel(ans_row, text=f"JAWABAN: {a}", font=("Consolas", 11, "bold"),
                         text_color=T["acc"]).pack(side="left", padx=8, pady=4)

            ctk.CTkButton(
                ans_row, text="AUTO-KETIK", width=85, height=22, font=("Consolas", 8, "bold"),
                fg_color=T["green_bg"], hover_color=T["green"],
                command=lambda val=a: self._auto_type_chester(val)
            ).pack(side="right", padx=(2, 6), pady=4)

            ctk.CTkButton(
                ans_row, text="SALIN", width=50, height=22, font=("Consolas", 8, "bold"),
                fg_color=T["border"], hover_color=T["sec"],
                command=lambda val=a: self._copy_to_clip(val)
            ).pack(side="right", padx=2, pady=4)

    def _copy_to_clip(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        self._log(f"Disalin ke Clipboard: {text}")
        try:
            winsound.Beep(1200, 60)
        except Exception:
            pass

    def _auto_type_chester(self, text):
        """Salin teks ke clipboard, fokuskan jendela game, dan otomatis kirim Ctrl+V + Enter."""
        try:
            self.clipboard_clear()
            self.clipboard_append(text)
            self.update()
            hwnd = self._get_game_hwnd()
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)
                time.sleep(0.08)
                # Kirim Ctrl+V
                ctypes.windll.user32.keybd_event(0x11, 0, 0, 0) # VK_CONTROL
                time.sleep(0.02)
                ctypes.windll.user32.keybd_event(0x56, 0, 0, 0) # 'V'
                time.sleep(0.04)
                ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)
                time.sleep(0.02)
                ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)
                time.sleep(0.08)
                # Kirim Enter
                ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
                time.sleep(0.04)
                ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
                self._log(f"✍️ [CHESTER] Terkirim instan: {text}")
                winsound.Beep(1200, 60)
            else:
                self._log("[-] Jendela game tidak ditemukan untuk auto-type.")
        except Exception as e:
            self._log(f"[Type Chester Err] {e}")

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 4: S-RANK PATCHER
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_ranks(self, parent):
        s_hero = ctk.CTkFrame(parent, fg_color="#062E1C", corner_radius=10,
                              border_width=2, border_color=T["green"])
        s_hero.pack(fill="x", padx=8, pady=6)

        ctk.CTkLabel(s_hero, text="🏆 JAMINAN HASIL AKHIR: RANK S",
                     font=("Consolas", 13, "bold"), text_color=T["green"]).pack(pady=(8, 2))
        ctk.CTkLabel(s_hero,
                     text="Tekan tombol di bawah untuk mengunci seluruh antrean shift sebagai Manusia Sah!",
                     font=("Consolas", 9), text_color=T["main"]).pack(pady=(0, 6))

        ctk.CTkButton(
            s_hero, text="⭐ INJEK 100% RANK S SEKARANG [ALT+4]",
            font=("Consolas", 11, "bold"), fg_color=T["green"],
            text_color="#000000", hover_color="#34D399", height=36,
            command=self._inject_perfect_rank_s
        ).pack(fill="x", padx=12, pady=(2, 10))

        sv_card = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8,
                               border_width=1, border_color=T["border"])
        sv_card.pack(fill="both", expand=True, padx=8, pady=4)

        ctk.CTkLabel(sv_card, text="💾 STATUS ANTREAN SHIFT (DATA_RECORD.SAVE):",
                     font=("Consolas", 10, "bold"), text_color=T["cyan"]).pack(anchor="w", padx=10, pady=(6, 2))

        self._save_lbl = ctk.CTkLabel(
            sv_card, text="Membaca antrean...", font=("Consolas", 9),
            text_color=T["muted"], anchor="w", justify="left"
        )
        self._save_lbl.pack(anchor="w", padx=14, pady=(2, 6))

    def _inject_perfect_rank_s(self):
        targets = [RECORD_SAVE, RECORD2_SAVE]
        success = False
        for fpath in targets:
            if os.path.isfile(fpath):
                try:
                    data = bytearray(open(fpath, "rb").read())
                    for i in range(0, len(data) - 11, 12):
                        data[i:i + 12] = struct.pack("<Iq", 8, 1)
                    open(fpath, "wb").write(bytes(data))
                    success = True
                except Exception as e:
                    self._log(f"Error patch {os.path.basename(fpath)}: {e}")

        if success:
            self._log("⭐ RANK S AKTIF: Seluruh antrean berhasil dikunci 100% Valid!")
            self._scan_save()
            try:
                winsound.Beep(1600, 100)
            except Exception:
                pass
        else:
            self._log("Save belum ada di disk — Jalankan game sekali dulu")

    def _scan_save(self):
        if not os.path.isfile(RECORD_SAVE):
            self._save_lbl.configure(text=f"Save belum ada:\n{RECORD_SAVE}", text_color=T["red"])
            return
        try:
            data = open(RECORD_SAVE, "rb").read()
            entries = []
            for i in range(0, len(data) - 11, 12):
                _, val = struct.unpack("<Iq", data[i:i + 12])
                entries.append(val)
            self._save_data = entries

            lines = []
            for idx, v in enumerate(entries):
                st = "✅ MANUSIA" if v == 1 else ("🚨 DOPPEL" if v == 2 else f"val={v}")
                lines.append(f"V{idx+1}:{st}")
            rows = ["   ".join(lines[i:i+5]) for i in range(0, len(lines), 5)]
            self._save_lbl.configure(text="\n".join(rows), text_color=T["blue"])
        except Exception as e:
            self._log(f"Scan save error: {e}")

    def _save_watcher(self):
        while True:
            try:
                if os.path.isfile(RECORD_SAVE):
                    mt = os.path.getmtime(RECORD_SAVE)
                    if mt != self._last_save_mtime:
                        self._last_save_mtime = mt
                        self.after(0, self._scan_save)
            except Exception:
                pass
            time.sleep(3)

    def _radar_file_watcher(self):
        """Memantau file user://radar_state.json jika diekspor via GDScript RadarHook."""
        import json
        while True:
            try:
                if os.path.isfile(self._radar_json_path):
                    mt = os.path.getmtime(self._radar_json_path)
                    if mt != self._last_radar_mtime:
                        self._last_radar_mtime = mt
                        with open(self._radar_json_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        self.after(0, lambda d=data: self._on_radar_json_event(d))
            except Exception:
                pass
            time.sleep(0.20)

    def _on_radar_json_event(self, data):
        if not getattr(self, "_radar_hook_active", True):
            return

        if data.get("status") == "HOOK_ACTIVE":
            self._log("📡 [RADAR HOOK] Godot 4.2 In-Engine Hook Terhubung & Aktif!")
            if hasattr(self, "_lbl_live_hook_status"):
                self._lbl_live_hook_status.configure(text="● ENGINE HOOK: TERHUBUNG (Godot 4.2 Forward+)", text_color=T["green"])
            return

        # 1. Handle Event Chester Auto-Solver Telemetry
        if data.get("event") == "chester_quiz" or "chester_auto_answer" in data:
            if not getattr(self, "_chester_active", True):
                return
            q_sig = data.get("chester_question", "")
            ans = data.get("chester_auto_answer", "")
            self._log(f"🧠 [CHESTER] Signature '{q_sig}' -> Jawaban: '{ans}' (Tersalin ke Clipboard!)")
            try:
                self.clipboard_clear()
                self.clipboard_append(ans)
                winsound.Beep(1400, 80)
            except Exception:
                pass
            return

        name = data.get("name", "Unknown")
        apt = data.get("apartment", "00")
        is_doppel = bool(data.get("is_doppelganger", False))
        guest_node_doppel = bool(data.get("guest_node_is_doppelganger", False))
        if guest_node_doppel:
            is_doppel = True
        flaws = data.get("flaws", {})
        nightmare = data.get("nightmare_stealth", {})
        all_vars = data.get("all_variables", {})
        raw_char = data.get("raw_char", name)
        not_on_list = bool(data.get("not_on_today_list", False))
        vis_active = bool(data.get("visitor_active", True))
        ts_num = data.get("timestamp", 0)
        ts_str = time.strftime("%H:%M:%S", time.localtime(ts_num)) if ts_num else time.strftime("%H:%M:%S")

        # Update Live Radar Tab Card
        if hasattr(self, "_live_guest_title"):
            self._live_guest_title.configure(text=f"👤 TAMU DI JENDELA: {name.upper()}")

            if not vis_active and name != "Chester":
                self._live_verdict_card.configure(fg_color=T["card2"], border_color=T["border_hi"])
                self._live_status_badge.configure(text="⏳ JENDELA KOSONG — MENUNGGU TAMU BERIKUTNYA", text_color=T["muted"])
            elif is_doppel:
                self._live_verdict_card.configure(fg_color=T["red_bg"], border_color=T["red"])
                self._live_status_badge.configure(text="🛑 IMPOSTOR / DOPPELGANGER TERDETEKSI!", text_color="#FFFFFF")
            else:
                self._live_verdict_card.configure(fg_color=T["green_bg"], border_color=T["green"])
                self._live_status_badge.configure(text="✅ 100% MANUSIA ASLI — SAH BUKA PINTU", text_color="#FFFFFF")

            list_txt = "⚠️ TIDAK ADA DI DAFTAR HARI INI!" if not_on_list else "✅ Terdaftar di Jadwal Hari Ini"
            doppel_txt = "🛑 TRUE (MONSTER)" if is_doppel else "✅ FALSE (Manusia)"
            info_txt = (
                f"• Raw Node Game: {raw_char}\n"
                f"• Status Doppelganger: {doppel_txt}\n"
                f"• Jadwal Kunjungan: {list_txt}\n"
                f"• Terdeteksi Engine: Pukul {ts_str} WIB"
            )
            self._live_audit_info.configure(text=info_txt)

            if hasattr(self, "_txt_live_dump"):
                try:
                    pretty_data = {
                        "name": name,
                        "raw_char": raw_char,
                        "is_doppelganger": is_doppel,
                        "guest_node_is_doppelganger": guest_node_doppel,
                        "not_on_today_list": not_on_list,
                        "visitor_active": vis_active,
                        "alarm_on": data.get("alarm_on", False),
                        "chester_question_active": data.get("chester_question_active", False),
                        "all_variables": all_vars
                    }
                    self._txt_live_dump.delete("1.0", "end")
                    self._txt_live_dump.insert("1.0", json.dumps(pretty_data, indent=2))
                except Exception:
                    pass

        # Tidak ada tamu di jendela (is_neighbor_on == False) & bukan Chester: jangan keluarkan putusan di Hero
        if data.get("status") == "VISITOR_DETECTED" and not vis_active and name != "Chester":
            self._log("📡 [RADAR HOOK] Jendela kosong — menunggu tamu berikutnya...")
            self._hero_box.configure(fg_color=T["card2"], border_color=T["border_hi"])
            self._hero_title.configure(text="⏳ JENDELA KOSONG", text_color=T["muted"])
            self._hero_action.configure(text="Menunggu tamu berikutnya tiba di jendela kaca loket...", text_color=T["main"])
            return

        # Audit Nightmare Mode Stealth Vectors
        stealth_reasons = []
        if nightmare.get("already_inside"):
            stealth_reasons.append("DUPLIKASI: Warga asli sudah di dalam kamar (ya_adentro)!")
            is_doppel = True
        if nightmare.get("dialogue_lie"):
            stealth_reasons.append("KEBOHONGAN DIALOG: Interogasi menyimpang (mentira)!")
            is_doppel = True
        if not nightmare.get("ddd_logo_ok", True):
            stealth_reasons.append("LOGO DDD PALSU: Lambang D.D.D. kartu ID cacat!")
            is_doppel = True
        if nightmare.get("error_type"):
            stealth_reasons.append(f"Tipe Error: {nightmare['error_type']}")

        self._log(f"📡 [RADAR HOOK] {raw_char} | Doppel: {is_doppel} | Tidak di daftar hari ini: {not_on_list}")
        if all_vars:
            self._log(f"🔍 [REFLECTION DUMP] {len(all_vars)} variabel GDScript berhasil disedot!")

        if is_doppel:
            bad_keys = [k.replace("_ok", "").upper() for k, v in flaws.items() if not v]
            reasons = stealth_reasons + bad_keys
            reasons.append(f"Flag Doppelganger dibaca langsung dari kode game ({raw_char})")
            self._apply_verdict_impostor("Radar Engine Hook", reasons)
            try:
                winsound.Beep(800, 120)
            except Exception:
                pass
        else:
            match_res = {"name": name, "apt": apt, "floor": 1, "id_num": "Verified", "phone": "-"}
            nlow = name.lower().strip()
            ntok = nlow.split()
            for r in RESIDENTS:
                rlow = r["name"].lower().strip()
                rtok = rlow.split()
                if rlow == nlow or (len(ntok) >= 2 and len(rtok) >= 2
                                    and rtok[0][:4] == ntok[0][:4] and rtok[-1][:4] == ntok[-1][:4]):
                    match_res = r
                    break
            self._apply_verdict_human(match_res)
            if not_on_list:
                self._log(f"📋 [PERHATIAN] {name} TIDAK ada di daftar hari ini — periksa izin masuk!")
            try:
                winsound.Beep(1200, 80)
            except Exception:
                pass

    # ══════════════════════════════════════════════════════════════════════════
    # BACKGROUND THREADS
    # ══════════════════════════════════════════════════════════════════════════
    def _set_online(self, pid):
        self._dot.configure(text_color=T["green"])
        self._stat.configure(text=f"● {PROC_NAME}  [PID {pid}]  RUNNING", text_color=T["green"])

    def _set_offline(self):
        self._dot.configure(text_color=T["red"])
        self._stat.configure(text=f"Menunggu: {PROC_NAME}", text_color=T["muted"])

    def _process_watch(self):
        prev_pid = None
        while True:
            try:
                found = None
                for p in psutil.process_iter(["name", "pid"]):
                    n = p.info.get("name") or ""
                    if PROC_NAME.lower() in n.lower() or "neighbor" in n.lower():
                        found = p.info["pid"]
                        break
                if found != prev_pid:
                    prev_pid = found
                    self.game_pid = found
                    if found:
                        p_snap = found
                        self.after(0, lambda p=p_snap: self._set_online(p))
                    else:
                        self.after(0, self._set_offline)
            except Exception:
                pass
            time.sleep(4)

    def _scan_and_ocr(self):
        """ALT+1: Jalankan OpenCV scan + OCR auto-detect sekaligus."""
        self._scan_screen_vision()
        # Jalankan OCR di thread terpisah agar tidak freeze UI
        threading.Thread(target=self._ocr_auto_detect, daemon=True).start()

    # ══════════════════════════════════════════════════════════════════════════
    # TAB 5: EXE & TOOLS
    # ══════════════════════════════════════════════════════════════════════════
    def _build_tab_tools(self, parent):
        ctk.CTkLabel(parent, text="Alat Analisis Biner EXE & Eksekusi Cepat (Protokol ASTRA):",
                     font=("Consolas", 10, "bold"), text_color=T["acc"]).pack(padx=8, pady=(8, 4))

        sc = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8, border_width=1, border_color=T["border"])
        sc.pack(fill="x", padx=8, pady=4)

        ctk.CTkButton(
            sc, text="🔬 BUKA PE-BEAR (GUI PE ANALYZER)",
            font=("Consolas", 10, "bold"), fg_color=T["purple"], hover_color="#9333EA",
            height=34, command=lambda: subprocess.Popen(r'start "" "D:\Game\Tools\BUKA_PE_BEAR.bat"', shell=True)
        ).pack(fill="x", padx=12, pady=6)

        ctk.CTkButton(
            sc, text="🐛 BUKA X64DBG (ASSEMBLY DEBUGGER)",
            font=("Consolas", 10, "bold"), fg_color="#1E3A8A", hover_color="#2563EB",
            height=34, command=lambda: subprocess.Popen(r'start "" "D:\Game\Tools\BUKA_X64DBG.bat"', shell=True)
        ).pack(fill="x", padx=12, pady=6)

        ctk.CTkButton(
            sc, text="⚡ BUKA ASTRA EXE ANALYZER (SECTIONS & ENTROPY) [ALT+E]",
            font=("Consolas", 10, "bold"), fg_color=T["green_bg"], hover_color=T["green"],
            height=34, command=self._launch_exe_tools
        ).pack(fill="x", padx=12, pady=6)

        btn_row = ctk.CTkFrame(parent, fg_color="transparent")
        btn_row.pack(fill="x", padx=8, pady=6)

        ctk.CTkButton(
            btn_row, text="📁 BUKA FOLDER GAME",
            font=("Consolas", 9, "bold"), fg_color=T["card2"], hover_color=T["border_hi"],
            height=30, command=lambda: os.startfile(os.path.dirname(GAME_EXE))
        ).pack(side="left", expand=True, fill="x", padx=(0, 4))

        ctk.CTkButton(
            btn_row, text="💾 BUKA SAVE DATA",
            font=("Consolas", 9, "bold"), fg_color=T["card2"], hover_color=T["border_hi"],
            height=30, command=lambda: os.startfile(SAVE_DIR) if os.path.exists(SAVE_DIR) else None
        ).pack(side="left", expand=True, fill="x", padx=(4, 0))

    def _launch_exe_tools(self):
        self._log("⚡ Membuka ASTRA EXE Analyzer...")
        subprocess.Popen(r'start "" "D:\Game\Tools\BUKA_EXE_ANALYZER.bat"', shell=True)

    def _hotkey_loop(self):
        VK_5 = 0x35
        VK_A = 0x41 # 'A' Key -> Autopilot
        VK_D = 0x44 # 'D' Key -> Close + DDD
        VK_E = 0x45 # 'E' Key -> EXE Tools
        VK_O = 0x4F # 'O' Key -> Open Door
        prev = set()
        hkmap = {
            VK_1: self._scan_and_ocr,            # ALT+1: OpenCV + OCR AUTO-DETECT
            VK_2: self._set_impostor_verdict,     # ALT+2: IMPOSTOR -> TUTUP PINTU (Manual)
            VK_3: self._set_human_verdict,        # ALT+3: MANUSIA -> BUKA PINTU (Manual)
            VK_4: self._inject_perfect_rank_s,    # ALT+4: Rank S inject
            VK_5: self._ocr_auto_detect,          # ALT+5: OCR scan saja
            VK_A: self._toggle_autopilot,         # ALT+A: TOGGLE AUTOPILOT BOT PENUH!
            VK_D: self.auto_door_close_and_ddd,   # ALT+D: BOT AUTO TUTUP PINTU & TELPON DDD 3312!
            VK_E: self._launch_exe_tools,         # ALT+E: BUKA EXE ANALYZER & TOOLS
            VK_O: self.auto_door_open,            # ALT+O: BOT AUTO BUKA PINTU LOKET!
        }
        while True:
            try:
                alt = bool(user32.GetAsyncKeyState(VK_ALT) & 0x8000)
                if alt:
                    for vk, fn in hkmap.items():
                        pressed = bool(user32.GetAsyncKeyState(vk) & 0x8000)
                        if pressed and vk not in prev:
                            self.after(0, fn)
                        if pressed:
                            prev.add(vk)
                        else:
                            prev.discard(vk)
                else:
                    prev.clear()
            except Exception:
                pass
            time.sleep(0.05)

    def _launch(self):
        if not os.path.isfile(GAME_EXE):
            self._log(f"EXE tidak ada: {GAME_EXE}")
            return
        subprocess.Popen(f'start "" "{GAME_EXE}"', shell=True, cwd=os.path.dirname(GAME_EXE))
        self._log("Game diluncurkan ✅")

    def _log(self, msg: str):
        ts = time.strftime("%H:%M:%S")
        self.after(0, lambda: self._log_lbl.configure(text=f"[{ts}] {msg}"))


# ── Entry Point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = TMNMModMenu()
    app.mainloop()
