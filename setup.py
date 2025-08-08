from cx_Freeze import setup, Executable

setup(name="QR Screenshot Scanner", executables=[Executable("QR Screenshot Scanner.py")], options={"build_exe": {"excludes": ["tkinter"]}})
