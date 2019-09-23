from threading import Lock
class Mqueue:
    def __init__(self,maxsize=0):
        self.__data = []
        self.__isfull = False
        self.__maxsize = maxsize
        self.__isempty = True
        self.__lock = Lock()
        self.__lock.acquire() # 上锁
    def qsize(self):
        return len(self.__data)

    def get(self):
        if self.qsize()<=0:
            self.__lock.acquire()
        else:
            if self.__lock.locked():
                self.__lock.release()
        return self.__data.pop(0)
        
    def put(self,data):
        if self.qsize()>=self.__maxsize:
            self.__lock.acquire()
        self.__data.append(data)


    def full(self):
        if self.__maxsize==0 or self.__maxsize==-1:
            return False
        elif len(self.__data)==self.__maxsize:
            return True
        else:
            return False
    def empty(self):
        if len(self.__data)==0:
            return True
        else:
            return False


q = Mqueue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.full())
print(q.qsize())
print(q.empty())
print("get",q.get())
q.put(4)