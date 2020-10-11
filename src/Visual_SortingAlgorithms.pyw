"""
Prototype Algorithms Visualized Sorting Prototypes Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.


"""

from PrototypeCore import *

def _util_eps_partition(target, offset, size, compfunc):
    print("Executing `_util_eps_partition()`")
    print("Target [target]: %s [size: %s]" % (target, len(target)))
    print("Sort Partition Begin [offset]: %s" % offset)
    print("Sort Partition Range [size]: %s" % size)
    print("Sort Partition End: %s" % (offset + size - 1))
    print("Sorting: %s" % ("Smallest to Largest [Forward Comparator]" if compfunc(0, 1) else "Largest to Smallest [Backward  Comparator]"))
    print()
    ioff = offset
    aoff = offset - 1
    pivot = target[(offset + size) - 1]
    print("Selected pivot element: [%s] %s" % (((offset + size) - 1), pivot))
    print("Iterating through target...")
    print()
    while (ioff < (offset + size)):
        print(target)
        print("Iteration index: [%s] %s" % (ioff, target[ioff]))
        print("Anchor index: [%s] %s" % (aoff, target[aoff]))
        print()
        if (compfunc(target[ioff], pivot)):
            print("Comparator between iterator and pivot is true:")
            aoff += 1
            print("Incremented anchor index: %s" % aoff)
            print("Exchanging anchor and iterator...")
            itert = target[ioff]
            anchr = target[aoff]
            target[ioff] = anchr
            target[aoff] = itert
            print("Iteration index: [%s] %s" % (ioff, target[ioff]))
            print("Anchor index: [%s] %s" % (aoff, target[aoff]))
            print()
        ioff += 1
    print("Iteration ended.")
    aoff += 1
    print("Incremented anchor index: %s" % aoff)
    print("Exchanging anchor and pivot...")
    anchr = target[aoff]
    target[aoff] = pivot
    target[(offset + size) - 1] = anchr
    print("Anchor index: [%s] %s" % (aoff, target[aoff]))
    print("Pivot: [%s] %s" % (((offset + size) - 1), target[(offset + size) - 1]))
    print(target)
    print()
    return aoff

def ExchangePartitionSort(target, offset, size, compfunc):
    print("Executing `ExchangePartitionSort()`")
    print("Target: %s [size: %s]" % (target, len(target)))
    print("Sort Begin [Offset]: %s" % offset)
    print("Sort Range [Size]: %s" % size)
    print("Sort End: %s" % (offset + size - 1))
    print("Sorting: %s" % ("Smallest to Largest [Forward Comparator]" if compfunc(0, 1) else "Largest to Smallest [Backward  Comparator]"))
    print()
    if ((offset + size) > offset):
        print("Size is sufficient for sorting.")
        print("Calling partitioning function: `_util_eps_partition()`")
        print("Arguments:")
        print("\t> target: %s" % target)
        print("\t> offset: %s" % offset)
        print("\t> size: %s" % size)
        print("\t> comfunc: `%s`" % compfunc.__name__)
        print()
        pivot = _util_eps_partition(target, offset, size, compfunc)
        print("Pivot captured: [%s] %s" % (pivot, target[pivot]))
        print()
        lsz = pivot - offset
        rsz = size - pivot - 1
        if (lsz > 0):
            print("Left partition size is sufficient for sorting.")
            print("Calling recursion on left partition...")
            print("Arguments:")
            print("\t> target: %s" % target)
            print("\t> offset: %s" % offset)
            print("\t> size: %s" % lsz)
            print("\t> compfunc: `%s`" % compfunc.__name__)
            print()
            ExchangePartitionSort(target, offset, lsz, compfunc)
            print("Recursion Ended.")
            print()
        else:
            print("Left partition size is insufficient for sorting.")
            print()
        if (rsz > 0):
            print("Right partition size is sufficient for sorting.")
            print("Calling recursion on right partition...")
            print("Arguments:")
            print("\t> target: %s" % target)
            print("\t> offset: %s" % offset)
            print("\t> size: %s" % lsz)
            print("\t> compfunc: `%s`" % compfunc.__name__)
            print()
            ExchangePartitionSort(target, pivot + 1, rsz, compfunc)
            print("Recursion Ended.")
            print()
        else:
            print("Right partition size is insufficient for sorting.")
            print()
    else:
        print("Size is insufficient for sorting")
            
        

def QuickSort(target, compfunc):
    print("Executing `QuickSort()`...")
    print("Target: %s [size: %s]" % (target, len(target)))
    print("Sorting: %s" % ("Smallest to Largest [Forward Comparator]" if compfunc(0, 1) else "Largest to Smallest [Backward  Comparator]"))
    print()
    sz = len(target)
    if (sz == 0) or (sz == 1):
        print("Not enough size to sort.")
        return
    else:
        print("Calling recursive function: `ExchangePartitionSort()`")
        print("Arguments:")
        print("\t> target: %s " % (target))
        print("\t> offset: %s" % 0)
        print("\t> sz: %s" % sz)
        print("\t> compfunc: `%s`" % compfunc.__name__) 
        print()      
        ExchangePartitionSort(target, 0, sz, compfunc)
        print("Quicksort Ended.")
        print()
