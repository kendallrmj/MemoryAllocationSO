import random
import time
import threading

from Process import Process
from FirstFit import FirstFit
from BestFit import BestFit
from WorstFit import WorstFit
from BuddySystem import BuddySystem
from Queue import Queue
from Draw import Draw

dicProcesses = {}
dicProcessesTimes = {}
processQueue = Queue()

firstFit = FirstFit(2048)
bestFit = BestFit(2048)
worstFit = WorstFit(2048)
buddySystem = BuddySystem(2048)

def createProcesses(nProcesses, seed):
    random.seed(seed)
    for i in range(nProcesses):
        initialMem = random.randint(1,128)
        execTime = random.randint(30,300)
        name = "P" + str(i)

        dicProcesses[name] = Process(initialMem, execTime)
        dicProcessesTimes[name] = time.time()
        processQueue.queue(name)

        firstFit.allocate(name, initialMem)
        bestFit.allocate(name, initialMem)
        worstFit.allocate(name, initialMem)
        buddySystem.allocate(name, initialMem)

        time.sleep(random.randint(5, 20)/10)

def killProcess(processName):
    firstFit.killProcess(processName)
    bestFit.killProcess(processName)
    worstFit.killProcess(processName)
    buddySystem.killProcess(processName)
    del dicProcesses[processName]
    del dicProcessesTimes[processName]

if __name__ == '__main__':
    finished = False
    t = threading.Thread(target=createProcesses, args=(100, 10))

    t.start()

    while(not finished):
        currentProcess = processQueue.pop()
        choice = random.randint(0,2)

        # LIBERAR MEMORIA (NEW)
        if(choice == 0 and dicProcesses[currentProcess].getHeap()):
            heap = dicProcesses[currentProcess].getHeap()
            if(heap):
                toFree = random.choice(list(heap.keys()))
                firstFit.removeHeapFromMemory(currentProcess, heap[toFree])
                bestFit.removeHeapFromMemory(currentProcess, heap[toFree])
                worstFit.removeHeapFromMemory(currentProcess, heap[toFree])
                buddySystem.removeHeapFromMemory(currentProcess, heap[toFree])
                dicProcesses[currentProcess].removeFromHeap(toFree)

        # PEDIR MEMORIA (NEW)
        if(choice == 1):
            heapSize = random.randint(1,128)
            dicProcesses[currentProcess].addToHeap(heapSize)
            firstFit.allocate(currentProcess, heapSize)
            bestFit.allocate(currentProcess, heapSize)
            worstFit.allocate(currentProcess, heapSize)
            buddySystem.allocate(currentProcess, heapSize)

        # VERIFICA SI TERMINO EL PROCESO ACUTAL
        if(time.time() - dicProcessesTimes[currentProcess] >= dicProcesses[currentProcess].getExecTime()):
            killProcess(currentProcess)
        else:
            processQueue.queue(currentProcess)
        
        # VERIFICA SI TERMINARON TODOS LOS PROCESOS
        if(not dicProcesses):
            finished = True

        # print("FIRST FIT")
        # quantity, freeMem = firstFit.getMemStatus()
        # print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
        # print("MEMORIA DISPONIBLE:\t" + str(freeMem))
        # print("PROCESOS RECHAZADOS:\t" + str(firstFit.getRefusedProcesses()))
        # print(firstFit.getMemory())
        # print("-------------------------------------------------------------------------------------------------------")

        # print("BEST FIT")
        # quantity, freeMem = bestFit.getMemStatus()
        # print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
        # print("MEMORIA DISPONIBLE:\t" + str(freeMem))
        # print("PROCESOS RECHAZADOS:\t" + str(bestFit.getRefusedProcesses()))
        # print(bestFit.getMemory())
        # print("-------------------------------------------------------------------------------------------------------")

        # print("WORST FIT")
        # quantity, freeMem = worstFit.getMemStatus()
        # print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
        # print("MEMORIA DISPONIBLE:\t" + str(freeMem))
        # print("PROCESOS RECHAZADOS:\t" + str(worstFit.getRefusedProcesses()))
        # print(worstFit.getMemory())
        # print("-------------------------------------------------------------------------------------------------------")

        # print("BUDDY SYSTEM")
        # quantity, freeMem = buddySystem.getMemStatus()
        # print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
        # print("MEMORIA DISPONIBLE:\t" + str(freeMem))
        # print("PROCESOS RECHAZADOS:\t" + str(buddySystem.getRefusedProcesses()))
        # print(buddySystem.getMemory())
        # print("-------------------------------------------------------------------------------------------------------")

        # print("-------------------------------------------------------------------------------------------------------")
        # print("-------------------------------------------------------------------------------------------------------")

        time.sleep(1)
    
    print("FINISHED")
    
    #draw(firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory())