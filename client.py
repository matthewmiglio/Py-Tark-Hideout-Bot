import numpy
import time

import pyautogui
import pygetwindow

from detection.image_rec import (
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)


pyautogui.FAILSAFE = False


def orientate_tarkov_client():
    tark_window = pygetwindow.getWindowsWithTitle("EscapeFromTarkov")[0]
    tark_window.moveTo(0, 0)
    tark_window.resizeTo(1299, 999)


def orientate_launcher():
    launcher_window = pygetwindow.getWindowsWithTitle("BsgLauncher")[0]
    launcher_window.moveTo(0, 0)
    launcher_window.resizeTo(1122, 744)


def orientate_terminal():
    try:
        terminal_window = pygetwindow.getWindowsWithTitle("Py-TarkBot")[0]
        terminal_window.moveTo(pyautogui.size()[0] - 430, 0)
    except:
        print("Couldnt orientate terminal.")


def screenshot(region=(0, 0, 1400, 1400)):
    if region is None:
        return pyautogui.screenshot()  # type: ignore
    return pyautogui.screenshot(region=region)  # type: ignore


def click(x, y, clicks=1, interval=0.0, duration=0.1, button="left"):
    # get current moust position
    origin = pyautogui.position()

    # move the mouse to the spot
    pyautogui.moveTo(x, y, duration=duration)

    # click it as many times as ur suppsoed to
    loops = 0
    while loops < clicks:
        pyautogui.click(x=x, y=y, button=button)
        loops += 1
        time.sleep(interval)

    # move mouse back to original position
    pyautogui.moveTo(origin[0], origin[1])


def get_to_hideout():
    while not check_if_in_hideout():
        click(x=150, y=977)
        time.sleep(5)
    print('At hideout')


def check_if_in_hideout():
    iar = numpy.asarray(screenshot())
    hideout_pixel = iar[979][183]
    if pixel_is_equal(hideout_pixel, [159, 157, 144], tol=30):
        return True
    return False



def cycle_hideout_tab():
    click(40, 932)
    time.sleep(1)



