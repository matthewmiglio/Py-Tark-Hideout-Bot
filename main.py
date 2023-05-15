from bitcoin_miner import handle_bitcoin_miner
from client import get_to_hideout, orientate_tarkov_client
from lavatory import handle_lavatory
from workbench import handle_workbench


def main():
    orientate_tarkov_client()

    while 1:
        get_to_hideout()

        handle_bitcoin_miner()

        handle_lavatory()

        handle_workbench()


main()


"""
TODO

Add workbench get_items
medstation
lavatory switch to bleach
nutrition unit - ewr


"""
