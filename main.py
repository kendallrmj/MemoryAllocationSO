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
from Draw import Draw
from matplotlib.lines import Line2D

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


if __name__ == '__main__':
    # SEED
    random.seed(10)

    finished = False

    processNumber = 0
    createProcess(processNumber)
    dicProcessesTimes["nextProcess"] = time.time()
    nextProcessTime = random.randint(5,20)/10
    processNumber += 1

   
    custom_lines1 = [Line2D([0], [0], color=colors[x], lw=4) for x in range(25)]
    custom_lines2 = [Line2D([0], [0], color=colors[x], lw=4) for x in range(25,50)]
    custom_lines3 = [Line2D([0], [0], color=colors[x], lw=4) for x in range(50,75)]
    custom_lines4 = [Line2D([0], [0], color=colors[x], lw=4) for x in range(75,100)]
    
    fig, ax = plt.subplots()
    legend1 = plt.legend(custom_lines1, ["P"+str(x) for x in range(25)],loc='upper left', bbox_to_anchor=(1, 1))
    legend2 = plt.legend(custom_lines2, ["P"+str(x) for x in range(25,50)],loc='upper left', bbox_to_anchor=(1.1, 1))
    legend3 = plt.legend(custom_lines3, ["P"+str(x) for x in range(50,75)],loc='upper left', bbox_to_anchor=(1.2, 1))
    legend4 = plt.legend(custom_lines4, ["P"+str(x) for x in range(75,100)],loc='upper left', bbox_to_anchor=(1.3, 1))
    legendRam = plt.legend([Line2D([0], [0], color=colors[100], lw=4)], ["RAM"],loc='lower left', bbox_to_anchor=(1, 1))
    
    #plt.figure()
    ax.add_artist(legend1)
    ax.add_artist(legend2)
    ax.add_artist(legend3)
    ax.add_artist(legend4)
    ax.add_artist(legendRam)    
    
    plt.subplots_adjust(left=0.05,right=0.57, bottom=0.21)
    plt.get_current_fig_manager().full_screen_toggle()
    
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
                #print("MEMORY REMOVED")
                toFree = random.choice(list(heap.keys()))
                firstFit.removeHeapFromMemory(currentProcess, heap[toFree])
                bestFit.removeHeapFromMemory(currentProcess, heap[toFree])
                worstFit.removeHeapFromMemory(currentProcess, heap[toFree])
                buddySystem.removeHeapFromMemory(currentProcess, heap[toFree])
                dicProcesses[currentProcess].removeFromHeap(toFree)

        # PEDIR MEMORIA (NEW)
        if(choice == 1):
            #print("MEMORY ALLOCATED")
            heapSize = random.randint(1,128)
            dicProcesses[currentProcess].addToHeap(heapSize)
            firstFit.allocate(currentProcess, heapSize)
            bestFit.allocate(currentProcess, heapSize)
            worstFit.allocate(currentProcess, heapSize)
            buddySystem.allocate(currentProcess, heapSize)

        # VERIFICA SI TERMINO EL PROCESO ACUTAL
        if(time.time() - dicProcessesTimes[currentProcess] >= dicProcesses[currentProcess].getExecTime()):
            #print("KILLING PROCESS")
            killProcess(currentProcess)
        else:
            processQueue.queue(currentProcess)
        
        # VERIFICA SI TERMINARON TODOS LOS PROCESOS
        if(not dicProcesses):
            finishProcesses()
            finished = True
    
        dataArray=[[x[2],0,0,0] for x in firstFit.getMemory()]
        process = [x[0] for x in firstFit.getMemory()]
        
        dataBest=[[0,x[2],0,0] for x in bestFit.getMemory()]
        processBest = [x[0] for x in bestFit.getMemory()]

        dataWorst=[[0,0,x[2],0] for x in worstFit.getMemory()]
        processWorst = [x[0] for x in worstFit.getMemory()]

        dataBuddy=[[0,0,0,x[2]] for x in buddySystem.getMemory()]
        processBuddy = [x[0] for x in buddySystem.getMemory()]

        dataArray.extend(dataBest)
        dataArray.extend(dataWorst)
        dataArray.extend(dataBuddy)
        
        process.extend(processBest)
        process.extend(processWorst)
        process.extend(processBuddy)
        
        data = np.array(dataArray)
        X = np.arange(data.shape[1])
        for i in range(data.shape[0]):
            if process[i] == 'E':
                color = colors[100]
            else:
                color = colors[int(process[i])]
            plt.bar(X, data[i],bottom = np.sum(data[:i], axis = 0),color = color)
        plt.pause(0.1)
        
    plt.show()
    print("FIRST FIT")
    quantity, freeMem = firstFit.getMemStatus()
    print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
    print("MEMORIA DISPONIBLE:\t" + str(freeMem))
    print("PROCESOS RECHAZADOS:\t" + str(firstFit.getRefusedProcesses()))
    print(firstFit.getMemory())
    print("-------------------------------------------------------------------------------------------------------")

    print("BEST FIT")
    quantity, freeMem = bestFit.getMemStatus()
    print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
    print("MEMORIA DISPONIBLE:\t" + str(freeMem))
    print("PROCESOS RECHAZADOS:\t" + str(bestFit.getRefusedProcesses()))
    print(bestFit.getMemory())
    print("-------------------------------------------------------------------------------------------------------")

    print("WORST FIT")
    quantity, freeMem = worstFit.getMemStatus()
    print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
    print("MEMORIA DISPONIBLE:\t" + str(freeMem))
    print("PROCESOS RECHAZADOS:\t" + str(worstFit.getRefusedProcesses()))
    print(worstFit.getMemory())
    print("-------------------------------------------------------------------------------------------------------")

    print("BUDDY SYSTEM")
    quantity, freeMem = buddySystem.getMemStatus()
    print("SEGMEMTOS DISPONIBLES:\t" + str(quantity))
    print("MEMORIA DISPONIBLE:\t" + str(freeMem))
    print("PROCESOS RECHAZADOS:\t" + str(buddySystem.getRefusedProcesses()))
    print(buddySystem.getMemory())
    print("-------------------------------------------------------------------------------------------------------")
    
    print("FINISHED")