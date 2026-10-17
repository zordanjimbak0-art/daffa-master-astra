r"""
================================================================================
ASTRA AI — MY VOICE ZOO MOD MENU & LIVE SAVE/MONO ENGINE v3.0
Architecture : Unity 6000 / 2022 Mono x64 (mono-2.0-bdwgc.dll + Assembly-CSharp.dll)
Target EXE   : MyVoiceZoo.exe (D:\Game\Games\MyVoiceZoo-SteamRIP.com\MyVoiceZoo\MyVoiceZoo.exe)
Save File    : %USERPROFILE%\AppData\LocalLow\DefaultCompany\MyVoiceZoo\save.json
Encryption   : Repeating XOR Cipher Key -> b"sdhfioshdio@#%#@%@$@dgfi!~@$#joash"
Hotkeys      : 100% 60% Mechanical Keyboard Compatible (ALT+1 .. ALT+9, ALT+0 Panic)
Designed for : Komandan DAFFA
================================================================================
"""

import os
import sys
import json
import time
import shutil
import struct
import ctypes
import ctypes.wintypes as wt
import threading
import subprocess
import winsound
import customtkinter as ctk
import psutil

try:
    import pymem
    import pymem.process
    PYMEM_OK = True
except ImportError:
    PYMEM_OK = False

# ==================== CONSTANTS & PATHS ====================
BASE_DIR = r"D:\Game\Games\MyVoiceZoo-SteamRIP.com"
GAME_DIR = os.path.join(BASE_DIR, "MyVoiceZoo")
GAME_EXE = os.path.join(GAME_DIR, "MyVoiceZoo.exe")
PROC_NAME = "MyVoiceZoo.exe"

SAVE_DIR = os.path.expandvars(r"%USERPROFILE%\AppData\LocalLow\DefaultCompany\MyVoiceZoo")
SAVE_PATH = os.path.join(SAVE_DIR, "save.json")
XOR_KEY = b"sdhfioshdio@#%#@%@$@dgfi!~@$#joash"

ANIMAL_NAMES = {
    "10001": "Lion (Singa)",          "10002": "Tiger (Harimau)",       "10003": "Bear (Beruang)",
    "10004": "Polar Bear (Kutub)",    "10005": "Panda",                 "10006": "Gorilla",
    "10007": "Elephant (Gajah)",      "10008": "Rhino (Badak)",         "10009": "Hippo (Kuda Nil)",
    "10010": "Horse (Kuda)",          "10011": "Reindeer (Rusa Kutub)", "10012": "Milk Cow (Sapi)",
    "10013": "Sheep (Domba)",         "10014": "Goat (Kambing)",        "10015": "Fox (Rubah)",
    "10016": "Dog (Anjing)",          "10017": "Cat (Kucing)",          "10018": "Bunny (Kelinci)",
    "10019": "Hamster",               "10020": "Sloth (Kukang)",        "10021": "Walrus (Anjing Laut)",
    "10022": "Penguin",               "10023": "Eagle (Elang)",         "10024": "Owl (Burung Hantu)",
    "10025": "Parrot (Beo)",          "10026": "Flamingo",              "10027": "Duck (Bebek)",
    "10028": "Turtle (Kura-kura)",    "10029": "Frog (Katak)",          "10030": "Snail (Siput)"
}

user32 = ctypes.windll.user32
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

# Virtual key codes (60% keyboard friendly: ALT + Number row 0-9)
VK_ALT = 0x12
VK_1, VK_2, VK_3, VK_4, VK_5 = 0x31, 0x32, 0x33, 0x34, 0x35
VK_6, VK_7, VK_8, VK_9, VK_0 = 0x36, 0x37, 0x38, 0x39, 0x30

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

T = {
    "bg"    : "#071318",
    "card"  : "#0D212A",
    "card2" : "#132F3C",
    "border": "#00B4D8",
    "acc"   : "#10B981",
    "acc2"  : "#34D399",
    "cyan"  : "#00E5FF",
    "gold"  : "#F59E0B",
    "purple": "#A855F7",
    "red"   : "#EF4444",
    "main"  : "#F8FAFC",
    "muted" : "#94A3B8",
}


