import math

class Heap:
    def __init__(self, mylist):
        self.heap = mylist
        first_leaf = math.floor(len(mylist)/2) 

        #starts at first parent
        for i in range(first_leaf):

        
    def heapify(self, index):
        #has a child
        if (2*index + 1 > len(self.heap)): return
        
        left = 2*index + 1
        right = left + 1
        # if has a right child
        if (2*index + 2 < len(self.heap)):
            right = left + 1

            #compare left and right child
            greater = 0
            if(self.heap[left] > self.heap[right]):
                greater = left
            else:
                greater = right

            if(self.heap[greater] > self.heap[index]):
                temp = self.heap[index]
                self.heap[index] = self.heap[greater]
                self.heap[greater] = temp
            return
        
        #no right child so just compare left child and heap
        else:
            #parent smaller than child
            if(self.heap[index] < self.heap[left]):
                temp = self.heap[index]
                self.heap[index] = self.heap[left]
                self.heap[left] = temp
            return
        

    def remove():

    