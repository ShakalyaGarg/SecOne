@echo off
REM Getting files using WMIC command, apps in Program Files, Program Files(x86)
REM Set output file path
set "outputfile=C:\Users\Nishchhal\Desktop\KAVACH\installed_apps.txt"
echo Applications > "%outputfile%"

REM Find applications in "Program Files" folder and write to output file
dir /s /b "%ProgramFiles%\*.exe" >> "%outputfile%"

REM Find applications in "Program Files (x86)" folder and write to output file
dir /s /b "%ProgramFiles(x86)%\*.exe" >> "%outputfile%"

