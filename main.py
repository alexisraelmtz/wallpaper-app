
import os
import datetime
from pathlib import Path
from crontab import CronTab
from run import change

# import glob
# import maya


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

    max_time = datetime.timedelta(hours=22)
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
        cron = CronTab(user="root")
        print(f"Perfect!\n{items} wallpapers Found\nProcessing...")

        for i, filename in enumerate(directory.glob("*.jpg"), start=1):
            if i == 1:
                print(f"Done! Number {i}")
                change(filename)
                continue
            job = cron.new(command='change(filename)', comment=(
                f"Done! Number {i}"))
            job.minute.during(1).every(0.10)
            cron.write()
        job.enable(False)
        advance = False


background_shift()
