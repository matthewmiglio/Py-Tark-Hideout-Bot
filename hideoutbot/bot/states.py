from hideoutbot.bot.client import restart_tarkov
from hideoutbot.stations.bitcoin_miner import handle_bitcoin_miner
from hideoutbot.stations.generator import check_for_fuel
from hideoutbot.stations.lavatory import handle_lavatory
from hideoutbot.stations.medstation import handle_medstation
from hideoutbot.stations.water_collector import handle_water_collector
from hideoutbot.stations.workbench import handle_workbench


def state_tree(state, logger, jobs):  # -> check_fuel
    if state == "start":
        restart_tarkov(logger)

        state = "check_fuel"

    if state == "restart":  # -> check_fuel
        print("Entered restart state")
        clip_that()
        logger.add_restart()

        restart_tarkov(logger)

        state = "check_fuel"

    elif state == "check_fuel":  # -> no_fuel, medstation
        state = check_for_fuel(logger)

    elif state == "no_fuel":  # -> program freeze
        for _ in range(3):
            logger.log("Generator has no fuel!!")
        while 1:
            pass

    elif state == "medstation":
        # leads to workbench
        if "medstation" in jobs:
            state = handle_medstation(logger)
        else:
            state = "workbench"

    elif state == "workbench":
        # leads to lavatory
        if "Workbench" in jobs:
            state = handle_workbench(logger)
        else:
            state = "lavatory"

    elif state == "lavatory":
        # leads to water
        if "Lavatory" in jobs:
            state = handle_lavatory(logger)
        else:
            state = "water"

    elif state == "water":
        # leads to bitcoin
        if "water" in jobs:
            state = handle_water_collector(logger)
        else:
            state = "bitcoin"

    elif state == "bitcoin":
        # leads to medstation

        if "Bitcoin" in jobs:
            state = handle_bitcoin_miner(logger)
        else:
            state = "medstation"

    return state


def clip_that():
    import time

    from hideoutbot.bot.client import click

    click(x=1904, y=921)
    print("Saved a replay of that failure")
    time.sleep(3)
