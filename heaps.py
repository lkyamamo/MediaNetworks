import math

class Heap:
    def __init__(self, mydict):
        #note these lists will be lists of tuples where
        self.heap = mydict
        first_leaf = math.floor(len(mydict)/2) 

        #heapify all nodes from first parent
        for i in range(first_leaf):
            self.heapify(first_leaf - 1 - i)
        
    def heapify(self, index):
        #has a child
        if (2*index + 1 >= len(self.heap)): return
        
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

            #swap if appropriate
            print(self.heap[greater][1])
            if(self.heap[greater][1] > self.heap[index][1]):
                temp = self.heap[index]
                self.heap[index] = self.heap[greater]
                self.heap[greater] = temp
                self.heapify(greater)
            return
        
        
        #no right child so just compare left child and heap
        else:
            #parent smaller than child
            print(self.heap[left][1])
            if(self.heap[index][1] < self.heap[left][1]):
                temp = self.heap[index]
                self.heap[index] = self.heap[left]
                self.heap[left] = temp
                self.heapify(left)
            return
        

    def remove():
        return
    