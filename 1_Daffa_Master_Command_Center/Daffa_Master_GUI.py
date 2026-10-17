"""
================================================================================
DAFFA MASTER COMMAND CENTER v5.0 ULTIMATE // ASTRA AI PROTOCOL
CustomTkinter v6.0.0 High-Tech Gaming & Security Operations Center
Hardware Optimized: AMD Ryzen 5 5600 | AMD Radeon RX 580 (4GB) | 16GB Dual-Channel
Ergonomic: 100% Compatible with 60% Mechanical Keyboards (No F1-F12 / Numpad required)
================================================================================
"""

import os
import sys
import subprocess
import threading
import time
import urllib.request
import webbrowser
import ctypes
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import psutil

# Set High DPI Awareness on Windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

# Appearance configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==================== PALET WARNA CYBERPUNK / WINDOWS 11 ====================
THEME = {
    "bg_main": "#080C14",
    "bg_panel": "#0E1524",
    "bg_card": "#131C30",
    "bg_card_hover": "#1C2844",
    "border": "#202E4A",
    "border_glow": "#00E5FF",
    "accent_cyan": "#00E5FF",
    "accent_cyan_hover": "#00B4D8",
    "accent_emerald": "#10B981",
    "accent_emerald_hover": "#059669",
    "accent_amber": "#F59E0B",
    "accent_gold": "#F59E0B",
    "accent_red": "#EF4444",
    "accent_purple": "#A855F7",
    "text_main": "#F8FAFC",
    "text_muted": "#94A3B8",
    "text_dark": "#0B0F19",
}

