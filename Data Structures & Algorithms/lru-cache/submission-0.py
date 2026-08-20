class LRUCache:

    def __init__(self, capacity: int):
        self.store={}
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        value=self.store[key]
        del(self.store[key])
        self.store[key]=value
        return value
        
    
    def put(self, key: int, value: int) -> None:
        if key not in self.store:
            self.store[key]=value
        else:
            del self.store[key]
            self.store[key]=value
            
        if len(self.store)>self.capacity:
            lru = list(self.store.keys())[0]
            del self.store[lru]


        
