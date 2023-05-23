import time

import numpy
import pyautogui

from hideoutbot.bot.client import check_if_in_hideout_cycle_mode, click, cycle_hideout_tab, get_to_hideout, screenshot
from hideoutbot.detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)


def handle_bitcoin_miner(logger):
    if get_to_hideout() == "restart":
        return "restart"

    logger.log("Handling bitcoin miner")

    if get_to_bitcoin_miner() == "restart":
        return "restart"
    time.sleep(4)

    print("Doing bitcoin miner checks")

    if check_for_bitcoin_miner_get_items():
        logger.log("Collecting bitcoin")
        click(x=1111, y=761)
        time.sleep(2)
        pyautogui.press("esc")
        logger.add_profit(327082)
        logger.add_bitcoin_collect()

    logger.log("No actions for bitcoin miner yet...")
    print("Moving to medstation")

    return "medstation"


def check_if_at_bitcoin_miner():
    iar = numpy.asarray(screenshot())

    yellow_bitcoin_icon_exists = False
    for x in range(945,970):
        pixel = iar[761][x]
        if pixel_is_equal(pixel, [169,126,40], tol=20):
            yellow_bitcoin_icon_exists = True

    bitcoin_farm_text_exists = False
    for x in range(720, 840):
        pixel = iar[512][x]
        if pixel_is_equal(pixel, [232, 231, 210], tol=20):
            bitcoin_farm_text_exists = True

    close_button_exists = False
    for x in range(1230, 1247):
        pixel = iar[509][x]
        if pixel_is_equal(pixel, [65, 7, 7], tol=20):
            close_button_exists = True


    if yellow_bitcoin_icon_exists and bitcoin_farm_text_exists and close_button_exists:
        return True
    return False


def get_to_bitcoin_miner():
    print("Getting to bitcoin miner")

    start_time = time.time()


    if not check_if_in_hideout_cycle_mode():
        print('Not in hideout cycle mode. entering cycle mode...')
        for x in range(700, 1200, 100):
            click(x, 930)

    time.sleep(4)

    while not check_if_at_bitcoin_miner():
        if time.time() - start_time > 60:
            print("Took too long to get to bitcoin miner")
            return "restart"
        cycle_hideout_tab()
        time.sleep(3)

    print("made it to bitcoin miner")


def find_bitcoin_miner_icon():
    current_image = screenshot()
    reference_folder = "bitcoin_miner_icon"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return get_first_location(locations)


def check_for_bitcoin_miner_get_items():
    current_image = screenshot()
    reference_folder = "bitcoin_miner_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)
