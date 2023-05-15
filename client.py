import subprocess
import sys
import time
import tkinter.messagebox

import numpy
import pyautogui
import pygetwindow

from detection.image_rec import (check_for_location, find_references,
                                 pixel_is_equal)
from utils.dependency import get_bsg_launcher_path

pyautogui.FAILSAFE = False


def close_tarkov_client(logger, tark_window):
    try:
        logger.log("Tark found open. Closing it.")
        tark_window = tark_window[0]
        tark_window.close()
    except BaseException:
        logger.log("error closing tarkov client.")


def close_launcher(logger, tark_launcher):
    logger.log("Tark launcher found open. Closing it.")
    tark_launcher = tark_launcher[0]
    tark_launcher.close()


def restart_tarkov(logger):
    # sourcery skip: extract-duplicate-method, extract-method
    orientate_terminal()

    # check if tarkov is open
    tark_window = pygetwindow.getWindowsWithTitle("EscapeFromTarkov")
    tark_launcher = pygetwindow.getWindowsWithTitle("BsgLauncher")

    # if tark open
    if len(tark_window) != 0:
        logger.log("Tarkov client detected. Closing it.")
        orientate_terminal()
        close_tarkov_client(logger, tark_window)
        time.sleep(5)

    # if launcher open
    if len(tark_launcher) != 0:
        logger.log("Tarkov launcher detected. Closing it.")
        orientate_terminal()
        close_launcher(logger, tark_launcher)
        time.sleep(5)

    # open tark launcher
    logger.log("Opening launcher.")
    try:
        subprocess.Popen(get_bsg_launcher_path())  # pylint: disable=consider-using-with
    except FileNotFoundError:
        tkinter.messagebox.showinfo(
            "CRITICAL ERROR",
            "Could not start launcher. Open a bug report on github and share your BSGlauncher install path.",
        )
        sys.exit("Launcher path not found")

    # Wait for launcher to open and load up
    logger.log("Waiting for launcher to open.")
    index = 0
    has_window = False
    while not has_window:
        orientate_terminal()
        time.sleep(1)
        index += 1
        if len(pygetwindow.getWindowsWithTitle("BsgLauncher")) > 0:
            has_window = True
        if index > 25:
            logger.log("Launcher failed to open.")
            return restart_tarkov(logger)
    time.sleep(5)

    # orientate launcher
    logger.log("orientating launcher")
    orientate_launcher()
    orientate_terminal()
    time.sleep(3)

    # wait for launcher play button to appear
    logger.log("Waiting for launcher's play button")
    if wait_for_play_button_in_launcher(logger) == "restart":
        return restart_tarkov(logger)

    # click play
    logger.log("Clicking play.")
    click(942, 558)
    time.sleep(20)

    # wait for client opening
    logger.log("Waiting for tarkov client to open.")
    if wait_for_tarkov_to_open(logger) == "restart":
        return restart_tarkov(logger)
    for index in range(0, 30, 2):
        orientate_terminal()
        logger.log(f"Manually giving tark time to load: {index}")
        time.sleep(2)

    # orientate tark client
    orientate_tarkov_client()
    orientate_terminal()
    time.sleep(1)

    # wait for us to reach main menu
    logger.log("Waiting for tarkov client to reach main menu.")
    if wait_for_tark_main(logger) == "restart":
        return restart_tarkov(logger)


def wait_for_tarkov_to_open(logger):
    tark_window = pygetwindow.getWindowsWithTitle("EscapeFromTarkov")
    loops = 0
    while len(tark_window) == 0:
        orientate_terminal()
        logger.log(f"Waiting for tarkov to open {loops}")
        loops = loops + 2
        time.sleep(2)
        tark_window = pygetwindow.getWindowsWithTitle("EscapeFromTarkov")
        if loops > 50:
            return "restart"

    logger.log("Tarkov client detected. Done waiting")


def wait_for_tark_main(logger):
    on_main = check_if_on_tark_main(logger)
    loops = 0
    while not on_main:
        orientate_terminal()
        logger.log(f"Waiting for tark main {loops}")
        loops = loops + 2
        time.sleep(2)
        on_main = check_if_on_tark_main(logger)
        if loops > 120:
            return "restart"
    logger.log("Made it to tarkov main.")


def check_if_on_tark_main(logger):
    logger.log("Checking if on tark main")
    iar = numpy.asarray(screenshot())
    pix_list = [
        iar[613][762],
        iar[616][926],
        iar[611][294],
        iar[618][769],
        iar[651][427],
        iar[615][1010],
        iar[648][290],
    ]

    return all(pixel_is_equal(pix, [175, 90, 50], tol=100) for pix in pix_list)


def wait_for_play_button_in_launcher(logger):
    loops = 0
    logger.log("Waiting for play button to appear.")
    while not check_if_play_button_exists_in_launcher():
        loops += 1
        if loops > 20:
            return "restart"
        time.sleep(1)

    logger.log("Done waiting for play button to appear.")


def check_if_play_button_exists_in_launcher():
    current_image = screenshot()
    reference_folder = "check_if_play_button_exists_in_launcher2"
    references = [
        "1.png",
        "2.png",
        "3.png",
        "4.png",
        "5.png",
    ]

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )
    return check_for_location(locations)


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
    start_time = time.time()

    while not check_if_in_hideout():
        if time.time() - start_time > 60:
            return 'restart'

        click(x=150, y=977)
        time.sleep(5)
    print("At hideout")


def check_if_in_hideout():
    iar = numpy.asarray(screenshot())
    hideout_pixel = iar[979][183]
    if pixel_is_equal(hideout_pixel, [159, 157, 144], tol=30):
        return True
    return False


def cycle_hideout_tab():
    click(40, 932)
    time.sleep(1)
