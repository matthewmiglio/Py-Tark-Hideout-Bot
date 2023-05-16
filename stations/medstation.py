import numpy
from client import click, cycle_hideout_tab, get_to_hideout, screenshot
from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)
import time
import pyautogui

# screenshot(region=[1000, 640, 200, 100])


def handle_medstation(logger):
    if get_to_hideout() == "restart":
        return "restart"

    logger.log("Handling medstation")

    # get to medstation
    if get_to_medstation() == "restart":
        return "restart"
    time.sleep(4)

    print('Doing checks')

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

        print('Going to workbench now')

        return "workbench"

    # check for get items
    elif check_for_medstation_get_items():
        logger.log("Collecting medstation items")

        # click get items
        click(x=1094, y=674)
        time.sleep(3)

        # click esc
        pyautogui.press("esc")
        time.sleep(2)

        print('Gonna redo medstation to restart craft')

        logger.add_medstation_collect()

        return "medstation"

    else:
        logger.log("No actions for medstation yet...")
        print('moving to workbench')
        return "workbench"


def check_if_at_medstation():
    iar = numpy.asarray(screenshot())

    medstation_text_exists = False
    for x in range(790, 802):
        pixel = iar[349][x]
        if pixel_is_equal(pixel, [237, 235, 214], tol=20):
            medstation_text_exists = True

    medstation_description_exists = False
    for x in range(965, 995):
        pixel = iar[414][x]
        if pixel_is_equal(pixel, [111, 119, 121], tol=20):
            medstation_description_exists = True

    production_text_exists = False
    for x in range(955, 975):
        pixel = iar[585][x]
        if pixel_is_equal(pixel, [167, 166, 151], tol=20):
            production_text_exists = True

    close_button_exists = False
    for x in range(1232, 1246):
        pixel = iar[355][x]
        if pixel_is_equal(pixel, [65, 7, 7], tol=20):
            close_button_exists = True

    current_bonuses_text_exists = False
    for x in range(970, 1010):
        pixel = iar[478][x]
        if pixel_is_equal(pixel, [177, 175, 160], tol=20):
            current_bonuses_text_exists = True

    if (
        medstation_text_exists
        and medstation_description_exists
        and close_button_exists
        and production_text_exists
        and current_bonuses_text_exists
    ):
        return True
    return False


def get_to_medstation():
    print("Getting to medstation")

    

    start_time = time.time()

    for x in range(300, 900, 100):
        click(x, 930)

    if check_if_at_medstation():
        print('already at medstation')
        return

    coord = None
    while coord is None:
        if time.time() - start_time > 60:
            print("Took too long getting to medstation, returning")
            return "restart"

        cycle_hideout_tab()
        time.sleep(1)
        coord = find_medstation_icon()
    click(coord[1], coord[0])
    time.sleep(2)

    if not check_if_at_medstation():
        print("Didnt get to medstation, restarting...")

        return "restart"

    print("made it to medstation")


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
