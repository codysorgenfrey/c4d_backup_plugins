from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

CLOUD = "D:\\OneDrive - Microsoft"
LOCALC4D = "C:\\Users\\cosorgen\\AppData\\Roaming\\Maxon\\Maxon Cinema 4D 2023_BCDB4759"
LOCALC4DROOT = "C:\\Program Files\\Maxon Cinema 4D 2023"
LOCALAE = "C:\\Program Files\\Adobe\\Adobe After Effects 2022\\Support Files"

print("Starting...")

#
# copy local into onedrive
#

# plugins
print("Copying local C4D plugins to cloud...")
copy_tree(src=LOCALC4D+"\\plugins", dst=CLOUD+"\\C4D Plugins Windows", update=1)
print("Done.")

print("Copying local AE plugins to cloud...")
copy_tree(src=LOCALAE+"\\Plug-ins\\User", dst=CLOUD+"\\AE Plugins Windows", update=1)
print("Done.")

# scripts
print("Copying local C4D scripts to cloud...")
copy_tree(src=LOCALC4D+"\\library\\scripts", dst=CLOUD+"\\C4D Scripts", update=1)
print("Done.")

print("Copying local AE scripts to cloud...")
copy_tree(src=LOCALAE+"\\Scripts", dst=CLOUD+"\\AE Scripts", update=1)
print("Done.")

# python libs
print("Copying local C4D python libs to cloud...")
copy_tree(src=LOCALC4D+"\\python310\\libs", dst=CLOUD+"\\C4D Python Libs", update=1)
print("Done.")

# xpools
print("Copying local C4D xpools to cloud...")
copy_tree(src=LOCALC4D+"\\library\\xgroup", dst=CLOUD+"\\C4D Xpresso Pools", update=1)
print("Done.")

# new.c4d
print("Copying local new.c4d to cloud...")
copy_file(src=LOCALC4DROOT+"\\new.c4d", dst=CLOUD+"\\new.c4d", update=1)
print("Done.")

#
# copy onedrive files into local
#

# plugins
print("Copying cloud C4D plugins to local...")
copy_tree(src=CLOUD+"\\C4D Plugins Windows", dst=LOCALC4D+"\\plugins", update=1)
print("Done.")

print("Copying cloud AE plugins to local...")
copy_tree(src=CLOUD+"\\AE Plugins Windows", dst=LOCALAE+"\\Plug-ins\\User", update=1)
print("Done.")

# scripts
print("Copying cloud C4D scripts to local...")
copy_tree(src=CLOUD+"\\C4D Scripts", dst=LOCALC4D+"\\library\\scripts", update=1)
print("Done.")

print("Copying cloud AE scripts to local...")
copy_tree(src=CLOUD+"\\AE Scripts", dst=LOCALAE+"\\Scripts", update=1)
print("Done.")

# python libs
print("Copying cloud C4D python libs to local...")
copy_tree(src=CLOUD+"\\C4D Python Libs", dst=LOCALC4D+"\\python39\\libs", update=1)
print("Done.")

# xpools
print("Copying cloud C4D xpools to local...")
copy_tree(src=CLOUD+"\\C4D Xpresso Pools", dst=LOCALC4D+"\\library\\xgroup", update=1)
print("Done.")

# new.c4d
print("Copying cloud new.c4d to local...")
copy_file(src=CLOUD+"\\new.c4d", dst=LOCALC4DROOT+"\\new.c4d", update=1)
print("Done.")