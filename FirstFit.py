class FirstFit:

    def __init__(self, memory):
        self.setMemory(memory)
        self.setRefusedProcesses([])
    
    # GETTERS
    def getMemory(self):
        return self.__memory

    def getRefusedProcesses(self):
        return self.__refusedProcesses


    # SETTERS
    def setMemory(self, memory):
        self.__memory = memory

    def setRefusedProcesses(self, refusedProcesses):
        self.__refusedProcesses = refusedProcesses


    # FUNCTIONS
    def allocate(self, process):
        isAsigned = False
        processBlockSize = process.getMemQuantity()
        for block in self.getMemory():
            if(block[0] == 'E' and not isAsigned):
                if(block[2] >= processBlockSize):
                    newBlock = []
                    index = self.getMemory().index(block)
                    newBlock.append('P')
                    newBlock.append(block[1])
                    newBlock.append(processBlockSize)
                    self.insertInMemory(index, newBlock)
                    isAsigned = True
                    break
        if not isAsigned:
            self.addRefusedProcess(process)
            

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
        if(tempBlock[2] > 0):
            tempMem.insert(index + 1, ['E', e[1] + e[2], tempBlock[2] - e[2]])
        self.setMemory(tempMem)