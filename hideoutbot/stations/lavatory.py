import time

import numpy
import pyautogui

from hideoutbot.bot.client import click, cycle_hideout_tab, get_to_hideout, screenshot
from hideoutbot.detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)


def handle_lavatory(logger):
    if get_to_hideout() == "restart":
        return "restart"

    logger.log("Handling lavatory")

    # get to lavatory
    if get_to_lavatory() == "restart":
        return "restart"
    time.sleep(4)

    print("Doing checks")

    # check if get_items exists
    if check_for_get_items_in_lavatory():
        logger.log("Getting items")
        click(x=1072, y=678)
        time.sleep(3)
        logger.add_lavatory_collect()
        logger.add_profit(10700)
        print("Returning back to lavatory to restart the craft")

    # if start exists, buy items, start, return None
    if check_for_start_in_lavatory():
        logger.log("Starting item craft")

        # right click bag
        click(871, 674, button="right")
        time.sleep(1)

        # click FBI
        click(x=930, y=700)
        time.sleep(4)

        # click purchase
        click(x=1191, y=152)
        time.sleep(1)

        # click input box
        click(x=695, y=482)
        time.sleep(1)

        # type 4
        pyautogui.press("4")
        time.sleep(1)

        # press y
        pyautogui.press("y")
        time.sleep(1)

        # press escape to get back to lavatory
        pyautogui.press("esc")
        time.sleep(2)

        # click start
        click(x=1064, y=678)
        time.sleep(1)

        # click handover
        click(x=641, y=678)
        time.sleep(3)

        logger.add_lavatory_start()

        print("Going to water now")


    print('leaving lavatory')
    pyautogui.press('esc')
    return "water"


def check_if_at_lavatory():
    iar = numpy.asarray(screenshot())

    lavatory_text_exists = False
    for x in range(732, 744):
        pixel = iar[358][x]
        if pixel_is_equal(pixel, [237, 235, 214], tol=20):
            lavatory_text_exists = True

    lavatory_description_text_exists = False
    for x in range(890, 925):
        pixel = iar[399][x]
        if pixel_is_equal(pixel, [126, 133, 137], tol=20):
            lavatory_description_text_exists = True

    black_region_deosnt_exist = True
    for x in range(850, 1150):
        for y in range(537, 580):
            pixel = iar[y][x]
            if not (pixel_is_equal(pixel, [2, 1, 1], tol=20)):
                black_region_deosnt_exist = False

    close_button_exists = False
    for x in range(1232, 1247):
        pixel = iar[352][x]
        if pixel_is_equal(pixel, [65, 7, 7], tol=20):
            close_button_exists = True

    if (
        lavatory_text_exists
        and lavatory_description_text_exists
        and close_button_exists
        and black_region_deosnt_exist
    ):
        return True
    return False


def get_to_lavatory():
    print("Getting to lavatory ")

    start_time = time.time()

    for x in range(300, 900, 100):
        click(x, 930)
    time.sleep(4)

    while not check_if_at_lavatory():
        if time.time() - start_time > 60:
            print("Took too long to get to lavatory")
            return "restart"
        cycle_hideout_tab()
        time.sleep(3)

    print("made it to lavatory")


def find_lavatory_icon():
    current_image = screenshot()
    reference_folder = "find_lavatory_symbol"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return get_first_location(locations)


def check_for_get_items_in_lavatory():
    current_image = screenshot()
    reference_folder = "lavatory_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_start_in_lavatory():
    current_image = screenshot(region=[1024, 656, 100, 60])
    reference_folder = "lavatory_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)
