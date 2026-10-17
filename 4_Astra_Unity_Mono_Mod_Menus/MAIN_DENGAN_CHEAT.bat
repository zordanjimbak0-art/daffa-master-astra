@echo off
title MY VOICE ZOO - ASTRA MOD MENU // Komandan DAFFA
echo [ASTRA] Launching My Voice Zoo Mod Menu...
start "" pythonw "%~dp0MYVOICEZOO_MOD_MENU.py"
timeout /t 1 >nul
cd /d "%~dp0MyVoiceZoo"
echo [ASTRA] Launching MyVoiceZoo.exe...
start "" "MyVoiceZoo.exe"
exit
