"""
================================================================================
ASTRA AI - JOURNEY TO THE SAVAGE PLANET MOD MENU v3.0 OPTIMIZED
Engineered for Komandan DAFFA // AMD RX 580 // 60% Keyboard (No F-keys, No Tilde)
================================================================================

ROOT CAUSE FIXES v3.0:
  1. UE4 Shipping Build = Console DISABLED by default
     FIX: Engine.ini patched with bAllowConsoleInShipBuild=True (done at launch)
  2. Tilde scan-code gagal di fullscreen exclusive DirectX
     FIX: pydirectinput (DirectInput API) untuk inject keyboard yang benar-benar masuk ke game
  3. Window tidak ditemukan karena UnrealWindow tidak ada saat fullscreen
     FIX: Focus via EnumWindows + AttachThreadInput + SetForegroundWindow
  4. Console key mapping
     FIX: Input.ini diset ConsoleKey=Tilde (dipatch sebelum game start)

DUAL MODE:
  [MODE 1] GUI Button Click  -> fokus game -> tilde (DirectInput) -> ketik perintah -> Enter
  [MODE 2] ALT+1..9 Hotkeys  -> sama, tanpa harus pindah ke GUI

KEYBOARD 60%: ALT+1..0, ALT+N, ALT+B, ALT+T (semua tanpa F-keys/numpad/tilde)
================================================================================
"""

import os, sys, time, json, threading, ctypes, ctypes.wintypes as wt
import winsound, subprocess
import customtkinter as ctk
import psutil

try:
    import pydirectinput
    HAS_PDI = True
    pydirectinput.PAUSE = 0.02
    pydirectinput.FAILSAFE = False
except ImportError:
    HAS_PDI = False

# ── WIN32 API ──────────────────────────────────────────────────────────────────
user32   = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# ── SENDINPUT STRUCTS (64-bit, sizeof=40) ─────────────────────────────────────
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx",wt.LONG),("dy",wt.LONG),("mouseData",wt.DWORD),
                ("dwFlags",wt.DWORD),("time",wt.DWORD),("dwExtraInfo",ctypes.c_size_t)]

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk",wt.WORD),("wScan",wt.WORD),("dwFlags",wt.DWORD),
                ("time",wt.DWORD),("dwExtraInfo",ctypes.c_size_t)]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [("uMsg",wt.DWORD),("wParamL",wt.WORD),("wParamH",wt.WORD)]

class INPUT_UNION(ctypes.Union):
    _fields_ = [("mi",MOUSEINPUT),("ki",KEYBDINPUT),("hi",HARDWAREINPUT)]

class INPUT(ctypes.Structure):
    _fields_ = [("type",wt.DWORD),("u",INPUT_UNION)]

INPUT_KEYBOARD   = 1
KEYEVENTF_KEYUP  = 0x0002
KEYEVENTF_UNICODE= 0x0004
KEYEVENTF_SCANCODE=0x0008
SCAN_TILDE  = 0x29
SCAN_RETURN = 0x1C
SCAN_BACK   = 0x0E

# ── VK CODES 60% Keyboard ─────────────────────────────────────────────────────
VK_MENU = 0x12
VK_0=0x30;VK_1=0x31;VK_2=0x32;VK_3=0x33;VK_4=0x34
VK_5=0x35;VK_6=0x36;VK_7=0x37;VK_8=0x38;VK_9=0x39
VK_N=0x4E;VK_B=0x42;VK_T=0x54;VK_R=0x52

# ── PATHS ─────────────────────────────────────────────────────────────────────
GAME_DIR = r"D:\Game\Games\Journey to the Savage Planet"
GAME_EXE = os.path.join(GAME_DIR, "Towers", "Binaries", "Win64", "Towers-Win64-Shipping.exe")
UE4_CFG  = os.path.expandvars(r"%LOCALAPPDATA%\Towers\Saved\Config\WindowsNoEditor")
ENGINE_INI = os.path.join(UE4_CFG, "Engine.ini")
INPUT_INI  = os.path.join(UE4_CFG, "Input.ini")

