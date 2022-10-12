from concurrent.futures import process
import random
from Process import Process
from FirstFit import FirstFit

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

    # FIRST FIT SIMULATION
    for process in dicProcesses:
        print(process + " size:\t" + str(dicProcesses[process].getMemQuantity()))
        print("ANTES:\t\t" + str(firstFit.getMemory()))
        firstFit.allocate(dicProcesses[process])
        print("DESPUES:\t" + str(firstFit.getMemory()))
        print('\n')

    print("Remove process2:")
    print("ANTES:\t\t" + str(firstFit.getMemory()))
    firstFit.removeFromMemory(firstFit.getMemory()[2])
    print("DESPUES:\t" + str(firstFit.getMemory()))
    print('\n')

    print("Remove process3:")
    print("ANTES:\t\t" + str(firstFit.getMemory()))
    firstFit.removeFromMemory(firstFit.getMemory()[3])
    print("DESPUES:\t" + str(firstFit.getMemory()))
    print('\n')