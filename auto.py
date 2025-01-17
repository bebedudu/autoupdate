import os
import sys
import requests
import subprocess
from pystray import MenuItem as item, Menu, Icon  # For system tray menu
from PIL import Image

# Global constants
CURRENT_VERSION = "1.0.0"  # Define your program's current version
UPDATE_URL = "https://example.com/latest_version"  # URL to check for the latest version
DOWNLOAD_URL = "https://example.com/downloads/my_program.exe"  # URL to download the latest version
APP_NAME = "My Program.exe"  # Name of the executable

def check_for_update():
    try:
        # Step 1: Check for updates
        response = requests.get(UPDATE_URL)
        latest_version = response.text.strip()

        if latest_version > CURRENT_VERSION:
            # Prompt user for update
            result = input("Update available! Do you want to update now? (yes/no): ").lower()
            if result == "yes":
                download_update(latest_version)
        else:
            print("You are already using the latest version!")
    except Exception as e:
        print(f"Error checking for updates: {e}")

def download_update(latest_version):
    try:
        # Step 2: Download the updated file
        response = requests.get(DOWNLOAD_URL, stream=True)
        with open("update_temp.exe", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Step 3: Replace the old executable
        update_path = os.path.join(os.getcwd(), "update_temp.exe")
        current_path = os.path.join(os.getcwd(), APP_NAME)
        
        # Replace the old file
        os.rename(current_path, f"{current_path}.old")
        os.rename(update_path, current_path)

        print("Update completed successfully!")
        restart_program()
    except Exception as e:
        print(f"Error updating program: {e}")

def restart_program():
    # Restart the updated program
    subprocess.Popen([sys.executable, APP_NAME])
    sys.exit()

def quit_app(icon, item):
    icon.stop()

def main():
    # System tray icon setup
    image = Image.new("RGB", (64, 64), "blue")
    menu = Menu(
        item("Update Program", lambda: check_for_update()),
        item("Quit", quit_app)
    )
    icon = Icon("MyApp", image, "My Application", menu)
    icon.run()

if __name__ == "__main__":
    main()
