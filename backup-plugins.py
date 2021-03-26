from shutil import copytree, copyfile

CLOUD = "D:\\OneDrive - Microsoft"
LOCAL = "C:\\Users\\cosorgen\\AppData\\Roaming\\MAXON\\Maxon Cinema 4D R23_DBA5903C"

print("Starting...")

#
# copy local into onedrive
#

# plugins
print("Copying local plugins to cloud...")
copytree(src=LOCAL+"\\plugins", dst=CLOUD+"\\C4D Plugins Windows", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# scripts
print("Copying local scripts to cloud...")
copytree(src=LOCAL+"\\library\\scripts", dst=CLOUD+"\\C4D Scripts", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# python libs
print("Copying local python libs to cloud...")
copytree(src=LOCAL+"\\python37\\libs", dst=CLOUD+"\\C4D Python Libs", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")

# xpools
print("Copying local xpools to cloud...")
copytree(src=LOCAL+"\\library\\xgroup", dst=CLOUD+"\\C4D Xpresso Pools", dirs_exist_ok=True, copy_function=copyfile)
print("Done.")