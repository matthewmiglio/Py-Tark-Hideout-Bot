import time
from functools import wraps
from queue import Queue


class Logger:
    """Handles logging statistics"""

    def __init__(self, queue=None, timed=True):
        """Logger init"""

        self.queue: Queue[dict[str, str | int]] = Queue() if queue is None else queue

        # time stats
        self.start_time = time.time() if timed else None
        self.time_since_start = 0

        # station stats
        self.workbench_starts = 0
        self.workbench_collects = 0
        self.bitcoin_collects = 0
        self.lavatory_starts = 0
        self.lavatory_collects = 0
        self.medstation_starts = 0
        self.medstation_collects = 0
        self.water_filters = 0
        self.water_collects = 0

        # log
        self.message = ""
        self.restarts = 0

        # idk lol
        self.errored = False

    def _update_queue(self):
        """updates the queue with a dictionary of mutable statistics"""
        if self.queue is None:
            return

        statistics: dict[str, str | int] = {
            "workbench_starts": self.workbench_starts,
            "time_since_start": self.calc_time_since_start(),
            "workbench_collects": self.workbench_collects,
            "bitcoin_collects": self.bitcoin_collects,
            "lavatory_starts": self.lavatory_starts,
            "lavatory_collects": self.lavatory_collects,
            "medstation_starts": self.medstation_starts,
            "medstation_collects": self.medstation_collects,
            "water_filters": self.water_filters,
            "water_collects": self.water_collects,
            "message": self.message,
            "restarts": self.restarts,
        }
        self.queue.put(statistics)

    @staticmethod
    def _updates_queue(func):
        """decorator to specify functions which update the queue with statistics"""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self._update_queue()  # pylint: disable=protected-access
            return result

        return wrapper

    @_updates_queue
    def add_restart(self):
        self.restarts += 1

    @_updates_queue
    def add_workbench_start(self):
        self.workbench_starts += 1

    @_updates_queue
    def add_workbench_collect(self):
        self.workbench_collects += 1

    @_updates_queue
    def add_bitcoin_collect(self):
        self.bitcoin_collects += 1

    @_updates_queue
    def add_lavatory_start(self):
        self.lavatory_starts += 1

    @_updates_queue
    def add_lavatory_collect(self):
        self.lavatory_collects += 1

    @_updates_queue
    def add_medstation_start(self):
        self.medstation_starts += 1

    @_updates_queue
    def add_medstation_collect(self):
        self.medstation_collects += 1

    @_updates_queue
    def add_water_filter(self):
        self.water_filters += 1

    @_updates_queue
    def add_water_collect(self):
        self.water_collects += 1

    @_updates_queue
    def log(self, string):
        self.message = string
        self.time_since_start =self.calc_time_since_start()



        print(f"[{self.time_since_start}] {string}")

    @_updates_queue
    def error(self, message: str):
        """logs an error"""
        self.errored = True
        self.status = f"Error: {message}"
        print(f"Error: {message}")

    @_updates_queue
    def add_restart(self):
        self.restarts += 1

    def calc_time_since_start(self) -> str:
        if self.start_time is not None:
            hours, remainder = divmod(time.time() - self.start_time, 3600)
            minutes, seconds = divmod(remainder, 60)
        else:
            hours, minutes, seconds = 0, 0, 0
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


# method to get the time in a readable format
def get_time():
    return time.strftime("%H:%M:%S", time.localtime())
