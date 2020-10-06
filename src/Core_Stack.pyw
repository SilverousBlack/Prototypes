"""
Prototype Algorithms Core - Stack Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.

Python Stack
    PyStack Model 2
    Rapid Data Management
    RDM-S002
    
----- ----- ----- ----- -----
Object: Stack
Members:
    > __content (variable) - memory space
    > pull^ (function) - adds an element at the beginning of the stack 
    > receive^ (function) - removes and returns the first element
    > swap* (function) - exchanges the last two elements
    > rotate* (function) - rotates the contents based on the range of rotation
    > push* (function) - adds an element at the end
    > peek* (function) - "previews" the last element
    > pop* (function) - removes and returns the last element
    > duplicate* (function) - pops once then pushes twice
    > empty* (function) - states the emptiness of the container
----- ----- ----- ----- -----
* standard implementation requirement
^ model implementation, non-required implementation
"""

class Stack:
    __content = []
    
    def __init__(self, other = None):
        if other == None:
            self.__content = []
        else:
            self.__content = [] * len(other)
            for i in range(len(other) - 1):
                self.__content[i] = other[i]
        
    def pull(self, obj):
        temp = Stack(self.__content)
        del self.__content
        self.__content = [obj] + temp.__content
        return self
        
    def receive(self):
        temp = Stack(self.__content)
        del self.__content
        self.__content = [] * (len(temp.__content) - 2)
        for i in range(len(temp.__content) - 2):
            self.__content[i] = temp.__content[i + 1]
        return temp.__content[0]
            
    def swap(self):
        temp = self.__content[len(self.__content) - 2]
        self.__content[len(self.__content) - 2] = self.__content[len(self.__content) - 1]
        self.__content[len(self.__content) - 1] = temp
        return self
    
    def push(self, obj):
        self.__content = self.__content + [obj]
        return self
    
    def rotate(self, rotrange):
        if rotrange >= len(self.__content):
            raise IndexError
        else:
            temp = Stack(self.__content)
        return self
