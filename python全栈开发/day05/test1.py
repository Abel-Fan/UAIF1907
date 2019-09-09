# 简单工厂模式
class Car:
    def __init__(self):
        self.name="Car"

class Byd:
    def __init__(self):
        self.name = "BYD"

class Dz:
    def __init__(self):
        self.name = "大众"


class Factory:
    @classmethod
    def create(cls,type):
        if type==0:
            return Car()
        elif type==1:
            return Byd()
        else:
            return Dz()

c1 = Factory.create(1)
print(c1.name)