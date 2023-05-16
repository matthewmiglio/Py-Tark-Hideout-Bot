from client import restart_tarkov
from stations.bitcoin_miner import handle_bitcoin_miner
from stations.generator import check_for_fuel
from stations.lavatory import handle_lavatory
from stations.medstation import handle_medstation
from stations.water_collector import handle_water_collector
from stations.workbench import handle_workbench


def state_tree(state, logger):
    if state == "restart":  # -> check_fuel
        # leads to medstation
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
        state = handle_medstation(logger)

    elif state == "workbench":
        # leads to lavatory
        state = handle_workbench(logger)

    elif state == "lavatory":
        # leads to water
        state = handle_lavatory(logger)

    elif state == "water":
        # leads to bitcoin
        state = handle_water_collector(logger)

    elif state == "bitcoin":
        # leads to medstation
        state = handle_bitcoin_miner(logger)

    return state
