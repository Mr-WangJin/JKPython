# -*-coding:utf-8 -*-

class Single(object):
    _instance = None
    i = 1
    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = super(Single, cls).__new__(cls,*args, **kwargs)
            return cls._instance

if __name__ == "__main__":
    a = Single()
    print a.i
    a.i = 2
    b = Single()
    b.i = 3
    print a.i, b.i