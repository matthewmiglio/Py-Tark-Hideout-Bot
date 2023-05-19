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


def handle_water_collector(logger):
    collected = False
    added_filter = False

    if get_to_hideout() == "restart":
        return "restart"

    logger.log("Handling water collector")

    if get_to_water_collector() == "restart":
        return "restart"
    time.sleep(4)
    print("doing water checks")

    if check_for_water_collector_get_items():
        logger.log("Collecting water collector items")
        click(x=1051, y=796)
        time.sleep(3)

        logger.add_water_collect()
        logger.add_profit(123300)

        print("returning to water to check for filter")
        collected = True


    if not check_for_water_collector_filter():
        logger.log("Adding a filter to water collector")

        # click filters dropdown
        click(x=930, y=790)
        time.sleep(1)

        # click topleft most filter
        click(x=975, y=796)
        time.sleep(1)

        added_filter = True

        # click escape
        pyautogui.press("esc")
        time.sleep(1)

        logger.add_water_filter()

        print("going to bitcoin")

        return "bitcoin"

    if not collected and not added_filter:
        logger.log("No actions for water collector yet...")
        print("going to bitcoin")
        return "bitcoin"


def check_if_at_water_collector():
    iar = numpy.asarray(screenshot())

    water_collector_text_exists = False
    for x in range(790, 820):
        pixel = iar[494][x]
        if pixel_is_equal(pixel, [237, 235, 214], tol=20):
            water_collector_text_exists = True

    purified_water_icon_exists = False
    for x in range(957, 975):
        pixel = iar[797][x]
        if pixel_is_equal(pixel, [210, 238, 243], tol=20):
            purified_water_icon_exists = True

    close_button_exists = False
    for x in range(1232, 1247):
        pixel = iar[493][x]
        if pixel_is_equal(pixel, [65, 7, 7], tol=20):
            close_button_exists = True

    if (
        water_collector_text_exists
        and purified_water_icon_exists
        and close_button_exists
    ):
        return True
    return False


def find_water_collector_icon():
    current_image = screenshot()
    reference_folder = "water_collector_icon"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return get_first_location(locations)


def get_to_water_collector():
    print("Getting to water")

    start_time = time.time()

    for x in range(300, 900, 100):
        click(x, 930)

    if check_if_at_water_collector():
        print("already here. returning")
        return

    coord = None
    while coord is None:
        if time.time() - start_time > 90:
            print("took too long getting to water. returning restart")
            return "restart"

        if check_if_at_water_collector():
            print('made it to water collector')

            return

        cycle_hideout_tab()
        time.sleep(3)


def check_for_water_collector_get_items():
    current_image = screenshot()
    reference_folder = "water_collector_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_water_collector_filter():
    iar = numpy.asarray(screenshot())
    pixel = iar[796][845]
    if pixel_is_equal(pixel, [116, 205, 248], tol=15):
        return True
    return False