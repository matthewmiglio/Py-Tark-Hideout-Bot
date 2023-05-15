import pyautogui
import numpy

import time
from client import click, cycle_hideout_tab, screenshot
from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)


def handle_water_collector(logger):
    logger.log('Handling water collector')

    get_to_water_collector()
    time.sleep(4)

    if check_for_water_collector_get_items():
        logger.log("Collecting water collector items")
        click(x=1051, y=796)
        time.sleep(3)
        pyautogui.press("esc")
        time.sleep(2)

        logger.add_water_collect()

        return handle_water_collector()

    elif not check_for_water_collector_filter():
        logger.log("Adding a filter to water collector")

        # click filters dropdown
        click(x=930, y=790)
        time.sleep(1)

        # click topleft most filter
        click(x=975, y=796)
        time.sleep(1)

        # click escape
        pyautogui.press("esc")
        time.sleep(1)

        logger.add_water_filter()

    else:
        logger.log("No actions for water collector yet...")


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
    for x in range(300, 900, 100):
        click(x, 930)

    coord = None
    while coord is None:
        cycle_hideout_tab()
        time.sleep(1)
        coord = find_water_collector_icon()
    click(coord[1], coord[0])


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


