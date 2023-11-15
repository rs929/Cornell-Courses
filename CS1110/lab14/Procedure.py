def procedure(n):
    """
    procedure example
    """
    n = n + 12
    return n

def minlist(list):
    if len(list)==1:
        return list[0]

    left = list[0]
    right = list[1:]
    value = minlist(right)
    if left > value:
        left = value
    return left

def checklist(list):
    if len(list)==1:
        return True

    left = list[0]
    right = list[1:]

    value = left <= checklist(right)
    return value


def complement(n):
    if n == 0:
        return 0
    if n<10:
        return 10-n


    left = n//10
    right = n%10

    oop1 = complement(left)*10
    oop2 = complement(right)

    return oop1 + oop2


def complement2(n):
    if n == 0:
        return 0
    if n<10:
        return 10-n


    left = n//10
    right = n%10

    oop1 = complement(left)
    oop2 = complement(right)

    return int(str(oop1)+str(oop2))

def complement3(n):
    if n < 10:
        return 10 - n
    left = complement(n/10)
    right = 10 - n%10
    return left*10+right

def pairswap(n):
    first = None
    for i in n:
        if first is not None:
            yield i
            yield first
            first = None
        else:
            first = i

def deepsum(nlist):
    if nlist == []:
        return []
    left = nlist[0]
    right = nlist[1:]
    value = deepsum(right)
    bigboy = left + value
    sum = 0
    for i in bigboy:
        sum = sum +1
    return sum
