import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("snake_game.py", base=base, icon="SS.png")]

cx_Freeze.setup(
    name = "Snake_Game",
    options = {"build_exe": {"packages":["tkinter","matplotlib"], "include_files":["SS.png"]}},
    version = "0.01",
    description = "Classic Snake game",
    executables = executables
    )