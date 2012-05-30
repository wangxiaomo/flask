#-*- coding: utf-8 -*-

class Foo(object):
    __slots__ = ['storage']

    def __init__(self):
        object.__setattr__(self, 'storage', {})


if __name__ == '__main__':
    x = Foo()
    print dir(x)
    s = x.storage
    print s
    s["x"] = 3
    print s
