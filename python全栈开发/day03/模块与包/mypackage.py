def mysum(*args):
    return sum(args)
def add():
    print("add")

from python全栈开发.day03.模块与包.mymodules.a.a2 import a2fun1



__all__ = ['mysum']

if __name__ =="__main__":
    print("mypackage被导入")
    print("abc")