import webbrowser
from client import orientate_tarkov_client
from states import state_tree
from stations.medstation import check_for_medstation_get_items

from utils.logger import Logger

from queue import Queue
import PySimpleGUI as sg

from interface import (
    THEME,
    disable_keys,
    main_layout,
    show_help_gui,
    user_config_keys,
)
import time

from utils.thread import StoppableThread, ThreadKilled


def main():
    # orientate_terminal()

    thread: WorkerThread | None = None
    comm_queue: Queue[dict[str, str | int]] = Queue()
    logger = Logger(comm_queue, timed=False)  # dont time the inital logger

    # window layout
    window = sg.Window("Py-TarkBot", main_layout)

    # start timer for autostart
    start_time = time.time()
    auto_start_time = 30  # seconds
    auto_started = False

    # run the gui
    while True:
        # get gui vars
        read = window.read(timeout=100)
        event, values = read or (None, None)

        # check if bot should be autostarted
        if (
            thread is None
            and values is not None
            and values["autostart"]
            and not auto_started
            and time.time() - start_time > auto_start_time
        ):
            auto_started = True
            event = "Start"

        if event in [sg.WIN_CLOSED, "Exit"]:
            # shut down the thread if it is still running
            shutdown_thread(thread)
            break

        if event == "Start":
            # start the bot with new queue and logger
            comm_queue = Queue()
            logger = Logger(comm_queue)
            thread = start_button_event(logger, window, values)

        elif event == "Stop":
            stop_button_event(logger, window, thread)

        elif event == "Help":
            show_help_gui()

        elif event == "Donate":
            webbrowser.open(
                "https://www.paypal.com/donate/"
                + "?business=YE72ZEB3KWGVY"
                + "&no_recurring=0"
                + "&item_name=Support+my+projects%21"
                + "&currency_code=USD"
            )

        elif event == "issues-link":
            webbrowser.open(
                "https://github.com/matthewmiglio/py-tarkbot/issues/new/choose"
            )

        elif event in user_config_keys:
            print("User created an event in the window")

        # handle when thread is finished
        if thread is not None and not thread.is_alive():
            # enable the start button and configuration after the thread is stopped
            for key in disable_keys:
                window[key].update(disabled=False)
            if thread.logger.errored:
                window["Stop"].update(disabled=True)
            else:
                # reset the communication queue and logger
                comm_queue = Queue()
                logger = Logger(comm_queue, timed=False)
                thread = None

        update_layout(window, logger)

    shutdown_thread(thread, kill=True)

    window.close()


def shutdown_thread(thread: StoppableThread | None, kill=True):
    if thread is not None:
        thread.shutdown_flag.set()
        if kill:
            thread.kill()


def update_layout(window: sg.Window, logger: Logger):
    # comm_queue: Queue[dict[str, str | int]] = logger.queue
    window["time_since_start"].update(logger.calc_time_since_start())  # type: ignore
    # update the statistics in the gui
    if not logger.queue.empty():
        # read the statistics from the logger
        for stat, val in logger.queue.get().items():
            window[stat].update(val)  # type: ignore


def start_button_event(logger: Logger, window, values):
    logger.log("Starting")

    for key in disable_keys:
        window[key].update(disabled=True)

    # setup thread and start it
    # args = (values["rows_to_target"], values["remove_offers_timer"])
    thread = WorkerThread(logger, args=[0, 0])
    thread.start()

    # enable the stop button after the thread is started
    window["Stop"].update(disabled=False)

    return thread


def stop_button_event(logger: Logger, window, thread):
    logger.log("Stopping")
    window["Stop"].update(disabled=True)
    shutdown_thread(thread, kill=True)  # send the shutdown flag to the thread


class WorkerThread(StoppableThread):
    def __init__(self, logger: Logger, args, kwargs=None):
        super().__init__(args, kwargs)
        self.logger = logger

    def run(self):
        try:
            placeholder_arg_1, placeholder_arg_2 = self.args  # parse thread args

            state = "restart"
            logger = Logger()

            loops = 0
            # loop until shutdown flag is set
            while not self.shutdown_flag.is_set():
                state = state_tree(state, logger)

        except ThreadKilled:
            return

        except Exception as exc:  # pylint: disable=broad-except
            # catch exceptions and log to not crash the main thread
            self.logger.error(str(exc))


if __name__ == "__main__":
    main()

    # from client import orientate_tarkov_client
    # orientate_tarkov_client()
    # print(check_for_medstation_get_items())
