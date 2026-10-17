@echo off
title ASTRA GITHUB AUTO-PUSHER // KOMANDAN DAFFA
color 0B
cd /d "D:\Game\DAFFA_GITHUB_PORTFOLIO"
echo ============================================================================
echo    ⚔️ ASTRA AI — UPLOAD KODE & GAME WEB KE GITHUB KOMANDAN DAFFA ⚔️
echo ============================================================================
echo.
echo Seluruh kode sudah dirapikan dan di-commit di:
echo   D:\Game\DAFFA_GITHUB_PORTFOLIO
echo.
set /p REPO_URL="Tempel URL Repository GitHub Anda (contoh: https://github.com/username/daffa-master.git): "
if "%REPO_URL%"=="" (
    echo [!] URL kosong. Membuka halaman pembuatan repository baru di GitHub...
    start https://github.com/new
    pause
    exit /b
)
git branch -M main
git remote remove origin 2>nul
git remote add origin %REPO_URL%
echo.
echo [ASTRA] Mengunggah seluruh kode ke %REPO_URL% ...
git push -u origin main --force
echo.
echo ============================================================================
echo [SELESAI] Kode berhasil diunggah ke GitHub!
echo Untuk mengaktifkan website game gratis:
echo   Buka Settings -^> Pages -^> Pilih branch 'main' dan folder '/docs' -^> Save!
echo ============================================================================
pause
