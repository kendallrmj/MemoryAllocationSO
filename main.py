from concurrent.futures import process
import random
import time
from process import Process

dicProcesses = {}

def createProcesses(nProcesses, seed):
    dic = {}
    random.seed(seed)
    for i in range(nProcesses):
        dic["process" + str(i)] = Process(random.randint(0,1000), random.randint(30,300), seed)
    return dic


def main():
    dicProcesses = createProcesses(4, 10)
    print(dicProcesses["process0"].getMemQuantity())

main()