# ==================== MONO C-API LIVE RUNTIME BRIDGE ====================
kernel32.CreateRemoteThread.argtypes = [
    wt.HANDLE, wt.LPVOID, ctypes.c_size_t, wt.LPVOID, wt.LPVOID, wt.DWORD, wt.LPDWORD
]
kernel32.CreateRemoteThread.restype = wt.HANDLE
kernel32.WaitForSingleObject.argtypes = [wt.HANDLE, wt.DWORD]
kernel32.GetProcAddress.argtypes = [wt.HMODULE, wt.LPCSTR]
kernel32.GetProcAddress.restype = ctypes.c_void_p
kernel32.LoadLibraryExW.argtypes = [wt.LPCWSTR, wt.HANDLE, wt.DWORD]
kernel32.LoadLibraryExW.restype = wt.HMODULE

DONT_RESOLVE_DLL_REFERENCES = 0x00000001


class MyVoiceZooMonoBridge:
    """
    Live Mono C-API Bridge untuk MyVoiceZoo.exe (mono-2.0-bdwgc.dll x64).
    Memungkinkan injeksi langsung ke:
      - Wallet._instance.<CurrentGold>k__BackingField (Offset 0x10)
      - Wallet.AddGold(Int64) / set_CurrentGold(Int64)
      - AnimalManager._instance.AddIncomePerSecond(Int64)
    """
    def __init__(self, pm: "pymem.Pymem"):
        self.pm = pm
        self.mono_mod = pymem.process.module_from_name(self.pm.process_handle, "mono-2.0-bdwgc.dll")
        if not self.mono_mod:
            raise RuntimeError("mono-2.0-bdwgc.dll belum termuat.")

        self.mono_base = self.mono_mod.lpBaseOfDll
        self.mono_path = self.mono_mod.filename

        self.scratchpad = self.pm.allocate(0x1000)
        self.ret_val_addr = self.scratchpad + 0x800
        self.str_buf_addr = self.scratchpad + 0x900
        self.arg_buf_addr = self.scratchpad + 0xA00

        self.exports = self._resolve_exports([
            b"mono_get_root_domain",
            b"mono_thread_attach",
            b"mono_domain_assembly_open",
            b"mono_assembly_get_image",
            b"mono_class_from_name",
            b"mono_class_vtable",
            b"mono_runtime_class_init",
            b"mono_vtable_get_static_field_data",
            b"mono_class_get_field_from_name",
            b"mono_field_get_offset",
            b"mono_class_get_method_from_name",
            b"mono_runtime_invoke",
        ])
        self.root_domain = self.call_x64(self.exports["mono_get_root_domain"])
        self.asm_image = 0

    def _resolve_exports(self, names):
        hmod = kernel32.LoadLibraryExW(self.mono_path, None, DONT_RESOLVE_DLL_REFERENCES)
        if not hmod:
            raise RuntimeError("Gagal LoadLibraryExW mono-2.0-bdwgc.dll")
        res = {}
        for n in names:
            addr = kernel32.GetProcAddress(hmod, n)
            if addr:
                res[n.decode()] = self.mono_base + (addr - hmod)
        kernel32.FreeLibrary(wt.HMODULE(hmod))
        return res

    def write_str(self, s: str, offset: int = 0) -> int:
        addr = self.str_buf_addr + offset
        b = s.encode("utf-8") + b"\x00"
        self.pm.write_bytes(addr, b, len(b))
        return addr

    def call_x64(self, func_addr: int, rcx: int = 0, rdx: int = 0, r8: int = 0, r9: int = 0, attach: bool = False) -> int:
        code = b"\x48\x83\xEC\x28"
        if attach and self.root_domain:
            code += (
                b"\x48\xB9" + struct.pack("<Q", self.root_domain) +
                b"\x48\xB8" + struct.pack("<Q", self.exports["mono_thread_attach"]) +
                b"\xFF\xD0"
            )
        code += (
            b"\x48\xB9" + struct.pack("<Q", rcx) +
            b"\x48\xBA" + struct.pack("<Q", rdx) +
            b"\x49\xB8" + struct.pack("<Q", r8) +
            b"\x49\xB9" + struct.pack("<Q", r9) +
            b"\x48\xB8" + struct.pack("<Q", func_addr) +
            b"\xFF\xD0" +
            b"\x48\xA3" + struct.pack("<Q", self.ret_val_addr) +
            b"\x48\x83\xC4\x28\xC3"
        )
        self.pm.write_bytes(self.scratchpad, code, len(code))
        self.pm.write_ulonglong(self.ret_val_addr, 0)
        ht = kernel32.CreateRemoteThread(self.pm.process_handle, None, 0, self.scratchpad, None, 0, None)
        if not ht:
            return 0
        kernel32.WaitForSingleObject(ht, 2500)
        kernel32.CloseHandle(ht)
        return self.pm.read_ulonglong(self.ret_val_addr)

    def get_image(self) -> int:
        if self.asm_image:
            return self.asm_image
        dll_path = os.path.join(GAME_DIR, "MyVoiceZoo_Data", "Managed", "Assembly-CSharp.dll")
        s_addr = self.write_str(dll_path, 0)
        asm = self.call_x64(self.exports["mono_domain_assembly_open"], self.root_domain, s_addr, attach=True)
        if asm:
            self.asm_image = self.call_x64(self.exports["mono_assembly_get_image"], asm, attach=True)
        return self.asm_image

    def get_static_instance(self, class_name: str, field_name: str = "_instance") -> tuple[int, int]:
        img = self.get_image()
        if not img:
            return 0, 0
        ns_addr = self.write_str("", 0)
        cl_addr = self.write_str(class_name, 64)
        klass = self.call_x64(self.exports["mono_class_from_name"], img, ns_addr, cl_addr, attach=True)
        if not klass:
            return 0, 0
        vtable = self.call_x64(self.exports["mono_class_vtable"], self.root_domain, klass, attach=True)
        if not vtable:
            return klass, 0
        self.call_x64(self.exports["mono_runtime_class_init"], vtable, attach=True)
        static_data = self.call_x64(self.exports["mono_vtable_get_static_field_data"], vtable, attach=True)
        if not static_data:
            return klass, 0
        fn_addr = self.write_str(field_name, 128)
        field = self.call_x64(self.exports["mono_class_get_field_from_name"], klass, fn_addr, attach=True)
        offset = 0
        if field:
            offset = self.call_x64(self.exports["mono_field_get_offset"], field, attach=True)
        inst = self.pm.read_ulonglong(static_data + offset)
        return klass, inst

    def add_gold_live(self, amount: int) -> bool:
        """Panggil Wallet.get_Instance().AddGold(amount) secara live agar UI langsung terupdate."""
        klass, inst = self.get_static_instance("Wallet", "_instance")
        if not klass or not inst:
            return False
        # Update backing field directly at +0x10 and invoke AddGold(amount)
        m_addr = self.write_str("AddGold", 192)
        method = self.call_x64(self.exports["mono_class_get_method_from_name"], klass, m_addr, 1, attach=True)
        if method:
            val_ptr = self.arg_buf_addr
            self.pm.write_longlong(val_ptr, int(amount))
            params_arr = self.arg_buf_addr + 16
            self.pm.write_ulonglong(params_arr, val_ptr)
            self.call_x64(self.exports["mono_runtime_invoke"], method, inst, params_arr, 0, attach=True)
            return True
        else:
            # Fallback direct field write (<CurrentGold>k__BackingField is first field at 0x10)
            cur = self.pm.read_longlong(inst + 0x10)
            self.pm.write_longlong(inst + 0x10, cur + int(amount))
            return True

    def read_gold_live(self) -> int | None:
        _, inst = self.get_static_instance("Wallet", "_instance")
        if inst:
            try:
                return self.pm.read_longlong(inst + 0x10)
            except Exception:
                return None
        return None