# ==================== DATABASE GAMES & TOOLS ====================
GAMES_DB = [
    # ── GAME MODS ──────────────────────────────────────────────
    {"name": "Cookie Clicker",     "icon": "🍪", "genre": "Idle / Incremental", "category": "MODS",     "status": "⚡ 10^29 GOD MODE",
     "bat": "../DAFFA_PROJECTS/MAIN_COOKIE_CLICKER.bat", "exe": "chrome.exe",
     "color": THEME["accent_amber"], "hotkeys": ["💰 Injeksi 10^29 Cookies Instan", "⚡ Hyper-Clicker 100.000 CPS", "👑 Auto-Buy Gedung Tertinggi", "💎 1.000 Sugar Lumps Unlocked"]},

    {"name": "Stardew Valley",     "icon": "🌾", "genre": "Farming RPG",      "category": "MODS",     "status": "MOD (P)",
     "bat": "Stardew Valley/MAIN_DENGAN_CHEAT.bat", "exe": "StardewModdingAPI.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["P = Buka CJB Cheats Menu", "ALT+2 = Speed 2x", "ALT+4 = Slowmo", "F1 = Auto-Clicker"]},

    {"name": "Project Zomboid",    "icon": "🧟", "genre": "Survival Horror",  "category": "MODS",     "status": "HOTKEY MOD",
     "bat": "Project Zomboid/MAIN_DENGAN_CHEAT.bat", "exe": "ProjectZomboid64.exe",
     "color": THEME["accent_amber"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Infinite Ammo", "ALT+3 = No Clip", "ALT+4 = Fast Build"]},

    {"name": "Subnautica 1",       "icon": "🌊", "genre": "Underwater Survival","category": "MODS",   "status": "NATIVE MOD",
     "bat": "Subnautica/MAIN_DENGAN_CHEAT.bat", "exe": "Subnautica.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["F2 atau \\ = Buka GUI Mod Menu", "ALT+1 = God", "ALT+2 = Infinite O2", "ALT+3 = Free Craft",
                 "ALT+4 = Fast Build", "ALT+5 = Speed 2.5x", "ALT+6 = Free Craft", "ALT+7 = Ghost", "ALT+8 = Invisible", "ALT+Q = Fast Build", "ALT+T = Unlock All"]},

    {"name": "Subnautica 2",       "icon": "🌊", "genre": "Underwater Survival","category": "MODS",   "status": "UE4SS MOD",
     "bat": "Subnautica 2/MAIN_DENGAN_CHEAT.bat", "exe": "Subnautica2-Win64-Shipping.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["ALT+1 = God", "ALT+2 = Infinite O2", "ALT+3 = Free Craft", "ALT+4 = Speed 2x"]},

    {"name": "Terraria",           "icon": "⛏️", "genre": "Sandbox Action",   "category": "MODS",     "status": "CE TABLE",
     "bat": "Terraria/MAIN_DENGAN_CHEAT.bat", "exe": "Terraria.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Journey Mode = God Mode bawaan game!", "ALT+2 = Speed 2x", "ALT+4 = Slowmo", "F1 = Auto-Clicker", "F2 = Auto-Miner"]},

    {"name": "MC Dungeons",        "icon": "⚔️", "genre": "Action RPG",       "category": "MODS",     "status": "ONLINE MOD",
     "bat": "Minecraft Dungeons/MAIN_DENGAN_CHEAT.bat", "exe": "Dungeons.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["Ctrl+1 = God Mode", "Ctrl+2 = Infinite Arrows", "Ctrl+3 = Max Emeralds", "Ctrl+4 = Cooldown 0", "Ctrl+5 = Turbo Melee"]},

    {"name": "Upin & Ipin",        "icon": "👦", "genre": "3D Adventure",     "category": "MODS",     "status": "UE4SS + SAVE",
     "bat": "Upin Ipin/MAIN_DENGAN_CHEAT.bat", "exe": "UIUniverse-Win64-Shipping.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["ALT+1 = God", "ALT+2 = Ghost/Terbang", "ALT+3 = Speed 3x", "ALT+4 = Slowmo", "ALT+5 = Teleport",
                 "ALT+6 = Reset Speed", "ALT+7 = FOV Lebar", "ALT+9 = Pause AI", "💰 Uang & Bahan: via Save Editor di GUI"]},

    {"name": "SpongeBob",          "icon": "🧽", "genre": "3D Platformer",    "category": "MODS",     "status": "SAVE & MACRO",
     "bat": "SpongeBob/MAIN_DENGAN_CHEAT.bat", "exe": "Ghost-Win64-Shipping.exe",
     "color": THEME["accent_amber"], "hotkeys": ["💰 Uang/HP: via Save Editor", "ALT+1 = God", "ALT+2 = Terbang (ON/OFF)", "ALT+4 = Lari Cepat (ON/OFF)"]},

    {"name": "Soulmask",           "icon": "🗡️", "genre": "Survival Crafting","category": "MODS",     "status": "CE + MACRO",
     "bat": "Soulmask/MAIN_DENGAN_CHEAT.bat", "exe": "WS.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Terbang/Ghost", "ALT+3 = Teleport", "ALT+4 = Speed 3x", "ALT+5 = Hancurkan", "Console: F10"]},

    {"name": "Quake Remaster",     "icon": "💀", "genre": "FPS Classic",      "category": "CONSOLE",  "status": "AUTOEXEC",
     "bat": "Quake/MAIN_DENGAN_CHEAT.bat", "exe": "quake_x64_steam.exe",
     "color": THEME["accent_purple"], "hotkeys": ["P = God Mode", "[ = Noclip", "] = Invisible", "\\ = All Weapons", "' = Quad Damage"]},

    {"name": "Metal Slug",         "icon": "🔫", "genre": "Run & Gun Arcade", "category": "MODS",     "status": "CE TABLE",
     "bat": "Metal Slug Attack Reloaded/MAIN_DENGAN_CHEAT.bat", "exe": "MSAR_steam.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Ctrl+1 = Uang 66 Juta", "Ctrl+2 = AP Unlimited", "Ctrl+3 = No Cooldown", "Ctrl+4 = Invincible"]},

    {"name": "Naruto UNS 4",       "icon": "🍥", "genre": "Fighting",         "category": "MODS",     "status": "CE TABLE",
     "bat": "Naruto Shippuden UNS4/MAIN_DENGAN_CHEAT.bat", "exe": "NSUNS4.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Cheat Engine + NarutoUNS4_DaffaCheat.ct", "Centang: Unlimited Ryo, Health, Chakra"]},

    {"name": "Naruto Revolution",  "icon": "🍥", "genre": "Fighting",         "category": "MODS",     "status": "CE TABLE",
     "bat": "Naruto Shippuden UNS Revolution/MAIN_DENGAN_CHEAT.bat", "exe": "NSUNSR.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Cheat Engine + NarutoRevo_DaffaCheat.ct", "Centang: Unlimited Ryo, Health, Chakra"]},

    {"name": "Postal 2",           "icon": "📬", "genre": "Open World FPS",   "category": "CONSOLE",  "status": "CONSOLE",
     "bat": "Postal 2/MAIN_DENGAN_CHEAT.bat", "exe": "Postal2.exe",
     "color": THEME["accent_red"], "hotkeys": ["~ = Buka Console", "SISSY = Enable Cheats", "IAmSoLame = God Mode", "IAmTheOne = All Weapons"]},

    {"name": "Serious Sam 2",      "icon": "🔫", "genre": "FPS Arena",        "category": "CONSOLE",  "status": "CONSOLE",
     "bat": "Serious Sam 2/MAIN_DENGAN_CHEAT.bat", "exe": "Sam2.exe",
     "color": THEME["accent_red"], "hotkeys": ["~ = Buka Console", "sam_iEnableCheats=2", "sam_iGodMode=1", "sam_iGiveAll=1"]},

    {"name": "Serious Sam TFE",    "icon": "🔫", "genre": "FPS Arena",        "category": "CONSOLE",  "status": "CONSOLE",
     "bat": "Serious Sam The First Encounter/MAIN_DENGAN_CHEAT.bat", "exe": "SeriousSam.exe",
     "color": THEME["accent_red"], "hotkeys": ["F1 = Buka Console", "Ketik: please god = Kebal", "Ketik: please giveall = Semua Senjata"]},

    {"name": "Snowed Under",       "icon": "❄️", "genre": "Puzzle Platformer","category": "MODS",     "status": "CE MOD (60% KB)",
     "bat": "Snowed.Under/MAIN_DENGAN_CHEAT.bat", "exe": "SnowProject.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["CTRL+1 = Lari Karakter 3x (Dunia Normal)", "CTRL+2 = Freeze World / Musuh", "CTRL+3 = Buka Save Editor (Item/HP)"]},

    {"name": "Albion Online",      "icon": "⚔️", "genre": "MMORPG Sandbox",  "category": "OFFICIAL", "status": "MMORPG RESMI",
     "bat": "AlbionOnline/MAIN.bat", "exe": "Albion-Online_BE.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["Sandbox MMORPG Resmi", "PvP & PvE Full Loot", "DILARANG NGE-CHEAT (EAC BANNED)"]},

    {"name": "Kingdom Rush Vengeance","icon":"👑","genre": "Tower Defense",   "category": "TRAINER",  "status": "AHK TRAINER",
     "bat": "Kingdom Rush Vengeance/MAIN_DENGAN_CHEAT.bat", "exe": "Kingdom Rush Vengeance.exe",
     "color": THEME["accent_amber"], "hotkeys": ["ALT+1 = Gold 99,999", "ALT+2 = Freeze Gold", "ALT+3 = Lives 999", "ALT+4 = Kingdom Gold Max"]},

    {"name": "Plants vs Zombies",  "icon": "🌻", "genre": "Tower Defense",    "category": "TRAINER",  "status": "AHK TRAINER",
     "bat": "Plants vs Zombies GOTY/MAIN_DENGAN_CHEAT.bat", "exe": "PlantsVsZombies.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["ALT+1 = Sun 9999", "ALT+2 = Lives 99", "ALT+3 = Koin 999,999", "ALT+4 = Freeze Sun (loop)"]},

    {"name": "Graveyard Keeper 2", "icon": "⚰️", "genre": "Simulation RPG",  "category": "MODS",     "status": "MOD MENU v2.3",
     "bat": "Graveyard Keeper 2/MAIN_DENGAN_CHEAT.bat", "exe": "GraveyardKeeper2.exe",
     "color": THEME["accent_purple"], "hotkeys": ["INSERT / ALT+M = Buka Mod Menu", "🎁 Spawner Item Apapun Instan", "🏃 Lari 2.2x", "💰 Uang Tak Terbatas"]},

    {"name": "Bloons TD 5",        "icon": "🎈", "genre": "Tower Defense",    "category": "MODS",     "status": "MASTER MOD",
     "bat": "Bloons TD 5/MAIN_DENGAN_CHEAT.bat", "exe": "BTD5-Win.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["⚡ 999k Monkey Money & 99k Token", "⭐ Rank 100 Max & Semua 35 Tower Max XP", "🔓 Semua Tier-4 Terbuka"]},

    {"name": "Kingdom Rush",       "icon": "🏰", "genre": "Tower Defense",    "category": "MODS",     "status": "AUTO GOD MODE",
     "bat": "KingdomRush/MAIN_DENGAN_CHEAT.bat", "exe": "Kingdom Rush.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Auto 999k Gems & 150 Stars", "Auto 99x Nukes & Freezes", "Auto All Heroes Lvl 10"]},

    {"name": "Kingdom Rush Frontiers","icon":"🏰","genre":"Tower Defense",    "category": "MODS",     "status": "AUTO GOD MODE",
     "bat": "KingdomRushFrontiers/MAIN_DENGAN_CHEAT.bat", "exe": "Kingdom Rush Frontiers.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Auto 999k Gems & 150 Stars", "Auto 99x Nukes & Freezes", "Auto Heroes Lvl 10"]},

    {"name": "Kingdom Rush Origins","icon":"🏰", "genre": "Tower Defense",    "category": "MODS",     "status": "AUTO GOD MODE",
     "bat": "kingdomrushorigins/MAIN_DENGAN_CHEAT.bat", "exe": "Kingdom Rush Origins.exe",
     "color": THEME["accent_amber"], "hotkeys": ["Auto 999k Gems & 150 Stars", "Auto 99x Nukes & Freezes", "Auto Heroes Lvl 10"]},

    {"name": "DREDGE",             "icon": "🎣", "genre": "Fishing Horror",   "category": "MODS",     "status": "MASTER SPAWNER",
     "bat": "DREDGE-SteamRIP.com/DREDGE/MAIN_DENGAN_CHEAT.bat", "exe": "DREDGE.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["INSERT / ALT+M = Buka Menu Spawner", "🎁 Live Spawner: Ikan/Item Apapun", "🧬 Spawn Ikan Mutasi Langka", "⚡ Speed 5.0x"]},

    {"name": "Subnautica Below Zero","icon":"❄️","genre":"Underwater Survival","category": "MODS",    "status": "⚡ ASTRA MOD MENU",
     "bat": "Subnautica-Below-Zero-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "SubnauticaZero.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Infinite Oxygen", "ALT+3 = Free Crafting", "ALT+4 = Fast Build", "ALT+5 = Super Speed 2.5x", "ALT+6 = Day | ALT+7 = Seatruck | ALT+8 = Exosuit", "ALT+9 = Unlock All | ALT+0 = Panic Reset"]},

    {"name": "Savage Planet",      "icon": "🪐", "genre": "Sci-Fi Adventure", "category": "MODS",     "status": "⚡ ASTRA MOD MENU",
     "bat": "Journey to the Savage Planet/MAIN_DENGAN_CHEAT.bat", "exe": "Towers-Win64-Shipping.exe",
     "color": THEME["accent_emerald"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Free Flight (Fly)", "ALT+3 = Ghost / Noclip", "ALT+4 = Speed 2.5x", "ALT+5 = Slowmo 0.5x | ALT+6 = Walk", "ALT+7 = Inject 999k Carbon & Alloy", "ALT+8 = Teleport | ALT+0 = Panic Reset"]},

    {"name": "Blasphemous",        "icon": "⚔️", "genre": "Soulslike Platformer", "category": "MODS",  "status": "⚡ ASTRA MOD MENU",
     "bat": "Blasphemous-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "Blasphemous.exe",
     "color": THEME["accent_red"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Infinite Fervor", "ALT+3 = Max Tears 999k", "ALT+4 = Speed 3x Boost", "ALT+5 = 1-Hit KO", "ALT+0 = Panic Reset"]},

    {"name": "Blasphemous 2",      "icon": "⚔️", "genre": "Soulslike Platformer", "category": "MODS",  "status": "⚡ ASTRA MOD MENU",
     "bat": "Blasphemous-2-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "Blasphemous 2.exe",
     "color": THEME["accent_red"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Infinite Fervor", "ALT+3 = Max Tears 999k", "ALT+4 = Speed 3x Boost", "ALT+5 = 1-Hit KO", "ALT+0 = Panic Reset"]},

    {"name": "That's Not My Neighbor", "icon": "🚪", "genre": "Horror / Deduction", "category": "MODS", "status": "⚡ AUTOPILOT RADAR",
     "bat": "Thats-Not-My-Neighbor-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "That's not my neighbor.exe",
     "color": THEME["accent_amber"], "hotkeys": ["ALT+1 = Autopilot Radar ON/OFF", "ALT+2 = Auto-Inspect All Docs", "ALT+3 = Auto-Call DDD (3312)", "ALT+4 = Auto-Check Tamu", "ALT+0 = Emergency Panic"]},

    {"name": "Binding of Isaac: Repentance", "icon": "☠️", "genre": "Roguelite Dungeon", "category": "MODS", "status": "⚡ ASTRA MOD MENU",
     "bat": "The.Binding.of.Isaac-Repentance-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "isaac-ng.exe",
     "color": THEME["accent_purple"], "hotkeys": ["ALT+1 = God Mode", "ALT+2 = Max HP 12 Hearts", "ALT+3 = Max Coins 99", "ALT+4 = Max Keys 99", "ALT+5 = Max Bombs 99", "ALT+6 = Unlock Collectibles", "ALT+0 = Panic Reset"]},

    {"name": "KR x PVZ Fusion",    "icon": "🌻", "genre": "Tower Defense Fusion", "category": "MODS", "status": "⚡ FUSION ENGINE",
     "bat": "FUSION_KR_PVZ/MAIN_FUSION.bat", "exe": "KR_PVZ_FUSION_MOD.py",
     "color": THEME["accent_emerald"], "hotkeys": ["God Mode Tower & Heroes", "Infinite Sun & Gems 99,999", "Instant Cool-down Ability", "Instant Win Wave"]},

    {"name": "My Voice Zoo",       "icon": "🦁", "genre": "Voice Zoo Tycoon",     "category": "MODS", "status": "⚡ ASTRA MOD MENU",
     "bat": "MyVoiceZoo-SteamRIP.com/MAIN_DENGAN_CHEAT.bat", "exe": "MyVoiceZoo.exe",
     "color": THEME["accent_cyan"], "hotkeys": ["ALT+1 = +1.000.000 Gold (Live & Save)", "ALT+2 = MAX Gold 999.999.999", "ALT+3 = Auto-Freeze Infinite Gold", "ALT+4 = Unlock Semua 30 Hewan Voice Zoo", "ALT+5 = Unlock Wind Island & Deep Cave", "ALT+6 = Beli Semua 4 Camp (Forest/Snow/Jungle/Savannah)", "ALT+7 = Unlock Semua 5 Kostum", "ALT+8 = 1-Click 100% God Mode Save", "ALT+9 = Quick Reload Game | ALT+0 = Restore Backup"]},

    {"name": "Astra 3D Action RPG","icon": "⚔️", "genre": "First-Person 3D RPG",  "category": "MODS", "status": "⚡ FPS PBR RPG",
     "bat": "../DAFFA_GAMES/MAIN_GAME_RPG_3D.bat", "exe": "chrome.exe",
     "color": THEME["accent_purple"], "hotkeys": ["WASD + Mouse 360 = First-Person Movement", "Klik Kiri = 3-Hit Combo Slash | Klik Kanan = Shield Parry", "Q = Dodge Roll | E = Blade Tempest | R = Abyssal Rupture", "C = Ganti Senjata (Sword/Axe) | F = Tempa Senjata / NPC", "V = Ganti Kamera (1ST/3RD) | G = Ganti GitHub PBR Texture"]},

    {"name": "SpaceX Falcon 9 3D", "icon": "🚀", "genre": "3D Orbital Simulator", "category": "MODS", "status": "⚡ 3D TELEMETRY",
     "bat": "../DAFFA_GAMES/MAIN_GAME_3D.bat", "exe": "chrome.exe",
     "color": THEME["accent_amber"], "hotkeys": ["SPACE = Ignition / Stage Separation", "W/S/A/D = Pitch & Roll Gimbal Vector", "SHIFT / CTRL = Throttle Up / Down", "L = Landing Gear | G = Grid Fins | C = Camera View"]},

    # ── Tools & Security Utilities ────────────────────────────
    {"name": "Security Scanner",   "icon": "🛡️", "genre": "Antivirus",       "category": "SECURITY", "status": "ANTIVIRUS",
     "bat": "../DAFFA_SYSTEM/DAFFA_SECURITY_SCANNER.bat", "exe": "",
     "color": THEME["accent_red"], "hotkeys": ["Jalankan scan keamanan sistem", "Bersihkan cache jaringan & malware"]},

    {"name": "Network Monitor",    "icon": "📡", "genre": "Packet Sniffer",   "category": "SECURITY", "status": "WIRESHARK MINI",
     "bat": "../DAFFA_SYSTEM/BUKA_NETWORK_MONITOR.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Lihat alur paket data mentah (Live)", "Membutuhkan Npcap"]},

    {"name": "URL X-Ray",          "icon": "🔍", "genre": "Web Recon",        "category": "SECURITY", "status": "WEB SCRAPER",
     "bat": "../DAFFA_PROJECTS/BUKA_URL_ANALYZER.bat", "exe": "",
     "color": THEME["accent_purple"], "hotkeys": ["Analisis Link Diam-diam", "Bongkar Judul, Script & Metadata Web"]},

    {"name": "Ping Sweeper",       "icon": "📶", "genre": "LAN Recon",        "category": "SECURITY", "status": "NET RECON",
     "bat": "../DAFFA_PROJECTS/BUKA_PING_SWEEPER.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Deteksi perangkat aktif di WiFi", "Pemindaian LAN Super Cepat"]},

    {"name": "APK X-Ray",          "icon": "📱", "genre": "Malware Analysis", "category": "SECURITY", "status": "MALWARE SCAN",
     "bat": "../DAFFA_PROJECTS/BUKA_APK_ANALYZER.bat", "exe": "",
     "color": THEME["accent_red"], "hotkeys": ["Bongkar Izin File Android APK", "Deteksi Virus RAT & Pencuri OTP"]},

    {"name": "HTTPS Checker",      "icon": "🔒", "genre": "SSL Audit",        "category": "SECURITY", "status": "SSL SCAN",
     "bat": "../DAFFA_PROJECTS/BUKA_HTTPS_CHECKER.bat", "exe": "",
     "color": THEME["accent_emerald"], "hotkeys": ["Cek Keamanan Enkripsi Website", "Deteksi Sertifikat Lemah / Man-in-the-Middle"]},

    {"name": "DNS Lookup",         "icon": "🌐", "genre": "Domain Intel",     "category": "SECURITY", "status": "DOMAIN INTEL",
     "bat": "../DAFFA_PROJECTS/BUKA_DNS_LOOKUP.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Ungkap IP Asli & Server Website", "Lacak DNS Record & Rute Jaringan"]},

    {"name": "Port Scanner",       "icon": "⚡", "genre": "Vuln Detection",   "category": "SECURITY", "status": "VULN DETECT",
     "bat": "../DAFFA_PROJECTS/BUKA_PORT_SCANNER.bat", "exe": "",
     "color": THEME["accent_amber"], "hotkeys": ["Deteksi Celah Keamanan Port Terbuka", "Cari Backdoor & Port Tersembunyi"]},

    {"name": "WiFi Detector",      "icon": "📡", "genre": "Intruder Alert",   "category": "SECURITY", "status": "INTRUDER ALERT",
     "bat": "../DAFFA_PROJECTS/BUKA_WIFI_DETECTOR.bat", "exe": "",
     "color": THEME["accent_red"], "hotkeys": ["Deteksi Penyusup di Jaringan WiFi", "Kelola Daftar Perangkat Dikenal"]},

    {"name": "GitHub Cloner",      "icon": "🐙", "genre": "Git Tools",        "category": "TOOLS",    "status": "GIT TUNNEL",
     "bat": "../DAFFA_PROJECTS/BUKA_GITHUB_CLONER.bat", "exe": "",
     "color": THEME["accent_purple"], "hotkeys": ["Unduh Repositori GitHub Berkecepatan Tinggi", "Membutuhkan Git"]},

    {"name": "Sherlock OSINT",     "icon": "🕵️", "genre": "OSINT Footprint", "category": "SECURITY", "status": "FOOTPRINT SCAN",
     "bat": "../DAFFA_PROJECTS/BUKA_SHERLOCK_OSINT.bat", "exe": "",
     "color": THEME["accent_amber"], "hotkeys": ["Lacak Jejak Digital Username", "Scan 300+ Platform Sosial Media"]},

    {"name": "Save Editor Universal","icon":"💾","genre": "Save Modding",     "category": "TOOLS",    "status": "SAVE MOD",
     "bat": "../DAFFA_PROJECTS/BUKA_SAVE_EDITOR.bat", "exe": "",
     "color": THEME["accent_emerald"], "hotkeys": ["Edit File Save JSON / TXT / DAT", "Manipulasi Nilai Variabel Game"]},

    {"name": "Auto Backup Tool",   "icon": "🔄", "genre": "Backup System",   "category": "TOOLS",    "status": "BACKUP",
     "bat": "../DAFFA_PROJECTS/BUKA_BACKUP_TOOL.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Pencadangan Otomatis Save Game", "Proteksi Korupsi File Real-Time"]},

    {"name": "Batch File Renamer", "icon": "📋", "genre": "File Manager",    "category": "TOOLS",    "status": "RENAME",
     "bat": "../DAFFA_PROJECTS/BUKA_BATCH_RENAMER.bat", "exe": "",
     "color": THEME["accent_purple"], "hotkeys": ["Ubah Nama File Massal Cepat", "Format Nomor Urut & Ekstensi"]},

    {"name": "Game Mod Installer", "icon": "🧩", "genre": "Mod Manager",     "category": "TOOLS",    "status": "MOD INSTALLER",
     "bat": "../DAFFA_PROJECTS/BUKA_MOD_INSTALLER.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Pasang Mod Otomatis ke Direktori Game", "Ekstraksi & Deployment ZIP Mod"]},

    {"name": "Integrity Checker",  "icon": "✅", "genre": "Hash Verifier",   "category": "TOOLS",    "status": "HASH CHECK",
     "bat": "../DAFFA_PROJECTS/BUKA_INTEGRITY_CHECKER.bat", "exe": "",
     "color": THEME["accent_emerald"], "hotkeys": ["Cek Kerusakan File Eksekusi", "Verifikasi Hash MD5 / SHA256"]},

    {"name": "Config Editor",      "icon": "⚙️", "genre": "Config Tweaker", "category": "TOOLS",    "status": "CONFIG",
     "bat": "../DAFFA_PROJECTS/BUKA_CONFIG_EDITOR.bat", "exe": "",
     "color": THEME["accent_amber"], "hotkeys": ["Ubah File INI / CFG / XML Game", "Tweak Pengaturan Grafis & Resolusi"]},

    {"name": "Auto Clicker",       "icon": "🖱️", "genre": "Macro Tool",     "category": "TOOLS",    "status": "MACRO",
     "bat": "../DAFFA_PROJECTS/BUKA_AUTO_CLICKER.bat", "exe": "",
     "color": THEME["accent_cyan"], "hotkeys": ["Klik Otomatis Berkecepatan Tinggi", "Interval Milidetik Kustom"]},

    {"name": "Hash Cracker",       "icon": "🔓", "genre": "Brute Force",     "category": "SECURITY", "status": "BRUTEFORCE",
     "bat": "../DAFFA_PROJECTS/BUKA_HASH_CRACKER.bat", "exe": "",
     "color": THEME["accent_red"], "hotkeys": ["Pecahkan Hash MD5 / NTLM / SHA1", "Akselerasi GPU Radeon RX 580"]},

    {"name": "Android & Termux",   "icon": "📱", "genre": "ADB Bridge",      "category": "TOOLS",    "status": "ADB BRIDGE",
     "bat": "../DAFFA_PROJECTS/BUKA_ANDROID_CONTROLLER.bat", "exe": "",
     "color": THEME["accent_emerald"], "hotkeys": ["Akses Shell Terminal Android Samsung A16", "Buka & Kontrol Termux Ubuntu Linux"]},
]


GAMES_LIST = [g for g in GAMES_DB if g.get("category") not in ("SECURITY", "TOOLS")]


# ==================== MODERN TOAST POPUP ====================
class ModernToast(ctk.CTkToplevel):
    def __init__(self, parent, message, color=THEME["accent_cyan"], duration=2600):
        super().__init__(parent)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(fg_color=THEME["bg_card"])

        # Border styling via outer frame
        frame = ctk.CTkFrame(
            self,
            fg_color=THEME["bg_card"],
            border_width=2,
            border_color=color,
            corner_radius=10
        )
        frame.pack(fill="both", expand=True, padx=2, pady=2)

        lbl = ctk.CTkLabel(
            frame,
            text=message,
            text_color=THEME["text_main"],
            font=("Consolas", 12, "bold"),
            padx=16,
            pady=10
        )
        lbl.pack()

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w = max(320, len(message) * 9 + 40)
        h = 52
        self.geometry(f"{w}x{h}+{sw - w - 24}+{sh - h - 60}")
        self.after(duration, self.destroy)

# ==================== MAIN APPLICATION CLASS ====================
class DaffaMasterApp(ctk.CTk):
    def show_toast(self, title, message="", color=THEME["accent_cyan"], duration=3000):
        try:
            full_msg = f"{title}\n{message}" if message else str(title)
            ModernToast(self, full_msg, color=color, duration=duration)
        except Exception:
            pass

    def __init__(self):
        super().__init__()

        self.title("⚔️ DAFFA MASTER COMMAND CENTER v6.0 ULTRA // STEAM & ROG ARMOURY EDITION")
        self.geometry("1400x880")
        self.minsize(1120, 700)
        self.configure(fg_color=THEME["bg_main"])

        # Set Official Among Us App Window Icon & Custom Cursor
        try:
            icon_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_icon.png")
            if os.path.exists(icon_p):
                from PIL import Image, ImageTk
                self._app_icon_photo = ImageTk.PhotoImage(Image.open(icon_p).resize((32, 32)))
                self.iconphoto(False, self._app_icon_photo)

            self._cur_arrow = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_arrow.cur").replace('\\', '/')
            self._cur_hand = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_hand.cur").replace('\\', '/')
            if os.path.exists(self._cur_arrow):
                self.config(cursor=f"@{self._cur_arrow}")
        except Exception:
            pass

        self.session_start   = time.time()
        self.active_tab      = "GAMES"
        self.running_exes    = set()
        self.card_widgets    = []
        self.indicator_labels= {}
        self.war_room_online = False

        # ── Fitur baru ────────────────────────────────────────
        self._fav_file    = os.path.join(os.path.dirname(__file__), "daffa_favorites.json")
        self._lp_file     = os.path.join(os.path.dirname(__file__), "daffa_lastplayed.json")
        self.favorites    = self._load_json(self._fav_file, [])
        self.last_played  = self._load_json(self._lp_file, {})   # {name: timestamp}
        self.sort_mode    = "default"   # "default" | "az" | "genre" | "recent"
        self.filter_cat   = "ALL"       # "ALL" | "MODS" | "TRAINER" | "CONSOLE" …
        self.proc_status  = {}          # {name: bool is_running}
        self._fav_btns    = {}          # {name: button_widget}
        self._cat_btns    = {}          # {cat: pill_widget}

        self.setup_ui()
        self.start_background_daemons()

    # ==================== HELPER: JSON PERSIST ====================
    def _load_json(self, path, default):
        try:
            if os.path.exists(path):
                import json
                return json.load(open(path, encoding="utf-8"))
        except Exception:
            pass
        return default

    def _save_json(self, path, data):
        import json
        try:
            json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ── FITUR 1: FAVORIT / PIN ────────────────────────────────
    def toggle_favorite(self, name: str, btn_widget=None):
        if name in self.favorites:
            self.favorites.remove(name)
            starred = False
        else:
            self.favorites.append(name)
            starred = True
        self._save_json(self._fav_file, self.favorites)
        if btn_widget:
            btn_widget.configure(text="⭐" if starred else "☆",
                                  text_color=THEME["accent_amber"] if starred else THEME["text_muted"])
        self._refresh_cards()

    # ── FITUR 2: CATEGORY FILTER ──────────────────────────────
    def set_filter_cat(self, cat: str):
        self.filter_cat = cat
        for c, btn in self._cat_btns.items():
            active = (c == cat)
            btn.configure(
                fg_color=THEME["accent_cyan"]   if active else "#1E293B",
                text_color=THEME["text_dark"]   if active else THEME["text_muted"]
            )
        self._refresh_cards()

    # ── FITUR 3: SORT ─────────────────────────────────────────
    def set_sort(self, mode: str):
        self.sort_mode = mode
        self._refresh_cards()

    def _apply_sort_filter(self, items):
        """Apply filter_cat + sort_mode to items list."""
        # Filter kategori
        if self.filter_cat != "ALL":
            items = [g for g in items if g.get("category","") == self.filter_cat]
        # Sort
        if self.sort_mode == "az":
            items = sorted(items, key=lambda g: g["name"].lower())
        elif self.sort_mode == "genre":
            items = sorted(items, key=lambda g: g.get("genre","").lower())
        elif self.sort_mode == "recent":
            items = sorted(items, key=lambda g: self.last_played.get(g["name"], 0), reverse=True)
        elif self.sort_mode == "fav":
            items = sorted(items, key=lambda g: (g["name"] not in self.favorites, g["name"].lower()))
        return items

    def _refresh_cards(self):
        """Re-render katalog dengan filter+sort aktif."""
        filtered = self._apply_sort_filter(list(GAMES_LIST))
        self.populate_cards(filtered)

    # ── FITUR 4: LAST PLAYED TRACK ────────────────────────────
    def _track_launch(self, name: str):
        self.last_played[name] = time.time()
        self._save_json(self._lp_file, self.last_played)

    def _last_played_str(self, name: str) -> str:
        ts = self.last_played.get(name, 0)
        if not ts:
            return "Belum pernah"
        delta = int(time.time() - ts)
        if delta < 60:
            return f"{delta}d lalu"
        elif delta < 3600:
            return f"{delta//60}m lalu"
        elif delta < 86400:
            return f"{delta//3600}j lalu"
        else:
            return f"{delta//86400}hr lalu"

    # ── FITUR 5: PROCESS MONITOR ──────────────────────────────
    def _process_monitor_loop(self):
        """Background thread: pantau proses game yg sedang running."""
        import psutil
        while True:
            try:
                running_names = {p.name().lower() for p in psutil.process_iter(["name"])}
                self.current_running_names = running_names
                for item in GAMES_LIST:
                    exe = item.get("exe", "")
                    if not exe:
                        continue
                    proc_name = os.path.basename(exe).lower()
                    is_run = proc_name in running_names
                    old    = self.proc_status.get(item["name"])
                    if is_run != old:
                        self.proc_status[item["name"]] = is_run
                        # Update dot colour
                        lbl = self.indicator_labels.get(item["name"])
                        if lbl:
                            try:
                                lbl.configure(
                                    text_color=THEME["accent_emerald"] if is_run else "#4B5563"
                                )
                            except Exception:
                                pass
            except Exception:
                pass
            time.sleep(5)

    # ── FITUR 6: KEYBOARD SHORTCUT GUIDE POPUP ────────────────
    def show_hotkey_guide(self, item: dict):
        """Popup daftar lengkap hotkey untuk satu game."""
        win = ctk.CTkToplevel(self)
        win.title(f"⌨️ Hotkey — {item['name']}")
        win.geometry("380x400")
        win.attributes("-topmost", True)
        win.configure(fg_color=THEME["bg_panel"])

        ctk.CTkLabel(win, text=f"⌨️ {item['name']}",
                     font=("Consolas", 13, "bold"),
                     text_color=item.get("color", THEME["accent_cyan"])
                     ).pack(padx=16, pady=(14, 4))
        ctk.CTkLabel(win, text="Hotkey Cheat Reference",
                     font=("Consolas", 9), text_color=THEME["text_muted"]
                     ).pack(padx=16, pady=(0, 10))

        scroll = ctk.CTkScrollableFrame(win, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        hotkeys = item.get("hotkeys", [])
        if isinstance(hotkeys, dict):
            pairs = list(hotkeys.items())
        elif isinstance(hotkeys, list):
            pairs = [(h, "") for h in hotkeys]
        else:
            pairs = []

        if not pairs:
            ctk.CTkLabel(scroll, text="Tidak ada hotkey terdaftar.",
                         font=("Consolas", 10), text_color=THEME["text_muted"]
                         ).pack(pady=20)
        for hk, desc in pairs:
            row = ctk.CTkFrame(scroll, fg_color="#0D1520", corner_radius=6)
            row.pack(fill="x", pady=3)
            ctk.CTkLabel(row, text=hk,
                         font=("Consolas", 10, "bold"),
                         text_color=THEME["accent_cyan"], width=90, anchor="w"
                         ).pack(side="left", padx=(10, 6), pady=6)
            ctk.CTkLabel(row, text=desc or "—",
                         font=("Consolas", 10),
                         text_color=THEME["text_main"], anchor="w"
                         ).pack(side="left", fill="x", expand=True, padx=(0, 10), pady=6)

        ctk.CTkButton(win, text="TUTUP", width=120, height=28,
                      font=("Consolas", 10, "bold"),
                      fg_color=THEME["accent_cyan"], text_color=THEME["text_dark"],
                      hover_color=THEME["accent_cyan_hover"],
                      command=win.destroy).pack(pady=(0, 12))

    # ==================== BUILD UI LAYOUT ====================
    def setup_ui(self):
        # 1. TOP HEADER HUD
        self.header_frame = ctk.CTkFrame(
            self,
            fg_color=THEME["bg_panel"],
            corner_radius=0,
            height=72,
            border_width=1,
            border_color=THEME["border"]
        )
        self.header_frame.pack(fill="x", side="top")
        self.setup_header()

        # 2. MAIN CONTAINER (SIDEBAR + CONTENT + COMMAND CENTER)
        self.body_container = ctk.CTkFrame(self, fg_color="transparent")
        self.body_container.pack(fill="both", expand=True, padx=12, pady=(10, 8))

        # 2A. LEFT NAVIGATION SIDEBAR
        self.sidebar = ctk.CTkFrame(
            self.body_container,
            width=230,
            fg_color=THEME["bg_panel"],
            corner_radius=12,
            border_width=1,
            border_color=THEME["border"]
        )
        self.sidebar.pack(side="left", fill="y", padx=(0, 10))
        self.sidebar.pack_propagate(False)
        self.setup_sidebar()

        # 2B. CENTER CONTENT PANEL (GAME & TOOL ROSTER)
        self.center_panel = ctk.CTkFrame(
            self.body_container,
            fg_color=THEME["bg_panel"],
            corner_radius=12,
            border_width=1,
            border_color=THEME["border"]
        )
        self.center_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.setup_center_panel()

        # 2C. RIGHT COMMAND CENTER PANEL
        self.cmd_panel = ctk.CTkFrame(
            self.body_container,
            width=330,
            fg_color=THEME["bg_panel"],
            corner_radius=12,
            border_width=1,
            border_color=THEME["border"]
        )
        self.cmd_panel.pack(side="right", fill="y")
        self.cmd_panel.pack_propagate(False)
        self.setup_command_panel()

        # 3. BOTTOM STATUS BAR
        self.bottom_bar = ctk.CTkFrame(
            self,
            fg_color=THEME["bg_panel"],
            corner_radius=0,
            height=54,
            border_width=1,
            border_color=THEME["border"]
        )
        self.bottom_bar.pack(fill="x", side="bottom")
        self.setup_bottom_bar()

    # ==================== TOP HEADER ====================
    def setup_header(self):
        # Left branding
        brand_box = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        brand_box.pack(side="left", padx=16, pady=10)

        # Official Among Us Avatar Mascot (Ground Truth dari Komandan DAFFA)
        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_header.png")
            if os.path.exists(icon_path):
                from PIL import Image
                self._header_mascot_img = ctk.CTkImage(
                    light_image=Image.open(icon_path),
                    dark_image=Image.open(icon_path),
                    size=(36, 36)
                )
                cur_h = getattr(self, "_cur_hand", "hand2")
                self.mascot_lbl = ctk.CTkLabel(brand_box, text="", image=self._header_mascot_img, cursor=f"@{cur_h}" if os.path.exists(cur_h) else "hand2")
                self.mascot_lbl.pack(side="left", padx=(0, 10))
                self.mascot_lbl.bind("<Button-1>", lambda e: self._on_mascot_click())
        except Exception:
            pass

        title = ctk.CTkLabel(
            brand_box,
            text="⚔️ DAFFA MASTER",
            font=("Consolas", 18, "bold"),
            text_color=THEME["accent_cyan"]
        )
        title.pack(side="left", padx=(0, 8))

        ver_pill = ctk.CTkLabel(
            brand_box,
            text="v6.0 ULTRA // GITHUB EDITION",
            font=("Consolas", 10, "bold"),
            fg_color="#00354D",
            text_color=THEME["accent_cyan"],
            corner_radius=6,
            padx=8,
            pady=2
        )
        ver_pill.pack(side="left")

        # Center Search Box
        search_box = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        search_box.pack(side="left", expand=True, fill="x", padx=30)

        self.search_entry = ctk.CTkEntry(
            search_box,
            placeholder_text="🔍 Ketik untuk cari game, mod, atau tools...",
            font=("Consolas", 12),
            height=36,
            fg_color=THEME["bg_card"],
            border_color=THEME["border"],
            border_width=1,
            corner_radius=8
        )
        self.search_entry.pack(fill="x")
        self.search_entry.bind("<KeyRelease>", self.on_search_query)

        # Right Telemetry HUD
        self.hud_box = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.hud_box.pack(side="right", padx=16)

        # CPU Metric Pill
        self.cpu_pill = ctk.CTkLabel(
            self.hud_box,
            text="⚡ CPU: --%",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["bg_card"],
            text_color=THEME["accent_emerald"],
            corner_radius=6,
            padx=10,
            pady=4
        )
        self.cpu_pill.pack(side="left", padx=4)

        # RAM Metric Pill
        self.ram_pill = ctk.CTkLabel(
            self.hud_box,
            text="💾 RAM: --%",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["bg_card"],
            text_color=THEME["accent_cyan"],
            corner_radius=6,
            padx=10,
            pady=4
        )
        self.ram_pill.pack(side="left", padx=4)

        # Disk D Metric Pill
        self.disk_pill = ctk.CTkLabel(
            self.hud_box,
            text="💿 D: --GB",
            font=("Consolas", 11, "bold"),
            fg_color=THEME["bg_card"],
            text_color=THEME["text_muted"],
            corner_radius=6,
            padx=10,
            pady=4
        )
        self.disk_pill.pack(side="left", padx=4)

        # War Room Pill
        self.war_room_pill = ctk.CTkButton(
            self.hud_box,
            text="⚔️ WAR ROOM",
            font=("Consolas", 11, "bold"),
            fg_color="#00354D",
            hover_color="#004D70",
            text_color=THEME["accent_cyan"],
            corner_radius=6,
            width=110,
            height=28,
            command=self.open_war_room_browser
        )
        self.war_room_pill.pack(side="left", padx=4)

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
        self.theme_pill.pack(side="left", padx=4)

        # GitHub Cloud Portal Button
        self.github_portal_pill = ctk.CTkButton(
            self.hud_box,
            text="☁️ GITHUB PORTAL",
            font=("Consolas", 11, "bold"),
            fg_color="#064E3B",
            hover_color="#047857",
            text_color="#34D399",
            corner_radius=6,
            width=130,
            height=28,
            command=self.open_github_cloud_portal
        )
        self.github_portal_pill.pack(side="left", padx=4)

        # 1-Click Cloud Save Backup Button
        self.cloud_save_pill = ctk.CTkButton(
            self.hud_box,
            text="💾 CLOUD SAVE",
            font=("Consolas", 11, "bold"),
            fg_color="#3B0764",
            hover_color="#581C87",
            text_color="#F472B6",
            corner_radius=6,
            width=115,
            height=28,
            command=self.trigger_cloud_save_backup
        )
        self.cloud_save_pill.pack(side="left", padx=4)

    def open_github_cloud_portal(self):
        """Membuka Web Command Portal & Repository GitHub Komandan Daffa."""
        import webbrowser
        webbrowser.open("https://zordanjimbak0-art.github.io/daffa-master-astra/portal.html")
        self.show_toast("☁️ GITHUB CLOUD PORTAL", "Membuka Astra Web Command Portal (zordanjimbak0-art)...", duration=2500)

    def trigger_cloud_save_backup(self):
        """Sinkronisasi otomatis Save Game ke Private GitHub Vault di background."""
        self.show_toast("💾 CLOUD SAVE VAULT", "Mengamankan seluruh Save Game ke Private GitHub Vault...", duration=2500)
        def _sync():
            try:
                bat_p = r"D:\Game\DAFFA_SYSTEM\BACKUP_SAVEGAME_KE_CLOUD.bat"
                vault_dir = r"D:\Game\DAFFA_SAVE_VAULT"
                if os.path.exists(vault_dir):
                    subprocess.run(["git", "add", "."], cwd=vault_dir, creationflags=0x08000000)
                    subprocess.run(["git", "commit", "-m", "backup: auto sync from Daffa Master GUI"], cwd=vault_dir, creationflags=0x08000000)
                    subprocess.run(["git", "push", "origin", "main"], cwd=vault_dir, creationflags=0x08000000)
                self.after(100, lambda: self.show_toast("✅ CLOUD BACKUP SUKSES", "Save Game aman di github.com/zordanjimbak0-art/daffa-savegame-vault!", duration=3000))
            except Exception as e:
                self.after(100, lambda: self.show_toast("⚠️ CLOUD SYNC INFO", f"Status: {e}", duration=2500))
        threading.Thread(target=_sync, daemon=True).start()


    def _on_mascot_click(self):
        """Easter Egg saat avatar Among Us diklik."""
        import winsound
        try:
            winsound.Beep(880, 70)
            winsound.Beep(1175, 120)
        except Exception:
            pass
        self.show_toast("🚨 CREWMATE SECURE", "Komandan DAFFA terverifikasi 100% INNOCENT! ASTRA AI aktif.", duration=2500)

    # ==================== LEFT SIDEBAR ====================
    def setup_sidebar(self):
        # User profile block
        profile_frame = ctk.CTkFrame(self.sidebar, fg_color=THEME["bg_card"], corner_radius=10)
        profile_frame.pack(fill="x", padx=10, pady=(12, 16))

        user_lbl = ctk.CTkLabel(
            profile_frame,
            text="👑 KOMANDAN DAFFA",
            font=("Consolas", 12, "bold"),
            text_color=THEME["text_main"]
        )
        user_lbl.pack(anchor="w", padx=12, pady=(8, 2))

        status_lbl = ctk.CTkLabel(
            profile_frame,
            text="● SYSTEM ARMED & SECURE",
            font=("Consolas", 9, "bold"),
            text_color=THEME["accent_emerald"]
        )
        status_lbl.pack(anchor="w", padx=12, pady=(0, 8))

        # Navigation Category Buttons
        nav_label = ctk.CTkLabel(
            self.sidebar,
            text="NAVIGASI KATALOG",
            font=("Consolas", 10, "bold"),
            text_color=THEME["text_muted"]
        )
        nav_label.pack(anchor="w", padx=14, pady=(4, 6))

        self.nav_buttons = {}
        tabs = [
            ("GAMES", f"🎮 Semua Game ({len(GAMES_LIST)})", self.show_all_games),
            ("MODS", f"⚡ Mod & Cheats ({len([g for g in GAMES_LIST if 'MOD' in g.get('status', '') or 'TABLE' in g.get('status', '') or 'TRAINER' in g.get('status', '') or 'CONSOLE' in g.get('status', '')])})", self.show_modded_games),
            ("SECURITY", f"🛡️ Cyber & Pentest ({len([g for g in GAMES_DB if g.get('category') == 'SECURITY'])})", self.show_security_tools),
            ("TOOLS", f"🛠️ System Utilities ({len([g for g in GAMES_DB if g.get('category') == 'TOOLS'])})", self.show_system_tools),
        ]

        for key, label, cmd in tabs:
            btn = ctk.CTkButton(
                self.sidebar,
                text=label,
                font=("Consolas", 11, "bold"),
                anchor="w",
                fg_color="transparent",
                hover_color=THEME["bg_card"],
                text_color=THEME["text_main"],
                corner_radius=8,
                height=38,
                command=cmd
            )
            btn.pack(fill="x", padx=10, pady=3)
            self.nav_buttons[key] = btn

        self.highlight_nav_tab("GAMES")

        # Separator
        sep = ctk.CTkFrame(self.sidebar, height=1, fg_color=THEME["border"])
        sep.pack(fill="x", padx=10, pady=16)

        # Quick Mission Direct Actions
        act_label = ctk.CTkLabel(
            self.sidebar,
            text="AKSI CEPAT TAKTIS",
            font=("Consolas", 10, "bold"),
            text_color=THEME["text_muted"]
        )
        act_label.pack(anchor="w", padx=14, pady=(0, 6))

        quick_actions = [
            ("⚔️ AI War Room (9090)", THEME["accent_cyan"], self.open_war_room_browser),
            ("💻 VS Code + MCP Suite", THEME["accent_purple"], self.run_vscode_mcp),
            ("🚨 Panic Button (EAC)", THEME["accent_red"], self.run_panic),
            ("🧹 Optimalisasi PC", THEME["accent_amber"], self.run_optimize),
            ("🔄 Restart Launcher", THEME["text_muted"], self.restart_gui)
        ]

        for text, col, action in quick_actions:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                font=("Consolas", 10, "bold"),
                anchor="w",
                fg_color=THEME["bg_card"],
                hover_color=THEME["bg_card_hover"],
                text_color=col,
                corner_radius=6,
                height=32,
                command=action
            )
            btn.pack(fill="x", padx=10, pady=3)

        # Official Among Us Banner at bottom of sidebar (Innersloth Asset)
        try:
            banner_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_official", "banner_logo.png")
            if os.path.exists(banner_p):
                from PIL import Image
                im_banner = Image.open(banner_p)
                bw = 190
                bh = int(im_banner.height * bw / im_banner.width)
                self._sidebar_banner_img = ctk.CTkImage(
                    light_image=im_banner,
                    dark_image=im_banner,
                    size=(bw, bh)
                )
                b_lbl = ctk.CTkLabel(self.sidebar, text="", image=self._sidebar_banner_img)
                b_lbl.pack(side="bottom", pady=(0, 16))
        except Exception:
            pass

    def highlight_nav_tab(self, tab_key):
        self.active_tab = tab_key
        for key, btn in self.nav_buttons.items():
            if key == tab_key:
                btn.configure(fg_color="#00354D", text_color=THEME["accent_cyan"])
            else:
                btn.configure(fg_color="transparent", text_color=THEME["text_main"])

    # ==================== CENTER PANEL (v6.0 STEAM / ROG HERO EDITION) ====================
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

    def _get_cover_image(self, item: dict, size=(112, 58), is_hero=False):
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
        cov_img = self._get_cover_image(item, size=(112, 58), is_hero=False)
        if cov_img:
            cov_lbl = ctk.CTkLabel(body, text="", image=cov_img, width=112, height=58, corner_radius=8)
        else:
            cov_lbl = ctk.CTkLabel(body, text=icon, font=("Segoe UI Emoji", 24), width=112, height=58,
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

        disp_name = item["name"] if len(item["name"]) <= 18 else item["name"][:17] + "…"
        title_lbl = ctk.CTkLabel(
            r1, text=disp_name,
            font=("Consolas", 11, "bold"),
            text_color=THEME["text_main"], anchor="w"
        )
        title_lbl.pack(side="left", fill="x", expand=True)
        title_lbl.bind("<Button-1>", lambda e, it=item: self.select_hero_item(it))

        disp_status = item.get("status", "READY")
        if len(disp_status) > 14:
            disp_status = disp_status[:13] + "…"
        badge_pill = ctk.CTkLabel(
            r1,
            text=disp_status,
            font=("Consolas", 8, "bold"),
            fg_color="#071324",
            text_color=color,
            corner_radius=5, padx=5, pady=1
        )
        badge_pill.pack(side="right", padx=(2, 0))

        # Row 2: Genre + Hotkey Snippet
        r2 = ctk.CTkFrame(right_box, fg_color="transparent")
        r2.pack(fill="x", pady=(2, 4))

        hotkeys = item.get("hotkeys", [])
        snippet_txt = hotkeys[0] if isinstance(hotkeys, list) and hotkeys else (
            list(hotkeys.keys())[0] if isinstance(hotkeys, dict) and hotkeys else genre
        )
        sub_txt = f"{genre} • {snippet_txt}" if genre else snippet_txt
        if len(sub_txt) > 30:
            sub_txt = sub_txt[:28] + ".."

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

    # ==================== RIGHT COMMAND CENTER ====================
    def setup_command_panel(self):
        # Header
        top_bar = ctk.CTkFrame(self.cmd_panel, fg_color="transparent")
        top_bar.pack(fill="x", padx=12, pady=(12, 6))

        title = ctk.CTkLabel(
            top_bar,
            text="⚡ COMMAND CENTER",
            font=("Consolas", 12, "bold"),
            text_color=THEME["accent_cyan"]
        )
        title.pack(side="left")

        # Scrollable container for all commands
        self.cmd_scroll = ctk.CTkScrollableFrame(
            self.cmd_panel,
            fg_color="transparent",
            corner_radius=8
        )
        self.cmd_scroll.pack(fill="both", expand=True, padx=8, pady=(0, 6))

        # Helper to add section headers
        def add_category_header(label):
            hdr = ctk.CTkLabel(
                self.cmd_scroll,
                text=label,
                font=("Consolas", 10, "bold"),
                text_color=THEME["text_muted"],
                anchor="w"
            )
            hdr.pack(fill="x", padx=6, pady=(10, 4))

        def add_action_button(text, fg_col, hover_col, text_col, cmd):
            btn = ctk.CTkButton(
                self.cmd_scroll,
                text=text,
                font=("Consolas", 10, "bold"),
                anchor="w",
                fg_color=fg_col,
                hover_color=hover_col,
                text_color=text_col,
                corner_radius=6,
                height=30,
                command=cmd
            )
            btn.pack(fill="x", padx=4, pady=2)
            return btn

        # 🌌 SECTION 1: ASTRA AI & HARNESS
        add_category_header("🌌 [ ASTRA AI & HARNESS ]")
        add_action_button("⚔️ Multi-Agent War Room (9090)", "#002B4D", "#004073", THEME["accent_cyan"], self.open_war_room_browser)
        add_action_button("🚀 1-Klik Semua Astra AI", "#002B36", "#004254", THEME["accent_emerald"], self.run_all_in_one)
        add_action_button("💻 VS Code + MCP Suite", "#231545", "#352069", THEME["accent_purple"], self.run_vscode_mcp)
        add_action_button("⚡ Unlimited Tokens (Local LLM)", "#003314", "#004D1F", THEME["accent_emerald"], self.run_token_booster)
        add_action_button("🎨 Adobe Illustrator Bridge", "#330033", "#4D004D", "#FF77E9", self.run_illustrator_bridge)
        add_action_button("🧊 Blender 3D Engine Bridge", "#331A00", "#4D2800", THEME["accent_amber"], self.run_blender_bridge)

        # 🎮 SECTION 2: MODS & SAVE EDITORS
        add_category_header("🎮 [ MODS & SAVE EDITORS ]")
        add_action_button("🦁 My Voice Zoo Mod Menu", "#06283D", "#0B3C5D", THEME["accent_cyan"], self.run_myvoicezoo_mod_menu)
        add_action_button("🚪 That's Not My Neighbor Menu", "#331500", "#4D2000", THEME["accent_amber"], self.run_tmnm_mod_menu)
        add_action_button("⚔️ Blasphemous 1 Mod Menu", "#330000", "#4D0000", THEME["accent_red"], self.run_blasphemous_mod_menu)
        add_action_button("⚔️ Blasphemous 2 Mod Menu", "#3D0008", "#59000C", THEME["accent_red"], self.run_blasphemous2_mod_menu)
        add_action_button("☠️ Isaac Repentance Menu", "#260A3D", "#3B105E", THEME["accent_purple"], self.run_isaac_mod_menu)
        add_action_button("❄️ Subnautica BZ Mod Menu", "#002B4D", "#004073", THEME["accent_cyan"], self.run_subnautica_bz_mod_menu)
        add_action_button("🌊 Subnautica 1 Mod Menu", "#003344", "#004D66", THEME["accent_cyan"], self.run_subnautica1_mod_menu)
        add_action_button("🪐 Savage Planet Mod Menu", "#332200", "#4D3300", THEME["accent_gold"], self.run_savage_planet_mod_menu)
        add_action_button("⚔️ Soulmask Mod Menu", "#2A1A00", "#402800", THEME["accent_amber"], self.run_soulmask_mod_menu)
        add_action_button("⛏️ Minecraft Dungeons Menu", "#0D2B0D", "#1A3D1A", THEME["accent_emerald"], self.run_mcdungeons_mod_menu)
        add_action_button("⚔️ Terraria Mod Menu", "#1A0D33", "#261A4D", THEME["accent_purple"], self.run_terraria_mod_menu)
        add_action_button("👦 Upin Ipin Mod Menu", "#33220D", "#4D3314", THEME["accent_amber"], self.run_upinipin_mod_menu)
        add_action_button("🧽 SpongeBob Mod Menu", "#001A33", "#00264D", THEME["accent_cyan"], self.run_spongebob_mod_menu)
        add_action_button("⚔️ Metal Slug Attack Reloaded", "#2B1000", "#401800", THEME["accent_amber"], self.run_metalslug_mod_menu)
        add_action_button("❄️ Snowed.Under Mod Menu", "#050A14", "#0A1428", THEME["accent_cyan"], self.run_snowedunder_mod_menu)
        add_action_button("🌊 Subnautica 2 Mod Menu", "#040E18", "#081828", THEME["accent_cyan"], self.run_subnautica2_mod_menu)
        add_category_header("🎮 [ SAVE PATCHERS ]")
        add_action_button("👑 Kingdom Rush SERIES Patcher", "#14050A", "#200A14", THEME["accent_purple"], self.run_kingdomrush_mod_menu)
        add_action_button("🌿 Plants vs Zombies Mod Menu", "#0A1400", "#142000", THEME["accent_emerald"], self.run_pvz_mod_menu)
        add_action_button("🎮 DREDGE Mod Menu", "#0A0A14", "#14142A", THEME["accent_purple"], self.run_dredge_mod_menu)
        add_action_button("⚰️ Graveyard Keeper 2 Menu", "#060A06", "#0D140D", THEME["accent_emerald"], self.run_gk2_mod_menu)
        add_action_button("🧟 Project Zomboid Mod Menu", "#0A0800", "#141200", THEME["accent_amber"], self.run_projectzomboid_mod_menu)
        add_action_button("🍬 Bloons TD 5 Mod Menu", "#000A14", "#001428", THEME["accent_cyan"], self.run_bloons_mod_menu)
        add_category_header("🎮 [ CLASSIC SHOOTERS ]")
        add_action_button("🔫 Serious Sam 2 Mod Menu", "#14000A", "#200014", THEME["accent_red"], self.run_ss2_mod_menu)
        add_action_button("🔫 Serious Sam TFE Mod Menu", "#0A0005", "#140010", THEME["accent_purple"], self.run_sstfe_mod_menu)
        add_action_button("💀 Quake Remastered Menu", "#0F0500", "#1A0800", THEME["accent_red"], self.run_quake_mod_menu)
        add_action_button("📬 Postal 2 Mod Menu", "#0A000A", "#140014", THEME["accent_purple"], self.run_postal2_mod_menu)
        add_category_header("🎮 [ NARUTO & ANIME ]")
        add_action_button("🍥 Naruto UNS4 Mod Menu", "#140A00", "#200F00", THEME["accent_amber"], self.run_naruto_uns4_mod_menu)
        add_action_button("🍥 Naruto UNS Revolution", "#140A00", "#200F00", THEME["accent_amber"], self.run_naruto_unsr_mod_menu)
        add_action_button("🚨 PANIC BUTTON (EAC Safe)", "#4D0000", "#730000", THEME["accent_red"], self.run_panic)
        add_action_button("🚨 EMERGENCY MEETING (Among Us)", "#550000", "#880000", THEME["accent_red"], self.trigger_emergency_meeting)
        add_action_button("⚡ MINIGAME: FIX WIRES (Among Us)", "#1E1B4B", "#312E81", "#818CF8", self.run_fix_wires_minigame)
        add_action_button("🔄 Deploy Cheats (n8n Sync)", "#003300", "#004D00", THEME["accent_emerald"], self.run_sync)
        add_action_button("💾 Backup Save Game", "#002E1C", "#00452A", THEME["accent_emerald"], self.run_backup)
        add_action_button("💰 Upin Ipin Save Editor", "#332200", "#4D3300", THEME["accent_amber"], self.run_upin_editor)
        add_action_button("🧽 SpongeBob Save Editor", "#332200", "#4D3300", THEME["accent_amber"], self.run_spongebob_editor)


        # ⚡ SECTION 3: HARDWARE & BOOSTERS
        add_category_header("⚡ [ HARDWARE & TUNING ]")
        add_action_button("⚡ Blur Auto Clicker (3.9.6)", "#201235", "#301B50", "#B388FF", self.run_blur_autoclicker)
        add_action_button("🍪 Cookie Clicker God Mode", "#332200", "#4D3300", "#F59E0B", self.run_cookie_master)
        add_action_button("🎮 60% Virtual Trainer Pad", "#162035", "#233352", "#00E5FF", self.run_trainer_pad)
        add_action_button("🧊 VRAM Governor (RX 580)", "#002B4D", "#004073", "#00E5FF", self.run_vram_governor)
        add_action_button("📱 Samsung A16 ADB Bridge", "#004D26", "#006633", "#10B981", self.run_adb_companion)
        add_action_button("🧪 MedBay Scan Diagnostics", "#0D2B1F", "#14402E", "#10B981", self.run_medbay_scan)
        add_action_button("🚀 FPS Booster (0.5ms Timer)", "#003300", "#004D00", THEME["accent_emerald"], self.run_booster)
        add_action_button("⚡ Ping Booster (Net Tuning)", "#001A33", "#00264D", THEME["accent_cyan"], self.run_ping_booster)
        add_action_button("🛠️ AMD RX 580 Tuning", "#4D0000", "#730000", THEME["accent_red"], self.run_rx580_tuning)
        add_action_button("🌿 AMD Eco Mode Profile", "#002E1C", "#00452A", THEME["accent_emerald"], self.run_eco_mode)
        add_action_button("🛡️ Registry Gaming Tweak Fix", "#26154D", "#3B2073", THEME["accent_purple"], self.run_registry_fix)
        add_action_button("👁️ Nyalakan HUD Overlay", "#12124D", "#1C1C73", THEME["accent_cyan"], self.run_hud)
        add_action_button("❌ Matikan HUD Overlay", "#3D0000", "#5C0000", THEME["accent_red"], self.kill_hud)

        # 🛡️ SECTION 4: SECURITY & SANDBOX
        add_category_header("🛡️ [ SECURITY & SANDBOX ]")
        add_action_button("🎯 Metasploit Console (MSF)", "#3D0A0A", "#5C0F0F", THEME["accent_red"], self.run_msfconsole)
        add_action_button("🛡️ Windows Sandbox (Isolasi)", "#2E1F00", "#452E00", THEME["accent_amber"], self.run_sandbox)
        add_action_button("🐧 Linux Sandbox (Terminal)", "#0D2B1F", "#14402E", THEME["accent_emerald"], self.run_linux_sandbox)
        add_action_button("📸 Mata Bionik (Live Camera)", "#002B36", "#004254", THEME["accent_cyan"], self.run_camera)
        add_action_button("🏴‍☠️ SteamUnlocked Launcher", "#3D0000", "#5C0000", THEME["accent_red"], self.run_steamunlocked)

        # 📊 SECTION 5: LIVE LOGS
        add_category_header("📊 [ LOG AKTIVITAS SISTEM ]")
        self.log_box = ctk.CTkTextbox(
            self.cmd_scroll,
            height=120,
            fg_color="#050811",
            text_color=THEME["accent_emerald"],
            font=("Consolas", 9),
            corner_radius=6,
            border_width=1,
            border_color=THEME["border"]
        )
        self.log_box.pack(fill="x", padx=4, pady=(2, 10))
        self.log("Daffa Master v5.0 Ultimate Siap.")
        self.log(f"{len(GAMES_DB)} Game & Tools Terdaftar.")

    # ==================== BOTTOM STATUS BAR ====================
    def setup_bottom_bar(self):
        import tkinter as tk

        self.status_lbl = ctk.CTkLabel(
            self.bottom_bar,
            text=f"🎮 {len(GAMES_LIST)} Games | 🛡️ {len([g for g in GAMES_DB if g.get('category') == 'SECURITY'])} Tools | 👑 Komandan DAFFA (ASTRA AI)",
            font=("Consolas", 10),
            text_color=THEME["text_muted"]
        )
        self.status_lbl.pack(side="left", padx=16, pady=16)

        self.session_timer_lbl = ctk.CTkLabel(
            self.bottom_bar,
            text="⏱️ Sesi: 00:00:00",
            font=("Consolas", 10, "bold"),
            text_color=THEME["accent_cyan"]
        )
        self.session_timer_lbl.pack(side="right", padx=16, pady=16)

        # ── AMONG US WALKING CHARACTERS (AUTHENTIC VECTOR SPRITES) ──
        self._setup_among_us()

    def _setup_among_us(self):
        """
        Among Us Crewmates berjalan di bottom bar dengan nama kustom & interaktif:
        - ZordanJimbak (Daffa), Naswa, Salim, Roby, Jibral
        - Interaktif: Klik untuk bicara, animasi loncat, dan SFX
        - Background match 100% THEME['bg_panel'] (zero kotak hitam)
        - Ukuran diperbesar ke TARGET_H=34 (size 28x34)
        """
        import tkinter as tk
        from PIL import Image, ImageTk

        BAR_BG = THEME["bg_panel"]
        CANVAS_W = 100
        CANVAS_H = 50
        SPRITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among_us_sprites")

        # Config: (color_key, display_name, name_color, quote, sfx_freq, speed, start_x)
        CREWMATES_CONFIG = [
            ("RED",    "ZordanJimbak", "#EF4444", "👑 Daffa (ZordanJimbak): 'Siap Komandan! Semua sistem aman & siap tempur!'", (1200, 900), 1.4,  510),
            ("CYAN",   "Naswa",        "#00E5FF", "✨ Naswa: 'Semangat Komandan Daffa! Tugas & riset grafika hari ini lancar jaya ya!'", (659, 880), 2.0,  660),
            ("GREEN",  "Salim",        "#10B981", "🛡️ Salim: 'Pertahanan siber & security tools aktif, siap audit target!'", (440, 659), 1.8,  810),
            ("PURPLE", "Roby",         "#A78BFA", "🎮 Roby: 'Gas mabar sekarang Komandan! Cheat engine & mod menu standby!'", (523, 784), 1.2,  960),
            ("YELLOW", "Jibral",       "#F59E0B", "⚡ Jibral: 'Speed boost aktif, 0ms latency, CPU 0.8% tanpa lag!'", (880, 1320), 2.2, 1110),
        ]

        self._au_crewmates = []

        cur_h = getattr(self, "_cur_hand", "hand2")
        cursor_spec = f"@{cur_h}" if os.path.exists(cur_h) else "hand2"

        for color_key, display_name, name_col, quote, sfx, speed, start_x in CREWMATES_CONFIG:
            imgs = {}
            for fr in range(8):
                for d_val, d_str in [(1, 'right'), (-1, 'left')]:
                    fn = os.path.join(SPRITE_DIR, f"{color_key}_{fr}_{d_str}.png")
                    if os.path.exists(fn):
                        imgs[(fr, d_val)] = ImageTk.PhotoImage(Image.open(fn))

            if not imgs:
                continue

            canvas = tk.Canvas(
                self.bottom_bar,
                width=CANVAS_W, height=CANVAS_H,
                bg=BAR_BG,
                highlightthickness=0, bd=0,
                cursor=cursor_spec
            )
            canvas.place(x=start_x, y=2)

            # Name tag above head (drop shadow + colored text)
            shadow_id = canvas.create_text(51, 6, text=display_name, font=("Consolas", 8, "bold"), fill="#000000")
            txt_id = canvas.create_text(50, 5, text=display_name, font=("Consolas", 8, "bold"), fill=name_col)

            # Sprite image centered below name (width ~29, canvas 100 -> x=35, y=12)
            img_id = canvas.create_image(35, 12, anchor="nw", image=imgs.get((0, 1)))

            # Mini Crewmate Pet Companion untuk ZordanJimbak (Komandan DAFFA)
            mini_id = None
            mini_imgs = {}
            if color_key == "RED":
                mini_r = os.path.join(SPRITE_DIR, "MINI_right.png")
                mini_l = os.path.join(SPRITE_DIR, "MINI_left.png")
                if os.path.exists(mini_r) and os.path.exists(mini_l):
                    try:
                        mini_imgs[1] = ImageTk.PhotoImage(Image.open(mini_r))
                        mini_imgs[-1] = ImageTk.PhotoImage(Image.open(mini_l))
                        mini_id = canvas.create_image(12, 26, anchor="nw", image=mini_imgs.get(1))
                    except Exception:
                        pass

            state = {
                "canvas": canvas,
                "img_id": img_id,
                "txt_id": txt_id,
                "shadow_id": shadow_id,
                "imgs":   imgs,
                "mini_id": mini_id,
                "mini_imgs": mini_imgs,
                "x":      float(start_x),
                "dir":    1,
                "frame":  0,
                "speed":  speed,
                "width":  CANVAS_W,
                "name":   display_name,
                "name_col": name_col,
                "quote":  quote,
                "sfx":    sfx,
            }

            # Interaksi Click & Hover
            canvas.bind("<Button-1>", lambda e, s=state: self._on_crewmate_click(s))
            canvas.bind("<Enter>", lambda e, s=state: canvas.itemconfig(s["txt_id"], fill="#FFFFFF"))
            canvas.bind("<Leave>", lambda e, s=state: canvas.itemconfig(s["txt_id"], fill=s["name_col"]))

            self._au_crewmates.append(state)

        self._animate_crewmates()

    def _on_crewmate_click(self, st):
        """Interaksi saat crewmate diklik: animasi lompat + SFX + quote dialog toast."""
        import winsound
        name = st["name"]
        quote = st["quote"]
        sfx = st["sfx"]

        # 1. SFX Audio
        try:
            jump_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio", "among_us_jump.wav")
            if os.path.exists(jump_p):
                winsound.PlaySound(jump_p, winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                winsound.Beep(sfx[0], 70)
                winsound.Beep(sfx[1], 110)
        except Exception:
            pass

        # 2. Bounce animation (melompat ke atas)
        c = st["canvas"]
        spr_id = st["img_id"]
        txt_id = st["txt_id"]
        shadow_id = st["shadow_id"]
        try:
            c.move(spr_id, 0, -8)
            c.move(txt_id, 0, -8)
            c.move(shadow_id, 0, -8)
            if st.get("mini_id"):
                c.move(st["mini_id"], 0, -8)
            self.after(140, lambda: [
                c.move(spr_id, 0, 8),
                c.move(txt_id, 0, 8),
                c.move(shadow_id, 0, 8),
                c.move(st["mini_id"], 0, 8) if st.get("mini_id") else None
            ])
        except Exception:
            pass

        # 3. Speech bubble toggle on name tag
        try:
            c.itemconfig(txt_id, text=f"💬 {name}", fill="#FFFFFF")
            self.after(2200, lambda: c.itemconfig(txt_id, text=name, fill=st["name_col"]))
        except Exception:
            pass

        # 4. Toast Notification
        self.show_toast(f"CREWMATE: {name.upper()}", quote, duration=3500)
        self.log(f"💬 Interaksi: {name} merespons Komandan.")

    def _animate_crewmates(self):
        """Animasi semua crewmate — gerak + 8-frame walk cycle 0% CPU overhead."""
        try:
            if self.state() == "iconic":
                self.after(1000, self._animate_crewmates)
                return
            bar_w = self.bottom_bar.winfo_width()
        except Exception:
            bar_w = 1400

        MIN_X = 500
        MAX_X = max(MIN_X + 100, bar_w - 230)

        for st in self._au_crewmates:
            if not st["canvas"].winfo_exists():
                continue

            st["x"] += st["speed"] * st["dir"]

            mx = max(MIN_X, MAX_X - st["width"])
            if st["x"] >= mx:
                st["x"]  = mx
                st["dir"] = -1
            elif st["x"] <= MIN_X:
                st["x"]  = MIN_X
                st["dir"] = 1

            st["canvas"].place(x=int(st["x"]), y=2)
            st["frame"] = (st["frame"] + 1) % 8
            img = st["imgs"].get((st["frame"], st["dir"]))
            if img:
                st["canvas"].itemconfig(st["img_id"], image=img)

            # Animate mini crewmate pet companion if present
            if st.get("mini_id") and st.get("mini_imgs"):
                mini_hop = -2 if (st["frame"] in [1, 5]) else (1 if (st["frame"] in [3, 7]) else 0)
                mini_x = 10 if st["dir"] == 1 else 66
                st["canvas"].coords(st["mini_id"], mini_x, 26 + mini_hop)
                mini_img = st["mini_imgs"].get(st["dir"])
                if mini_img:
                    st["canvas"].itemconfig(st["mini_id"], image=mini_img)

        self.after(90, self._animate_crewmates)


    # ==================== FILTERING & SEARCH ====================
    def show_all_games(self):
        self.highlight_nav_tab("GAMES")
        self.section_title.configure(text=f"🎮 KATALOG SEMUA GAME ({len(GAMES_LIST)})")
        self.populate_cards(GAMES_LIST)

    def show_modded_games(self):
        self.highlight_nav_tab("MODS")
        self.section_title.configure(text="⚡ GAME DENGAN MOD & CHEATS")
        items = [g for g in GAMES_LIST if "MOD" in g.get("status", "") or "TABLE" in g.get("status", "") or "TRAINER" in g.get("status", "") or "CONSOLE" in g.get("status", "")]
        self.populate_cards(items)

    def show_security_tools(self):
        self.highlight_nav_tab("SECURITY")
        self.section_title.configure(text="🛡️ CYBER RECON & PENTEST LAB")
        items = [g for g in GAMES_DB if g.get("category") == "SECURITY"]
        self.populate_cards(items)

    def show_system_tools(self):
        self.highlight_nav_tab("TOOLS")
        self.section_title.configure(text="🛠️ SYSTEM UTILITIES & EDITORS")
        items = [g for g in GAMES_DB if g.get("category") == "TOOLS"]
        self.populate_cards(items)

    def on_search_query(self, event=None):
        if hasattr(self, "_search_debounce_id") and self._search_debounce_id:
            try:
                self.after_cancel(self._search_debounce_id)
            except Exception:
                pass
        self._search_debounce_id = self.after(220, self._do_search_query)

    def _do_search_query(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            # Revert to current tab filter
            if self.active_tab == "GAMES": self.show_all_games()
            elif self.active_tab == "MODS": self.show_modded_games()
            elif self.active_tab == "SECURITY": self.show_security_tools()
            elif self.active_tab == "TOOLS": self.show_system_tools()
            return

        def _match_hotkeys(hks):
            if isinstance(hks, dict):
                return any(query in str(k).lower() or query in str(v).lower() for k, v in hks.items())
            elif isinstance(hks, (list, tuple)):
                return any(query in str(hk).lower() for hk in hks)
            return False

        filtered = [
            g for g in GAMES_DB
            if query in g["name"].lower()
            or query in g.get("status", "").lower()
            or query in g.get("genre", "").lower()
            or _match_hotkeys(g.get("hotkeys", []))
        ]
        self.section_title.configure(text=f"🔍 HASIL PENCARIAN: '{query}'")
        self.populate_cards(filtered)

    # ==================== HOTKEYS POPUP ====================
    def show_hotkey_dialog(self, item):
        dlg = ctk.CTkToplevel(self)
        dlg.title(f"Petunjuk: {item['name']}")
        dlg.geometry("460x380")
        dlg.attributes("-topmost", True)
        dlg.configure(fg_color=THEME["bg_panel"])

        box = ctk.CTkFrame(dlg, fg_color=THEME["bg_card"], corner_radius=10)
        box.pack(fill="both", expand=True, padx=14, pady=14)

        title = ctk.CTkLabel(
            box,
            text=f"🎮 {item['name']}",
            font=("Consolas", 14, "bold"),
            text_color=item.get("color", THEME["accent_cyan"])
        )
        title.pack(anchor="w", padx=16, pady=(14, 2))

        status_lbl = ctk.CTkLabel(
            box,
            text=f"Status: {item.get('status', 'Ready')}",
            font=("Consolas", 10),
            text_color=THEME["text_muted"]
        )
        status_lbl.pack(anchor="w", padx=16, pady=(0, 10))

        sep = ctk.CTkFrame(box, height=1, fg_color=THEME["border"])
        sep.pack(fill="x", padx=14, pady=4)

        hdr = ctk.CTkLabel(
            box,
            text="DAFTAR HOTKEY / PETUNJUK CHEAT:",
            font=("Consolas", 11, "bold"),
            text_color=THEME["text_main"]
        )
        hdr.pack(anchor="w", padx=16, pady=(8, 6))

        scroll = ctk.CTkScrollableFrame(box, fg_color="transparent", height=160)
        scroll.pack(fill="both", expand=True, padx=14, pady=(0, 10))

        hotkeys = item.get("hotkeys", [])
        if isinstance(hotkeys, dict):
            items_list = [f"{k} = {v}" for k, v in hotkeys.items()]
        else:
            items_list = list(hotkeys)

        for hk in items_list:
            line = ctk.CTkLabel(
                scroll,
                text=f"▸ {hk}",
                font=("Consolas", 10),
                text_color=THEME["accent_cyan"],
                anchor="w",
                justify="left"
            )
            line.pack(fill="x", pady=2)

        close_btn = ctk.CTkButton(
            box,
            text="TUTUP",
            font=("Consolas", 11, "bold"),
            fg_color="#1E293B",
            hover_color="#334155",
            text_color=THEME["text_main"],
            height=32,
            command=dlg.destroy
        )
        close_btn.pack(fill="x", padx=14, pady=(0, 12))
        self.log(f"Buka info cheat: {item['name']}")

    # ==================== LAUNCH LOGIC ====================
    def _find_mod_menu(self, game_folder: str) -> str | None:
        """
        Cari file *MOD_MENU*.py / *MOD*.py dengan strategi multi-level:
        1. Folder game langsung
        2. Parent level 1 (SteamRIP root)
        3. Parent level 2 (Games root)
        4. Subfolder rekursif dari game_folder
        """
        import glob
        patterns = ["*MOD_MENU*.py", "*FUSION_MOD*.py", "*MOD*.py", "*TRAINER*.py"]

        # Level 0: folder game langsung
        for pat in patterns:
            hits = [h for h in glob.glob(os.path.join(game_folder, pat)) if "__pycache__" not in h]
            if hits: return hits[0]

        # Level 1: parent langsung (untuk EXE dalam subfolder Game/Game/Game.exe)
        parent1 = os.path.dirname(game_folder)
        for pat in patterns:
            hits = [h for h in glob.glob(os.path.join(parent1, pat)) if "__pycache__" not in h]
            if hits: return hits[0]

        # Level 2: grandparent (untuk EXE sangat dalam seperti a/b/c/game.exe)
        parent2 = os.path.dirname(parent1)
        for pat in patterns:
            hits = [h for h in glob.glob(os.path.join(parent2, pat)) if "__pycache__" not in h]
            if hits: return hits[0]

        # Fallback: scan rekursif dari game_folder
        for pat in patterns:
            hits = [h for h in glob.glob(os.path.join(game_folder, "**", pat), recursive=True) if "__pycache__" not in h]
            if hits: return hits[0]

        return None

    def _auto_inject_mod_menu(self, game_folder: str, game_name: str, color: str) -> bool:
        """
        Auto-inject: launch mod menu Python secara aman.
        Return True jika mod menu ditemukan & diluncurkan.
        """
        menu = self._find_mod_menu(game_folder)
        if menu:
            import psutil, shutil
            menu_basename = os.path.basename(menu)
            already = False
            try:
                for p in psutil.process_iter(["cmdline"]):
                    try:
                        cmd = p.info.get("cmdline")
                        if cmd and menu_basename.lower() in " ".join(cmd).lower():
                            already = True
                            break
                    except Exception:
                        pass
            except Exception:
                pass

            if not already:
                py_bin = shutil.which("pythonw") or sys.executable
                # cmd /c start → pythonw dapat desktop session GUI penuh
                # (tanpa ini: pythonw crash di win32gui BitBlt / screen grab)
                subprocess.Popen(
                    f'cmd /c start "" "{py_bin}" "{menu}"',
                    cwd=os.path.dirname(menu),
                    shell=True
                )
                self.after(0, lambda: self.log(f"[AUTO INJECT] {menu_basename} aktif untuk {game_name}"))
                self.after(0, lambda: ModernToast(self, f"⚡ CHEAT INJECTED: {game_name}", color))
            else:
                self.after(0, lambda: self.log(f"[AUTO INJECT] {menu_basename} sudah running, skip duplikat"))
            return True
        return False

    def launch_item(self, item):
        """
        N8N-STYLE LAUNCH PIPELINE:
        1. Resolve EXE → prioritas field 'exe' (absolute) dulu, fallback ke 'bat' (relative)
        2. Validasi file exists → error informatif jika tidak ada
        3. Launch GAME langsung via subprocess (non-blocking)
        4. Setelah 1.5s → inject mod menu di background (pythonw)
        Urutan ini memastikan GAME SELALU BUKA DULU, mod menu menyusul.
        """
        name  = item["name"]
        color = item.get("color", THEME["accent_cyan"])

        # ── Track last played ──────────────────────────────────
        self._track_launch(name)

        # ── Albion Online EAC warning ──────────────────────────
        if name == "Albion Online":
            if not messagebox.askyesno(
                "PERINGATAN RESMI",
                "Albion Online dilindungi Easy Anti-Cheat (EAC).\n"
                "Dilarang menyuntikkan memory/cheat agar tidak terbanned!\n\n"
                "Lanjutkan buka game resmi?"
            ):
                return

        # ══════════════════════════════════════════════════════
        # STEP 1 — Resolve target file
        # Prioritas: BAT launcher resmi (membungkus game + cheat) → EXE absolut / relative
        # ══════════════════════════════════════════════════════
        exe_abs = item.get("exe", "").strip()
        bat_rel = item.get("bat", "").strip()

        full_path   = ""
        launch_mode = "bat"  # "exe" atau "bat"

        # 1. Coba BAT launcher dulu (karena BAT membungkus game + mod menu/cheat)
        if bat_rel:
            if bat_rel.startswith("../"):
                resolved = os.path.normpath(
                    os.path.join(r"D:\Game\DAFFA_SYSTEM", bat_rel))
            else:
                resolved = os.path.join(r"D:\Game\Games", bat_rel)

            if os.path.isfile(resolved):
                full_path   = resolved
                launch_mode = "bat"

        # 2. Jika BAT tidak ada / tidak dispesifikasi, coba EXE
        if not full_path and exe_abs:
            if os.path.isabs(exe_abs) and os.path.isfile(exe_abs):
                full_path   = exe_abs
                launch_mode = "exe"
            elif bat_rel:
                # Coba cari nama EXE di folder bat_rel
                bat_dir = os.path.dirname(os.path.join(r"D:\Game\Games", bat_rel))
                candidate = os.path.join(bat_dir, exe_abs)
                if os.path.isfile(candidate):
                    full_path   = candidate
                    launch_mode = "exe"
                else:
                    # Scan rekursif di folder game untuk file exe tersebut
                    for root, dirs, files in os.walk(bat_dir):
                        for f in files:
                            if f.lower() == exe_abs.lower():
                                full_path   = os.path.join(root, f)
                                launch_mode = "exe"
                                break
                        if full_path:
                            break

        if not full_path:
            self.log(f"GAGAL: Launcher/EXE tidak ditemukan untuk → {name}")
            messagebox.showerror(
                "File Game Tidak Ditemukan",
                f"Tidak dapat menemukan launcher atau EXE untuk:\n{name}\n\n"
                f"BAT: {bat_rel}\n"
                f"EXE: {exe_abs}\n\n"
                "Pastikan game dan launcher sudah terpasang di D:\\Game\\Games"
            )
            return

        # ══════════════════════════════════════════════════════
        # STEP 2 — Tentukan game_folder untuk mod menu search
        # ══════════════════════════════════════════════════════
        game_folder = os.path.dirname(full_path)
        # Untuk EXE dalam subfolder game (mis. Blasphemous/Blasphemous/Blasphemous.exe)
        # mod menu biasanya ada di parent SteamRIP folder
        # _find_mod_menu sudah handle scan parent otomatis

        # ══════════════════════════════════════════════════════
        # STEP 3 — Launch GAME LANGSUNG (tidak perlu menunggu mod menu)
        # ══════════════════════════════════════════════════════
        if launch_mode == "exe":
            subprocess.Popen(
                f'start "" "{full_path}"',
                shell=True, cwd=game_folder
            )
        else:
            subprocess.Popen(
                f'start "" "{full_path}"',
                shell=True, cwd=game_folder
            )

        self.log(f"[LAUNCH] {name} → {os.path.basename(full_path)}")

        # ══════════════════════════════════════════════════════
        # STEP 4 — Inject mod menu SETELAH 1.5s (non-blocking)
        # ══════════════════════════════════════════════════════
        def _delayed_inject():
            time.sleep(1.5)
            self._auto_inject_mod_menu(game_folder, name, color)

        threading.Thread(target=_delayed_inject, daemon=True).start()

        ModernToast(self, f"🚀 {name} diluncurkan!", color)

    def open_item_folder(self, item):
        # Resolve folder dari exe (absolute) atau bat (relative)
        exe_abs = item.get("exe", "").strip()
        bat_rel = item.get("bat", "").strip()

        folder = ""
        if exe_abs:
            folder = os.path.dirname(exe_abs)
            # Naik ke parent SteamRIP jika EXE ada dalam subfolder dalam
            if not os.path.exists(folder):
                folder = ""
        if not folder and bat_rel:
            if bat_rel.startswith("../"):
                full_path = os.path.normpath(os.path.join(r"D:\Game\DAFFA_SYSTEM", bat_rel))
            else:
                full_path = os.path.join(r"D:\Game\Games", bat_rel)
            folder = os.path.dirname(full_path)

        if folder and os.path.exists(folder):
            self.log(f"Buka folder: {folder}")
            subprocess.Popen(f'explorer "{folder}"', shell=True)
            ModernToast(self, f"📁 Folder {item['name']} dibuka!")
        else:
            messagebox.showerror("Error", f"Folder tidak ditemukan:\n{folder}")

    # ==================== COMMAND HANDLERS ====================
    def open_war_room_browser(self):
        self.log("Buka Multi-Agent War Room di Browser...")
        url = "http://localhost:9090"
        # Check if server is running, if not start it
        try:
            urllib.request.urlopen(url, timeout=1)
        except Exception:
            srv = r"D:\Game\DAFFA_PROJECTS\Astra_AI_War_Room\server.py"
            if os.path.exists(srv):
                subprocess.Popen(["python", srv], cwd=r"D:\Game\DAFFA_PROJECTS\Astra_AI_War_Room")
                time.sleep(1)
        webbrowser.open(url)
        ModernToast(self, "⚔️ AI War Room Aktif (Port 9090)!")

    def run_vscode_mcp(self):
        self.log("Buka Visual Studio Code dengan ASTRA MCP Suite...")
        s = r"C:\Users\USER\Desktop\BUKA_VSCODE_DENGAN_MCP.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "💻 VS Code + MCP Suite Terbuka!", THEME["accent_purple"])
        else:
            messagebox.showerror("Error", "Script VS Code MCP tidak ditemukan!")

    def run_msfconsole(self):
        self.log("Buka Metasploit Framework Console...")
        s = r"C:\Users\USER\Desktop\BUKA_MSFCONSOLE.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🎯 Metasploit Console Dibuka!", THEME["accent_red"])
        else:
            messagebox.showerror("Error", "Script Metasploit tidak ditemukan!")

    def run_all_in_one(self):
        self.log("1-Klik Jalankan Semua Sub-Sistem Astra AI...")
        s = r"D:\Game\DAFFA_PROJECTS\1_KLIK_JALANKAN_SEMUA_ASTRA_AI.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🚀 Semua Sistem Astra AI Aktif!", THEME["accent_emerald"])

    def run_token_booster(self):
        self.log("Buka Unlimited Token Booster (Ollama)...")
        s = r"D:\Game\DAFFA_PROJECTS\BUKA_UNLIMITED_TOKENS.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "⚡ Token Booster Aktif!", THEME["accent_emerald"])

    def run_illustrator_bridge(self):
        self.log("Buka Adobe Illustrator Live Bridge...")
        s = r"D:\Game\DAFFA_PROJECTS\BUKA_ILLUSTRATOR_BRIDGE.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🎨 Illustrator Bridge Aktif!", "#FF77E9")

    def run_blender_bridge(self):
        self.log("Buka Blender 3D Engine Bridge...")
        s = r"D:\Game\DAFFA_PROJECTS\blender_bridge.py"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /k "python \"{s}\""', shell=True)
            ModernToast(self, "🧊 Blender 3D Engine Aktif!", THEME["accent_amber"])

    def run_panic(self):
        self.log("PANIC BUTTON aktif! Membersihkan memori & cheat...")
        s = r"D:\Game\DAFFA_MASTER_CHEATS_ARCHIVE\PANIC_CLEANUP.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🚨 Memori Dibersihkan!", THEME["accent_red"])

    def trigger_emergency_meeting(self):
        """Memicu modal darurat EMERGENCY MEETING ala Among Us."""
        import winsound
        from PIL import Image

        self.log("🚨 [EMERGENCY MEETING] Dipanggil oleh Komandan DAFFA!")

        # Play siren sound
        siren_wav = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio", "among_us_emergency.wav")
        if os.path.exists(siren_wav):
            try:
                winsound.PlaySound(siren_wav, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception:
                pass

        dlg = ctk.CTkToplevel(self)
        dlg.title("🚨 EMERGENCY MEETING // ASTRA AI")
        dlg.geometry("520x430")
        dlg.attributes("-topmost", True)
        dlg.configure(fg_color="#0A0E17")

        sw = dlg.winfo_screenwidth()
        sh = dlg.winfo_screenheight()
        dlg.geometry(f"520x430+{(sw-520)//2}+{(sh-430)//2}")

        outer = ctk.CTkFrame(
            dlg,
            fg_color="#0A0E17",
            border_width=2,
            border_color="#EF4444",
            corner_radius=12
        )
        outer.pack(fill="both", expand=True, padx=4, pady=4)

        # Emergency icon
        em_icon_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "among-us-assets", "Tasks", "emergencyButton_MiraBase-sharedassets0.assets-185.png")
        if os.path.exists(em_icon_p):
            try:
                im_em = Image.open(em_icon_p).convert("RGBA").resize((72, 72), Image.Resampling.LANCZOS)
                dlg._em_img = ctk.CTkImage(light_image=im_em, dark_image=im_em, size=(72, 72))
                ctk.CTkLabel(outer, text="", image=dlg._em_img).pack(pady=(16, 4))
            except Exception:
                ctk.CTkLabel(outer, text="🚨", font=("Consolas", 32)).pack(pady=(16, 4))
        else:
            ctk.CTkLabel(outer, text="🚨", font=("Consolas", 32)).pack(pady=(16, 4))

        ctk.CTkLabel(outer, text="EMERGENCY MEETING!", font=("Consolas", 20, "bold"), text_color="#EF4444").pack(pady=(2, 2))
        ctk.CTkLabel(outer, text="Komandan DAFFA memanggil protokol darurat Kru Antariksa:", font=("Consolas", 10), text_color="#94A3B8").pack(pady=(0, 14))

        def do_panic_kill():
            dlg.destroy()
            self.run_panic()

        def do_boost_ram():
            dlg.destroy()
            self.run_optimize()

        def do_restart():
            dlg.destroy()
            self.restart_gui()

        btn_frame = ctk.CTkFrame(outer, fg_color="transparent")
        btn_frame.pack(fill="x", padx=30)

        ctk.CTkButton(
            btn_frame,
            text="💀 PANIC KILL ALL GAME PROCESSES",
            font=("Consolas", 12, "bold"),
            fg_color="#660000",
            hover_color="#990000",
            text_color="#FFFFFF",
            height=38,
            command=do_panic_kill
        ).pack(fill="x", pady=4)

        ctk.CTkButton(
            btn_frame,
            text="⚡ PURGE RAM & MAX CPU BOOST",
            font=("Consolas", 12, "bold"),
            fg_color="#004D26",
            hover_color="#006633",
            text_color="#10B981",
            height=38,
            command=do_boost_ram
        ).pack(fill="x", pady=4)

        ctk.CTkButton(
            btn_frame,
            text="🔄 RESTART DAFFA MASTER",
            font=("Consolas", 12, "bold"),
            fg_color="#00354D",
            hover_color="#004C6D",
            text_color="#00E5FF",
            height=38,
            command=do_restart
        ).pack(fill="x", pady=4)

        ctk.CTkButton(
            btn_frame,
            text="❌ BATAL / KEMBALI",
            font=("Consolas", 11),
            fg_color="#1E293B",
            hover_color="#334155",
            text_color="#94A3B8",
            height=32,
            command=dlg.destroy
        ).pack(fill="x", pady=(8, 12))

    def run_fix_wires_minigame(self):
        """Membuka minigame interaktif Fix Wires Among Us."""
        self.log("⚡ Membuka Minigame Electrical: Fix Wires...")

        def on_completed():
            self.log("🎉 [TASK COMPLETED] Kabel tersambung 100%! Menjalankan auto-optimasi sistem...")
            self.run_optimize()
            ModernToast(self, "⚡ TASK COMPLETED! Daya Pulih & Sistem Dioptimasi!", THEME["accent_emerald"])

        modal = FixWiresModal(self, on_complete=on_completed)

    def run_sync(self):
        self.log("Deploying Cheats & Sync...")
        s = r"D:\Game\DAFFA_MASTER_CHEATS_ARCHIVE\SYNC_DEPLOY_CHEATS.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🔄 Mod Synchronized!", THEME["accent_emerald"])

    def run_backup(self):
        self.log("Memulai backup save game...")
        s = r"D:\Game\DAFFA_MASTER_CHEATS_ARCHIVE\AUTO_SAVE_BACKUP.py"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /c "python \"{s}\""', shell=True)
            ModernToast(self, "💾 Backup Save Berjalan!", THEME["accent_emerald"])

    def run_upin_editor(self):
        self.log("Buka Upin Ipin Save Editor...")
        s = r"D:\Game\DAFFA_SYSTEM\UPIN_IPIN_SAVE_EDITOR.py"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /c "python \"{s}\""', shell=True)
            ModernToast(self, "💰 Upin Ipin Save Editor Terbuka!", THEME["accent_amber"])

    def run_spongebob_editor(self):
        self.log("Buka SpongeBob Save Editor...")
        s = r"D:\Game\DAFFA_SYSTEM\SPONGEBOB_SAVE_EDITOR.py"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /c "python \"{s}\""', shell=True)
            ModernToast(self, "🧽 SpongeBob Save Editor Terbuka!", THEME["accent_amber"])

    def run_subnautica_bz_mod_menu(self):
        self.log("Buka Subnautica Below Zero Mod Menu...")
        s = r"D:\Game\Games\Subnautica-Below-Zero-SteamRIP.com\SUBNAUTICA_BELOW_ZERO_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "❄️ Subnautica BZ Mod Menu Aktif!", THEME["accent_cyan"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_savage_planet_mod_menu(self):
        self.log("Buka Journey to the Savage Planet Mod Menu...")
        s = r"D:\Game\Games\Journey to the Savage Planet\SAVAGE_PLANET_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "🪐 Savage Planet Mod Menu Aktif!", THEME["accent_amber"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_subnautica1_mod_menu(self):
        self.log("Buka Subnautica 1 Mod Menu...")
        s = r"D:\Game\Games\Subnautica\SUBNAUTICA_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "🌊 Subnautica 1 Mod Menu Aktif!", THEME["accent_cyan"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_terraria_mod_menu(self):
        self.log("Buka Terraria Mod Menu...")
        s = r"D:\Game\Games\Terraria\TERRARIA_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "⚔️ Terraria Mod Menu Aktif!", THEME["accent_purple"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_soulmask_mod_menu(self):
        self.log("Buka Soulmask Mod Menu...")
        s = r"D:\Game\Games\Soulmask\SOULMASK_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "⚔️ Soulmask Mod Menu Aktif!", THEME["accent_amber"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_mcdungeons_mod_menu(self):
        self.log("Buka Minecraft Dungeons Mod Menu...")
        s = r"D:\Game\Games\Minecraft Dungeons\MINECRAFT_DUNGEONS_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "⛏️ MC Dungeons Mod Menu Aktif!", THEME["accent_emerald"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_upinipin_mod_menu(self):
        self.log("Buka Upin Ipin Mod Menu...")
        s = r"D:\Game\Games\Upin Ipin\UPIN_IPIN_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "👦 Upin Ipin Mod Menu Aktif!", THEME["accent_amber"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def run_spongebob_mod_menu(self):
        self.log("Buka SpongeBob Mod Menu...")
        s = r"D:\Game\Games\SpongeBob\SPONGEBOB_MOD_MENU.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s], cwd=os.path.dirname(s))
            ModernToast(self, "🧽 SpongeBob Mod Menu Aktif!", THEME["accent_cyan"])
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{s}")

    def _launch_menu(self, path: str, label: str, color: str):
        """Generic launcher untuk semua mod menu Python (CREATE_NEW_CONSOLE fix)."""
        if os.path.exists(path):
            import shutil
            py_bin = shutil.which("pythonw") or sys.executable
            subprocess.Popen(
                [py_bin, path],
                cwd=os.path.dirname(path),
                creationflags=subprocess.CREATE_NEW_CONSOLE,
            )
            ModernToast(self, f"{label} Aktif!", color)
        else:
            messagebox.showerror("Error", f"Mod Menu tidak ditemukan:\n{path}")

    def run_myvoicezoo_mod_menu(self):
        self.log("Buka My Voice Zoo Mod Menu...")
        self._launch_menu(r"D:\Game\Games\MyVoiceZoo-SteamRIP.com\MYVOICEZOO_MOD_MENU.py", "🦁 My Voice Zoo", THEME["accent_cyan"])

    def run_tmnm_mod_menu(self):
        self.log("Buka That's Not My Neighbor Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Thats-Not-My-Neighbor-SteamRIP.com\TMNM_MOD_MENU.py", "🚪 That's Not My Neighbor", THEME["accent_amber"])

    def run_blasphemous_mod_menu(self):
        self.log("Buka Blasphemous Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Blasphemous-SteamRIP.com\BLASPHEMOUS_MOD_MENU.py", "⚔️ Blasphemous", THEME["accent_red"])

    def run_blasphemous2_mod_menu(self):
        self.log("Buka Blasphemous 2 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Blasphemous-2-SteamRIP.com\BLASPHEMOUS2_MOD_MENU.py", "⚔️ Blasphemous 2", THEME["accent_red"])

    def run_isaac_mod_menu(self):
        self.log("Buka Isaac Mod Menu...")
        self._launch_menu(r"D:\Game\Games\The.Binding.of.Isaac-Repentance-SteamRIP.com\ISAAC_MOD_MENU.py", "☠️ Isaac", THEME["accent_purple"])

    def run_metalslug_mod_menu(self):
        self.log("Buka Metal Slug Attack Reloaded Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Metal Slug Attack Reloaded\METAL_SLUG_MOD_MENU.py", "⚔️ Metal Slug", THEME["accent_amber"])

    def run_snowedunder_mod_menu(self):
        self.log("Buka Snowed.Under Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Snowed.Under\SNOWED_UNDER_MOD_MENU.py", "❄️ Snowed.Under", THEME["accent_cyan"])

    def run_subnautica2_mod_menu(self):
        self.log("Buka Subnautica 2 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Subnautica 2\SUBNAUTICA2_MOD_MENU.py", "🌊 Subnautica 2", THEME["accent_cyan"])

    def run_kingdomrush_mod_menu(self):
        self.log("Buka Kingdom Rush Series Save Patcher...")
        self._launch_menu(r"D:\Game\Games\Kingdom Rush Vengeance\KINGDOM_RUSH_MOD_MENU.py", "👑 Kingdom Rush", THEME["accent_purple"])

    def run_pvz_mod_menu(self):
        self.log("Buka Plants vs Zombies Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Plants vs Zombies GOTY\PLANTS_VS_ZOMBIES_MOD_MENU.py", "🌿 PvZ", THEME["accent_emerald"])

    def run_dredge_mod_menu(self):
        self.log("Buka DREDGE Mod Menu...")
        self._launch_menu(r"D:\Game\Games\DREDGE-SteamRIP.com\DREDGE_MOD_MENU.py", "🎮 DREDGE", THEME["accent_purple"])

    def run_gk2_mod_menu(self):
        self.log("Buka Graveyard Keeper 2 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Graveyard Keeper 2\GRAVEYARD_KEEPER2_MOD_MENU.py", "⚰️ GK2", THEME["accent_emerald"])

    def run_projectzomboid_mod_menu(self):
        self.log("Buka Project Zomboid Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Project Zomboid\PROJECT_ZOMBOID_MOD_MENU.py", "🧟 Project Zomboid", THEME["accent_amber"])

    def run_bloons_mod_menu(self):
        self.log("Buka Bloons TD 5 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Bloons TD 5\BLOONS_TD5_MOD_MENU.py", "🍬 Bloons TD5", THEME["accent_cyan"])

    def run_ss2_mod_menu(self):
        self.log("Buka Serious Sam 2 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Serious Sam 2\SERIOUS_SAM2_MOD_MENU.py", "🔫 Serious Sam 2", THEME["accent_red"])

    def run_sstfe_mod_menu(self):
        self.log("Buka Serious Sam TFE Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Serious Sam The First Encounter\SERIOUS_SAM_TFE_MOD_MENU.py", "🔫 SS-TFE", THEME["accent_purple"])

    def run_quake_mod_menu(self):
        self.log("Buka Quake Remastered Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Quake\QUAKE_MOD_MENU.py", "💀 Quake", THEME["accent_red"])

    def run_postal2_mod_menu(self):
        self.log("Buka Postal 2 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Postal 2\POSTAL2_MOD_MENU.py", "📬 Postal 2", THEME["accent_purple"])

    def run_naruto_uns4_mod_menu(self):
        self.log("Buka Naruto UNS4 Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Naruto Shippuden UNS4\NARUTO_UNS4_MOD_MENU.py", "🍥 Naruto UNS4", THEME["accent_amber"])

    def run_naruto_unsr_mod_menu(self):
        self.log("Buka Naruto UNS Revolution Mod Menu...")
        self._launch_menu(r"D:\Game\Games\Naruto Shippuden UNS Revolution\NARUTO_UNS_REVOLUTION_MOD_MENU.py", "🍥 Naruto UNSR", THEME["accent_amber"])

    def run_blur_autoclicker(self):
        self.log("Membuka Blur Auto Clicker (High Precision)...")
        p = os.path.expandvars(r"%LocalAppData%\BlurAutoClicker\BlurAutoClicker.exe")
        if os.path.exists(p):
            subprocess.Popen([p])
            ModernToast(self, "⚡ Blur Auto Clicker Aktif!", "#B388FF")
        else:
            messagebox.showerror("Error", f"Blur Auto Clicker tidak ditemukan:\n{p}")

    def run_cookie_master(self):
        self.log("Membuka Daffa Cookie Clicker God Mode...")
        self._launch_menu(r"D:\Game\DAFFA_SYSTEM\Daffa_Cookie_Master.py", "🍪 Cookie Clicker Master", THEME["accent_amber"])

    def run_trainer_pad(self):
        self.log("Membuka 60% Virtual Trainer Pad...")
        self._launch_menu(r"D:\Game\DAFFA_SYSTEM\Daffa_Trainer_Pad.py", "🎮 60% Trainer Pad", THEME["accent_cyan"])

    def run_vram_governor(self):
        self.log("Membuka AMD RX 580 VRAM Governor...")
        self._launch_menu(r"D:\Game\DAFFA_SYSTEM\Daffa_VRAM_Governor.py", "🧊 VRAM Governor", THEME["accent_cyan"])

    def run_adb_companion(self):
        self.log("Membuka Samsung Galaxy A16 ADB Bridge...")
        self._launch_menu(r"D:\Game\DAFFA_SYSTEM\Daffa_ADB_Companion.py", "📱 Samsung A16 Bridge", THEME["accent_emerald"])

    def run_medbay_scan(self):
        self.log("Membuka Among Us MedBay Scan Diagnostics...")
        self._launch_menu(r"D:\Game\DAFFA_SYSTEM\Daffa_MedBay_Scan.py", "🧪 MedBay Scanner", THEME["accent_emerald"])

    def run_booster(self):

        self.log("FPS Booster: Mengoptimalkan prioritas proses game...")
        try:
            boosted = 0
            for game in GAMES_LIST:
                exe = game.get('exe', '')
                if exe:
                    r = subprocess.run(f'wmic process where name="{exe}" CALL setpriority 128',
                                       shell=True, capture_output=True, text=True, timeout=5)
                    if 'ReturnValue = 0' in r.stdout:
                        boosted += 1
            subprocess.run('powershell -Command "[System.GC]::Collect()"', shell=True, capture_output=True, timeout=5)
            self.log(f"FPS Boost selesai! {boosted} proses dinaikkan ke High Priority.")
            ModernToast(self, f"🚀 FPS Boost: {boosted} proses dioptimalkan!", THEME["accent_emerald"])
        except Exception as e:
            self.log(f"Booster error: {e}")

    def run_ping_booster(self):
        self.log("Memulai Ping Booster...")
        s = r"D:\Game\DAFFA_PROJECTS\BUKA_PING_BOOSTER.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /c "{s}"', shell=True)
            ModernToast(self, "⚡ Ping Booster Terbuka!", THEME["accent_cyan"])

    def run_rx580_tuning(self):
        self.log("Menjalankan AMD RX 580 Tuning Profile...")
        s = r"D:\Game\DAFFA_SYSTEM\AMD_RX580_TUNING.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🛠️ RX 580 Tuning Diaktifkan!", THEME["accent_red"])

    def run_eco_mode(self):
        self.log("Mengaktifkan AMD Eco Mode Profile...")
        s = r"D:\Game\DAFFA_SYSTEM\AMD_ECO_MODE.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🌿 AMD Eco Mode Diaktifkan!", THEME["accent_emerald"])

    def run_registry_fix(self):
        self.log("Menerapkan Registry Gaming Fix...")
        s = r"D:\Game\DAFFA_SYSTEM\REGISTRY_GAMING_FIX.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🛡️ Registry Gaming Fix Diterapkan!", THEME["accent_purple"])

    def run_hud(self):
        self.log("HUD Overlay diaktifkan!")
        s = r"D:\Game\DAFFA_SYSTEM\Daffa_HUD_Overlay.py"
        if os.path.exists(s):
            subprocess.Popen(['pythonw', s])
            ModernToast(self, "👁️ HUD Overlay Muncul!", THEME["accent_cyan"])

    def kill_hud(self):
        subprocess.run('taskkill /F /IM pythonw.exe /FI "WINDOWTITLE eq Daffa HUD*"', shell=True, capture_output=True)
        self.log("Perintah kill HUD Overlay dikirim.")
        ModernToast(self, "❌ HUD Overlay Dimatikan!", THEME["accent_red"])

    def run_sandbox(self):
        self.log("Membuka Windows Sandbox...")
        s = r"D:\Game\DAFFA_SYSTEM\JALANKAN_SANDBOX.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🛡️ Ruang Isolasi Sandbox Terbuka!", THEME["accent_amber"])

    def run_linux_sandbox(self):
        self.log("Membuka Linux Sandbox...")
        s = r"D:\Game\DAFFA_PROJECTS\BUKA_LINUX_SANDBOX.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start cmd /c "{s}"', shell=True)
            ModernToast(self, "🐧 Linux Sandbox Terbuka!", THEME["accent_emerald"])

    def run_camera(self):
        self.log("Membuka Mata Bionik...")
        script = r"D:\Game\DAFFA_SYSTEM\Bionic_Live.py"
        if os.path.exists(script):
            subprocess.Popen(f'start cmd /k "python \"{script}\""', shell=True)
            ModernToast(self, "📸 Mata Bionik Aktif!", THEME["accent_cyan"])

    def run_steamunlocked(self):
        self.log("Membuka SteamUnlocked Launcher...")
        exe_path = r"C:\Users\USER\AppData\Local\SteamUnlocked Launcher\steamunlocked-launcher.exe"
        if os.path.exists(exe_path):
            subprocess.Popen(f'start "" "{exe_path}"', shell=True)
            ModernToast(self, "🏴‍☠️ SteamUnlocked Launcher Terbuka!", THEME["accent_red"])

    def run_optimize(self):
        self.log("Menjalankan optimalisasi sistem...")
        s = r"D:\Game\DAFFA_SYSTEM\OPTIMASI_KOMPUTER_DAFFA.bat"
        if not os.path.exists(s):
            s = r"D:\Game\DAFFA_SYSTEM\OPTIMALISASI_SISTEM.bat"
        if os.path.exists(s):
            subprocess.Popen(f'start "" "{s}"', shell=True)
            ModernToast(self, "🧹 Optimalisasi PC Berjalan!", THEME["accent_amber"])

    def restart_gui(self):
        self.log("Restarting Daffa Master Launcher...")
        os.execl(sys.executable, sys.executable, *sys.argv)

    def log(self, msg):
        try:
            timestamp = time.strftime("%H:%M:%S")
            self.log_box.insert("end", f"[{timestamp}] {msg}\n")
            self.log_box.see("end")
        except Exception:
            pass

    # ==================== BACKGROUND DAEMONS ====================
    def start_background_daemons(self):
        # 1. Telemetry and Process Tracker thread
        t1 = threading.Thread(target=self.telemetry_loop, daemon=True)
        t1.start()

        # 2. Process monitor — dot hijau real-time (Fitur 5)
        t2 = threading.Thread(target=self._process_monitor_loop, daemon=True)
        t2.start()

        # 3. Clock tick
        self.tick_timer()

    def tick_timer(self):
        elapsed = int(time.time() - self.session_start)
        h, m, s = elapsed // 3600, (elapsed % 3600) // 60, elapsed % 60
        self.session_timer_lbl.configure(text=f"⏱️ Sesi: {h:02d}:{m:02d}:{s:02d}")
        self.after(1000, self.tick_timer)

    def telemetry_loop(self):
        import socket
        while True:
            try:
                # Fast CPU and RAM via psutil
                cpu = int(psutil.cpu_percent(interval=None))
                ram = int(psutil.virtual_memory().percent)

                # Disk D: free
                try:
                    d_free = psutil.disk_usage("D:").free / (1024**3)
                    d_str = f"💿 D: {d_free:.1f}GB"
                except Exception:
                    d_str = "💿 D: --"

                # Check War Room port 9090 (Fast non-blocking socket check < 1ms)
                try:
                    with socket.create_connection(("127.0.0.1", 9090), timeout=0.04):
                        self.war_room_online = True
                except Exception:
                    self.war_room_online = False

                # Process list for running games (re-use cache from process monitor thread)
                current_procs = getattr(self, "current_running_names", set())
                if not current_procs:
                    try:
                        current_procs = {p.info['name'].lower() for p in psutil.process_iter(['name']) if p.info.get('name')}
                    except Exception:
                        pass

                # Update UI in safe thread
                self.after(0, self.update_telemetry_ui, cpu, ram, d_str, current_procs)
            except Exception:
                pass
            time.sleep(3.0)

    def update_telemetry_ui(self, cpu, ram, d_str, procs):
        try:
            self.cpu_pill.configure(
                text=f"⚡ CPU: {cpu}%",
                text_color=THEME["accent_red"] if cpu > 80 else THEME["accent_emerald"]
            )
            self.ram_pill.configure(
                text=f"💾 RAM: {ram}%",
                text_color=THEME["accent_red"] if ram > 85 else THEME["accent_cyan"]
            )
            self.disk_pill.configure(text=d_str)

            if self.war_room_online:
                self.war_room_pill.configure(
                    text="⚔️ WAR ROOM (ON)",
                    fg_color="#004D26",
                    text_color=THEME["accent_emerald"]
                )
            else:
                self.war_room_pill.configure(
                    text="⚔️ WAR ROOM (OFF)",
                    fg_color="#00354D",
                    text_color=THEME["accent_cyan"]
                )

            # Update running indicator dots on visible cards
            for game_name, dot in self.indicator_labels.items():
                target_exe = None
                for g in GAMES_DB:
                    if g["name"] == game_name:
                        target_exe = os.path.basename(g.get("exe", "")).lower()
                        break
                if target_exe and target_exe in procs:
                    dot.configure(text_color=THEME["accent_emerald"])
                else:
                    dot.configure(text_color="#4B5563")
        except Exception:
            pass

