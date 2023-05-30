from hideoutbot.bot.client import restart_tarkov
from hideoutbot.stations.bitcoin_miner import handle_bitcoin_miner
from hideoutbot.stations.generator import check_for_fuel
from hideoutbot.stations.lavatory import handle_lavatory
from hideoutbot.stations.medstation import handle_medstation
from hideoutbot.stations.scav_case import handle_scav_case
from hideoutbot.stations.water_collector import handle_water_collector
from hideoutbot.stations.workbench import handle_workbench


def state_tree(state, logger, jobs):  # -> check_fuel
    print("-------------------------------------\n")

    if state == "start":
        restart_tarkov(logger)

        state = "check_fuel"

    if state == "restart":  # -> check_fuel
        print("Entered restart state")
        clip_that()
        logger.add_restart()

        restart_tarkov(logger)

        state = "check_fuel"

    elif state == "check_fuel":  # -> no_fuel,
        state = check_for_fuel(logger)

    elif state == "no_fuel":  # -> program freeze
        for _ in range(3):
            logger.log("Generator has no fuel!!")
        while 1:
            pass

    elif state == "autorestart":
        print("Entered autorestart state")
        logger.add_autorestart()

        restart_tarkov(logger)

        state = "check_fuel"

    # bitcoin -> workbench -> water -> scav -> medstation -> lavatory -> bitcoin

    elif state == "bitcoin":
        # if its time for autorestart, state = autorestart then return
        time_string = logger.time_since_start

        hours_running = int(time_string.split(":")[0])

        autorestarts = logger.autorestarts

        if hours_running >= autorestarts:
            state = "autorestart"
        else:
            print("Entered bitcoin state")

            if "Bitcoin" in jobs:
                state = handle_bitcoin_miner(logger)
            else:
                state = "workbench"

            print(f"State after bitcoin is {state}")

    elif state == "workbench":
        print("Entered workbench state")

        if "Workbench" in jobs:
            state = handle_workbench(logger)
        else:
            state = "water"

        print(f"State after workbench is {state}")

    elif state == "water":
        print("Entered water state")

        if "water" in jobs:
            state = handle_water_collector(logger)
        else:
            state = "scav_case"

        print(f"State after water is {state}")

    elif state == "scav_case":
        print("Entered scav_case state")

        if "scav_case" in jobs:
            # unpack scav case craft type from job list

            if "15000" in jobs:
                craft_type = "15000"
            elif "95000" in jobs:
                craft_type = "95000"
            elif "Moonshine" in jobs:
                craft_type = "moonshine"
            elif "Intel" in jobs:
                craft_type = "intel"
            else:
                craft_type = "2500"

            state = handle_scav_case(logger, craft_type)
        else:
            state = "medstation"

        print(f"State after scav_case is {state}")

    elif state == "medstation":
        print("Entered medstation state")

        if "medstation" in jobs:
            state = handle_medstation(logger)
        else:
            state = "lavatory"

        print(f"State after medstation is {state}")

    elif state == "lavatory":
        print("Entered lavatory state")

        if "Lavatory" in jobs:
            state = handle_lavatory(logger)
        else:
            state = "bitcoin"

        print(f"State after lavatory is {state}")

    return state


def clip_that():
    import time

    from hideoutbot.bot.client import click

    click(x=1904, y=921)
    print("Saved a replay of that failure")
    time.sleep(3)
