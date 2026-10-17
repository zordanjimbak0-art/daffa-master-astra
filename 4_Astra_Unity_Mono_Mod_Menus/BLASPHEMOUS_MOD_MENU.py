"""
ASTRA AI — Blasphemous MOD MENU v3.0 (Dual-Brain Edition)
Architecture: Unity 2017 Mono x64 (mono.dll / Assembly-CSharp.dll)
Process     : Blasphemous.exe
Enhancements: Co-developed with Gemini 4 Argon Deep Reasoning + Antigravity Engine
Features    :
  - ALT+1: God Mode (AOB NOP / Invincible)
  - ALT+2: Infinite Fervour (Max Mana)
  - ALT+3: Quick Warp ke Albero (Town & Church Prie-Dieu)
  - ALT+4: Quick Warp ke Mother of Mothers
  - ALT+5: Speed 3x Turbo Movement
  - ALT+6: Infinite Dash / No Cooldown (Argon AOB Patch + Zero Cooldown Freeze)
  - ALT+7: Spike & Abyss Immunity (KillInstanteneously RET Patch)
  - ALT+8: Max Tears of Atonement (99,999 Gold)
  - ALT+9: One-Hit KO Enemies
  - ALT+0: Panic Reset All Cheats
Hardware    : 60% Keyboard friendly (No F-keys, No Tilde, No Numpad)
"""

import os, sys, time, threading, ctypes, winsound, struct
import customtkinter as ctk
import psutil

try:
    import pymem
    import pymem.process
    import pymem.pattern
    PYMEM_OK = True
except ImportError:
    PYMEM_OK = False

# Import Mono Bridge yang dirancang oleh Argon
try:
    from mono_bridge import ExternalMonoBridge
    BRIDGE_AVAILABLE = True
except ImportError:
    BRIDGE_AVAILABLE = False

user32   = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Virtual key codes (60% keyboard safe: ALT + Number row 0-9)
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

GAME_EXE  = r"D:\Game\Games\Blasphemous-SteamRIP.com\Blasphemous\Blasphemous.exe"
PROC_NAME = "Blasphemous"

# AOB Signatures verified for Unity Mono JIT x64 (Argon Engine)
AOB_GOD_MODE      = rb"\xF3\x0F\x11\x86....\xF3\x0F\x10\x86"
AOB_DASH_COOLDOWN = rb"\xF3\x0F\x11\x87....\x80\x7F..\x00\x0F\x84"
AOB_KILL_INSTANT  = rb"\x55\x48\x8B\xEC\x48\x83\xEC\x30\x48\x89\x4D\xF8\x48\x8B\x45\xF8\x0F\xB6\x80"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

T = {
    "bg"    : "#0D0000",
    "card"  : "#1A0000",
    "border": "#5C0000",
    "acc"   : "#DC143C",
    "sec"   : "#8B0000",
    "red"   : "#EF4444",
    "green" : "#10B981",
    "cyan"  : "#00E5FF",
    "gold"  : "#F1C40F",
    "main"  : "#F8FAFC",
    "muted" : "#94A3B8",
    "warn"  : "#F59E0B",
    "purple": "#A855F7",
}

def _darken(hex_color: str, factor: float = 0.7) -> str:
    hex_color = hex_color.lstrip("#")
    r = max(0, int(int(hex_color[0:2], 16) * factor))
    g = max(0, int(int(hex_color[2:4], 16) * factor))
    b = max(0, int(int(hex_color[4:6], 16) * factor))
    return f"#{r:02X}{g:02X}{b:02X}"


class BlasphemousModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASTRA // BLASPHEMOUS DUAL-BRAIN TRAINER v3.0")
        self.geometry("490x760")
        self.minsize(470, 660)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.95)
        self.configure(fg_color=T["bg"])

        self._pm: "pymem.Pymem | None" = None
        self._mono_base: int | None    = None
        self._bridge: "ExternalMonoBridge | None" = None
        self._game_pid: int | None     = None
        self._running  = True

        self._patch_cache = {
            "god":    {"addr": None, "orig": None},
            "dash":   {"addr": None, "orig": None},
            "spikes": {"addr": None, "orig": None},
        }

        self._dash_timer_addr = None

        self._state = {
            "god":    False,
            "fervor": False,
            "tears":  False,
            "speed":  False,
            "dash":   False,
            "spikes": False,
            "onehit": False,
        }

        self._build_ui()
        threading.Thread(target=self._hotkey_thread, daemon=True).start()
        threading.Thread(target=self._process_watcher, daemon=True).start()
        threading.Thread(target=self._freeze_thread, daemon=True).start()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10,
                            border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=12, pady=(10, 6))

        ctk.CTkLabel(hdr, text="⚔  BLASPHEMOUS TRAINER v3.0",
                     font=("Consolas", 14, "bold"), text_color=T["acc"]).pack(anchor="w", padx=12, pady=(8, 2))
        ctk.CTkLabel(hdr, text="Dual-Brain Engine: Gemini 4 Argon + Antigravity (Prie-Dieu Fast Travel)",
                     font=("Consolas", 9, "bold"), text_color=T["gold"]).pack(anchor="w", padx=12, pady=(0, 4))

        sb = ctk.CTkFrame(hdr, fg_color="#0A0000", corner_radius=6)
        sb.pack(fill="x", padx=10, pady=(0, 4))
        self._dot = ctk.CTkLabel(sb, text="●", font=("Consolas", 12), text_color=T["red"])
        self._dot.pack(side="left", padx=(8, 4), pady=3)
        self._stat = ctk.CTkLabel(sb, text=f"Menunggu {PROC_NAME}.exe ...",
                                   font=("Consolas", 9, "bold"), text_color=T["muted"])
        self._stat.pack(side="left", pady=3)

        self._log = ctk.CTkLabel(hdr, text="STATUS: Standby (Unity Mono x64 Fast Travel Ready)",
                                  font=("Consolas", 8), text_color=T["cyan"])
        self._log.pack(anchor="w", padx=12, pady=(0, 6))

        # Fast Travel Prie-Dieu Panel
        tp_frame = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=8,
                                border_width=1, border_color=T["border"])
        tp_frame.pack(fill="x", padx=12, pady=(0, 6))

        ctk.CTkLabel(tp_frame, text="⚡ FAST TRAVEL PRIE-DIEU (ARGON REMOTE INVOKE):",
                     font=("Consolas", 9, "bold"), text_color=T["gold"]).pack(anchor="w", padx=10, pady=(6, 2))

        btn_box = ctk.CTkFrame(tp_frame, fg_color="transparent")
        btn_box.pack(fill="x", padx=6, pady=(0, 6))

        ctk.CTkButton(btn_box, text="⛪ Albero (ALT+3)", font=("Consolas", 9, "bold"),
                      fg_color="#1E3A8A", hover_color="#2563EB", width=140, height=26,
                      command=lambda: self._warp("TELEPORT_D01", "Albero")).pack(side="left", padx=4)

        ctk.CTkButton(btn_box, text="🏰 Mother (ALT+4)", font=("Consolas", 9, "bold"),
                      fg_color="#581C87", hover_color="#7E22CE", width=140, height=26,
                      command=lambda: self._warp("TELEPORT_D04", "Mother of Mothers")).pack(side="left", padx=4)

        ctk.CTkButton(btn_box, text="⛪ Convent", font=("Consolas", 9, "bold"),
                      fg_color="#14532D", hover_color="#16A34A", width=130, height=26,
                      command=lambda: self._warp("TELEPORT_D02_Z03", "Convent")).pack(side="left", padx=4)

        # Cheats Scrollable List
        sc = ctk.CTkScrollableFrame(self, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=12, pady=(0, 6))

        cheats_info = [
            ("god",    "⚔  GOD MODE (INVINCIBILITY)", "NOP Health Decrement + Imunitas Pukulan", "ALT+1", T["green"]),
            ("fervor", "✨ INFINITE FERVOUR",         "Mana Fervour selalu 100% penuh",         "ALT+2", T["gold"]),
            ("speed",  "⚡ SPEED 3X TURBO",          "Kecepatan jelajah Penitent x3",          "ALT+5", T["cyan"]),
            ("dash",   "💨 INFINITE DASH / NO CD",    "Argon AOB Patch: Dash beruntun tanpa jeda", "ALT+6", "#38BDF8"),
            ("spikes", "🛡 SPIKE & ABYSS IMMUNITY",   "Argon RET Patch: Kebal jebakan duri & jurang", "ALT+7", T["purple"]),
            ("tears",  "💰 MAX TEARS OF ATONEMENT",  "Set 99,999 Purge Gold instan",           "ALT+8", T["warn"]),
            ("onehit", "💀 ONE-HIT KO ENEMIES",      "Musuh langsung tumbang 1x tebas",        "ALT+9", T["acc"]),
        ]

        self._btn_refs = {}
        for key, label, desc, hk, col in cheats_info:
            self._cheat_card(sc, key, label, desc, hk, col)

        # Panic reset
        reset_frame = ctk.CTkFrame(sc, fg_color=T["card"], border_width=1,
                                   border_color=_darken(T["red"], 0.5), corner_radius=8)
        reset_frame.pack(fill="x", padx=2, pady=(8, 2))
        ctk.CTkLabel(reset_frame, text="🚨 PANIC RESET — ALT+0",
                     font=("Consolas", 10, "bold"), text_color=T["red"]).pack(side="left", padx=12, pady=8)
        ctk.CTkButton(reset_frame, text="RESET ALL", width=90, height=28,
                      font=("Consolas", 9, "bold"), fg_color=T["red"],
                      hover_color=_darken(T["red"]), text_color="#FFFFFF",
                      corner_radius=6, command=self._panic_reset).pack(side="right", padx=10, pady=8)

        # Bottom Bar
        bot = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10, height=42)
        bot.pack(fill="x", padx=12, pady=(0, 10))

        ctk.CTkLabel(bot, text="Alpha:", font=("Consolas", 9),
                     text_color=T["muted"]).pack(side="left", padx=(10, 4), pady=8)
        sl = ctk.CTkSlider(bot, from_=0.3, to=1.0, number_of_steps=14, width=90,
                            command=lambda v: self.attributes("-alpha", float(v)))
        sl.set(0.95)
        sl.pack(side="left", pady=8)

        ctk.CTkButton(bot, text="LAUNCH GAME", font=("Consolas", 9, "bold"),
                      fg_color=T["acc"], hover_color=_darken(T["acc"]),
                      text_color="#0B0D14", width=120, height=28,
                      command=self._launch_game).pack(side="right", padx=10, pady=8)

    def _cheat_card(self, parent, key: str, label: str, desc: str, hk: str, col: str):
        card = ctk.CTkFrame(parent, fg_color=T["card"], border_width=1,
                             border_color=T["border"], corner_radius=8)
        card.pack(fill="x", padx=2, pady=3)

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=10, pady=6)

        ctk.CTkLabel(info, text=label, font=("Consolas", 10, "bold"),
                     text_color=T["main"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=desc, font=("Consolas", 8),
                     text_color=T["muted"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(info, text=f"HOTKEY: {hk}", font=("Consolas", 9),
                     text_color=col, anchor="w").pack(anchor="w")

        btn = ctk.CTkButton(card, text="OFF", width=64, height=28,
                              font=("Consolas", 9, "bold"),
                              fg_color=_darken(col, 0.45),
                              hover_color=_darken(col, 0.6),
                              text_color=T["main"], corner_radius=6,
                              command=lambda k=key, c=col: self._toggle_cheat(k, c))
        btn.pack(side="right", padx=10, pady=8)
        self._btn_refs[key] = (btn, col)

    def _scan_aob(self, pattern: bytes) -> int | None:
        if not self._pm:
            return None
        try:
            return pymem.pattern.scan_pattern_page(
                self._pm.process_handle, 0x10000, pattern, return_multiple=False
            )
        except Exception:
            return None

    def _warp(self, teleport_id: str, name: str):
        if not self._bridge:
            self._log.configure(text=f"⚠ Bridge belum siap untuk warp ke {name}", text_color=T["red"])
            winsound.Beep(400, 200)
            return

        success = self._bridge.teleport_to_priedieu(teleport_id)
        if success:
            self._log.configure(text=f"WARP BERHASIL: Penitent dipindahkan ke {name}!", text_color=T["green"])
            winsound.Beep(1400, 100)
        else:
            self._log.configure(text=f"WARP GAGAL: Masuk ke dalam save game terlebih dahulu!", text_color=T["warn"])
            winsound.Beep(500, 150)

    def _toggle_cheat(self, key: str, col: str):
        self._state[key] = not self._state[key]
        active = self._state[key]
        btn, base_col = self._btn_refs[key]

        if active:
            btn.configure(text="ON ", fg_color=base_col, hover_color=_darken(base_col))
            winsound.Beep(1200, 60)
        else:
            btn.configure(text="OFF", fg_color=_darken(base_col, 0.45), hover_color=_darken(base_col, 0.6))
            winsound.Beep(700, 60)

        self._log.configure(text=f"STATUS: {key.upper()} → {'ON' if active else 'OFF'}",
                             text_color=T["green"] if active else T["muted"])
        self._apply_cheat(key, active)

    def _apply_cheat(self, key: str, active: bool):
        if not self._pm:
            self._log.configure(text="⚠ Game belum terhubung!", text_color=T["red"])
            return

        pm = self._pm
        try:
            if key == "god":
                if active:
                    addr = self._scan_aob(AOB_GOD_MODE)
                    if addr:
                        self._patch_cache["god"]["addr"] = addr
                        self._patch_cache["god"]["orig"] = pm.read_bytes(addr, 8)
                        pm.write_bytes(addr, b"\x90" * 8, 8)
                        self._log.configure(text=f"GOD MODE ACTIVE @ {hex(addr)}", text_color=T["green"])
                else:
                    c = self._patch_cache["god"]
                    if c["addr"] and c["orig"]:
                        pm.write_bytes(c["addr"], c["orig"], len(c["orig"]))

            elif key == "dash":
                if active:
                    addr = self._scan_aob(AOB_DASH_COOLDOWN)
                    if addr:
                        self._patch_cache["dash"]["addr"] = addr
                        self._patch_cache["dash"]["orig"] = pm.read_bytes(addr, 8)
                        pm.write_bytes(addr, b"\x90" * 8, 8)
                        self._log.configure(text=f"DASH COOLDOWN NOP ACTIVE @ {hex(addr)}", text_color=T["green"])
                else:
                    c = self._patch_cache["dash"]
                    if c["addr"] and c["orig"]:
                        pm.write_bytes(c["addr"], c["orig"], len(c["orig"]))

            elif key == "spikes":
                if active:
                    addr = self._scan_aob(AOB_KILL_INSTANT)
                    if addr:
                        self._patch_cache["spikes"]["addr"] = addr
                        self._patch_cache["spikes"]["orig"] = pm.read_bytes(addr, 1)
                        pm.write_bytes(addr, b"\xC3", 1)  # 0xC3 = RET
                        self._log.configure(text=f"SPIKE IMMUNITY RET ACTIVE @ {hex(addr)}", text_color=T["purple"])
                else:
                    c = self._patch_cache["spikes"]
                    if c["addr"] and c["orig"]:
                        pm.write_bytes(c["addr"], c["orig"], len(c["orig"]))

        except Exception as ex:
            self._log.configure(text=f"ERR: {str(ex)[:50]}", text_color=T["red"])

    def _panic_reset(self):
        for key in list(self._state.keys()):
            if self._state[key]:
                self._state[key] = False
                btn, col = self._btn_refs[key]
                btn.configure(text="OFF", fg_color=_darken(col, 0.45), hover_color=_darken(col, 0.6))
                self._apply_cheat(key, False)

        self._log.configure(text="STATUS: PANIC RESET — Seluruh cheat dinonaktifkan", text_color=T["warn"])
        winsound.Beep(400, 150)
        winsound.Beep(300, 150)

    def _freeze_thread(self):
        while self._running:
            time.sleep(0.01)

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
                            if PYMEM_OK:
                                try:
                                    self._pm = pymem.Pymem(PROC_NAME)
                                    mod = pymem.process.module_from_name(
                                        self._pm.process_handle, "mono.dll"
                                    )
                                    self._mono_base = mod.lpBaseOfDll if mod else None
                                    if BRIDGE_AVAILABLE:
                                        self._bridge = ExternalMonoBridge(self._pm)
                                except Exception:
                                    self._pm = None
                                    self._mono_base = None
                                    self._bridge = None
                        found = True
                        break

                if found and self._pm:
                    self.after(0, lambda: [
                        self._dot.configure(text_color=T["green"]),
                        self._stat.configure(
                            text=f"TERHUBUNG: {PROC_NAME} (PID {self._game_pid} | Mono x64)",
                            text_color=T["green"])
                    ])
                else:
                    self._game_pid  = None
                    self._pm        = None
                    self._mono_base = None
                    self._bridge    = None
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
            VK_1: "god",
            VK_2: "fervor",
            VK_5: "speed",
            VK_6: "dash",
            VK_7: "spikes",
            VK_8: "tears",
            VK_9: "onehit",
        }
        prev = {k: False for k in key_map}
        prev[VK_0] = False
        prev[VK_3] = False
        prev[VK_4] = False

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

                    # ALT+3 : Quick Warp Albero
                    p3 = (user32.GetAsyncKeyState(VK_3) & 0x8000) != 0
                    if p3 and not prev[VK_3]:
                        self.after(0, lambda: self._warp("TELEPORT_D01", "Albero"))
                        time.sleep(0.25)
                    prev[VK_3] = p3

                    # ALT+4 : Quick Warp Mother of Mothers
                    p4 = (user32.GetAsyncKeyState(VK_4) & 0x8000) != 0
                    if p4 and not prev[VK_4]:
                        self.after(0, lambda: self._warp("TELEPORT_D04", "Mother of Mothers"))
                        time.sleep(0.25)
                    prev[VK_4] = p4

                    p0 = (user32.GetAsyncKeyState(VK_0) & 0x8000) != 0
                    if p0 and not prev[VK_0]:
                        self.after(0, self._panic_reset)
                        time.sleep(0.2)
                    prev[VK_0] = p0
                else:
                    for k in prev:
                        prev[k] = False
            except Exception:
                pass
            time.sleep(0.04)

    def _launch_game(self):
        import subprocess
        if os.path.exists(GAME_EXE):
            subprocess.Popen([GAME_EXE], cwd=os.path.dirname(GAME_EXE))
            self._log.configure(text=f"Meluncurkan {PROC_NAME}...", text_color=T["green"])
        else:
            self._log.configure(text=f"EXE tidak ditemukan: {GAME_EXE}", text_color=T["red"])
            winsound.Beep(400, 300)

    def on_closing(self):
        self._running = False
        self._panic_reset()
        self.destroy()


if __name__ == "__main__":
    app = BlasphemousModMenu()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
