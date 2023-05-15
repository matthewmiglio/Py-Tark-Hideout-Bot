import pyautogui
import time
from client import click, cycle_hideout_tab, screenshot
from detection.image_rec import check_for_location, find_references, get_first_location, make_reference_image_list


def handle_workbench():
    print('Handling workbench')
    get_to_workbench()
    time.sleep(4)

    if check_for_workbench_start():
        print('Starting workbench craft')

        #click start button
        click(x=1100, y=711)
        time.sleep(1)

        #click handover button
        click(x=654, y=672)
        time.sleep(3)

        #click escape to leave workbench
        pyautogui.press('esc')

    elif check_for_workbench_get_items():
        print('Dont know how to collect workbench craft')
        pyautogui.press('esc')
        time.sleep(2)

    else:
        print('No actions for workbench yet...')
        pyautogui.press('esc')
        time.sleep(2)




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
    for x in range(300,900,100):
        click(x,930)

    coord = None
    while coord is None:
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
