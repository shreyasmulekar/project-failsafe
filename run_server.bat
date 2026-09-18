@echo off
title PROJECT FAILSAFE - Organizer Server
color 0A
echo ========================================================
echo         PROJECT FAILSAFE: LOCAL EVENT SERVER
echo ========================================================
echo.
echo Starting Python HTTP and API Server on port 8000...
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python was not found in PATH.
    echo Trying py launcher...
    start http://localhost:8000
    py server.py
    pause
    exit /b
)

start "" http://localhost:8000
python server.py
pause
