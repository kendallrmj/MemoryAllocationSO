# Implementation:
# 1- Input memory blocks and processes with sizes.
# 2- Initialize all memory blocks as free.
# 3- Start by picking each process and find the
#    maximum block size that can be assigned to
#    current process i.e., find max(bockSize[1], 
#    blockSize[2],.....blockSize[n]) > 
#    processSize[current], if found then assign 
#    it to the current process.
# 5- If not then leave that process and keep checking
#    the further processes.

# Python3 implementation of worst - Fit algorithm 
  
# Function to allocate memory to blocks as 
# per worst fit algorithm 
def worstFit(blockSize, m, processSize, n):
      
    # Stores block id of the block 
    # allocated to a process 
      
    # Initially no block is assigned 
    # to any process 
    allocation = [-1] * n
      
    # pick each process and find suitable blocks 
    # according to its size ad assign to it 
    for i in range(n):
          
        # Find the best fit block for 
        # current process 
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1: 
                    wstIdx = j 
                elif blockSize[wstIdx] < blockSize[j]: 
                    wstIdx = j
  
        # If we could find a block for 
        # current process 
        if wstIdx != -1:
              
            # allocate block j to p[i] process 
            allocation[i] = wstIdx 
  
            # Reduce available memory in this block. 
            blockSize[wstIdx] -= processSize[i]
  
    print("Process No. Process Size Block no.")
    for i in range(n):
        print(i + 1, "         ", 
              processSize[i], end = "     ") 
        if allocation[i] != -1:
            print(allocation[i] + 1) 
        else:
            print("Not Allocated")
  
# Driver code 
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600] 
    processSize = [212, 417, 112, 426] 
    m = len(blockSize) 
    n = len(processSize) 
  
    worstFit(blockSize, m, processSize, n)
  
# This code is contributed by PranchalK