from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

CLOUD = "D:\\OneDrive - Microsoft"
LOCAL = "C:\\Users\\cosorgen\\AppData\\Roaming\\MAXON\\Maxon Cinema 4D R23_DBA5903C"
LOCALROOT = "C:\\Program Files\\Maxon Cinema 4D R23"

print("Starting...")

#
# copy local into onedrive
#

# plugins
print("Copying local plugins to cloud...")
copy_tree(src=LOCAL+"\\plugins", dst=CLOUD+"\\C4D Plugins Windows", update=1)
print("Done.")

# scripts
print("Copying local scripts to cloud...")
copy_tree(src=LOCAL+"\\library\\scripts", dst=CLOUD+"\\C4D Scripts", update=1)
print("Done.")

# python libs
print("Copying local python libs to cloud...")
copy_tree(src=LOCAL+"\\python37\\libs", dst=CLOUD+"\\C4D Python Libs", update=1)
print("Done.")

# xpools
print("Copying local xpools to cloud...")
copy_tree(src=LOCAL+"\\library\\xgroup", dst=CLOUD+"\\C4D Xpresso Pools", update=1)
print("Done.")

# new.c4d
print("Copying local new.c4d to cloud...")
copy_file(src=LOCALROOT+"\\new.c4d", dst=CLOUD+"\\new.c4d", update=1)
print("Done.")

#
# copy onedrive files into local
#

# plugins
print("Copying cloud plugins to local...")
copy_tree(src=CLOUD+"\\C4D Plugins Windows", dst=LOCAL+"\\plugins", update=1)
print("Done.")

# scripts
print("Copying cloud scripts to local...")
copy_tree(src=CLOUD+"\\C4D Scripts", dst=LOCAL+"\\library\\scripts", update=1)
print("Done.")

# python libs
print("Copying cloud python libs to local...")
copy_tree(src=CLOUD+"\\C4D Python Libs", dst=LOCAL+"\\python37\\libs", update=1)
print("Done.")

# xpools
print("Copying cloud xpools to local...")
copy_tree(src=CLOUD+"\\C4D Xpresso Pools", dst=LOCAL+"\\library\\xgroup", update=1)
print("Done.")

# new.c4d
print("Copying cloud new.c4d to local...")
copy_file(src=CLOUD+"\\new.c4d", dst=LOCALROOT+"\\new.c4d", update=1)
print("Done.")