import os
from pathlib import Path
import time
import ctypes


def background_shift():
    advance = True
    default = os.getcwd()
    response = (
        input(f"Is {default} your desired choice to fetch Wallpaper Photos? ")
        .strip()
        .lower()
    )
    if response == "no" or response == "n":
        selection = input("Type relative path of Folder to fetch Photos:\n>").strip()
        # selection = "Documents/Python/bg_shifter/bgs"
        directory = Path(os.path.join("C:/Users/7K/", selection))
        # print(directory)
    else:
        print("Ok, ")
        directory = Path(default)
    while advance:
        print("Perfect!\nProcessing...")
        check = False
        for i, filename in enumerate(directory.glob("*.jpg"), start=1):
            # print(filename)
            print(f"Done! Number {i}")
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, str(filename), 0
            )
            time.sleep(2)
            check = True
        if not check:
            print("None Found")
        advance = False


background_shift()


# count# Files
# time now
# left = time.now - time.midnight
# pulse = left/count#
# cron.every(pulse)
