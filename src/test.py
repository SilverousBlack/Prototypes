from Prototype import *
from copy import *

some = [80, 90, 70, 6, 50, 90, 70, 45]

print(some)
print("Calling Sorting Function: `QuickSort()`")
print("Arguments:")
print("\t> target: %s" % some)
print("\t> compfunc: %s" % util_comparator_fw.__name__)
print()

visual.QuickSort(some, util_comparator_fw)

print(some)
