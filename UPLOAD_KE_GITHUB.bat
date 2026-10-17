@echo off
title ASTRA GITHUB AUTO-PUSHER // zordanjimbak0-art
color 0B
cd /d "D:\Game\DAFFA_GITHUB_PORTFOLIO"
echo ============================================================================
echo    ASTRA AI - AUTO UPLOAD KE GITHUB: zordanjimbak0-art/daffa-master-astra
echo ============================================================================
echo.
echo [LANGKAH 1] Di tab Chrome yang baru terbuka:
echo             Langsung klik tombol hijau "Create repository" di paling bawah!
echo.
echo [LANGKAH 2] Setelah klik "Create repository" di Chrome,
echo             tekan ENTER di jendela ini untuk langsung upload semua kode!
echo ============================================================================
pause
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/zordanjimbak0-art/daffa-master-astra.git
echo.
echo [ASTRA] Mengunggah seluruh kode ke https://github.com/zordanjimbak0-art/daffa-master-astra.git ...
echo (Jika muncul popup Sign in with your browser, klik tombol hijau Sign in with your browser)
git push -u origin main --force
echo.
echo ============================================================================
echo [SELESAI] Seluruh kode berhasil naik ke:
echo   https://github.com/zordanjimbak0-art/daffa-master-astra
echo.
echo Membuka halaman repository GitHub Komandan...
start https://github.com/zordanjimbak0-art/daffa-master-astra
echo ============================================================================
pause
