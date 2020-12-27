import os
from pathlib import Path
import time
import ctypes


def background_shift():
    advance = True
    default = (os.getcwd())
    response = input(
        f"Is {default} your desired choice to fetch Wallpaper Photos? ").strip().lower()
    if response not in "yes":
        selection = input(
            "Type relative path of Folder to fetch Photos:\n ").strip()
        # selection = "Documents/Python/bg_shifter/bgs"
        directory = Path(os.path.join("C:/Users/7K/", selection))
        # print(directory)
    else:
        pass
    while advance:
        print("Perfect!\n Processing...")
        for i, filename in enumerate(directory.glob("*.jpg"), start=1):
            # print(filename)
            print(f"Done! Number {i}")
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, str(filename), 0)
            time.sleep(2)
        advance = False


background_shift()
