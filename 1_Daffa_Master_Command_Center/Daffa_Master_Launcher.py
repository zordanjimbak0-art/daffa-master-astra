import os
import sys
import time
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("="*78)
    print("       🌟 DAFFA MASTER COMMAND CENTER — GAME & CHEAT LAUNCHER 🌟")
    print("="*78)
    print(" Pilih game untuk dimainkan beserta CHEAT/MOD resminya:")
    print("-"*78)

def main():
    base = r"D:\Game\Games"
    
    games = {
        "1":  {"name": "Stardew Valley",              "status": "✅ MOD MENU (P)", "bat": os.path.join(base, "Stardew Valley", "MAIN_DENGAN_CHEAT.bat"), "info": "P = CJB Cheats, ALT+2 Speed 2x, ALT+4 Slowmo"},
        "2":  {"name": "Project Zomboid",             "status": "✅ HOTKEY MOD (ALT+1..0)", "bat": os.path.join(base, "Project Zomboid", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God Mode, ALT+2 Inf Ammo, ALT+3 NoClip, ALT+4 Fast Build"},
        "3":  {"name": "Subnautica 1",                "status": "✅ NATIVE MOD (F2/\\)", "bat": os.path.join(base, "Subnautica", "MAIN_DENGAN_CHEAT.bat"), "info": "F2 atau \\ = Buka GUI, ALT+1 God, ALT+2 O2, ALT+3 Free Craft"},
        "4":  {"name": "Subnautica 2 (UE5)",          "status": "✅ UE4SS MOD (ALT+1..4)", "bat": os.path.join(base, "Subnautica 2", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Inf O2, ALT+3 Free Craft, ALT+4 Speed 2x"},
        "5":  {"name": "Subnautica Below Zero",       "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "Subnautica-Below-Zero-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 O2, ALT+3 Free Craft, ALT+5 Speed 2.5x"},
        "6":  {"name": "Terraria",                    "status": "✅ CE TABLE / JOURNEY", "bat": os.path.join(base, "Terraria", "MAIN_DENGAN_CHEAT.bat"), "info": "Journey Mode bawaan game, ALT+2 Speed 2x, Auto-Miner"},
        "7":  {"name": "Minecraft Dungeons",          "status": "✅ ONLINE / UE4SS MOD", "bat": os.path.join(base, "Minecraft Dungeons", "MAIN_DENGAN_CHEAT.bat"), "info": "Ctrl+1 God Mode, Ctrl+2 Arrows, Ctrl+3 Max Emeralds"},
        "8":  {"name": "Upin & Ipin Universe",        "status": "✅ UE4SS + SAVE MOD", "bat": os.path.join(base, "Upin Ipin", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Ghost/Fly, ALT+3 Speed, Save Editor"},
        "9":  {"name": "SpongeBob Cosmic Shake",      "status": "✅ SAVE & MACRO", "bat": os.path.join(base, "SpongeBob", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Fly ON/OFF, ALT+4 Fast Run"},
        "10": {"name": "Soulmask",                    "status": "✅ CE + MACRO", "bat": os.path.join(base, "Soulmask", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Fly, ALT+3 Teleport, Console: F10"},
        "11": {"name": "Quake (Remaster)",            "status": "✅ AUTOEXEC MOD", "bat": os.path.join(base, "Quake", "MAIN_DENGAN_CHEAT.bat"), "info": "P = God, [ = Noclip, ] = Invisible, \\ = All Weapons"},
        "12": {"name": "Metal Slug Attack Reloaded",  "status": "✅ CE TABLE", "bat": os.path.join(base, "Metal Slug Attack Reloaded", "MAIN_DENGAN_CHEAT.bat"), "info": "Ctrl+1 66M Uang, Ctrl+2 AP Unlimited, Ctrl+4 Invincible"},
        "13": {"name": "Naruto UNS 4",                "status": "✅ CE TABLE", "bat": os.path.join(base, "Naruto Shippuden UNS4", "MAIN_DENGAN_CHEAT.bat"), "info": "Cheat Engine + NarutoUNS4_DaffaCheat.ct (Ryo, HP, Chakra)"},
        "14": {"name": "Naruto UNS Revolution",       "status": "✅ CE TABLE", "bat": os.path.join(base, "Naruto Shippuden UNS Revolution", "MAIN_DENGAN_CHEAT.bat"), "info": "Cheat Engine + NarutoRevo_DaffaCheat.ct (Ryo, HP, Chakra)"},
        "15": {"name": "Postal 2",                    "status": "✅ CONSOLE CHEAT", "bat": os.path.join(base, "Postal 2", "MAIN_DENGAN_CHEAT.bat"), "info": "~ = Console, SISSY = Enable, IAmSoLame = God Mode"},
        "16": {"name": "Serious Sam 2",               "status": "✅ CONSOLE CHEAT", "bat": os.path.join(base, "Serious Sam 2", "MAIN_DENGAN_CHEAT.bat"), "info": "~ = Console, sam_iEnableCheats=2, sam_iGodMode=1"},
        "17": {"name": "Serious Sam TFE",             "status": "✅ CONSOLE CHEAT", "bat": os.path.join(base, "Serious Sam The First Encounter", "MAIN_DENGAN_CHEAT.bat"), "info": "F1 = Console, please god = Kebal, please giveall"},
        "18": {"name": "Snowed Under",                "status": "✅ CE MOD (60% KB)", "bat": os.path.join(base, "Snowed.Under", "MAIN_DENGAN_CHEAT.bat"), "info": "CTRL+1 Speed 3x, CTRL+2 Freeze World, CTRL+3 Save Editor"},
        "19": {"name": "Kingdom Rush Vengeance",      "status": "✅ AHK TRAINER", "bat": os.path.join(base, "Kingdom Rush Vengeance", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 Gold 99k, ALT+2 Freeze Gold, ALT+3 Lives 999"},
        "20": {"name": "Plants vs Zombies GOTY",       "status": "✅ AHK TRAINER", "bat": os.path.join(base, "Plants vs Zombies GOTY", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 Sun 9999, ALT+2 Lives 99, ALT+3 Koin 999k"},
        "21": {"name": "Graveyard Keeper 2",          "status": "✅ MOD MENU v2.3", "bat": os.path.join(base, "Graveyard Keeper 2", "MAIN_DENGAN_CHEAT.bat"), "info": "INSERT / ALT+M = Item Spawner, Speed 2.2x, Inf Money"},
        "22": {"name": "Bloons TD 5",                 "status": "✅ MASTER MOD", "bat": os.path.join(base, "Bloons TD 5", "MAIN_DENGAN_CHEAT.bat"), "info": "999k Money & 99k Token, Rank 100 Max, All Towers Max XP"},
        "23": {"name": "Kingdom Rush",                "status": "✅ AUTO GOD MODE", "bat": os.path.join(base, "KingdomRush", "MAIN_DENGAN_CHEAT.bat"), "info": "Auto 999k Gems & 150 Stars, All Heroes Lvl 10"},
        "24": {"name": "Kingdom Rush Frontiers",       "status": "✅ AUTO GOD MODE", "bat": os.path.join(base, "KingdomRushFrontiers", "MAIN_DENGAN_CHEAT.bat"), "info": "Auto 999k Gems & 150 Stars, Auto Heroes Lvl 10"},
        "25": {"name": "Kingdom Rush Origins",         "status": "✅ AUTO GOD MODE", "bat": os.path.join(base, "kingdomrushorigins", "MAIN_DENGAN_CHEAT.bat"), "info": "Auto 999k Gems & 150 Stars, Auto Heroes Lvl 10"},
        "26": {"name": "DREDGE (Deluxe + All DLC)",   "status": "✅ MASTER SPAWNER", "bat": os.path.join(base, "DREDGE-SteamRIP.com", "DREDGE", "MAIN_DENGAN_CHEAT.bat"), "info": "INSERT / ALT+M = Spawner Ikan/Item Apapun, Speed 5x"},
        "27": {"name": "Journey to Savage Planet",    "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "Journey to the Savage Planet", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Fly, ALT+3 Ghost, ALT+4 Speed 2.5x"},
        "28": {"name": "That's Not My Neighbor",       "status": "✅ AUTOPILOT RADAR", "bat": os.path.join(base, "Thats-Not-My-Neighbor-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 Radar Autopilot, ALT+2 Inspect Docs, ALT+3 Call DDD"},
        "29": {"name": "Blasphemous",                 "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "Blasphemous-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God Mode, ALT+2 Fervor, ALT+3 Tears 999k, ALT+5 1-Hit KO"},
        "30": {"name": "Blasphemous 2",               "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "Blasphemous-2-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God Mode, ALT+2 Fervor, ALT+3 Tears 999k, ALT+5 1-Hit KO"},
        "31": {"name": "Binding of Isaac: Repentance", "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "The.Binding.of.Isaac-Repentance-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 God, ALT+2 Max HP, ALT+3 Coins, ALT+6 Collectibles"},
        "32": {"name": "KR x PVZ Fusion Mod",         "status": "✅ FUSION ENGINE v1.0", "bat": os.path.join(base, "FUSION_KR_PVZ", "MAIN_FUSION.bat"), "info": "God Mode Tower/Heroes, Inf Sun & Gems 99k, No Cooldown"},
        "33": {"name": "Albion Online",               "status": "⚠️ RESMI (EAC PROTECTED)", "bat": os.path.join(base, "AlbionOnline", "MAIN.bat"), "info": "MMORPG Resmi Server Online (EAC Banned Jika Cheat)"},
        "34": {"name": "My Voice Zoo",                "status": "✅ ASTRA MOD MENU", "bat": os.path.join(base, "MyVoiceZoo-SteamRIP.com", "MAIN_DENGAN_CHEAT.bat"), "info": "ALT+1 +1M Gold, ALT+2 999M Gold, ALT+4 Unlock 30 Hewan, ALT+8 100% God Save"},
        "35": {"name": "Astra 3D Action RPG",         "status": "✅ FPS PBR RPG", "bat": r"D:\Game\DAFFA_GAMES\MAIN_GAME_RPG_3D.bat", "info": "First-Person 3D RPG, 3-Hit Combo, Shield Parry, GitHub PBR & GLB Assets"},
        "36": {"name": "SpaceX Falcon 9 3D",          "status": "✅ 3D TELEMETRY", "bat": r"D:\Game\DAFFA_GAMES\MAIN_GAME_3D.bat", "info": "3D Orbital Launch & Booster Landing Simulator"},
    }

    while True:
        print_header()
        for key in sorted(games.keys(), key=lambda x: int(x)):
            game = games[key]
            num = key.rjust(2)
            print(f" [{num}] {game['name'].ljust(33)} | {game['status']}")
        print("-"*78)
        print(" [ G] 🚀 Buka DAFFA MASTER GUI DASHBOARD")
        print(" [ 0] 🚪 KELUAR")
        print("-"*78)
        
        choice = input(f"\n Masukkan angka pilihan (1-{len(games)} / G / 0): ").strip().upper()
        
        if choice == '0':
            print("\n Sampai jumpa, Komandan DAFFA! 🫡")
            time.sleep(1)
            sys.exit()
        elif choice == 'G':
            print("\n 🚀 Membuka DAFFA MASTER GUI DASHBOARD...")
            gui_bat = r"D:\Game\DAFFA_MASTER_CENTER.bat"
            if os.path.isfile(gui_bat):
                subprocess.Popen(f'start "" "{gui_bat}"', shell=True, cwd=r"D:\Game")
            else:
                subprocess.Popen(['pythonw', r"D:\Game\DAFFA_SYSTEM\Daffa_Master_GUI.py"], cwd=r"D:\Game\DAFFA_SYSTEM")
            time.sleep(1.5)
            input("\n Tekan ENTER untuk kembali...")
        elif choice == '33':
            clear_screen()
            print("="*78)
            print(" ⚠️  PERINGATAN: ALBION ONLINE RESMI")
            print("="*78)
            print("\n Albion Online adalah game MMORPG murni (Online Server).")
            print(" Game ini menggunakan Easy Anti-Cheat (EAC).")
            print(" DILARANG menyuntikkan memory/cheat apapun agar akun tidak BANNED.")
            lanjut = input("\n Tetap buka game resmi tanpa cheat? (Y/T): ").strip().upper()
            if lanjut == 'Y':
                bat_path = games['33']['bat']
                if os.path.exists(bat_path):
                    print("\n 🚀 Meluncurkan Albion Online...")
                    subprocess.Popen(f'start "" "{bat_path}"', shell=True, cwd=os.path.dirname(bat_path))
                    time.sleep(2)
            input("\n Tekan ENTER untuk kembali ke menu...")
        elif choice in games:
            game = games[choice]
            clear_screen()
            print("="*78)
            print(f" MELUNCURKAN: {game['name']}")
            print("="*78)
            print(f"\n 💡 INFO CHEAT: {game['info']}")
            
            bat_path = game['bat']
            if os.path.exists(bat_path):
                print(f"\n 🚀 Membuka game launcher + cheat...")
                time.sleep(1)
                bat_dir = os.path.dirname(bat_path)
                subprocess.Popen(f'start "" "{bat_path}"', shell=True, cwd=bat_dir)
                print("\n Game & mod menu sedang dibuka! Anda bisa kembali ke menu.")
                input("\n Tekan ENTER untuk kembali ke menu...")
            else:
                print(f"\n ❌ Launcher tidak ditemukan di:\n    {bat_path}")
                input("\n Tekan ENTER untuk kembali...")
        else:
            print("\n ❌ Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
