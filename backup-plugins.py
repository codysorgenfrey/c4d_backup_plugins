import os
import shutil

def copy_directory(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for item in os.listdir(src_dir):
        src_file = os.path.join(src_dir, item)
        dst_file = os.path.join(dst_dir, item)

        if os.path.isdir(src_file):
            copy_directory(src_file, dst_file)
        else:
            if os.path.exists(dst_file):
                if os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                    shutil.copy2(src_file, dst_file)
            else:
                shutil.copy2(src_file, dst_file)

CLOUD = "D:\\OneDrive - Microsoft"
LOCALC4D = "C:\\Users\\cosorgen\\AppData\\Roaming\\Maxon\\Maxon Cinema 4D 2025_789E552B"
LOCALC4DROOT = "C:\\Program Files\\Maxon Cinema 4D 2025"
LOCALAE = "C:\\Program Files\\Adobe\\Adobe After Effects 2024\\Support Files"
C4DPYTHONFOLDER = "python311"

print("Starting...")

#
# copy local into onedrive
#

# plugins
print("Copying local C4D plugins to cloud...")
copy_directory(LOCALC4D+"\\plugins", CLOUD+"\\C4D Plugins Windows")
print("Done.")

print("Copying local AE plugins to cloud...")
copy_directory(LOCALAE+"\\Plug-ins\\User", CLOUD+"\\AE Plugins Windows")
print("Done.")

# scripts
print("Copying local C4D scripts to cloud...")
copy_directory(LOCALC4D+"\\library\\scripts", CLOUD+"\\C4D Scripts")
print("Done.")

print("Copying local AE scripts to cloud...")
copy_directory(LOCALAE+"\\Scripts", CLOUD+"\\AE Scripts")
print("Done.")

# python libs
print("Copying local C4D python libs to cloud...")
copy_directory(LOCALC4D+"\\"+C4DPYTHONFOLDER+"\\libs", CLOUD+"\\C4D Python Libs")
print("Done.")

# xpools
print("Copying local C4D xpools to cloud...")
copy_directory(LOCALC4D+"\\library\\xgroup", CLOUD+"\\C4D Xpresso Pools")
print("Done.")

#
# copy onedrive files into local
#

# plugins
print("Copying cloud C4D plugins to local...")
copy_directory(CLOUD+"\\C4D Plugins Windows", LOCALC4D+"\\plugins")
print("Done.")

print("Copying cloud AE plugins to local...")
copy_directory(CLOUD+"\\AE Plugins Windows", LOCALAE+"\\Plug-ins\\User")
print("Done.")

# scripts
print("Copying cloud C4D scripts to local...")
copy_directory(CLOUD+"\\C4D Scripts", LOCALC4D+"\\library\\scripts")
print("Done.")

print("Copying cloud AE scripts to local...")
copy_directory(CLOUD+"\\AE Scripts", LOCALAE+"\\Scripts")
print("Done.")

# python libs
print("Copying cloud C4D python libs to local...")
copy_directory(CLOUD+"\\C4D Python Libs", LOCALC4D+"\\"+C4DPYTHONFOLDER+"\\libs")
print("Done.")

# xpools
print("Copying cloud C4D xpools to local...")
copy_directory(CLOUD+"\\C4D Xpresso Pools", LOCALC4D+"\\library\\xgroup")
print("Done.")
