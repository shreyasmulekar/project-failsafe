@echo off
title PROJECT FAILSAFE 2090 - DEDICATED LAN SERVER
color 0b
echo =========================================================================
echo       PROJECT FAILSAFE 2090 // IEEE WIE FORENSIC AI ESCAPE ROOM
echo                     DEDICATED LOCAL LAN SERVER
echo =========================================================================
echo.

cd /d "%~dp0"

echo [1/3] Detecting Host IPv4 Network Configuration...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    echo       LAN IP Address Found: %%a
)
echo.
echo [2/3] Checking Python installation...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in your system PATH!
    echo Please install Python 3.10+ from python.org and tick "Add to PATH".
    pause
    exit /b 1
)

echo [3/3] Starting Project Failsafe HTTP & WebSocket Server on Port 8000...
echo.
echo =========================================================================
echo  SERVER URL FOR PARTICIPANT LAPTOPS:
echo  http://10.100.8.89:8000
echo.
echo  ORGANIZER COMMAND CENTER URL:
echo  http://localhost:8000/admin.html
echo =========================================================================
echo.
echo [NOTE] Keep this window open during the tournament!
echo.

python server.py
pause
