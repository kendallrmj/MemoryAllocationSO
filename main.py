import random
from Process import Process
from FirstFit import FirstFit
from BestFit import BestFit
from WorstFit import WorstFit

dicProcesses = {}

def createProcesses(nProcesses, seed):
    dic = {}
    random.seed(seed)
    for i in range(nProcesses):
        dic["process" + str(i)] = Process(random.randint(0,10), random.randint(30,300))
    return dic


if __name__ == '__main__':
    dicProcesses = createProcesses(4, 10)

    # BLOCK = ['E' for empty or 'P' for process, startPos, blockSize]
    firstFit = FirstFit([['E', 0, 1000]])
    bestFit = BestFit([['E', 0, 1000]])
    worstFit = WorstFit([['E', 0, 1000]])

    # FIRST FIT SIMULATION
    # for process in dicProcesses:
    #     print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
    #     print("ANTES:\t\t" + str(firstFit.getMemory()))
    #     firstFit.allocate(dicProcesses[process])
    #     print("DESPUES:\t" + str(firstFit.getMemory()))
    #     print('\n')

    # print("Remove process2:")
    # print("ANTES:\t\t" + str(firstFit.getMemory()))
    # firstFit.removeFromMemory(firstFit.getMemory()[2])
    # print("DESPUES:\t" + str(firstFit.getMemory()))
    # print('\n')

    # print("Remove process3:")
    # print("ANTES:\t\t" + str(firstFit.getMemory()))
    # firstFit.removeFromMemory(firstFit.getMemory()[3])
    # print("DESPUES:\t" + str(firstFit.getMemory()))
    # print('\n')

    # BEST FIT SIMULATION
    # for process in dicProcesses:
    #     print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
    #     print("ANTES:\t\t" + str(bestFit.getMemory()))
    #     bestFit.allocate(dicProcesses[process])
    #     print("DESPUES:\t" + str(bestFit.getMemory()))
    #     print('\n')

    # print("Remove process2:")
    # print("ANTES:\t\t" + str(bestFit.getMemory()))
    # bestFit.removeFromMemory(bestFit.getMemory()[2])
    # print("DESPUES:\t" + str(bestFit.getMemory()))
    # print('\n')

    # print("Remove process3:")
    # print("ANTES:\t\t" + str(bestFit.getMemory()))
    # bestFit.removeFromMemory(bestFit.getMemory()[3])
    # print("DESPUES:\t" + str(bestFit.getMemory()))
    # print('\n')

    # WORST FIT SIMULATION
    for process in dicProcesses:
        print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
        print("ANTES:\t\t" + str(worstFit.getMemory()))
        worstFit.allocate(dicProcesses[process])
        print("DESPUES:\t" + str(worstFit.getMemory()))
        print('\n')

    print("Remove process2:")
    print("ANTES:\t\t" + str(worstFit.getMemory()))
    worstFit.removeFromMemory(worstFit.getMemory()[2])
    print("DESPUES:\t" + str(worstFit.getMemory()))
    print('\n')

    print("Remove process3:")
    print("ANTES:\t\t" + str(worstFit.getMemory()))
    worstFit.removeFromMemory(worstFit.getMemory()[3])
    print("DESPUES:\t" + str(worstFit.getMemory()))
    print('\n')
    