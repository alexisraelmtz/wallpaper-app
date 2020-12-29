import time
import os
import datetime
from pathlib import Path
from run import change, sleep_minutes

# import glob
# import maya
# from crontab import CronTab


def background_shift():
    advance = True
    default = Path(os.getcwd())
    # response = (
    #     input(f"Is {default} your desired choice to fetch Wallpaper Photos? ")
    #     .strip()
    #     .lower()
    # )
    response = "n"

    if response == "no" or response == "n":
        # selection = input("Type relative path of Folder to fetch Photos:\n>").strip()
        selection = "C:/Users/7K/Documents/Python/bg_shifter/bgs"
        directory = Path(os.path.join("C:/Users/7K/", selection))
        # print(directory)
    else:
        print("Ok, ")
        directory = default
    try:
        count = os.listdir(directory)
        items = 0
        for n in count:
            _, f_ext = os.path.splitext(n)
            if f_ext == ".jpg":
                items += 1
    except ValueError:
        advance = False
        return "Processing...\nNone Found"

    max_time = datetime.timedelta(hours=22)  # 22
    check = datetime.datetime.now()
    time_left = max_time - datetime.timedelta(
        hours=check.hour,
        minutes=check.minute,
        seconds=check.second,
        microseconds=check.microsecond,
    )
    interval = int(((time_left) / items).total_seconds() / 60)
    print(f"Change Wallpaper every {interval} minutes for {items} times.")

    while advance:
        print(f"Perfect!\n{items} wallpapers Found\nProcessing...")
        for i, filename in enumerate(directory.glob("*.jpg"), start=1):
            if i == 1:
                change(filename)
                print(f"Done! Number {i}")
                continue
            sleep_minutes(interval)
            change(filename)
            print(f"Done! Number {i}")

        advance = False


background_shift()
