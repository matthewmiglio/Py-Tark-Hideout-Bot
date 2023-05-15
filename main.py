from bitcoin_miner import handle_bitcoin_miner
from client import get_to_hideout, orientate_tarkov_client
from lavatory import handle_lavatory
from medstation import handle_medstation
from water_collector import handle_water_collector
from workbench import handle_workbench


def main():
    orientate_tarkov_client()

    while 1:
        get_to_hideout()

        handle_bitcoin_miner()

        handle_lavatory()

        handle_workbench()

        handle_water_collector()

        handle_medstation()

main()
# orientate_tarkov_client()


"""
TODO

Add workbench get_items
medstation
lavatory switch to bleach
nutrition unit - ewr


"""
