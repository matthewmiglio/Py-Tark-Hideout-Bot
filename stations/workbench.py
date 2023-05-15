import pyautogui
import time
from client import click, cycle_hideout_tab, get_to_hideout, screenshot
from detection.image_rec import check_for_location, find_references, get_first_location, make_reference_image_list


def handle_workbench(logger):
    if get_to_hideout()=='restart':return'restart'
    

    logger.log('Handling workbench')
    if get_to_workbench()=='restart':return 'restart'
    time.sleep(4)

    if check_for_workbench_start():
        logger.log('Starting workbench craft')

        #click start button
        click(x=1100, y=711)
        time.sleep(1)

        #click handover button
        click(x=654, y=672)
        time.sleep(3)

        #click escape to leave workbench
        pyautogui.press('esc')

        logger.add_workbench_start()

        return 'lavatory'

    elif check_for_workbench_get_items():
        logger.log('Collecting items from workbench')
        
        #click get items
        click(x=1091, y=713)
        time.sleep(2)
        
        #leave workbench
        pyautogui.press('esc')
        time.sleep(2)

        logger.add_workbench_collect()

        #rerun workbench alg to start the craft after collecting items
        return 'lavatory'

    else:
        logger.log('No actions for workbench yet...')
        pyautogui.press('esc')
        time.sleep(2)

        return 'lavatory'



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
    start_time = time.time()

    for x in range(300,900,100):
        click(x,930)

    coord = None
    while coord is None:
        if time.time() - start_time > 60:
            return "restart"

        cycle_hideout_tab()
        time.sleep(1)
        coord = find_workbench_icon()
    click(coord[1], coord[0])



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