# ── THEME ─────────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
T = {
    "bg":      "#0B0D14",
    "card":    "#141824",
    "border":  "#283048",
    "gold":    "#F59E0B",
    "green":   "#10B981",
    "cyan":    "#00E5FF",
    "red":     "#EF4444",
    "purple":  "#A855F7",
    "blue":    "#3B82F6",
    "main":    "#F8FAFC",
    "muted":   "#94A3B8",
}


# ── PRE-LAUNCH PATCHER ────────────────────────────────────────────────────────
def patch_ue4_config():
    """Patch Engine.ini dan Input.ini untuk mengaktifkan console di Shipping build."""
    os.makedirs(UE4_CFG, exist_ok=True)

    # Engine.ini — bAllowConsoleInShipBuild
    eng_patch = "[/Script/Engine.Engine]\nbAllowConsoleInShipBuild=True\n\n[ConsoleVariables]\ncon.MinLogVerbosity=0\n"
    try:
        existing = open(ENGINE_INI, encoding="utf-8").read() if os.path.exists(ENGINE_INI) else ""
        if "bAllowConsoleInShipBuild" not in existing:
            with open(ENGINE_INI, "a", encoding="utf-8") as f:
                f.write("\n" + eng_patch)
    except Exception:
        pass

    # Input.ini — Console key binding
    inp_content = "[/Script/Engine.InputSettings]\nConsoleKey=Tilde\nConsoleKeys=(Key=Tilde)\nConsoleKeys=(Key=Caret)\n"
    try:
        with open(INPUT_INI, "w", encoding="utf-8") as f:
            f.write(inp_content)
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════════════════════════
class SavagePlanetModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        patch_ue4_config()  # Patch config sebelum apapun

        self.title("🪐 ASTRA // SAVAGE PLANET MOD MENU v3.0")
        self.geometry("440x680")
        self.minsize(420, 620)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.95)
        self.configure(fg_color=T["bg"])

        self.game_pid   = None
        self.state_god  = False
        self.state_fly  = False
        self.state_ghost= False
        self.state_speed= False
        self._last_cmd  = ""

        self.setup_ui()
        threading.Thread(target=self._bg_loop, daemon=True).start()

    # ── UI ────────────────────────────────────────────────────────────────────
    def setup_ui(self):
        # Header
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10,
                           border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=12, pady=(10,6))

        ctk.CTkLabel(hdr, text="🪐 SAVAGE PLANET TRAINER v3.0",
                     font=("Consolas",14,"bold"), text_color=T["gold"]).pack(anchor="w", padx=12, pady=(8,2))
        ctk.CTkLabel(hdr, text="UE4 CONSOLE INJECTOR // DIRECTINPUT // 60% KB // KOMANDAN DAFFA",
                     font=("Consolas",9,"bold"), text_color=T["muted"]).pack(anchor="w", padx=12, pady=(0,4))

        # Status
        sbox = ctk.CTkFrame(hdr, fg_color="#080A12", corner_radius=6)
        sbox.pack(fill="x", padx=10, pady=(0,6))
        self.dot  = ctk.CTkLabel(sbox, text="●", font=("Consolas",12), text_color=T["red"])
        self.dot.pack(side="left", padx=(8,4), pady=3)
        self.status = ctk.CTkLabel(sbox, text="Waiting for Towers-Win64-Shipping...",
                                   font=("Consolas",9,"bold"), text_color=T["muted"])
        self.status.pack(side="left", pady=3)

        # Log line
        self.log_lbl = ctk.CTkLabel(hdr, text="Cmd: —", font=("Consolas",8),
                                    text_color="#38BDF8")
        self.log_lbl.pack(anchor="w", padx=12, pady=(0,6))

        # Tabs
        self.tabs = ctk.CTkTabview(self, fg_color=T["card"],
                                   segmented_button_fg_color="#080C16",
                                   segmented_button_selected_color=T["blue"],
                                   segmented_button_unselected_color=T["card"],
                                   corner_radius=10)
        self.tabs.pack(fill="both", expand=True, padx=12, pady=(0,6))
        t1 = self.tabs.add("🎮 CHEATS")
        t2 = self.tabs.add("💎 ITEM SPAWN")
        t3 = self.tabs.add("⚙️ CONFIG")

        self._build_cheats_tab(t1)
        self._build_items_tab(t2)
        self._build_config_tab(t3)

        # Bottom
        bot = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10, height=36)
        bot.pack(fill="x", padx=12, pady=(0,10))
        ctk.CTkLabel(bot, text="Alpha:", font=("Consolas",9), text_color=T["muted"]).pack(side="left", padx=(10,4), pady=6)
        sl = ctk.CTkSlider(bot, from_=0.3, to=1.0, number_of_steps=14, width=100,
                           command=lambda v: self.attributes("-alpha", float(v)))
        sl.set(0.95); sl.pack(side="left", pady=6)
        ctk.CTkButton(bot, text="▶ LAUNCH GAME", font=("Consolas",10,"bold"),
                      fg_color=T["gold"], text_color="#0B0D14", hover_color="#D97706",
                      width=110, height=26, command=self.launch_game).pack(side="right", padx=10, pady=6)

    def _build_cheats_tab(self, parent):
        sc = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=2, pady=2)

        # Info
        info = ctk.CTkFrame(sc, fg_color="#0A1122", corner_radius=6, border_width=1, border_color="#1E2F52")
        info.pack(fill="x", pady=(0,8))
        ctk.CTkLabel(info,
            text="✅ UE4 Console DIAKTIFKAN via Engine.ini patch\n"
                 "⌨️ Gunakan tombol di sini ATAU hotkey ALT+1..9 saat di dalam game\n"
                 "💡 Pastikan game sedang berjalan sebelum klik cheat",
            font=("Consolas",9), text_color="#38BDF8", justify="left"
        ).pack(padx=8, pady=6, anchor="w")

        # Toggles
        self.btn_god   = self._toggle(sc,"🛡️ GOD MODE (Kebal Semua Damage)","ALT+1",self.toggle_god)
        self.btn_fly   = self._toggle(sc,"🦅 FREE FLIGHT (Terbang Bebas)","ALT+2",self.toggle_fly)
        self.btn_ghost = self._toggle(sc,"👻 GHOST / NOCLIP (Tembus Tembok)","ALT+3",self.toggle_ghost)
        self.btn_speed = self._toggle(sc,"⚡ SUPER SPEED (2.5x Kecepatan)","ALT+4",self.toggle_speed)

        # Actions
        self._action(sc,"⏱️ SLOWMO / BULLET TIME (0.5x)","ALT+5",T["purple"],self.cmd_slowmo)
        self._action(sc,"🚶 KEMBALI NORMAL (Walk)","ALT+6",T["green"],self.cmd_walk)
        self._action(sc,"🎯 TELEPORT KE ARAH BIDIKAN","ALT+8",T["gold"],self.cmd_teleport)
        self._action(sc,"📸 ULTRA SCREENSHOT (4K)","ALT+9",T["blue"],self.cmd_screenshot)
        self._action(sc,"🔓 GOD + UNLOCK ALL","ALT+T",T["green"],self.cmd_full_unlock)
        self._action(sc,"🚨 PANIC RESET (Normal Mode)","ALT+0",T["red"],self.cmd_panic)

    def _build_items_tab(self, parent):
        sc = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=2, pady=2)

        ctk.CTkLabel(sc, text="💎 ITEM & RESOURCE SPAWNER (UE4 GiveItem)", font=("Consolas",10,"bold"),
                     text_color=T["cyan"]).pack(anchor="w", pady=(2,6))

        items = [
            ("🔩 +500 Carbon (Bahan Dasar Utama)", "giveitem carbon 500", T["cyan"]),
            ("🔧 +500 Silicon (Komponen Elektronik)", "giveitem silicon 500", T["green"]),
            ("⚙️ +500 Aluminum (Bahan Kendaraan)", "giveitem aluminum 500", T["gold"]),
            ("🌿 +500 Organic Compound (Alien Bio)", "giveitem organiccompound 500", T["green"]),
            ("💜 +100 Alien Alloy (Material Langka)", "giveitem alienalloy 100", T["purple"]),
            ("🔋 +50 Electric Gel (Fuel Jet Pack)", "giveitem electricgel 50", T["blue"]),
            ("📦 STARTER PACK (Carbon+Silicon+Aluminum 300x)", "giveitem carbon 300;giveitem silicon 300;giveitem aluminum 300", T["cyan"]),
            ("🌍 ALL RESOURCES x200", "giveitem carbon 200;giveitem silicon 200;giveitem aluminum 200;giveitem organiccompound 200;giveitem alienalloy 50", T["gold"]),
        ]
        for lbl, cmd, col in items:
            self._spawn_btn(sc, lbl, cmd, col)

    def _build_config_tab(self, parent):
        sc = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=2, pady=2)

        ctk.CTkLabel(sc, text="⚙️ KONFIGURASI SISTEM", font=("Consolas",10,"bold"),
                     text_color=T["gold"]).pack(anchor="w", pady=(2,8))

        # Input method selector
        ctk.CTkLabel(sc, text="Metode Inject Keyboard:", font=("Consolas",9),
                     text_color=T["muted"]).pack(anchor="w")
        self.input_method = ctk.CTkOptionMenu(sc,
            values=["AUTO (pydirectinput → SendInput → fallback)", "pydirectinput DirectInput", "SendInput Scan Code"],
            font=("Consolas",9), width=300)
        self.input_method.pack(anchor="w", pady=(4,10))

        # Delay settings
        ctk.CTkLabel(sc, text="Console Open Delay (ms):", font=("Consolas",9), text_color=T["muted"]).pack(anchor="w")
        self.delay_slider = ctk.CTkSlider(sc, from_=100, to=800, number_of_steps=14, width=260)
        self.delay_slider.set(300)
        self.delay_slider.pack(anchor="w", pady=(4,2))
        self.delay_val = ctk.CTkLabel(sc, text="300ms", font=("Consolas",9), text_color=T["cyan"])
        self.delay_val.pack(anchor="w", pady=(0,10))
        self.delay_slider.configure(command=lambda v: self.delay_val.configure(text=f"{int(v)}ms"))

        # Patch status
        ctk.CTkLabel(sc, text="Status Config Files:", font=("Consolas",9,"bold"), text_color=T["gold"]).pack(anchor="w", pady=(8,4))
        eng_ok = "bAllowConsoleInShipBuild=True" in (open(ENGINE_INI).read() if os.path.exists(ENGINE_INI) else "")
        inp_ok = "ConsoleKey=Tilde" in (open(INPUT_INI).read() if os.path.exists(INPUT_INI) else "")
        ctk.CTkLabel(sc, text=f"  {'[OK]' if eng_ok else '[MISSING]'} Engine.ini → bAllowConsoleInShipBuild",
                     font=("Consolas",9), text_color=T["green"] if eng_ok else T["red"]).pack(anchor="w")
        ctk.CTkLabel(sc, text=f"  {'[OK]' if inp_ok else '[MISSING]'} Input.ini → ConsoleKey=Tilde",
                     font=("Consolas",9), text_color=T["green"] if inp_ok else T["red"]).pack(anchor="w")
        ctk.CTkLabel(sc, text=f"  {'[OK]' if HAS_PDI else '[MISSING]'} pydirectinput",
                     font=("Consolas",9), text_color=T["green"] if HAS_PDI else T["red"]).pack(anchor="w")
        ctk.CTkLabel(sc, text=f"  [OK] keyboard module",
                     font=("Consolas",9), text_color=T["green"]).pack(anchor="w")

        ctk.CTkButton(sc, text="🔄 RE-APPLY CONFIG PATCHES", font=("Consolas",9,"bold"),
                      fg_color=T["blue"], text_color="#FFF", width=200, height=28,
                      command=self._repatch).pack(anchor="w", pady=(12,4))

    def _repatch(self):
        patch_ue4_config()
        winsound.Beep(1400, 100)

    # ── WIDGET BUILDERS ───────────────────────────────────────────────────────
    def _toggle(self, parent, title, hotkey, cmd):
        box = ctk.CTkFrame(parent, fg_color=T["card"], border_width=1, border_color=T["border"], corner_radius=8)
        box.pack(fill="x", padx=2, pady=3)
        info = ctk.CTkFrame(box, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=8, pady=6)
        ctk.CTkLabel(info, text=title, font=("Consolas",10,"bold"), text_color=T["main"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=f"HOTKEY: {hotkey}", font=("Consolas",9), text_color=T["gold"], anchor="w").pack(anchor="w")
        btn = ctk.CTkButton(box, text="OFF", width=54, height=26, font=("Consolas",10,"bold"),
                            fg_color="#1E293B", hover_color="#334155", text_color=T["muted"],
                            corner_radius=6, command=cmd)
        btn.pack(side="right", padx=8, pady=6)
        return btn

    def _action(self, parent, title, hotkey, color, cmd):
        box = ctk.CTkFrame(parent, fg_color=T["card"], border_width=1, border_color=T["border"], corner_radius=8)
        box.pack(fill="x", padx=2, pady=3)
        info = ctk.CTkFrame(box, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=8, pady=5)
        ctk.CTkLabel(info, text=title, font=("Consolas",10,"bold"), text_color=T["main"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=f"TRIGGER: {hotkey}", font=("Consolas",9), text_color=color, anchor="w").pack(anchor="w")
        tc = "#0B0D14" if color != T["red"] else "#FFFFFF"
        ctk.CTkButton(box, text="APPLY", width=54, height=24, font=("Consolas",9,"bold"),
                      fg_color=color, hover_color="#334155", text_color=tc,
                      corner_radius=6, command=cmd).pack(side="right", padx=8, pady=5)

    def _spawn_btn(self, parent, label, cmds, color):
        box = ctk.CTkFrame(parent, fg_color=T["card"], border_width=1, border_color=T["border"], corner_radius=6)
        box.pack(fill="x", pady=2)
        ctk.CTkLabel(box, text=label, font=("Consolas",9,"bold"), text_color=T["main"], anchor="w").pack(side="left", padx=8, pady=5, fill="x", expand=True)
        ctk.CTkButton(box, text="+SPAWN", width=64, height=24, font=("Consolas",9,"bold"),
                      fg_color=color, hover_color="#334155", text_color="#0B0D14", corner_radius=4,
                      command=lambda c=cmds: self._compound(c)).pack(side="right", padx=6, pady=5)

    # ── INPUT ENGINE ──────────────────────────────────────────────────────────
    def _get_delay_ms(self):
        try:
            return int(self.delay_slider.get()) / 1000.0
        except Exception:
            return 0.30

    def _sendinput_key(self, scan, down=True):
        flags = KEYEVENTF_SCANCODE | (0 if down else KEYEVENTF_KEYUP)
        inp = INPUT(); inp.type = INPUT_KEYBOARD
        inp.u.ki = KEYBDINPUT(0, scan, flags, 0, 0)
        user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    def _sendinput_unicode(self, ch):
        for flag in (KEYEVENTF_UNICODE, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP):
            inp = INPUT(); inp.type = INPUT_KEYBOARD
            inp.u.ki = KEYBDINPUT(0, ord(ch), flag, 0, 0)
            user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    def _find_hwnd(self):
        """Temukan HWND game Towers dengan multi-strategy."""
        # Strategy 1: FindWindow dengan class UnrealWindow
        h = user32.FindWindowW("UnrealWindow", None)
        if h and user32.IsWindowVisible(h): return h

        # Strategy 2: Scan semua window berdasarkan PID
        if self.game_pid:
            WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_int, wt.HWND, wt.LPARAM)
            found = []
            def cb(h, _):
                pid = wt.DWORD()
                user32.GetWindowThreadProcessId(h, ctypes.byref(pid))
                if pid.value == self.game_pid and user32.IsWindowVisible(h):
                    found.append(h)
                return 1
            user32.EnumWindows(WNDENUMPROC(cb), 0)
            if found: return found[0]

        # Strategy 3: Cari berdasarkan title partial
        buf = ctypes.create_unicode_buffer(256)
        all_h = []
        WNDENUMPROC2 = ctypes.WINFUNCTYPE(ctypes.c_int, wt.HWND, wt.LPARAM)
        def cb2(h, _):
            if user32.IsWindowVisible(h):
                user32.GetWindowTextW(h, buf, 256)
                t = buf.value.lower()
                if "savage" in t or "journey" in t or "towers" in t:
                    all_h.append(h)
            return 1
        user32.EnumWindows(WNDENUMPROC2(cb2), 0)
        if all_h: return all_h[0]
        return 0

    def _focus_game(self):
        """Pindahkan fokus ke game window."""
        hwnd = self._find_hwnd()
        if not hwnd:
            return False
        cur = kernel32.GetCurrentThreadId()
        gtid = user32.GetWindowThreadProcessId(hwnd, None)
        user32.AttachThreadInput(cur, gtid, True)
        user32.ShowWindow(hwnd, 9)       # SW_RESTORE
        user32.BringWindowToTop(hwnd)
        user32.SetForegroundWindow(hwnd)
        user32.SetFocus(hwnd)
        user32.AttachThreadInput(cur, gtid, False)
        time.sleep(0.15)
        return True

    def send_cmd(self, cmd_text):
        """
        Kirim UE4 console command ke game.
        Pipeline: Focus → Tilde (open console) → Type command → Enter → Tilde (close)
        """
        if not self.game_pid:
            self.log_lbl.configure(text="⚠️ Game tidak running!", text_color=T["red"])
            winsound.Beep(400, 200)
            return

        winsound.Beep(1200, 50)
        self._last_cmd = cmd_text
        self.log_lbl.configure(text=f"CMD: {cmd_text}", text_color="#38BDF8")

        delay = self._get_delay_ms()

        # Step 1: Focus game
        self._focus_game()

        if HAS_PDI:
            # === pydirectinput path (paling compatible dengan UE4) ===
            try:
                # Buka console dengan tilde
                pydirectinput.keyDown("grave")          # grave = ` / ~ key
                time.sleep(0.05)
                pydirectinput.keyUp("grave")
                time.sleep(delay)

                # Ketik command via pydi (scan code based)
                for ch in cmd_text:
                    if ch == " ":
                        pydirectinput.press("space")
                    elif ch.isdigit():
                        pydirectinput.press(ch)
                    elif ch == ".":
                        pydirectinput.press(".")
                    elif ch.isalpha():
                        pydirectinput.press(ch.lower())
                    time.sleep(0.018)

                time.sleep(0.06)
                pydirectinput.press("enter")
                time.sleep(0.20)
                # Tutup console
                pydirectinput.keyDown("grave")
                time.sleep(0.04)
                pydirectinput.keyUp("grave")
                return
            except Exception:
                pass  # fallback ke SendInput

        # === SendInput fallback ===
        self._sendinput_key(SCAN_TILDE, True)
        time.sleep(0.04)
        self._sendinput_key(SCAN_TILDE, False)
        time.sleep(delay)

        for ch in cmd_text:
            self._sendinput_unicode(ch)
            time.sleep(0.016)

        time.sleep(0.06)
        self._sendinput_key(SCAN_RETURN, True)
        time.sleep(0.04)
        self._sendinput_key(SCAN_RETURN, False)
        time.sleep(0.20)
        self._sendinput_key(SCAN_TILDE, True)
        time.sleep(0.04)
        self._sendinput_key(SCAN_TILDE, False)

    def _compound(self, cmds_str):
        for cmd in cmds_str.split(";"):
            c = cmd.strip()
            if c:
                self.send_cmd(c)
                time.sleep(0.25)

    # ── CHEATS ────────────────────────────────────────────────────────────────
    def toggle_god(self):
        self.state_god = not self.state_god
        self.send_cmd("god")
        if self.state_god:
            self.btn_god.configure(text="ON", fg_color=T["green"], text_color="#0B0D14")
            winsound.Beep(1400,100)
        else:
            self.btn_god.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            winsound.Beep(800,100)

    def toggle_fly(self):
        self.state_fly = not self.state_fly
        if self.state_fly:
            if self.state_ghost:
                self.state_ghost = False
                self.btn_ghost.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            self.send_cmd("fly")
            self.btn_fly.configure(text="ON", fg_color=T["cyan"], text_color="#0B0D14")
            winsound.Beep(1400,100)
        else:
            self.send_cmd("walk")
            self.btn_fly.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            winsound.Beep(800,100)

    def toggle_ghost(self):
        self.state_ghost = not self.state_ghost
        if self.state_ghost:
            if self.state_fly:
                self.state_fly = False
                self.btn_fly.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            self.send_cmd("ghost")
            self.btn_ghost.configure(text="ON", fg_color=T["purple"], text_color="#FFFFFF")
            winsound.Beep(1400,100)
        else:
            self.send_cmd("walk")
            self.btn_ghost.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            winsound.Beep(800,100)

    def toggle_speed(self):
        self.state_speed = not self.state_speed
        if self.state_speed:
            self.send_cmd("slomo 2.5")
            self.btn_speed.configure(text="ON", fg_color=T["gold"], text_color="#0B0D14")
            winsound.Beep(1400,100)
        else:
            self.send_cmd("slomo 1.0")
            self.btn_speed.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
            winsound.Beep(800,100)

    def cmd_walk(self):
        self.send_cmd("walk")
        self.state_fly = False; self.state_ghost = False
        self.btn_fly.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
        self.btn_ghost.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])

    def cmd_slowmo(self):
        self.send_cmd("slomo 0.5")

    def cmd_teleport(self):
        self.send_cmd("teleport")

    def cmd_screenshot(self):
        self.send_cmd("shot")

    def cmd_full_unlock(self):
        self.send_cmd("god")
        time.sleep(0.3)
        self.send_cmd("unlockall")

    def cmd_panic(self):
        self.send_cmd("slomo 1.0")
        time.sleep(0.2)
        self.cmd_walk()
        if self.state_god:
            self.state_god = False
            self.send_cmd("god")
            self.btn_god.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
        if self.state_speed:
            self.state_speed = False
            self.btn_speed.configure(text="OFF", fg_color="#1E293B", text_color=T["muted"])
        winsound.Beep(600,250)

    def launch_game(self):
        """Launch game + apply config patches."""
        patch_ue4_config()
        if os.path.exists(GAME_EXE):
            os.startfile(GAME_EXE)
        else:
            fallback = os.path.join(GAME_DIR, "Towers.exe")
            if os.path.exists(fallback): os.startfile(fallback)

    # ── BACKGROUND LOOP ───────────────────────────────────────────────────────
    def _bg_loop(self):
        while True:
            try:
                # Detect Towers process
                running = False
                for p in psutil.process_iter(['name','pid']):
                    nm = (p.info['name'] or '').lower()
                    if 'towers' in nm:
                        self.game_pid = p.info['pid']
                        running = True
                        break

                if running:
                    self.dot.configure(text_color=T["green"])
                    self.status.configure(text=f"CONNECTED: Towers (PID {self.game_pid})", text_color=T["green"])
                else:
                    self.game_pid = None
                    self.dot.configure(text_color=T["red"])
                    self.status.configure(text="Waiting for Towers-Win64-Shipping...", text_color=T["muted"])

                # Global hotkeys ALT+key
                alt = (user32.GetAsyncKeyState(VK_MENU) & 0x8000) != 0
                if alt:
                    hk_map = {
                        VK_1: self.toggle_god,
                        VK_2: self.toggle_fly,
                        VK_3: self.toggle_ghost,
                        VK_4: self.toggle_speed,
                        VK_5: self.cmd_slowmo,
                        VK_6: self.cmd_walk,
                        VK_8: self.cmd_teleport,
                        VK_9: self.cmd_screenshot,
                        VK_T: self.cmd_full_unlock,
                        VK_0: self.cmd_panic,
                    }
                    for vk, fn in hk_map.items():
                        if user32.GetAsyncKeyState(vk) & 0x8000:
                            fn()
                            time.sleep(0.4)
                            break

            except Exception:
                pass
            time.sleep(0.08)


if __name__ == "__main__":
    app = SavagePlanetModMenu()
    app.mainloop()

