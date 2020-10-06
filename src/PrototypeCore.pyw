"""
Prototype ALgorithms Core Prototypes Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.


"""

from queue import *
from Core_Stack import *

def util_comparator_fw(left, right):
    return left < right

def util_comparator_bw(left, right):
    return left > right

def util_comparator_eq(left, right):
    return left == right