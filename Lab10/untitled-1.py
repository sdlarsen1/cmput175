class MaxBinHeap():
    
    def __init__(self):
        self.heapList = [0]
        self.currentsize = 0
        
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self, item):
        self.heapList.append(item)
        self.currentsize += 1
        self.percUp(self.currentsize)
    
    def percDown(self, i):
        while (i * 2) <= self.currentsize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def maxChild(self, i):
        if i * 2 + 1 > self.currentsize: 
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentsize]
        self.currentsize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1    
    
        
def main():
    myHeap = MaxBinHeap()
    alist = [16, 12, 17, 3, 5, 2, 10, 9, 20, 14, 18, 22, 30, 25]
    #myHeap.buildHeap(alist)
    for x in alist:
        myHeap.insert(x)
    print(myHeap.heapList)
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
    print(myHeap.delMax())
main()