import ctypes


def change(filename):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        {SPI_SETDESKWALLPAPER}, 0, {str(filename)}, 0)
