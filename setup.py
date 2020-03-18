import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

includefiles = ['images/']

setup(  name = "WormholeIdentification",
        version = "1.0",
        description = "A tool to help you identify wormholes and their attributes visually",
        options = {'build_exe': {'includes':["tkinter","guizero","ctypes"],'include_files':includefiles}},
        executables = [Executable("eveWhID.py", base=base)])



