class WorstFit:

    def __init__(self, memorySize):
        # BLOCK = ['E' for empty or 'P' for process, startPos, blockSize]
        self.setMemory([['E', 0, memorySize]])
        self.setMemorySize(memorySize)
        self.setRefusedProcesses([])
    
    # GETTERS
    def getMemory(self):
        return self.__memory

    def getRefusedProcesses(self):
        return self.__refusedProcesses

    def getMemorySize(self):
        return self.__memorySize


    # SETTERS
    def setMemory(self, memory):
        self.__memory = memory

    def setRefusedProcesses(self, refusedProcesses):
        self.__refusedProcesses = refusedProcesses

    def setMemorySize(self, memorySize):
        self.__memorySize = memorySize


    # FUNCTIONS
    def allocate(self, processName, processBlockSize):
        isAsigned = False
        worstFit = 0
        for block in self.getMemory():
            if(block[0] == 'E'):
                if(block[2] >= processBlockSize):
                    if(worstFit == 0 or block[2] > worstFit[2]):
                        worstFit = block
                        isAsigned = True
        if isAsigned:
            newBlock = []
            index = self.getMemory().index(worstFit)
            newBlock.append(processName)
            newBlock.append(worstFit[1])
            newBlock.append(processBlockSize)
            self.insertInMemory(index, newBlock)
        else:
            self.addRefusedProcess(processName)
    
    def addRefusedProcess(self, refusedProcess):
        tempList = self.getRefusedProcesses()
        tempList.append(refusedProcess)
        self.setRefusedProcesses(tempList)
    
    def removeFromMemory(self, e):
        tempMem = self.getMemory()
        index = tempMem.index(e)
        toRemove = []

        tempMem[index][0] = 'E'
        for i in range(len(tempMem) - 1):
            if(tempMem[i][0] == 'E' and tempMem[i + 1][0] == 'E'):
                tempMem[i + 1][1] = tempMem[i][1] 
                tempMem[i + 1][2] += tempMem[i][2]
                toRemove.append(tempMem[i])
        for e in toRemove:
            tempMem.remove(e)
        
        self.setMemory(tempMem)

    def insertInMemory(self, index, e):
        tempBlock = self.getMemory()[index]
        tempMem = self.getMemory()
        tempMem.insert(index, e)
        tempMem.remove(tempBlock)
        if(tempBlock[2] > 0 and (tempBlock[2] - e[2]) > 0):
            tempMem.insert(index + 1, ['E', e[1] + e[2], tempBlock[2] - e[2]])
        self.setMemory(tempMem)
