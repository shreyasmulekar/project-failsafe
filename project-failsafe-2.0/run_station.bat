@echo off
title PROJECT FAILSAFE 2.0 - SECURE OFFLINE STATION
echo =====================================================================
echo  PROJECT FAILSAFE 2.0: IEEE WIE AI FORENSICS ESCAPE ROOM
echo  HOLOGRAPHIC QUANTUM REACTOR HUD (2050+ TACTICAL STATION)
echo =====================================================================
echo.

if exist ProjectFailsafe2.exe (
    start "" "ProjectFailsafe2.exe"
) else (
    start "" "%~dp0index.html"
)
exit /b
