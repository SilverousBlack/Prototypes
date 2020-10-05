"""
Prototype Algorithms Core Library
(c) Silverous Black, 2020

Licence(s): MIT
Goals:
    * Create a enumeration classication class for:
        > Buffer Type
        > Container Type [Linear, Poly]
        > Algorithm Type
    * 
"""

from enum import Enum

@Enum.unique
class BufferType(Enum):
    Linear = 0 
    Circular = 1
    Reverse = 2
    ReverseCircular = 4
    Polyspace = 5

class CommonContainer():
    __size: int
    __bufferform: BufferType
    __buffer: []
    
    def __init__(self, size: int = 0, bufferform: BufferType = Polyspace):
        self.__size = size
        self.__bufferform = bufferform
        self.__buffer = [] * self.__size
    
    def access(self, index, range = 0):
        