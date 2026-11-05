class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity>0:
            self.cap=capacity
            self.arr=[0]*self.cap
            self.size=0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        if self.size<self.cap:
            self.arr[self.size]=n
            self.size+=1
        else:
            self.resize()
            self.arr[self.size]=n
            self.size+=1
            


    def popback(self) -> int:
        x=self.arr[self.size-1]
        self.size-=1
        self.arr[self.size]=0
        return x
 

    def resize(self) -> None:
        self.cap=self.cap*2
        n_arr=[0]*(self.cap)
        for i,x in enumerate(self.arr):
            n_arr[i]=x
        self.arr=n_arr



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.cap
