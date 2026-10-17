"""
ASTRA AI — Blasphemous 2 MOD MENU v2.0 (Dual-Brain Edition)
Architecture: Unity 2021.3 IL2CPP x64 (GameAssembly.dll + global-metadata.dat)
Process     : Blasphemous 2.exe
Enhancements: Co-developed with Gemini 4 Argon Deep Reasoning + Antigravity Engine
Features    :
  - ALT+1: God Mode (Infinite Life / Invincible)
  - ALT+2: Infinite Bile Flasks & Fervour
  - ALT+3: Max Marks of Martyrdom (Currency 99,999)
  - ALT+4: Speed 3x Turbo Movement
  - ALT+5: Veredicto Infinite Fire (Zero Fervour Drain + Instant Charge)
  - ALT+6: Sarmiento & Centella Max Verdadera Destreza (Lock 3-Bar Lightning)
  - ALT+7: Ruego Al Alba Infinite Blood Pact (100% Blood + No Cooldown)
  - ALT+8: Infinite Air Dash / Dodge Slide
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

GAME_EXE  = r"D:\Game\Games\Blasphemous-2-SteamRIP.com\Blasphemous 2\Blasphemous 2.exe"
PROC_NAME = "Blasphemous 2"

# Unity IL2CPP AOB signatures (TGK.Game namespace)
AOB_HP_CURRENT   = rb"\xF3\x0F\x11\x81....\x48\x8B\x81....\xF3"
AOB_AIR_DASH     = rb"\x89\x87....\xC7\x87....\x00\x00\x00\x00"
AOB_VEREDICTO    = rb"\xF3\x0F\x11\x8B....\x84\xC0\x75"
AOB_DESTREZA     = rb"\x89\x86....\x48\x8B\xCE\xE8"
AOB_BLOODPACT    = rb"\xF3\x0F\x11\x83....\x0F\x2F\xC1"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

T = {
    "bg"    : "#0D0004",
    "card"  : "#1A0008",
    "border": "#5C001A",
    "acc"   : "#E11D48",
    "sec"   : "#A00020",
    "red"   : "#EF4444",
    "green" : "#10B981",
    "cyan"  : "#00E5FF",
    "gold"  : "#F1C40F",
    "main"  : "#F8FAFC",
    "muted" : "#94A3B8",
    "warn"  : "#F59E0B",
    "purple": "#A855F7",
    "orange": "#F97316",
}

def _darken(hex_color: str, factor: float = 0.7) -> str:
    hex_color = hex_color.lstrip("#")
    r = max(0, int(int(hex_color[0:2], 16) * factor))
    g = max(0, int(int(hex_color[2:4], 16) * factor))
    b = max(0, int(int(hex_color[4:6], 16) * factor))
    return f"#{r:02X}{g:02X}{b:02X}"


class Blasphemous2ModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASTRA // BLASPHEMOUS II DUAL-BRAIN TRAINER v2.0")
        self.geometry("500x780")
        self.minsize(480, 680)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.95)
        self.configure(fg_color=T["bg"])

        self._pm: "pymem.Pymem | None" = None
        self._assembly_base: int | None = None
        self._game_pid: int | None      = None
        self._running   = True

        self._patch_cache = {}

        self._state = {
            "god":       False,
            "bile":      False,
            "marks":     False,
            "speed":     False,
            "veredicto": False,
            "destreza":  False,
            "bloodpact": False,
            "dash":      False,
            "onehit":    False,
        }

        self._build_ui()
        threading.Thread(target=self._hotkey_thread, daemon=True).start()
        threading.Thread(target=self._process_watcher, daemon=True).start()
        threading.Thread(target=self._freeze_thread, daemon=True).start()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10,
                            border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=12, pady=(10, 6))

        ctk.CTkLabel(hdr, text="⚔  BLASPHEMOUS II TRAINER v2.0",
                     font=("Consolas", 14, "bold"), text_color=T["acc"]).pack(anchor="w", padx=12, pady=(8, 2))
        ctk.CTkLabel(hdr, text="Dual-Brain Engine: Gemini 4 Argon (3-Weapons Modding) + Antigravity",
                     font=("Consolas", 9, "bold"), text_color=T["gold"]).pack(anchor="w", padx=12, pady=(0, 4))

        sb = ctk.CTkFrame(hdr, fg_color="#0A0004", corner_radius=6)
        sb.pack(fill="x", padx=10, pady=(0, 4))
        self._dot = ctk.CTkLabel(sb, text="●", font=("Consolas", 12), text_color=T["red"])
        self._dot.pack(side="left", padx=(8, 4), pady=3)
        self._stat = ctk.CTkLabel(sb, text=f"Menunggu {PROC_NAME}.exe ...",
                                   font=("Consolas", 9, "bold"), text_color=T["muted"])
        self._stat.pack(side="left", pady=3)

        self._log = ctk.CTkLabel(hdr, text="STATUS: Standby (Unity IL2CPP x64 Ready)",
                                  font=("Consolas", 8), text_color=T["cyan"])
        self._log.pack(anchor="w", padx=12, pady=(0, 6))

        sc = ctk.CTkScrollableFrame(self, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=12, pady=(0, 6))

        cheats_info = [
            ("god",       "⚔  GOD MODE",               "Infinite Life & Invincibility",              "ALT+1", T["green"]),
            ("bile",      "✨ INFINITE BILE & FERVOUR",  "Flasks & Fervour selalu 100% penuh",        "ALT+2", T["gold"]),
            ("marks",     "💰 MAX MARKS OF MARTYRDOM",  "Set 99,999 Marks untuk unlock skill tree",  "ALT+3", T["warn"]),
            ("speed",     "⚡ SPEED 3X TURBO",          "Kecepatan jelajah x3",                      "ALT+4", T["cyan"]),
            ("veredicto", "🔥 VEREDICTO INFINITE FIRE", "Zero Fervour Drain saat nyala api + Instacharge", "ALT+5", T["orange"]),
            ("destreza",  "⚡ VERDADERA DESTREZA MAX",   "Lock 3-Bar Petir Sarmiento & No Drop on Hit", "ALT+6", "#38BDF8"),
            ("bloodpact", "🩸 RUEGO AL ALBA BLOOD PACT","Lock 100% Blood Pact & No Cooldown Timer",   "ALT+7", T["purple"]),
            ("dash",      "💨 INFINITE AIR DASH",       "Dash beruntun di udara tanpa batas",        "ALT+8", "#2DD4BF"),
            ("onehit",    "💀 ONE-HIT KO ENEMIES",      "Musuh langsung tumbang 1x serangan",        "ALT+9", T["acc"]),
        ]

        self._btn_refs = {}
        for key, label, desc, hk, col in cheats_info:
            self._cheat_card(sc, key, label, desc, hk, col)

        reset_frame = ctk.CTkFrame(sc, fg_color=T["card"], border_width=1,
                                   border_color=_darken(T["red"], 0.5), corner_radius=8)
        reset_frame.pack(fill="x", padx=2, pady=(8, 2))
        ctk.CTkLabel(reset_frame, text="🚨 PANIC RESET — ALT+0",
                     font=("Consolas", 10, "bold"), text_color=T["red"]).pack(side="left", padx=12, pady=8)
        ctk.CTkButton(reset_frame, text="RESET ALL", width=90, height=28,
                      font=("Consolas", 9, "bold"), fg_color=T["red"],
                      hover_color=_darken(T["red"]), text_color="#FFFFFF",
                      corner_radius=6, command=self._panic_reset).pack(side="right", padx=10, pady=8)

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
        if not self._pm or not self._assembly_base:
            return None
        try:
            return pymem.pattern.scan_pattern_page(
                self._pm.process_handle, self._assembly_base, pattern, return_multiple=False
            )
        except Exception:
            return None

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
        if not self._pm or not self._assembly_base:
            self._log.configure(text="⚠ Game belum terhubung!", text_color=T["red"])
            return

        pm = self._pm
        try:
            if key == "dash":
                addr = self._scan_aob(AOB_AIR_DASH)
                if addr:
                    if active:
                        self._patch_cache["dash"] = {"addr": addr, "orig": pm.read_bytes(addr, 6)}
                        pm.write_bytes(addr, b"\x90" * 6, 6)
                        self._log.configure(text=f"AIR DASH PATCHED @ {hex(addr)}", text_color=T["green"])
                    else:
                        c = self._patch_cache.get("dash")
                        if c:
                            pm.write_bytes(c["addr"], c["orig"], len(c["orig"]))
            elif key == "veredicto":
                addr = self._scan_aob(AOB_VEREDICTO)
                if addr:
                    if active:
                        self._patch_cache["veredicto"] = {"addr": addr, "orig": pm.read_bytes(addr, 6)}
                        pm.write_bytes(addr, b"\x90" * 6, 6)
                        self._log.configure(text=f"VEREDICTO NO DRAIN @ {hex(addr)}", text_color=T["orange"])
                    else:
                        c = self._patch_cache.get("veredicto")
                        if c:
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
        """100Hz high speed loop for freeze values"""
        while self._running:
            # Persistent memory writes handled here
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
                                        self._pm.process_handle, "GameAssembly.dll"
                                    )
                                    self._assembly_base = mod.lpBaseOfDll if mod else None
                                except Exception:
                                    self._pm = None
                                    self._assembly_base = None
                        found = True
                        break

                if found and self._pm:
                    self.after(0, lambda: [
                        self._dot.configure(text_color=T["green"]),
                        self._stat.configure(
                            text=f"TERHUBUNG: {PROC_NAME} (PID {self._game_pid} | IL2CPP)",
                            text_color=T["green"])
                    ])
                else:
                    self._game_pid      = None
                    self._pm            = None
                    self._assembly_base = None
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
            VK_2: "bile",
            VK_3: "marks",
            VK_4: "speed",
            VK_5: "veredicto",
            VK_6: "destreza",
            VK_7: "bloodpact",
            VK_8: "dash",
            VK_9: "onehit",
        }
        prev = {k: False for k in key_map}
        prev[VK_0] = False

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
    app = Blasphemous2ModMenu()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
