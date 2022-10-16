import random
import time
import numpy as np
import matplotlib.pyplot as plt
from process import Process
from FirstFit import FirstFit
from BestFit import BestFit
from WorstFit import WorstFit
from BuddySystem import BuddySystem
from Queue import Queue


dicProcesses = {}
dicProcessesTimes = {}
processQueue = Queue()

firstFit = FirstFit(2048)
bestFit = BestFit(2048)
worstFit = WorstFit(2048)
buddySystem = BuddySystem(2048)

colors=[]
for i in range(0,101):
    r = lambda: random.randint(0,255)
    color='#%02X%02X%02X' % (r(),r(),r())    
    while color in colors:
        color='#%02X%02X%02X' % (r(),r(),r())
    colors.append(color)

def createProcess(processNumber):
    initialMem = random.randint(1,128)
    execTime = random.randint(30,300)
    name = str(processNumber)

    dicProcesses[name] = Process(initialMem, execTime)
    dicProcessesTimes[name] = time.time()
    processQueue.queue(name)

    firstFit.allocate(name, initialMem)
    bestFit.allocate(name, initialMem)
    worstFit.allocate(name, initialMem)
    buddySystem.allocate(name, initialMem)


def killProcess(processName):
    firstFit.killProcess(processName)
    bestFit.killProcess(processName)
    worstFit.killProcess(processName)
    buddySystem.killProcess(processName)
    del dicProcesses[processName]
    del dicProcessesTimes[processName]

def finishProcesses():
    buddySystem.finish()
    dicProcesses.clear()
    dicProcessesTimes.clear()
    processQueue.clear()

def draw(choice):
    if(choice != 2):
        dataArray, process = firstFit.getDataToDraw()
        dataBest, processBest =  bestFit.getDataToDraw()
        dataWorst, processWorst =  worstFit.getDataToDraw()
        dataBuddy, processBuddy =  buddySystem.getDataToDraw()

        dataArray.extend(dataBest) 
        dataArray.extend(dataWorst) 
        dataArray.extend(dataBuddy) 
         
        process.extend(processBest) 
        process.extend(processWorst) 
        process.extend(processBuddy) 

        data = np.array(dataArray)
        tcks = np.arange(20)
        X = np.arange(data.shape[1])
        for i in range(data.shape[0]):
            if process[i] == 'E':
                color = colors[100]
            else:
                color = colors[int(process[i])]
            bot = np.sum(data[:i], axis = 0)
            plt.bar(X, data[i],bottom = bot,color = color)


if __name__ == '__main__':
    # SEED
    random.seed(17)

    finished = False

    processNumber = 0
    createProcess(processNumber)
    dicProcessesTimes["nextProcess"] = time.time()
    nextProcessTime = random.randint(5,20)/10
    processNumber += 1

    while(not finished):
        currentProcess = processQueue.pop()
        choice = random.randint(0,2)

        # CREA NUEVO PROCESO
        if((time.time() - dicProcessesTimes["nextProcess"] >= nextProcessTime) and (processNumber < 100)):
            createProcess(processNumber)
            dicProcessesTimes["nextProcess"] = time.time()
            nextProcessTime = random.randint(5,20)/10
            processNumber += 1

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
            finishProcesses()
            finished = True
    
        draw(choice)
        plt.pause(0.1)
        
    plt.show()
    print("FINISHED")