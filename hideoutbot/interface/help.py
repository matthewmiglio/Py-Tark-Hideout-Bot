import PySimpleGUI as sg

from .theme import THEME


def show_help_gui():
    out_text = (
        "I got nothing so far..."
    )

    sg.theme(THEME)
    layout = [
        [sg.Text(out_text)],
    ]
    window = sg.Window("Py-TarkBot", layout)
    while True:
        read = window.read()
        event, _ = read or (None, None)
        if event in [sg.WIN_CLOSED, "Exit"]:
            break
    window.close()
