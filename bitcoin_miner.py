import time
from client import click, cycle_hideout_tab, screenshot
from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
)
import pyautogui


def handle_bitcoin_miner(logger):
    logger.log("Handling bitcoin miner")

    get_to_bitcoin_miner()
    time.sleep(4)

    if check_for_bitcoin_miner_get_items():
        logger.log("Collecting bitcoin")
        click(x=1111, y=761)
        time.sleep(2)
        pyautogui.press("esc")
        logger.add_workstation_collect()


def get_to_bitcoin_miner():
    for x in range(300, 900, 100):
        click(x, 930)

    coord = None
    while coord is None:
        cycle_hideout_tab()
        time.sleep(1)
        coord = find_bitcoin_miner_icon()
    click(coord[1], coord[0])


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


