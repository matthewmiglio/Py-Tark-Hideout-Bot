from client import click, cycle_hideout_tab, get_to_hideout, screenshot
from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
)
import time
import pyautogui

# screenshot(region=[1000, 640, 200, 100])


def handle_medstation(logger):

    if get_to_hideout()=='restart':return'restart'
    

    logger.log("Handling medstation")

    # get to medstation
    get_to_medstation()
    time.sleep(4)

    # check for start
    if check_for_medstation_start():
        logger.log("Starting medstation craft")

        # click start button
        click(x=1113, y=677)
        time.sleep(2)

        # click handover button
        click(x=645, y=673)
        time.sleep(2)

        # press esc to leave this menu
        pyautogui.press("esc")

        logger.add_medstation_start()

        return "workbench"

    # check for get items
    elif check_for_medstation_get_items():
        logger.log('Collecting medstation items')

        #click get items
        click(x=1094, y=674)
        time.sleep(3)

        #click esc
        pyautogui.press("esc")
        time.sleep(2)
        
        return "medstation"

    else:
        logger.log("No actions for medstation yet...")
        return "workbench"


def get_to_medstation():
    for x in range(300, 900, 100):
        click(x, 930)

    coord = None
    while coord is None:
        cycle_hideout_tab()
        time.sleep(1)
        coord = find_medstation_icon()
    click(coord[1], coord[0])


def find_medstation_icon():
    current_image = screenshot()
    reference_folder = "medstation_icon"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return get_first_location(locations)


def check_for_medstation_start():
    current_image = screenshot()
    reference_folder = "medstation_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_medstation_get_items():
    current_image = screenshot()
    reference_folder = "medstation_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)

