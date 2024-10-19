@echo off
echo Compiling Python script into an executable...
python -m PyInstaller --onefile main.py

echo Compilation finished. Check the 'dist' folder for the executable.
pause
