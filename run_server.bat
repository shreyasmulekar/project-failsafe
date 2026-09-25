@echo off
title PROJECT FAILSAFE - Organizer Server
color 0A
echo ========================================================
echo         PROJECT FAILSAFE: LOCAL EVENT SERVER
echo ========================================================
echo.

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python not found on standard PATH. Trying py launcher...
    start "Project Failsafe Server" py server.py
) else (
    echo Starting Python HTTP and API Server on port 8000...
    start "Project Failsafe Server" python server.py
)

echo Waiting for server initialization on http://127.0.0.1:8000...
timeout /t 2 /nobreak >nul

echo Launching Organizer Command Center in Edge/Chrome...
start "" http://127.0.0.1:8000/admin.html

echo.
echo Organizer Console active at: http://127.0.0.1:8000/admin.html
echo LAN Participant URL: http://localhost:8000
echo.
pause
