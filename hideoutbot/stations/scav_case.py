import numpy
import time

from hideoutbot.bot.client import click, cycle_hideout_tab, get_to_hideout, screenshot
from hideoutbot.detection.image_rec import (
    check_for_location,
    find_references,
    make_reference_image_list,
    pixel_is_equal,
)
import pyautogui


def handle_scav_case(logger, craft_type):
    logger.log("Handling scav case")

    # get_to_hideout()

    # get_to_scav_case()

    # scroll down in scav case to see all the possible crafts

    # pyautogui.moveTo(x=1271, y=543)
    # time.sleep(1)
    # pyautogui.dragTo(x=1271, y=650)
    # time.sleep(1)

    if craft_type == "moonshine":
        logger.log("Handling moonshine craft")

        if check_for_moonshine_start():
            logger.log("Starting moonshine scav case...")
            click(1049, 469)

    elif craft_type == "intel":
        logger.log("Handling intel craft")

        if check_for_intel_start():
            logger.log("Starting intel scav case...")
            click(1050, 639)

    elif craft_type == "95000":
        logger.log("Handling 95000 craft")

        if check_for_95000_start():
            logger.log("Starting 95000 scav case...")
            click(1070, 725)

    elif craft_type == "15000":
        logger.log("Handling 15000 craft")

        if check_for_15000_get_items():
            logger.log("Collecting 15000 scav case items...")
            click(1066, 784)
            time.sleep(3)
            pyautogui.press("esc")
            time.sleep(5)

        if check_for_15000_start():
            logger.log("Starting 15000 scav case...")
            click(1068, 785)

    elif craft_type == "2500":
        logger.log("Handling 2500 craft")

        if check_for_2500_get_items():
            logger.log("Collecting 2500 scav case items...")
            click(1059, 528)
            time.sleep(3)
            pyautogui.press("esc")
            time.sleep(5)

        if check_for_2500_start():
            logger.log("Starting 2500 scav case...")
            click(1060, 555)


def check_for_2500_get_items():
    current_image = screenshot([1015, 500, 110, 60])
    reference_folder = "scav_case_2500_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_15000_get_items():
    current_image = screenshot([1020, 760, 140, 80])
    reference_folder = "scav_case_15000_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_moonshine_start():
    current_image = screenshot([960, 405, 200, 100])
    reference_folder = "scav_case_moonshine_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_2500_start():
    current_image = screenshot([992, 465, 200, 120])
    reference_folder = "scav_case_2500_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_intel_start():
    current_image = screenshot([1005, 585, 125, 80])
    reference_folder = "scav_case_intel_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_95000_start():
    current_image = screenshot([1025, 675, 200, 80])
    reference_folder = "scav_case_95000_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_15000_start():
    current_image = screenshot([1025, 750, 200, 80])
    reference_folder = "scav_case_15000_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def get_to_scav_case():
    print("Getting to scav case")

    start_time = time.time()

    for x in range(300, 900, 100):
        click(x, 930)

    while not check_if_at_scav_case():
        cycle_hideout_tab()
        time.sleep(2)

        time_taken = time.time() - start_time

        if time_taken > 60:
            print("Took too long getting to scav case. restarting")
            return "restart"

    print(f"made it to scav case in {str(time_taken)[:4]} sec")


def check_if_at_scav_case():
    iar = numpy.asarray(screenshot())

    scav_case_text_exists = False
    for x in range(770, 820):
        this_pixel = iar[351][x]
        if pixel_is_equal(this_pixel, [237, 235, 214], tol=20):
            scav_case_text_exists = True
            break

    scav_case_description_exists = False
    for x in range(1185, 1220):
        this_pixel = iar[400][x]
        if pixel_is_equal(this_pixel, [132, 140, 144], tol=20):
            scav_case_description_exists = True
            break

    current_bonuses_text_exists = False
    for x in range(1010, 1035):
        this_pixel = iar[462][x]
        if pixel_is_equal(this_pixel, [223, 221, 201], tol=20):
            current_bonuses_text_exists = True
            break

    blue_jacket_exists = False
    for x in range(550, 600):
        this_pixel = iar[223][x]
        if pixel_is_equal(this_pixel, [17, 71, 152], tol=20):
            blue_jacket_exists = True
            break
    if (
        blue_jacket_exists
        and scav_case_text_exists
        and scav_case_description_exists
        and current_bonuses_text_exists
    ):
        return True
    return False