# ==================== AMONG US MINIGAME: FIX WIRES ====================
class FixWiresModal(ctk.CTkToplevel):
    def __init__(self, parent, on_complete=None):
        super().__init__(parent)
        self.parent = parent
        self.on_complete = on_complete
        self.completed = False

        self.title("⚡ ELECTRICAL: FIX WIRES // ASTRA AI")
        self.geometry("540x480")
        self.attributes("-topmost", True)
        self.configure(fg_color="#080C14")

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w, h = 540, 480
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        outer = ctk.CTkFrame(
            self,
            fg_color="#080C14",
            border_width=2,
            border_color="#00E5FF",
            corner_radius=12
        )
        outer.pack(fill="both", expand=True, padx=4, pady=4)

        # Header
        h_frame = ctk.CTkFrame(outer, fg_color="transparent")
        h_frame.pack(fill="x", padx=16, pady=(12, 4))

        ctk.CTkLabel(
            h_frame,
            text="⚡ ELECTRICAL: FIX WIRES",
            font=("Consolas", 16, "bold"),
            text_color="#00E5FF"
        ).pack(side="left")

        self.lbl_task_status = ctk.CTkLabel(
            h_frame,
            text="[ 0 / 4 WIRES CONNECTED ]",
            font=("Consolas", 11, "bold"),
            text_color="#F59E0B"
        )
        self.lbl_task_status.pack(side="right")

        ctk.CTkLabel(
            outer,
            text="Tarik kabel dari terminal kiri ke terminal kanan yang warnanya cocok:",
            font=("Consolas", 10),
            text_color="#94A3B8"
        ).pack(pady=(0, 6))

        # Canvas for electrical panel
        self.can_w = 500
        self.can_h = 280
        import tkinter as tk
        self.canvas = tk.Canvas(
            outer,
            width=self.can_w,
            height=self.can_h,
            bg="#0E1524",
            highlightthickness=1,
            highlightbackground="#1E293B",
            bd=0
        )
        self.canvas.pack(pady=4)

        # Colors & Pin Setup
        import random
        self.COLORS = [
            ("RED",     "#EF4444"),
            ("BLUE",    "#3B82F6"),
            ("YELLOW",  "#F59E0B"),
            ("MAGENTA", "#EC4899"),
        ]

        left_colors = list(self.COLORS)
        random.shuffle(left_colors)

        right_colors = list(self.COLORS)
        random.shuffle(right_colors)

        y_slots = [45, 105, 165, 225]
        self.left_pins = {}
        self.right_pins = {}

        for i, (col_name, hex_code) in enumerate(left_colors):
            py = y_slots[i]
            self.canvas.create_rectangle(15, py - 16, 50, py + 16, fill="#1F2937", outline="#374151", width=2)
            self.canvas.create_rectangle(50, py - 6, 70, py + 6, fill=hex_code, outline="")
            self.canvas.create_oval(60, py - 10, 80, py + 10, fill=hex_code, outline="#000000", width=2)
            self.left_pins[col_name] = {
                "x": 70, "y": py,
                "hex": hex_code,
                "connected": False,
                "target_right": None,
                "line_id": None
            }

        for i, (col_name, hex_code) in enumerate(right_colors):
            py = y_slots[i]
            self.canvas.create_rectangle(self.can_w - 50, py - 16, self.can_w - 15, py + 16, fill="#1F2937", outline="#374151", width=2)
            self.canvas.create_rectangle(self.can_w - 70, py - 6, self.can_w - 50, py + 6, fill=hex_code, outline="")
            self.canvas.create_oval(self.can_w - 80, py - 10, self.can_w - 60, py + 10, fill=hex_code, outline="#000000", width=2)
            self.right_pins[col_name] = {
                "x": self.can_w - 70, "y": py,
                "hex": hex_code,
                "connected": False
            }

        self.dragging_wire = None
        self.temp_line_id = None

        self.canvas.bind("<Button-1>", self._on_canvas_press)
        self.canvas.bind("<B1-Motion>", self._on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_canvas_release)

        f_frame = ctk.CTkFrame(outer, fg_color="transparent")
        f_frame.pack(fill="x", padx=16, pady=(10, 6))

        self.btn_reset = ctk.CTkButton(
            f_frame,
            text="🔄 Acak Ulang Kabel",
            font=("Consolas", 11),
            fg_color="#1E293B",
            hover_color="#334155",
            width=140,
            height=32,
            command=self._reset_wires
        )
        self.btn_reset.pack(side="left")

        ctk.CTkButton(
            f_frame,
            text="Tutup",
            font=("Consolas", 11),
            fg_color="#334155",
            hover_color="#475569",
            width=80,
            height=32,
            command=self.destroy
        ).pack(side="right")

    def _on_canvas_press(self, event):
        if self.completed:
            return
        ex, ey = event.x, event.y
        for col_name, data in self.left_pins.items():
            if abs(ex - data["x"]) < 25 and abs(ey - data["y"]) < 20:
                if data["connected"]:
                    if data["line_id"]:
                        self.canvas.delete(data["line_id"])
                    if data["target_right"]:
                        self.right_pins[data["target_right"]]["connected"] = False
                    data["connected"] = False
                    data["target_right"] = None
                    self._update_status()

                self.dragging_wire = col_name
                self.temp_line_id = self.canvas.create_line(
                    data["x"], data["y"], ex, ey,
                    fill=data["hex"], width=8, capstyle="round"
                )
                break

    def _on_canvas_drag(self, event):
        if self.dragging_wire and self.temp_line_id:
            data = self.left_pins[self.dragging_wire]
            self.canvas.coords(self.temp_line_id, data["x"], data["y"], event.x, event.y)

    def _on_canvas_release(self, event):
        if not self.dragging_wire:
            return
        col_name = self.dragging_wire
        left_data = self.left_pins[col_name]
        ex, ey = event.x, event.y

        matched = False
        right_data = self.right_pins.get(col_name)
        if right_data:
            if abs(ex - right_data["x"]) < 30 and abs(ey - right_data["y"]) < 25:
                matched = True
                self.canvas.coords(self.temp_line_id, left_data["x"], left_data["y"], right_data["x"], right_data["y"])
                left_data["connected"] = True
                left_data["target_right"] = col_name
                left_data["line_id"] = self.temp_line_id
                right_data["connected"] = True
                self.temp_line_id = None
                self.dragging_wire = None

                try:
                    import winsound
                    winsound.Beep(700, 60)
                except Exception:
                    pass

                self._check_all_connected()

        if not matched:
            if self.temp_line_id:
                self.canvas.delete(self.temp_line_id)
                self.temp_line_id = None
            self.dragging_wire = None

    def _check_all_connected(self):
        count = sum(1 for d in self.left_pins.values() if d["connected"])
        self._update_status()
        if count == 4 and not self.completed:
            self.completed = True
            self.lbl_task_status.configure(text="[ 4 / 4 TASK COMPLETED! ]", text_color="#10B981")

            try:
                import winsound
                vic_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio", "among_us_victory.wav")
                if os.path.exists(vic_p):
                    winsound.PlaySound(vic_p, winsound.SND_FILENAME | winsound.SND_ASYNC)
                else:
                    winsound.Beep(880, 100)
                    winsound.Beep(1175, 150)
            except Exception:
                pass

            self.canvas.create_rectangle(80, 100, 420, 180, fill="#0A0E17", outline="#10B981", width=2)
            self.canvas.create_text(250, 130, text="🎉 TASK COMPLETED!", font=("Consolas", 16, "bold"), fill="#10B981")
            self.canvas.create_text(250, 155, text="⚡ 100% Power Restored & Memory Purged!", font=("Consolas", 10), fill="#00E5FF")

            if self.on_complete:
                self.after(1600, self._finish_with_reward)

    def _finish_with_reward(self):
        self.destroy()
        if self.on_complete:
            self.on_complete()

    def _update_status(self):
        count = sum(1 for d in self.left_pins.values() if d["connected"])
        self.lbl_task_status.configure(text=f"[ {count} / 4 WIRES CONNECTED ]", text_color="#10B981" if count == 4 else "#F59E0B")

    def _reset_wires(self):
        for data in self.left_pins.values():
            if data["line_id"]:
                self.canvas.delete(data["line_id"])
            data["connected"] = False
            data["target_right"] = None
            data["line_id"] = None
        for data in self.right_pins.values():
            data["connected"] = False
        self.completed = False
        self._update_status()

