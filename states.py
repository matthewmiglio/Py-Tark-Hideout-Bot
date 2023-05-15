

from client import restart_tarkov
from stations.bitcoin_miner import handle_bitcoin_miner
from stations.lavatory import handle_lavatory
from stations.medstation import handle_medstation
from stations.water_collector import handle_water_collector
from stations.workbench import handle_workbench


def state_tree(state,logger):
    

    if state == 'restart':
        #leads to medstation
        restart_tarkov(logger)
        state = 'medstation'

    elif state == 'medstation':
        #leads to workbench
        state = handle_medstation(logger)


    elif state == 'workbench':
        #leads to lavatory
        state = handle_workbench(logger)


    elif state == 'lavatory':
        #leads to water
        state = handle_lavatory(logger)


    elif state == 'water':
        #leads to bitcoin
        state = handle_water_collector(logger)


    elif state == 'bitcoin':
        #leads to medstation
        state = handle_bitcoin_miner(logger)


    return state