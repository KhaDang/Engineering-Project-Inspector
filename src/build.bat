@echo off

echo ================================
echo Building Engineering File Manager
echo ================================

rmdir /S /Q build
rmdir /S /Q dist

pyinstaller ^
--clean ^
--onefile ^
--windowed ^
--icon=assets\logo.ico ^
--name="Engineering File Manager" ^
main.py

pause