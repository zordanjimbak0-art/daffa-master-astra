import os
import sys
import json
import math
import struct
import base64
import socket
import psutil
import customtkinter as ctk
from tkinter import filedialog
from collections import Counter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

XOR_KEY = b"sdhfioshdio@#%#@%@$@dgfi!~@$#joash"

def compute_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    n = len(data)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())

class AstraDiagnosticsWorkbench(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🛡️ ASTRA AI — Binary Architecture, Save Telemetry & System Auditor v6.5")
        self.geometry("1060x680")
        self.configure(fg_color="#070B14")

        # Header
        hdr = ctk.CTkFrame(self, fg_color="#0F172A", height=64, corner_radius=0)
        hdr.pack(fill="x", side="top")

        ctk.CTkLabel(
            hdr,
            text="🛡️ ASTRA BINARY ARCHITECTURE & SAVE TELEMETRY WORKBENCH",
            font=("Consolas", 17, "bold"),
            text_color="#00F2FE"
        ).pack(side="left", padx=20, pady=16)

        ctk.CTkButton(
            hdr,
            text="🌐 BUKA WEB CYBER LAB",
            font=("Consolas", 12, "bold"),
            fg_color="#059669",
            hover_color="#047857",
            width=180,
            height=34,
            command=self.open_web_lab
        ).pack(side="right", padx=16)

        # Main layout
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=16, pady=14)

        left = ctk.CTkFrame(body, width=320, fg_color="#111827", corner_radius=12)
        left.pack(side="left", fill="y", padx=(0, 12))
        left.pack_propagate(False)

        right = ctk.CTkFrame(body, fg_color="#111827", corner_radius=12)
        right.pack(side="left", fill="both", expand=True)

        # Left controls
        ctk.CTkLabel(left, text="⚡ MODUL INSPEKSI LOKAL", font=("Consolas", 14, "bold"), text_color="#38BDF8").pack(anchor="w", padx=16, pady=(16, 10))

        ctk.CTkButton(
            left, text="🔍 1. Audit File .EXE / .DLL Game", font=("Consolas", 12, "bold"),
            fg_color="#0284C7", hover_color="#0369A1", height=38, command=self.pick_and_audit_pe
        ).pack(fill="x", padx=16, pady=6)

        ctk.CTkButton(
            left, text="🗝️ 2. Inspect Save My Voice Zoo", font=("Consolas", 12, "bold"),
            fg_color="#7C3AED", hover_color="#6D28D9", height=38, command=self.inspect_myvoicezoo_save
        ).pack(fill="x", padx=16, pady=6)

        ctk.CTkButton(
            left, text="📡 3. Audit Port & Layanan Lokal", font=("Consolas", 12, "bold"),
            fg_color="#059669", hover_color="#047857", height=38, command=self.audit_local_ports
        ).pack(fill="x", padx=16, pady=6)

        ctk.CTkButton(
            left, text="🖥️ 4. Telemetry Proses & Memori", font=("Consolas", 12, "bold"),
            fg_color="#E11D48", hover_color="#BE123C", height=38, command=self.audit_running_processes
        ).pack(fill="x", padx=16, pady=6)

        ctk.CTkButton(
            left, text="📦 5. Sync Hasil Audit ke GitHub", font=("Consolas", 12, "bold"),
            fg_color="#1E293B", hover_color="#334155", height=38, command=self.sync_to_github
        ).pack(fill="x", padx=16, pady=(18, 6))

        # Right console output
        ctk.CTkLabel(right, text="📟 LAPORAN TELEMETRI & STRUKTUR BINER REAL-TIME", font=("Consolas", 14, "bold"), text_color="#00FF9D").pack(anchor="w", padx=18, pady=(16, 8))

        self.console = ctk.CTkTextbox(right, font=("Consolas", 12), fg_color="#04070D", text_color="#00FF9D", corner_radius=8)
        self.console.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.write_log("[ASTRA DIAGNOSTICS WORKBENCH v6.5 READY]")
        self.write_log("Komandan: Muhamad Daffa Cahya | Rig: AMD Ryzen 5 5600 + Radeon RX 580")
        self.write_log("Pilih salah satu modul di panel kiri untuk memulai inspeksi teknis...\n")
        self.audit_local_ports()

    def write_log(self, msg: str):
        self.console.insert("end", msg + "\n")
        self.console.see("end")

    def open_web_lab(self):
        import webbrowser
        local_html = r"D:\Game\DAFFA_GITHUB_PORTFOLIO\docs\cyberlab.html"
        if os.path.exists(local_html):
            webbrowser.open(local_html)
        else:
            webbrowser.open("https://zordanjimbak0-art.github.io/daffa-master-astra/cyberlab.html")

    def pick_and_audit_pe(self):
        initial_dir = r"D:\Game\Games" if os.path.exists(r"D:\Game\Games") else r"D:\Game"
        fpath = filedialog.askopenfilename(
            initialdir=initial_dir,
            title="Pilih File .EXE atau .DLL Game",
            filetypes=[("Executable & DLL", "*.exe *.dll"), ("All Files", "*.*")]
        )
        if not fpath:
            return
        self.audit_pe_file(fpath)

    def audit_pe_file(self, fpath: str):
        try:
            with open(fpath, "rb") as f:
                header = f.read(4096)
                sample = f.read(512 * 1024)
            data = header + sample
            ent = compute_entropy(data)
            is_pe = len(header) >= 64 and header[:2] == b"MZ"
            arch = "Unknown"
            sections_info = []
            if is_pe:
                pe_off = struct.unpack("<I", header[0x3C:0x40])[0]
                if pe_off + 24 <= len(header):
                    machine = struct.unpack("<H", header[pe_off + 4:pe_off + 6])[0]
                    num_sec = struct.unpack("<H", header[pe_off + 6:pe_off + 8])[0]
                    opt_sz = struct.unpack("<H", header[pe_off + 20:pe_off + 22])[0]
                    arch = "x64 (AMD64 / 0x8664)" if machine == 0x8664 else ("x86 (i386 / 0x014C)" if machine == 0x014C else hex(machine))
                    sec_table = pe_off + 24 + opt_sz
                    for i in range(min(num_sec, 10)):
                        off = sec_table + i * 40
                        if off + 40 <= len(header):
                            sname = header[off:off+8].rstrip(b"\x00").decode("ascii", errors="ignore")
                            vsize = struct.unpack("<I", header[off+8:off+12])[0]
                            rsize = struct.unpack("<I", header[off+16:off+20])[0]
                            sections_info.append(f"{sname} (Virtual: {vsize//1024}KB, Raw: {rsize//1024}KB)")

            folder = os.path.dirname(fpath)
            engine_type = "Native C/C++ Binary"
            if os.path.exists(os.path.join(folder, "GameAssembly.dll")):
                engine_type = "Unity Engine (IL2CPP Native Backend)"
            elif os.path.exists(os.path.join(folder, "UnityPlayer.dll")):
                engine_type = "Unity Engine (Mono .NET Managed Runtime)"

            self.write_log("=" * 72)
            self.write_log(f"[PE64 BINARY AUDIT] {os.path.basename(fpath)}")
            self.write_log(f" • Lokasi File   : {fpath}")
            self.write_log(f" • Ukuran File   : {os.path.getsize(fpath) / (1024*1024):.2f} MB")
            self.write_log(f" • Arsitektur    : {arch}")
            self.write_log(f" • Deteksi Engine: {engine_type}")
            self.write_log(f" • Entropi Biner : {ent:.3f} bits/byte ({'Kompresi/Proteksi Tinggi' if ent > 7.2 else 'Standar Terbuka'})")
            if sections_info:
                self.write_log(f" • Section Table : {', '.join(sections_info)}")
            self.write_log("=" * 72 + "\n")
        except Exception as e:
            self.write_log(f"[ERROR] Gagal membaca biner: {e}")

    def inspect_myvoicezoo_save(self):
        save_p = os.path.expanduser(r"~\AppData\LocalLow\DefaultCompany\MyVoiceZoo\save.json")
        self.write_log("=" * 72)
        self.write_log("[SAVE DATA TELEMETRY] Memeriksa save.json My Voice Zoo...")
        if not os.path.exists(save_p):
            self.write_log(f" • File belum ditemukan di: {save_p}")
            return
        raw = open(save_p, "rb").read()
        try:
            text = raw.decode("utf-8")
            if not text.strip().startswith("{"):
                raise ValueError("Encoded")
        except Exception:
            dec = bytes(b ^ XOR_KEY[i % len(XOR_KEY)] for i, b in enumerate(raw))
            text = dec.decode("utf-8", errors="ignore")
        self.write_log(f" • Ukuran Payload: {len(raw)} bytes")
        self.write_log(f" • Cuplikan JSON : {text[:320]}...")
        self.write_log("=" * 72 + "\n")

    def audit_local_ports(self):
        self.write_log("=" * 72)
        self.write_log("[LOCAL SERVICE & PORT TELEMETRY — 127.0.0.1]")
        ports = [
            (8888, "Astra Cockpit Stream-Deck Server"),
            (11434, "Ollama Local LLM Server"),
            (5037, "Android ADB Bridge Daemon (Samsung Galaxy A16)"),
            (8080, "Local Web Development Server"),
        ]
        for port, label in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.15)
            is_open = (s.connect_ex(("127.0.0.1", port)) == 0)
            s.close()
            state = "ONLINE (OPEN)" if is_open else "STANDBY (CLOSED)"
            self.write_log(f" • Port {port:<5d} | {state:<18s} | {label}")
        self.write_log("=" * 72 + "\n")

    def audit_running_processes(self):
        self.write_log("=" * 72)
        self.write_log("[TOP MEMORY PROCESSES — RYZEN 5 5600 / 16GB RAM]")
        procs = []
        for p in psutil.process_iter(["pid", "name", "memory_info"]):
            try:
                mb = p.info["memory_info"].rss / (1024 * 1024)
                procs.append((mb, p.info["pid"], p.info["name"]))
            except Exception:
                pass
        procs.sort(reverse=True)
        for mb, pid, name in procs[:10]:
            self.write_log(f" • PID {pid:<6d} | {mb:7.1f} MB | {name}")
        self.write_log("=" * 72 + "\n")

    def sync_to_github(self):
        import subprocess
        portfolio_dir = r"D:\Game\DAFFA_GITHUB_PORTFOLIO"
        subprocess.Popen(["cmd.exe", "/c", "git add . && git commit -m \"chore: sync diagnostics telemetry\" && git push origin main"], cwd=portfolio_dir, creationflags=0x08000000)
        self.write_log("✅ Sinkronisasi telemetri ke GitHub (zordanjimbak0-art/daffa-master-astra) sedang berjalan di background!")

if __name__ == "__main__":
    app = AstraDiagnosticsWorkbench()
    app.mainloop()
