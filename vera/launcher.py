"""VERA launcher — finds pythonw.exe and runs assistant.py with no console window."""
import os
import sys
import shutil
import subprocess

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
    # VERA.exe lives in launcher_out\ — assistant.py is one level up
    if os.path.exists(os.path.join(exe_dir, 'assistant.py')):
        base = exe_dir
    else:
        base = os.path.dirname(exe_dir)
else:
    base = os.path.dirname(os.path.abspath(__file__))

pythonw = shutil.which("pythonw") or shutil.which("python")
assistant = os.path.join(base, "assistant.py")
subprocess.Popen([pythonw, assistant], cwd=base)
