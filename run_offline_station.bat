@echo off
title PROJECT FAILSAFE - AditiOS v2.4 Terminal
color 0A
echo ========================================================
echo       PROJECT FAILSAFE: ADITIOS v2.4 HUD TERMINAL
echo ========================================================
echo.
echo Launching AditiOS v2.4 interactive terminal...
echo.
start "" "%~dp0aditi_os_widget.html"
echo Station launched successfully.
timeout /t 2 >nul
exit /b