# ==================== AMONG US SPLASH SCREEN ====================
class AmongUsSplashScreen(ctk.CTkToplevel):
    def __init__(self, parent, on_complete=None):
        super().__init__(parent)
        self.parent = parent
        self.on_complete = on_complete
        self.closed = False
        self.phase = "shhh"  # "shhh" -> "space"

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(fg_color="#060910")

        w, h = 660, 430
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "assets")
        among_assets = os.path.join(assets_dir, "among-us-assets")
        sprites_dir = os.path.join(assets_dir, "among_us_sprites")
        self.audio_dir = os.path.join(assets_dir, "audio")

        # Custom cursor
        cur_p = os.path.join(assets_dir, "among_us_arrow.cur").replace('\\', '/')
        if os.path.exists(cur_p):
            try:
                self.config(cursor=f"@{cur_p}")
            except Exception:
                pass

        # Outer border frame
        self.outer = ctk.CTkFrame(
            self,
            fg_color="#060910",
            border_width=2,
            border_color="#00E5FF",
            corner_radius=12
        )
        self.outer.pack(fill="both", expand=True, padx=2, pady=2)

        # ── CONTAINER 1: SHHHHH! INTRO (Phase 1) ──
        self.shh_frame = ctk.CTkFrame(self.outer, fg_color="transparent")
        self.shh_frame.pack(fill="both", expand=True)

        shh_dir = os.path.join(among_assets, "SHHHHH!")
        crew_p = os.path.join(shh_dir, "no_crew-sharedassets2.assets-22.png")
        shh_p = os.path.join(shh_dir, "no_shh-sharedassets2.assets-17.png")

        if os.path.exists(crew_p) and os.path.exists(shh_p):
            try:
                from PIL import Image, ImageTk
                im_c = Image.open(crew_p).convert("RGBA")
                ch = 180
                cw = int(im_c.width * ch / im_c.height)
                im_c = im_c.resize((cw, ch), Image.Resampling.LANCZOS)
                self._shh_crew_img = ctk.CTkImage(light_image=im_c, dark_image=im_c, size=(cw, ch))
                ctk.CTkLabel(self.shh_frame, text="", image=self._shh_crew_img).pack(pady=(25, 6))

                im_s = Image.open(shh_p).convert("RGBA")
                sw_w = 260
                sh_h = int(im_s.height * sw_w / im_s.width)
                im_s = im_s.resize((sw_w, sh_h), Image.Resampling.LANCZOS)
                self._shh_txt_img = ctk.CTkImage(light_image=im_s, dark_image=im_s, size=(sw_w, sh_h))
                ctk.CTkLabel(self.shh_frame, text="", image=self._shh_txt_img).pack(pady=(2, 10))
            except Exception:
                pass

        ctk.CTkLabel(
            self.shh_frame,
            text="JANGAN BICARA // ASTRA AI SEDANG MEMPERSIAPKAN SISTEM...",
            font=("Consolas", 12, "bold"),
            text_color="#EF4444"
        ).pack(pady=(4, 0))

        # ── CONTAINER 2: STARFIELD & SQUAD (Phase 2 - hidden initially) ──
        self.space_frame = ctk.CTkFrame(self.outer, fg_color="transparent")

        # Header banner logo
        logo_path = os.path.join(among_assets, "Logos", "bannerLogo_AmongUs-sharedassets0.assets-137.png")
        if os.path.exists(logo_path):
            try:
                from PIL import Image, ImageTk
                im_logo = Image.open(logo_path).convert("RGBA")
                lw = 240
                lh = int(im_logo.height * lw / im_logo.width)
                im_logo = im_logo.resize((lw, lh), Image.Resampling.LANCZOS)
                self._logo_img = ctk.CTkImage(light_image=im_logo, dark_image=im_logo, size=(lw, lh))
                ctk.CTkLabel(self.space_frame, text="", image=self._logo_img).pack(pady=(10, 2))
            except Exception:
                ctk.CTkLabel(self.space_frame, text="AMONG US", font=("Consolas", 24, "bold"), text_color="#EF4444").pack(pady=(10, 2))
        else:
            ctk.CTkLabel(self.space_frame, text="AMONG US", font=("Consolas", 24, "bold"), text_color="#EF4444").pack(pady=(10, 2))

        # Subtitle
        ctk.CTkLabel(
            self.space_frame,
            text="★ DAFFA MASTER COMMAND CENTER // ASTRA AI v5.0 ★",
            font=("Consolas", 11, "bold"),
            text_color="#00E5FF"
        ).pack(pady=(0, 4))

        # Space Canvas
        self.canvas_w = 610
        self.canvas_h = 160
        import tkinter as tk
        self.canvas = tk.Canvas(
            self.space_frame,
            width=self.canvas_w,
            height=self.canvas_h,
            bg="#050811",
            highlightthickness=1,
            highlightbackground="#1C2844",
            bd=0
        )
        self.canvas.pack(pady=4)

        # Starfield
        stars_path = os.path.join(among_assets, "Background", "Stars-sharedassets0.assets-56.png")
        self._star_w = 0
        if os.path.exists(stars_path):
            try:
                from PIL import Image, ImageTk
                star_im = Image.open(stars_path).convert("RGBA")
                sh_scaled = self.canvas_h
                sw_scaled = int(star_im.width * sh_scaled / star_im.height)
                star_im = star_im.resize((sw_scaled, sh_scaled), Image.Resampling.LANCZOS)
                self._star_w = sw_scaled
                self._star_photo = ImageTk.PhotoImage(star_im)
                self._star_id1 = self.canvas.create_image(0, 0, anchor="nw", image=self._star_photo)
                self._star_id2 = self.canvas.create_image(self._star_w, 0, anchor="nw", image=self._star_photo)
            except Exception:
                pass

        # Squad crewmates
        self.crewmates_data = [
            ("RED",    "ZordanJimbak", "#EF4444", 0),
            ("CYAN",   "Naswa",        "#00E5FF", -80),
            ("GREEN",  "Salim",        "#10B981", -160),
            ("PURPLE", "Roby",         "#A78BFA", -240),
            ("YELLOW", "Jibral",       "#F59E0B", -320),
        ]

        self.crew_sprites = {}
        for color_key, _, _, _ in self.crewmates_data:
            self.crew_sprites[color_key] = []
            for fr in range(8):
                fn = os.path.join(sprites_dir, f"{color_key}_{fr}_right.png")
                if os.path.exists(fn):
                    try:
                        from PIL import Image, ImageTk
                        im = Image.open(fn).convert("RGBA")
                        self.crew_sprites[color_key].append(ImageTk.PhotoImage(im))
                    except Exception:
                        pass

        self.crew_elements = []
        base_y = 96
        for color_key, name, name_col, x_offset in self.crewmates_data:
            sprites = self.crew_sprites.get(color_key, [])
            default_spr = sprites[0] if sprites else None
            sh_id = self.canvas.create_text(x_offset + 1, base_y - 25, text=name, font=("Consolas", 8, "bold"), fill="#000000")
            tx_id = self.canvas.create_text(x_offset, base_y - 26, text=name, font=("Consolas", 8, "bold"), fill=name_col)
            im_id = self.canvas.create_image(x_offset, base_y, anchor="center", image=default_spr) if default_spr else None
            self.crew_elements.append({
                "color": color_key,
                "name": name,
                "offset": x_offset,
                "sh_id": sh_id,
                "tx_id": tx_id,
                "im_id": im_id,
                "sprites": sprites,
            })

        # Progress bar container
        p_frame = ctk.CTkFrame(self.space_frame, fg_color="transparent")
        p_frame.pack(fill="x", padx=25, pady=(8, 2))

        self.lbl_status = ctk.CTkLabel(
            p_frame,
            text="[ 15% ] 🚀 Menghubungkan ASTRA AI Core Engine...",
            font=("Consolas", 11, "bold"),
            text_color="#94A3B8",
            anchor="w"
        )
        self.lbl_status.pack(side="left")

        self.lbl_pct = ctk.CTkLabel(
            p_frame,
            text="15%",
            font=("Consolas", 11, "bold"),
            text_color="#00E5FF",
            anchor="e"
        )
        self.lbl_pct.pack(side="right")

        self.pbar = ctk.CTkProgressBar(
            self.space_frame,
            width=610,
            height=10,
            progress_color="#00E5FF",
            fg_color="#131C30",
            corner_radius=5
        )
        self.pbar.pack(pady=(2, 6))
        self.pbar.set(0.15)

        # Skip hint
        hint_lbl = ctk.CTkLabel(
            self.space_frame,
            text="⚡ Tekan [Space] / [Enter] atau Klik di mana saja untuk langsung masuk",
            font=("Consolas", 9),
            text_color="#475569"
        )
        hint_lbl.pack(pady=(2, 6))

        # Skip bindings
        self.bind("<Button-1>", lambda e: self.finish())
        self.outer.bind("<Button-1>", lambda e: self.finish())
        self.canvas.bind("<Button-1>", lambda e: self.finish())
        self.shh_frame.bind("<Button-1>", lambda e: self.finish())
        self.bind("<space>", lambda e: self.finish())
        self.bind("<Return>", lambda e: self.finish())
        self.bind("<Escape>", lambda e: self.finish())

        # Audio playback helper
        self.play_sound("among_us_shh.wav")

        # After 900ms, switch from SHHH to Space Starfield
        self.after(900, self._start_space_phase)

    def play_sound(self, filename):
        try:
            import winsound
            fn = os.path.join(self.audio_dir, filename)
            if os.path.exists(fn):
                winsound.PlaySound(fn, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception:
            pass

    def _start_space_phase(self):
        if self.closed:
            return
        self.phase = "space"
        self.shh_frame.pack_forget()
        self.space_frame.pack(fill="both", expand=True)

        # Play Among Us Theme
        self.play_sound("among_us_theme.wav")

        # Start animation
        self.progress = 0.15
        self.anim_step = 0
        self.star_scroll_x = 0
        self.squad_start_x = 80
        self.squad_end_x = 520

        self.steps = [
            (0.25, "🚀 Menghubungkan ASTRA AI Core Engine..."),
            (0.40, "🎮 Memindai game terpasang & database cheat trainer..."),
            (0.58, "🛡️ Memuat modul runtime memory injector & security audit..."),
            (0.75, "👨‍🚀 Menginisialisasi Kru Antariksa: ZordanJimbak, Naswa, Salim, Roby, Jibral..."),
            (0.88, "⚡ Sinkronisasi Telemetry AMD Ryzen 5 5600 + RX 580..."),
            (0.96, "🏴‍☠️ Menyiapkan SteamUnlocked Launcher & War Room..."),
            (1.00, "👑 DAFFA MASTER SIAP TEMPUR! Meluncurkan Command Center..."),
        ]

        self.after(35, self._tick_space_animation)

    def _tick_space_animation(self):
        if self.closed or self.phase != "space":
            return

        self.anim_step += 1
        self.progress = min(1.0, self.progress + 0.018)
        self.pbar.set(self.progress)
        pct_int = int(self.progress * 100)
        self.lbl_pct.configure(text=f"{pct_int}%")

        for threshold, desc in self.steps:
            if self.progress <= threshold:
                self.lbl_status.configure(text=f"[ {pct_int:02d}% ] {desc}")
                break

        if self._star_w > 0:
            self.star_scroll_x = (self.star_scroll_x - 1.4) % self._star_w
            self.canvas.coords(self._star_id1, self.star_scroll_x, 0)
            self.canvas.coords(self._star_id2, self.star_scroll_x + self._star_w, 0)

        lead_x = self.squad_start_x + (self.squad_end_x - self.squad_start_x) * self.progress
        frame_idx = (self.anim_step // 2) % 8
        base_y = 100

        for elem in self.crew_elements:
            cx = lead_x + elem["offset"]
            hop = -2 if (frame_idx in [1, 5]) else (1 if (frame_idx in [3, 7]) else 0)
            cy = base_y + hop

            sprites = elem["sprites"]
            if sprites and elem["im_id"]:
                self.canvas.itemconfig(elem["im_id"], image=sprites[frame_idx % len(sprites)])
                self.canvas.coords(elem["im_id"], cx, cy)

            self.canvas.coords(elem["sh_id"], cx + 1, cy - 25)
            self.canvas.coords(elem["tx_id"], cx, cy - 26)

        if self.progress >= 1.0:
            self.lbl_status.configure(text="[ 100% ] 👑 DAFFA MASTER SIAP TEMPUR! Meluncurkan Command Center...")
            self.pbar.configure(progress_color="#10B981")
            self.play_sound("among_us_victory.wav")
            self.after(380, self.finish)
            return

        self.after(35, self._tick_space_animation)

    def finish(self):
        if self.closed:
            return
        self.closed = True
        self.destroy()
        if self.on_complete:
            self.on_complete()

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    app = DaffaMasterApp()
    app.withdraw()  # Sembunyikan window utama saat loading splash screen

    def on_splash_finish():
        app.deiconify()
        app.lift()
        app.focus_force()

    splash = AmongUsSplashScreen(app, on_complete=on_splash_finish)
    app.mainloop()
