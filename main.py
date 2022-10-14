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

firstFit = FirstFit(1024)
bestFit = BestFit(1024)
worstFit = WorstFit(1024)
buddySystem = BuddySystem(1024)

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
        print(firstFit.getMemory())
        currentProcess = processQueue.pop()
        # PEDIR MEMORIA (NEW)
        if(random.randint(0,1) == 0):
            heapSize = random.randint(1,128)
            dicProcesses[currentProcess].addToHeap(heapSize)
            firstFit.allocate(currentProcess, heapSize)
            bestFit.allocate(currentProcess, heapSize)
            worstFit.allocate(currentProcess, heapSize)
            buddySystem.allocate(currentProcess, heapSize)
            print("ASIGNADO")

        # LIBERAR MEMORIA (NEW)
        if(random.randint(0,1) == 0):
            heap = dicProcesses[currentProcess].getHeap()
            if(heap):
                toFree = random.choice(list(heap.keys()))
                firstFit.removeFromMemory(currentProcess, heap[toFree])
                print("LIBERADO")

        if(time.time() - dicProcessesTimes[currentProcess] >= dicProcesses[currentProcess].getExecTime()):
            killProcess(currentProcess)
        if(not dicProcesses):
            finished = True
        processQueue.queue(currentProcess)
        time.sleep(1)
    
    print("FINISHED")
    
    #draw(firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory(), firstFit.getMemory())