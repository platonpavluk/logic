@echo off
echo ===========================================
echo Installing required Python libraries...
echo ===========================================

REM Перевірка наявності pip і встановлення, якщо не встановлено
python -m ensurepip --upgrade

REM Оновлення pip до останньої версії
python -m pip install --upgrade pip

REM Встановлення необхідних бібліотек
pip install pyglet
pip install soundfile
pip install pyaudio
pip install chipmunk-python

REM Встановлення PyInstaller для створення exe файлів
pip install pyinstaller

echo ===========================================
echo All required libraries, including PyInstaller, are installed.
pause
