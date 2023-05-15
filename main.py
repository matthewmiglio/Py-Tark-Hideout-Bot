from admin_check import check_if_program_is_running_in_admin
from logger import Logger
from bitcoin_miner import handle_bitcoin_miner
from client import get_to_hideout, orientate_tarkov_client
from lavatory import handle_lavatory
from medstation import handle_medstation
from water_collector import handle_water_collector
from workbench import handle_workbench

logger = Logger()

def main():
    orientate_tarkov_client()

    while 1:
        get_to_hideout()

        handle_bitcoin_miner(logger)

        handle_lavatory(logger)

        handle_workbench(logger)

        handle_water_collector(logger)

        handle_medstation(logger)


# main()
# orientate_tarkov_client()


"""
TODO

Add workbench get_items
medstation
lavatory switch to bleach
nutrition unit - ewr


"""
