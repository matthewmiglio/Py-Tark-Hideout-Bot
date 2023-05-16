import numpy
import pyautogui
import time
from client import click, cycle_hideout_tab, get_to_hideout, screenshot
from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
    pixel_is_equal,
)


def handle_workbench(logger):
    if get_to_hideout() == "restart":
        return "restart"

    logger.log("Handling workbench")
    if get_to_workbench() == "restart":
        return "restart"
    time.sleep(4)

    if check_for_workbench_start():
        logger.log("Starting workbench craft")

        # click start button
        click(x=1100, y=711)
        time.sleep(1)

        # click handover button
        click(x=654, y=672)
        time.sleep(3)

        # click escape to leave workbench
        pyautogui.press("esc")

        logger.add_workbench_start()

        print("moving to lavatory now")

        return "lavatory"

    elif check_for_workbench_get_items():
        logger.log("Collecting items from workbench")

        # click get items
        click(x=1091, y=713)
        time.sleep(2)

        # leave workbench
        pyautogui.press("esc")
        time.sleep(2)

        logger.add_workbench_collect()

        # rerun workbench alg to start the craft after collecting items

        print("rerunning workbench")
        return "workbench"

    else:
        logger.log("No actions for workbench yet...")
        pyautogui.press("esc")
        time.sleep(2)

        print("moving to lavatory")

        return "lavatory"


def check_if_at_workbench():
    iar = numpy.asarray(screenshot())

    workbench_icon_exists = False
    for x in range(665, 690):
        pixel = iar[352][x]
        if pixel_is_equal(pixel, [211, 210, 201], tol=20):
            workbench_icon_exists = True

    workbench_description_exists = False
    for x in range(740, 780):
        pixel = iar[427][x]
        if pixel_is_equal(pixel, [98, 104, 105], tol=20):
            workbench_description_exists = True

    production_text_exists = False
    for x in range(960, 1000):
        pixel = iar[628][x]
        if pixel_is_equal(pixel, [134, 133, 121], tol=20):
            production_text_exists = True

    close_button_exists = False
    for x in range(1232, 1247):
        pixel = iar[354][x]
        if pixel_is_equal(pixel, [65, 7, 7], tol=20):
            close_button_exists = True

    if (
        workbench_icon_exists
        and workbench_description_exists
        and close_button_exists
        and production_text_exists
    ):
        return True
    return False


def check_for_workbench_start():
    current_image = screenshot()
    reference_folder = "workbench_start"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def check_for_workbench_get_items():
    current_image = screenshot()
    reference_folder = "workbench_get_items"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return check_for_location(locations)


def get_to_workbench():
    print("getting to workbench")

    start_time = time.time()

    for x in range(300, 900, 100):
        click(x, 930)

    if check_if_at_workbench():
        print("already here")
        return

    coord = None
    while coord is None:
        if time.time() - start_time > 60:
            print("took too long getting to workbench")
            return "restart"

        cycle_hideout_tab()
        time.sleep(1)
        coord = find_workbench_icon()
    click(coord[1], coord[0])
    time.sleep(2)

    if not check_if_at_workbench():
        print("didnt make it to workbench")
        return "restart"
    print("made it to workbench")


def find_workbench_icon():
    current_image = screenshot()
    reference_folder = "workbench_icon"
    references = make_reference_image_list(reference_folder)

    locations = find_references(
        screenshot=current_image,
        folder=reference_folder,
        names=references,
        tolerance=0.99,
    )

    return get_first_location(locations)
