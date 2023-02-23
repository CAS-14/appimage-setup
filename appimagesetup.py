import sys
import os

if len(sys.argv) != 2:
    print("You must provide one argument.")
    sys.exit()

program_path = sys.argv[1]
program_name = program_path.split("/")[-1]

if program_name.split(".")[-1].lower() != "appimage":
    print("You must provide an AppImage file.")
    sys.exit()

if not os.path.exists(program_path):
    print(f"{program_path}: File not found!")
    sys.exit()

home = os.path.expanduser("~")
if not os.path.exists(os.path.join(home, "Applications")):
    os.mkdir(os.path.join(home, "Applications"))

os.rename(program_path, os.path.join(home, "Applications", program_name))
print("Moved file to ~/Applications")

print("Now setting up the .desktop file...")
app_name = input("Name: ")
app_categories = input("Categories (separate with ;): ")

desktop_file = os.path.join(home, ".local", "share", "applications", f"{app_name.replace(' ', '_')}.desktop")

with open(desktop_file, "w") as f:
    f.write(
        f"""
        [Desktop Entry]
        Name={app_name}
        Exec={os.path.join(home, "Applications", program_name)}
        Terminal=false
        Type=Application
        Categories={app_categories};
        """
    )

print("Done! You should be able to find the app in your applications menu now.")