#!/usr/bin/env python3
# ==============================================================================
# ASTRA 3D RPG ENGINE - SERVER & CLIENT RUNTIME
# Dedicated for Komandan DAFFA
# Game: ASTRA BLADE - RUINS OF DAFFA (3D ACTION RPG)
# Architecture: AMD Ryzen 5 5600, AMD Radeon RX 580 (4GB VRAM), 16GB RAM
# ==============================================================================

import os
import sys
import time
import webbrowser
import threading
import subprocess
import urllib.request
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Safe UTF-8 configuration for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PORT = 9998
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AstraRPGHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        pass

def launch_game_client():
    url = f"http://localhost:{PORT}/"
    profile_dir = os.path.join(BASE_DIR, ".rpg_profile")
    try:
        os.makedirs(profile_dir, exist_ok=True)
    except Exception:
        pass

    chrome_paths = [
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    ]
    edge_paths = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
    ]

    # 1. Prioritaskan Google Chrome (Browser Utama Komandan) dengan Dedicated Profile
    for cp in chrome_paths:
        if os.path.exists(cp):
            try:
                proc = subprocess.Popen([
                    cp,
                    f"--user-data-dir={profile_dir}",
                    f"--app={url}",
                    "--start-fullscreen",
                    "--no-first-run",
                    "--no-default-browser-check"
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
                time.sleep(0.4)
                if proc.poll() is None:
                    return
            except Exception as e:
                print(f"[ASTRA RPG] Info Chrome: {e}")

    # 2. Alternatif Microsoft Edge dengan Dedicated Profile
    for ep in edge_paths:
        if os.path.exists(ep):
            try:
                proc = subprocess.Popen([
                    ep,
                    f"--user-data-dir={profile_dir}",
                    f"--app={url}",
                    "--start-fullscreen",
                    "--no-first-run",
                    "--no-default-browser-check"
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
                time.sleep(0.4)
                if proc.poll() is None:
                    return
            except Exception as e:
                print(f"[ASTRA RPG] Info Edge: {e}")

    # 3. Fallback OS Shell: Default Browser Windows
    print(f"[ASTRA RPG] Membuka browser default...")
    try:
        os.startfile(url)
    except Exception:
        try:
            subprocess.Popen(f'start "" "{url}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            webbrowser.open(url)

def start_server():
    try:
        server = HTTPServer(('127.0.0.1', PORT), AstraRPGHandler)
    except OSError as e:
        if getattr(e, 'winerror', None) == 10048 or "Address already in use" in str(e):
            print("==================================================================")
            print(f" [OK] Server RPG 3D sudah aktif di: http://localhost:{PORT}")
            print(f" [OK] Membuka jendela permainan STANDALONE FULLSCREEN...")
            print("==================================================================")
            launch_game_client()
            return
        raise e

    print("==================================================================")
    print("      ⚔️ ASTRA BLADE: RUINS OF DAFFA (3D DARK FANTASY ACTION RPG)")
    print("      Visual: Three.js PBR, HDR Bloom, Dynamic Torches & Shadows  ")
    print("      Combat: 3-Hit Combo, Dodge Roll (i-Frames), Parry, Spells   ")
    print("      Hardware: AMD Ryzen 5 5600 + AMD Radeon RX 580 (4GB VRAM)   ")
    print("==================================================================")
    print(f" [OK] Server RPG 3D aktif di: http://localhost:{PORT}")
    print(f" [OK] Membuka client permainan...")
    print("==================================================================")

    threading.Timer(0.8, launch_game_client).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[ASTRA RPG] Server dinonaktifkan.")
        server.server_close()

if __name__ == "__main__":
    start_server()
