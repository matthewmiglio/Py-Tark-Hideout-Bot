import time
from client import click, cycle_hideout_tab, get_to_hideout, screenshot
import pyautogui

from detection.image_rec import (
    check_for_location,
    find_references,
    get_first_location,
    make_reference_image_list,
)


def handle_lavatory(logger):

    if get_to_hideout()=='restart':return'restart'
    

    logger.log('Handling lavatory')
    
    # get to lavatory
    get_to_lavatory()
    time.sleep(4)

    # check if get_items exists
    if check_for_get_items_in_lavatory():
        logger.log('Getting items')
        click(x=1072, y=678)
        time.sleep(3)
        pyautogui.press("esc")
        logger.add_lavatory_collect()
        return 'lavatory'
    

    # if start exists, buy items, start, return None
    elif check_for_start_in_lavatory():
        logger.log('Starting item craft')

        #right click bag
        click(871,674,button='right')
        time.sleep(1)

        #click FBI
        click(x=930, y=700)
        time.sleep(4)

        #click purchase
        click(x=1191, y=152)
        time.sleep(1)

        #click input box
        click(x=695, y=482)
        time.sleep(1)

        #type 4
        pyautogui.press('4')
        time.sleep(1)

        #press y
        pyautogui.press('y')
        time.sleep(1)

        #press escape to get back to lavatory
        pyautogui.press('esc')
        time.sleep(2)

        #click start
        click(x=1064, y=678)
        time.sleep(1)

        #click handover
        click(x=641, y=678)
        time.sleep(3)
        pyautogui.press("esc")
        
        logger.add_lavatory_start()
        return 'water'
    
    else:
        logger.log('No actions for lavatory yet...')
        pyautogui.press("esc")
        time.sleep(2)
        return 'water'


def get_to_lavatory():
    for x in range(300,900,100):
        click(x,930)

    coord = None
    while coord is None:
        cycle_hideout_tab()
        time.sleep(1)
        coord = find_lavatory_icon()
    click(coord[1], coord[0])


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


