"""
Prototype ALgorithms Core Prototypes Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.


"""

from collections import deque

class Stack(object):
    content: deque
    
    def __init__(self, other = None):
        if other == None:
            self.content = deque()
        else:
            self.content = deque(other)        

    def push(self, obj):
        self.content.append(obj)
        return self

    def pop(self):
        return self.content.pop()

    def peek(self):
        return self.content[len(self.content) - 1]

    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)
        return self
    
    def duplicate(self):
        a = self.pop()
        self.push(a)
        self.push(a)
        return self

    def rotate(self, rangerot):
        if rangerot > len(self.content):
            raise IndexError
        else:
            self.content.rotate(rangerot)
        return self
