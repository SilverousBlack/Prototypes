"""
Prototype Algorithms Core Prototypes Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.


"""

from PrototypeCore import *

def _util_eps_partition(target, offset, size, compfunc):
    ioff = offset
    aoff = offset - 1
    pivot = target[(offset + size) - 1]
    while (ioff < (offset + size)):
        if (compfunc(target[ioff], pivot)):
            aoff += 1
            itert = target[ioff]
            anchr = target[aoff]
            target[ioff] = anchr
            target[aoff] = itert
        ioff += 1
    aoff += 1
    anchr = target[aoff]
    target[aoff] = pivot
    target[(offset + size) - 1] = anchr
    return aoff

def ExchangePartitionSort(target, offset, size, compfunc):
    if ((offset + size) > offset):
        pivot = _util_eps_partition(target, offset, size, compfunc)
        lsz = pivot - offset
        rsz = size - pivot - 1
        if (lsz > 0):
            ExchangePartitionSort(target, offset, lsz, compfunc)
        if (rsz > 0):
            ExchangePartitionSort(target, pivot + 1, rsz, compfunc)
        

def QuickSort(target, compfunc):
    sz = len(target)
    if (sz == 0) or (sz == 1):
        return
    else:      
        ExchangePartitionSort(target, 0, sz, compfunc)
