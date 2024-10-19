import os
import subprocess

def compile_to_exe(script_name):
    """Компілює Python-скрипт у .exe файл."""
    try:
        # Команда для компіляції через PyInstaller
        subprocess.run(["pyinstaller", "--onefile", script_name], check=True)
        print(f"Файл {script_name} успішно скомпільовано в .exe")
    except subprocess.CalledProcessError as e:
        print(f"Помилка під час компіляції: {e}")

def clean_up():
    """Видаляє тимчасові файли після компіляції."""
    try:
        # Видаляємо тимчасові папки PyInstaller'а
        os.remove("build")
        os.remove("__pycache__")
        os.remove("dist")
        print("Чистка завершена.")
    except Exception as e:
        print(f"Помилка під час чистки: {e}")

if __name__ == "__main__":
    script_name = "main.py"  # Назва вашого головного файлу
    compile_to_exe(script_name)
    clean_up()
