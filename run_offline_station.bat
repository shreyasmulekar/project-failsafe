@echo off
title PROJECT FAILSAFE - Station Client
color 0B
echo ========================================================
echo       PROJECT FAILSAFE: STANDALONE OFFLINE STATION
echo ========================================================
echo.
echo Launching ADITI-OS Terminal in default browser...
echo.
start "" "%~dp0public\index.html"
echo Station launched in offline standalone mode.
timeout /t 3 >nul
exit /b
