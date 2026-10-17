#!/usr/bin/env python3
# ==============================================================================
# ASTRA 3D NEURAL ENGINE - SERVER & POST-PROCESSING ASSET MANAGER
# Dedicated for Komandan DAFFA
# Hardware: AMD Ryzen 5 5600, AMD Radeon RX 580 (4GB VRAM), 16GB RAM
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

PORT = 9999
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS_TO_CACHE = [
    ("three.min.js", "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"),
    ("CopyShader.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"),
    ("LuminosityHighPassShader.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"),
    ("EffectComposer.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"),
    ("RenderPass.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"),
    ("ShaderPass.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"),
    ("UnrealBloomPass.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"),
    ("GLTFLoader.js", "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"),
]

def cache_assets():
    print("[ASTRA 3D] Menyiapkan shader post-processing & Three.js r128...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    for filename, url in SCRIPTS_TO_CACHE:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath) or os.path.getsize(filepath) < 500:
            try:
                print(f"[ASTRA 3D] Mengunduh modul grafis: {filename}...")
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=12) as resp, open(filepath, "wb") as f:
                    f.write(resp.read())
            except Exception as e:
                print(f"[ASTRA 3D] Peringatan unduh {filename}: {e}")
    print("[ASTRA 3D] Seluruh library grafis siap (Offline Ready).")

class AstraHTTPHandler(SimpleHTTPRequestHandler):
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
    profile_dir = os.path.join(BASE_DIR, ".game_profile")
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
                print(f"[ASTRA 3D] Info Chrome: {e}")

    # 2. Alternatif Microsoft Edge dengan Dedicated Profile (Cegah Error 32 Lockfile)
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
                print(f"[ASTRA 3D] Info Edge: {e}")

    # 3. Fallback Bulletproof: Buka default browser Windows via OS Shell
    print(f"[ASTRA 3D] Meluncurkan browser default Windows...")
    try:
        os.startfile(url)
    except Exception:
        try:
            subprocess.Popen(f'start "" "{url}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            webbrowser.open(url)

def start_server():
    cache_assets()
    try:
        server = HTTPServer(('127.0.0.1', PORT), AstraHTTPHandler)
    except OSError as e:
        if getattr(e, 'winerror', None) == 10048 or "Address already in use" in str(e):
            print("==================================================================")
            print(f" [OK] Server 3D sudah berjalan di: http://localhost:{PORT}")
            print(f" [OK] Membuka jendela permainan STANDALONE...")
            print("==================================================================")
            launch_game_client()
            return
        raise e

    print("==================================================================")
    print("      ASTRA PROTOCOL - DAFFA STARFIGHTER 3D ULTRA ENGINE          ")
    print("      Grafis: Cinema HDR Bloom, PBR Sci-Fi, Procedural Nebulas    ")
    print("      Hardware: AMD Ryzen 5 5600 + AMD Radeon RX 580 (4GB VRAM)   ")
    print("==================================================================")
    print(f" [OK] Engine 3D aktif di: http://localhost:{PORT}")
    print(f" [OK] Membuka jendela permainan STANDALONE FULLSCREEN...")
    print("==================================================================")

    threading.Timer(0.8, launch_game_client).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[ASTRA 3D] Server dinonaktifkan.")
        server.server_close()

if __name__ == "__main__":
    start_server()