# ==================== XOR SAVE.JSON ENGINE ====================
def xor_crypt(data: bytes) -> bytes:
    klen = len(XOR_KEY)
    return bytes(b ^ XOR_KEY[i % klen] for i, b in enumerate(data))


def load_save_json() -> dict:
    if os.path.exists(SAVE_PATH):
        try:
            raw = open(SAVE_PATH, "rb").read()
            dec = xor_crypt(raw).decode("utf-8")
            return json.loads(dec)
        except Exception:
            pass
    # Default clean save structure if save.json doesn't exist yet
    animals = {str(10000 + i): {"ID": 10000 + i, "IsCollected": (i == 1), "Name": ""} for i in range(1, 31)}
    pos = {str(10000 + i): {"ID": 10000 + i, "X": float((i % 6) * 3 - 7), "Y": float((i // 6) * 3 - 3), "Z": 0.0, "SortingOrder": 0} for i in range(1, 31)}
    return {
        "AnimalSaveDataDict": animals,
        "CurrentGold": 1000,
        "SettingSaveData": {"BGMVolume": 0.5, "SFXVolume": 0.5},
        "IsTutorialCompleted": True,
        "AnimalPosSaveDataDict": pos,
        "AreaSaveData": {"IsUnlock_WindIsland": False, "IsUnlock_DeepCave": False},
        "CampSaveData": {"IsBuy_Forest": False, "IsBuy_Snow": False, "IsBuy_Jungle": False, "IsBuy_Savannah": False},
        "CostumeSaveData": {
            "CostumeBuyStateDict": {"Default": True, "Duck": False, "Reindeer": False, "Frog": False, "Cat": False},
            "EquippedCostumeID": 0
        }
    }


def write_save_json(data: dict) -> bool:
    try:
        os.makedirs(SAVE_DIR, exist_ok=True)
        if os.path.exists(SAVE_PATH):
            shutil.copy2(SAVE_PATH, SAVE_PATH + ".bak")
        txt = json.dumps(data, indent=2).encode("utf-8")
        enc = xor_crypt(txt)
        with open(SAVE_PATH, "wb") as f:
            f.write(enc)
        return True
    except Exception:
        return False


# ==================== MAIN MOD MENU GUI ====================
class MyVoiceZooModMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🦁 ASTRA // MY VOICE ZOO MOD MENU & SAVE UNLOCKER v3.0")
        self.geometry("540x790")
        self.minsize(500, 700)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.96)
        self.configure(fg_color=T["bg"])

        self._pm = None
        self._bridge: MyVoiceZooMonoBridge | None = None
        self._running = True
        self._inf_gold_loop = False

        self._build_ui()
        self._refresh_save_summary()

        threading.Thread(target=self._process_watcher, daemon=True).start()
        threading.Thread(target=self._hotkey_listener, daemon=True).start()

    def _beep(self, freq=880, dur=80):
        try:
            winsound.Beep(freq, dur)
        except Exception:
            pass

    def _build_ui(self):
        # 1. Header
        hdr = ctk.CTkFrame(self, fg_color=T["card"], corner_radius=10, border_width=1, border_color=T["border"])
        hdr.pack(fill="x", padx=12, pady=(10, 6))

        t_row = ctk.CTkFrame(hdr, fg_color="transparent")
        t_row.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(t_row, text="🦁 MY VOICE ZOO // ASTRA TRAINER v3.0",
                     font=("Consolas", 14, "bold"), text_color=T["cyan"]).pack(side="left")
        ctk.CTkLabel(t_row, text="60% KEYBOARD READY",
                     font=("Consolas", 9, "bold"), text_color=T["gold"]).pack(side="right")

        ctk.CTkLabel(hdr, text="Live Mono C-API Memory Bridge + XOR Save.json Unlocker • Komandan DAFFA",
                     font=("Consolas", 9), text_color=T["muted"]).pack(anchor="w", padx=12, pady=(0, 6))

        # Status Bar
        sb = ctk.CTkFrame(hdr, fg_color="#040B0E", corner_radius=6)
        sb.pack(fill="x", padx=10, pady=(0, 8))
        self._dot = ctk.CTkLabel(sb, text="●", font=("Consolas", 13), text_color=T["red"])
        self._dot.pack(side="left", padx=(8, 4), pady=4)
        self._stat_lbl = ctk.CTkLabel(sb, text="Menunggu MyVoiceZoo.exe (Save Unlocker Aktif Offline/Online)...",
                                      font=("Consolas", 9, "bold"), text_color=T["muted"])
        self._stat_lbl.pack(side="left", pady=4)

        # Live Telemetry Summary Card
        sum_card = ctk.CTkFrame(self, fg_color=T["card2"], corner_radius=8, border_width=1, border_color="#1E3A4C")
        sum_card.pack(fill="x", padx=12, pady=(0, 6))
        self._sum_lbl = ctk.CTkLabel(
            sum_card,
            text="💰 Gold: -- | 🐾 Hewan: --/30 | 🏝️ Area: --/2 | ⛺ Camp: --/4 | 🎭 Kostum: --/5",
            font=("Consolas", 10, "bold"),
            text_color=T["acc2"]
        )
        self._sum_lbl.pack(padx=10, pady=7)

        # Scrollable Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=10, pady=(0, 6))

        def section(title_txt, color=T["cyan"]):
            f = ctk.CTkFrame(scroll, fg_color="transparent")
            f.pack(fill="x", pady=(8, 3))
            ctk.CTkLabel(f, text=title_txt, font=("Consolas", 11, "bold"), text_color=color).pack(side="left")

        def btn(parent, text, hk, color, cmd):
            row = ctk.CTkFrame(parent, fg_color=T["card"], corner_radius=8, border_width=1, border_color="#163242")
            row.pack(fill="x", pady=3)
            ctk.CTkLabel(row, text=hk, font=("Consolas", 10, "bold"), text_color=T["gold"], width=68, anchor="w").pack(side="left", padx=(10, 4), pady=6)
            ctk.CTkLabel(row, text=text, font=("Consolas", 10, "bold"), text_color=T["main"], anchor="w").pack(side="left", fill="x", expand=True, pady=6)
            b = ctk.CTkButton(row, text="AKTIFKAN", width=95, height=26, font=("Consolas", 10, "bold"),
                              fg_color=color, hover_color=T["acc"], text_color="#041014", command=cmd)
            b.pack(side="right", padx=8, pady=5)
            return b

        # SECTION 1: LIVE GOLD & INCOME CHEATS
        section("💰 [ 1. GOLD & INCOME BOOSTER (LIVE + SAVE) ]", T["gold"])
        btn(scroll, "Inject +1.000.000 Gold Instan (Live & Save)", "ALT+1", T["gold"], lambda: self.inject_gold(1_000_000))
        btn(scroll, "Set MAX GOLD 999.999.999 (Sultan Zoo)", "ALT+2", T["gold"], lambda: self.set_max_gold(999_999_999))
        self._btn_inf = btn(scroll, "Auto-Freeze Infinite Gold Loop (ON/OFF)", "ALT+3", T["cyan"], self.toggle_inf_gold)

        # SECTION 2: ANIMALS, AREAS, CAMPS & COSTUMES UNLOCKER
        section("🦁 [ 2. UNLOCK SEMUA HEWAN, AREA, CAMP & KOSTUM ]", T["acc2"])
        btn(scroll, "Unlock Semua 30 Hewan Voice Zoo (100% Collection)", "ALT+4", T["acc"], self.unlock_all_animals)
        btn(scroll, "Unlock Semua Area (Wind Island & Deep Cave)", "ALT+5", T["cyan"], self.unlock_all_areas)
        btn(scroll, "Beli Semua 4 Camp (Forest, Snow, Jungle, Savannah)", "ALT+6", T["acc"], self.unlock_all_camps)
        btn(scroll, "Unlock Semua 5 Kostum (Duck, Reindeer, Frog, Cat)", "ALT+7", T["purple"], self.unlock_all_costumes)

        # SECTION 3: 1-CLICK GOD SAVE & BACKUP
        section("👑 [ 3. 1-CLICK 100% PERFECT SAVE & RESTORE ]", T["purple"])
        btn(scroll, "🔥 1-CLICK UNLOCK SEMUA (999M Gold + 30 Hewan + Area + Camp)", "ALT+8", T["gold"], self.unlock_everything_godmode)
        btn(scroll, "🚀 Reload / Restart Game agar Save Langsung Aktif", "ALT+9", T["cyan"], self.reload_game_with_save)
        btn(scroll, "♻️ Panic Reset / Restore Backup Save Asli (.bak)", "ALT+0", T["red"], self.restore_backup_save)

        # Bottom Log Box
        self._log_box = ctk.CTkTextbox(self, height=95, fg_color="#040B0E", text_color=T["acc2"],
                                       font=("Consolas", 9), corner_radius=6, border_width=1, border_color="#163242")
        self._log_box.pack(fill="x", padx=12, pady=(0, 10))
        self.log("🦁 ASTRA My Voice Zoo Mod Menu v3.0 Siap, Komandan DAFFA!")
        self.log(f"📂 Lokasi Save: {SAVE_PATH}")

    def log(self, msg: str):
        ts = time.strftime("%H:%M:%S")
        try:
            self._log_box.insert("end", f"[{ts}] {msg}\n")
            self._log_box.see("end")
        except Exception:
            pass

    def _refresh_save_summary(self):
        try:
            data = load_save_json()
            gold = data.get("CurrentGold", 0)
            live_g = self._bridge.read_gold_live() if self._bridge else None
            if live_g is not None and live_g >= 0:
                gold = live_g

            animals = data.get("AnimalSaveDataDict", {})
            c_anim = sum(1 for v in animals.values() if v.get("IsCollected"))

            areas = data.get("AreaSaveData", {})
            c_area = int(bool(areas.get("IsUnlock_WindIsland"))) + int(bool(areas.get("IsUnlock_DeepCave")))

            camps = data.get("CampSaveData", {})
            c_camp = sum(1 for k in ("IsBuy_Forest", "IsBuy_Snow", "IsBuy_Jungle", "IsBuy_Savannah") if camps.get(k))

            costumes = data.get("CostumeSaveData", {}).get("CostumeBuyStateDict", {})
            c_cost = sum(1 for v in costumes.values() if v)

            self._sum_lbl.configure(
                text=f"💰 Gold: {gold:,} | 🐾 Hewan: {c_anim}/30 | 🏝️ Area: {c_area}/2 | ⛺ Camp: {c_camp}/4 | 🎭 Kostum: {c_cost}/5"
            )
        except Exception:
            pass

    # ==================== CHEAT ACTIONS ====================
    def inject_gold(self, amount: int = 1_000_000):
        self._beep(980, 70)
        live_ok = False
        if self._bridge:
            try:
                live_ok = self._bridge.add_gold_live(amount)
            except Exception as e:
                self.log(f"[Mono] Info: {e}")

        data = load_save_json()
        data["CurrentGold"] = min(999_999_999, int(data.get("CurrentGold", 0)) + amount)
        write_save_json(data)
        self._refresh_save_summary()
        mode_str = "LIVE MEMORY + SAVE" if live_ok else "SAVE.JSON"
        self.log(f"💰 +{amount:,} Gold berhasil ditambahkan ({mode_str})! Total: {data['CurrentGold']:,}")

    def set_max_gold(self, target: int = 999_999_999):
        self._beep(1100, 90)
        live_ok = False
        if self._bridge:
            try:
                cur = self._bridge.read_gold_live() or 0
                diff = max(0, target - cur)
                if diff > 0:
                    live_ok = self._bridge.add_gold_live(diff)
            except Exception:
                pass

        data = load_save_json()
        data["CurrentGold"] = target
        write_save_json(data)
        self._refresh_save_summary()
        self.log(f"👑 MAX GOLD {target:,} diaktifkan ({'LIVE + SAVE' if live_ok else 'SAVE.JSON'})!")

    def toggle_inf_gold(self):
        self._inf_gold_loop = not self._inf_gold_loop
        self._beep(1200 if self._inf_gold_loop else 500, 80)
        self._btn_inf.configure(
            text="AKTIF (ON)" if self._inf_gold_loop else "AKTIFKAN",
            fg_color=T["acc"] if self._inf_gold_loop else T["cyan"]
        )
        self.log(f"🔄 Auto-Freeze Infinite Gold: {'ON' if self._inf_gold_loop else 'OFF'}")

    def unlock_all_animals(self):
        self._beep(1040, 80)
        data = load_save_json()
        animals = data.setdefault("AnimalSaveDataDict", {})
        for i in range(1, 31):
            aid = str(10000 + i)
            if aid not in animals:
                animals[aid] = {"ID": 10000 + i, "IsCollected": True, "Name": ""}
            else:
                animals[aid]["IsCollected"] = True
        data["IsTutorialCompleted"] = True
        write_save_json(data)
        self._refresh_save_summary()
        self.log("🦁 Semua 30 Hewan My Voice Zoo telah di-UNLOCK di save.json!")

    def unlock_all_areas(self):
        self._beep(1080, 80)
        data = load_save_json()
        data["AreaSaveData"] = {
            "IsUnlock_WindIsland": True,
            "IsUnlock_DeepCave": True
        }
        write_save_json(data)
        self._refresh_save_summary()
        self.log("🏝️ Wind Island & Deep Cave berhasil di-UNLOCK!")

    def unlock_all_camps(self):
        self._beep(1120, 80)
        data = load_save_json()
        data["CampSaveData"] = {
            "IsBuy_Forest": True,
            "IsBuy_Snow": True,
            "IsBuy_Jungle": True,
            "IsBuy_Savannah": True
        }
        write_save_json(data)
        self._refresh_save_summary()
        self.log("⛺ Semua 4 Camp (Forest, Snow, Jungle, Savannah) berhasil dibeli/di-UNLOCK!")

    def unlock_all_costumes(self):
        self._beep(1160, 80)
        data = load_save_json()
        cost = data.setdefault("CostumeSaveData", {"CostumeBuyStateDict": {}, "EquippedCostumeID": 0})
        cost["CostumeBuyStateDict"] = {
            "Default": True,
            "Duck": True,
            "Reindeer": True,
            "Frog": True,
            "Cat": True
        }
        write_save_json(data)
        self._refresh_save_summary()
        self.log("🎭 Semua 5 Kostum (Default, Duck, Reindeer, Frog, Cat) berhasil di-UNLOCK!")

    def unlock_everything_godmode(self):
        self._beep(880, 60)
        self._beep(1320, 110)
        data = load_save_json()
        data["CurrentGold"] = 999_999_999
        data["IsTutorialCompleted"] = True
        animals = data.setdefault("AnimalSaveDataDict", {})
        for i in range(1, 31):
            aid = str(10000 + i)
            if aid not in animals:
                animals[aid] = {"ID": 10000 + i, "IsCollected": True, "Name": ""}
            else:
                animals[aid]["IsCollected"] = True
        data["AreaSaveData"] = {"IsUnlock_WindIsland": True, "IsUnlock_DeepCave": True}
        data["CampSaveData"] = {"IsBuy_Forest": True, "IsBuy_Snow": True, "IsBuy_Jungle": True, "IsBuy_Savannah": True}
        data["CostumeSaveData"] = {
            "CostumeBuyStateDict": {"Default": True, "Duck": True, "Reindeer": True, "Frog": True, "Cat": True},
            "EquippedCostumeID": data.get("CostumeSaveData", {}).get("EquippedCostumeID", 0)
        }
        write_save_json(data)
        if self._bridge:
            try:
                self._bridge.add_gold_live(999_999_999)
            except Exception:
                pass
        self._refresh_save_summary()
        self.log("🔥 [GOD MODE] 999M Gold + 30 Hewan + 2 Area + 4 Camp + 5 Kostum UNLOCKED 100%!")

    def reload_game_with_save(self):
        """Restart MyVoiceZoo.exe dengan cepat tanpa ditimpa AutoSave saat keluar."""
        self._beep(700, 80)
        self.log("🚀 Me-restart MyVoiceZoo.exe agar Save Baru langsung dimuat...")
        # Backup current modded save before killing process
        modded_bytes = open(SAVE_PATH, "rb").read() if os.path.exists(SAVE_PATH) else None
        subprocess.run('taskkill /F /IM "MyVoiceZoo.exe"', shell=True, capture_output=True)
        time.sleep(0.8)
        if modded_bytes:
            with open(SAVE_PATH, "wb") as f:
                f.write(modded_bytes)
        if os.path.exists(GAME_EXE):
            subprocess.Popen([GAME_EXE], cwd=GAME_DIR)
            self.log("✅ MyVoiceZoo.exe diluncurkan kembali dengan Save God Mode!")

    def restore_backup_save(self):
        self._inf_gold_loop = False
        self._beep(440, 120)
        bak = SAVE_PATH + ".bak"
        if os.path.exists(bak):
            shutil.copy2(bak, SAVE_PATH)
            self._refresh_save_summary()
            self.log("♻️ Backup save.json.bak berhasil dipulihkan!")
        else:
            self.log("ℹ️ Belum ada file backup save.json.bak.")

    # ==================== BACKGROUND WATCHERS ====================
    def _process_watcher(self):
        while self._running:
            try:
                found_pid = None
                for p in psutil.process_iter(["pid", "name"]):
                    if p.info["name"] and p.info["name"].lower() == PROC_NAME.lower():
                        found_pid = p.info["pid"]
                        break

                if found_pid:
                    if not self._pm or self._pm.process_id != found_pid:
                        if PYMEM_OK:
                            try:
                                self._pm = pymem.Pymem(PROC_NAME)
                                self._bridge = MyVoiceZooMonoBridge(self._pm)
                                self.after(0, lambda p=found_pid: (
                                    self._dot.configure(text_color=T["acc"]),
                                    self._stat_lbl.configure(text=f"TERHUBUNG KE MYVOICEZOO.EXE (PID: {p}) — MONO BRIDGE AKTIF", text_color=T["acc2"]),
                                    self.log(f"✅ Terhubung ke {PROC_NAME} (PID {p}) via Mono C-API Bridge!")
                                ))
                            except Exception:
                                self.after(0, lambda p=found_pid: (
                                    self._dot.configure(text_color=T["gold"]),
                                    self._stat_lbl.configure(text=f"MYVOICEZOO.EXE AKTIF (PID: {p}) — SAVE ENGINE READY", text_color=T["gold"])
                                ))
                    # Infinite gold loop if enabled
                    if self._inf_gold_loop and self._bridge:
                        try:
                            cur = self._bridge.read_gold_live()
                            if cur is not None and cur < 99_999_999:
                                self._bridge.add_gold_live(99_999_999 - cur)
                        except Exception:
                            pass
                else:
                    if self._pm is not None:
                        self._pm = None
                        self._bridge = None
                        self.after(0, lambda: (
                            self._dot.configure(text_color=T["red"]),
                            self._stat_lbl.configure(text="MyVoiceZoo.exe tidak berjalan (Save Unlocker Standby)", text_color=T["muted"])
                        ))

                self.after(0, self._refresh_save_summary)
            except Exception:
                pass
            time.sleep(2.0)

    def _hotkey_listener(self):
        prev = {k: False for k in (VK_1, VK_2, VK_3, VK_4, VK_5, VK_6, VK_7, VK_8, VK_9, VK_0)}
        actions = {
            VK_1: lambda: self.inject_gold(1_000_000),
            VK_2: lambda: self.set_max_gold(999_999_999),
            VK_3: self.toggle_inf_gold,
            VK_4: self.unlock_all_animals,
            VK_5: self.unlock_all_areas,
            VK_6: self.unlock_all_camps,
            VK_7: self.unlock_all_costumes,
            VK_8: self.unlock_everything_godmode,
            VK_9: self.reload_game_with_save,
            VK_0: self.restore_backup_save,
        }
        while self._running:
            try:
                alt_down = (user32.GetAsyncKeyState(VK_ALT) & 0x8000) != 0
                for vk, fn in actions.items():
                    is_down = alt_down and ((user32.GetAsyncKeyState(vk) & 0x8000) != 0)
                    if is_down and not prev[vk]:
                        self.after(0, fn)
                    prev[vk] = is_down
            except Exception:
                pass
            time.sleep(0.04)


if __name__ == "__main__":
    app = MyVoiceZooModMenu()
    app.mainloop()
