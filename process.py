import random

class Process:

    def __init__(self, memQuantity, execTime, seed):
        random.seed(seed)
        self.setMemQuantity(memQuantity)
        self.setExecTime(execTime)
        self.setHeap([])
        self.setHasFinished(False)


    # GETTERS
    def getMemQuantity(self):
        return self.__memQuantity

    def getExecTime(self):
        return self.__execTime
    
    def getHeap(self):
        return self.__heap

    def getHasFinished(self):
        return self.__hasFinished


    # SETTERS
    def setMemQuantity(self, memQuantity):
        self.__memQuantity = memQuantity

    def setExecTime(self, execTime):
        self.__execTime = execTime

    def setHeap(self, heap):
        self.__heap = heap

    def setHasFinished(self, hasFinished):
        self.__hasFinished = hasFinished