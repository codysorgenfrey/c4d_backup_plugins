from shutil import copytree, copyfile

CLOUD = "D:\\OneDrive - Microsoft"
LOCAL = "C:\\Users\\cosorgen\\AppData\\Roaming\\MAXON\\Maxon Cinema 4D R23_DBA5903C"

print("Starting...")

#
# copy onedrive files into local
#

# plugins
print("Copying cloud plugins to local...")
copytree(src=CLOUD+"\\C4D Plugins Windows", dst=LOCAL+"\\plugins", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# scripts
print("Copying cloud scripts to local...")
copytree(src=CLOUD+"\\C4D Scripts", dst=LOCAL+"\\library\\scripts", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# python libs
print("Copying cloud python libs to local...")
copytree(src=CLOUD+"\\C4D Python Libs", dst=LOCAL+"\\python37\\libs", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# xpools
print("Copying cloud xpools to local...")
copytree(src=CLOUD+"\\C4D Xpresso Pools", dst=LOCAL+"\\library\\xgroup", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")