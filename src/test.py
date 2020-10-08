from Prototype import *
from copy import *

some = [80, 90, 70, 6, 50, 90, 70, 45]
build1 = TreeNode(6, 3)
build = TreeNode(6, 3, True, [build1])
another = TreeNode(6, "value", True, [build])
temp = another[[0, 0]]
another[[0, 0]] = TreeNode(6, "new")
another[0].set_uid(10)
another.attach_node(build1)
build = Stack()

QuickSort(some, util_comparator_fw)

print(another)
print(isinstance(build, CDSM))
print(some)