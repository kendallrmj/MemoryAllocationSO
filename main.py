import random
from Process import Process
from FirstFit import FirstFit
from BestFit import BestFit
from WorstFit import WorstFit
from BuddySystem import BuddySystem
from Draw import draw

dicProcesses = {}

def createProcesses(nProcesses, seed):
    dic = {}
    random.seed(seed)
    for i in range(nProcesses):
        dic["process" + str(i)] = Process(random.randint(1,256), random.randint(30,300))
    return dic


if __name__ == '__main__':
    dicProcesses = createProcesses(4, 10)

    firstFit = FirstFit(1024)
    bestFit = BestFit(1024)
    worstFit = WorstFit(1024)
    buddySystem = BuddySystem(1024)

    # # FIRST FIT SIMULATION
    # for process in dicProcesses:
    #     print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
    #     print("ANTES:\t\t" + str(firstFit.getMemory()))
    #     firstFit.allocate(process, dicProcesses[process].getMemQuantity())
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
    #     bestFit.allocate(process, dicProcesses[process].getMemQuantity())
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
    # for process in dicProcesses:
    #     print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
    #     print("ANTES:\t\t" + str(worstFit.getMemory()))
    #     worstFit.allocate(process, dicProcesses[process].getMemQuantity())
    #     print("DESPUES:\t" + str(worstFit.getMemory()))
    #     print('\n')

    # print("Remove process2:")
    # print("ANTES:\t\t" + str(worstFit.getMemory()))
    # worstFit.removeFromMemory(worstFit.getMemory()[2])
    # print("DESPUES:\t" + str(worstFit.getMemory()))
    # print('\n')

    # print("Remove process3:")
    # print("ANTES:\t\t" + str(worstFit.getMemory()))
    # worstFit.removeFromMemory(worstFit.getMemory()[3])
    # print("DESPUES:\t" + str(worstFit.getMemory()))
    # print('\n')

    # BUDDY SYSTEM SIMULATION
    for process in dicProcesses:
        print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
        print("ANTES:\t\t" + str(buddySystem.getMemory()))
        buddySystem.allocate(process, dicProcesses[process].getMemQuantity())
        print("DESPUES:\t" + str(buddySystem.getMemory()))
        print('\n')

    print("Remove process2:")
    print("ANTES:\t\t" + str(buddySystem.getMemory()))
    buddySystem.removeFromMemory(buddySystem.getMemory()[2])
    print("DESPUES:\t" + str(buddySystem.getMemory()))
    print('\n')

    print("Remove process3:")
    print("ANTES:\t\t" + str(buddySystem.getMemory()))
    buddySystem.removeFromMemory(buddySystem.getMemory()[3])
    print("DESPUES:\t" + str(buddySystem.getMemory()))
    print('\n')
    
    #draw(firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory())