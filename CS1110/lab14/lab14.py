"""
A module with several recursive functions on sequences

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def sum_list(thelist):
    """
    Returns the sum of the integers in list thelist.

        Example: sum_list([34]) is 34
        Example: sum_list([7,34,1,2,2]) is 46

    Parameter thelist: the list to sum
    Precondition: thelist is a list of ints
    """
    #Handle Small Data
    if len(thelist) == 1:
        return thelist[0]
    elif thelist == []:
        return 0

    #Break Data into 2 Parts
    left = thelist[0]
    right = thelist[1:]

    #Add Parts
    return left + sum_list(right)

def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter v: The value to count
    Precondition: v is an int
    """
    #Small numbers
    if v not in thelist:
        return 0
    elif thelist == []:
        return 0
    elif len(thelist) == 1 and thelist[0] == v:
        return 1
    #Divide
    left = numberof(thelist[:1], v)
    right = thelist[1:]
    return  left + numberof(right, v)


# OPTIONAL EXERCISES

def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.

    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    # HINT: You can still do this with divide-and-conquer
    # The tricky part is combining the answers
    if thelist == []:
        return thelist
    elif len(thelist) == 1:
        return thelist

    left = thelist[:1]
    right = thelist[1:]

    if left[0] == right[0]:
        left = []

    return left + remove_dups(right)


def number_not(thelist, v):
    """
    Returns the number of elements in thelist that are NOT v.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    if v not in thelist:
        return len(thelist)
    elif len(thelist) == 1 and v in thelist:
        return 0

    left = thelist[:1]
    right = thelist[1:]

    return number_not(left, v) + number_not(right, v)



def remove_first(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).

    Note: This can be done easily using the method index. Don't do that.
    Do it recursively.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    count = thelist.count(v)
    if v not in thelist:
        return thelist

    left = thelist[:1]
    right = thelist[1:]
    if left == [v]:
        left = []
    if right.count(v) == thelist.count(v):
        return remove_first(left, v) + remove_first(right, v)
    else:
        return left+right

def Richie_Challenge(listo):
    new = listo[:]
    if len(listo)%2 != 0:
        new.append(0)
    final = []
    for x in range(0, len(new), 2):
        y = new[x] + new[x+1]
        final.append(y)
    return final

def pairswap(nlist):
    if len(nlist)%2!=0:
        list = nlist[:-1]
    else:
        list = nlist[:]
    for x in range(0, len(list), 2):
        a = list[x]
        b = list[x+1]
        nlist[x] = b
        nlist[x+1] = a

def colavg(table):
    rows = len(table)
    fin = []
    for x in range(rows):
        sum = 0
        for y in range(len(table[0])):
            a = table[x][y]
            sum = sum + a
        fin.append(sum/len(table[0]))
    return fin

def filter(nlist):
    if len(nlist)==0:
        return nlist
    left = nlist[:1]
    right = nlist[1:]

    if left[0] < 0:
        left = []
    return left + filter(right)
def sumlist(thelist):
    if len(thelist) == 1:
        return thelist[0]

    left = thelist[:1]
    right = thelist[1:]

    return sumlist(left) + sumlist(right)

def sum_nestedlist(thelist):
    if len(thelist) == 1 and type(thelist[0]) == int:
        return thelist[0]

    left = thelist[:1]
    right = thelist[1:]

    if type(left[0]) == list:
        left = sum_nestedlist(left[0])
    elif type(left[0]) == int:
        left = left[0]

    right = sum_nestedlist(right)
    return left + right

def encode(cipher, text):
    fin = ''
    for x in text:
        for y in cipher:
            if x == y:
                x = cipher[y]
        fin = fin + x
    return fin

def invert(cipher):
    for x in cipher:
        a = x
        b = cipher[x]
        del cipher[x]
        cipher[b] = a

def decode(nlist):
    if nlist == []:
        return ''
    left = nlist[:1]
    right = nlist[1:]

    left = left[0][0]*left[0][1]
    return left + decode(right)

def encode(text):
    if text == '':
        return []

    left = [[text[0],1]]
    right = text[1:]
    right = encode(right)

    if len(right) == 0:
        return left
    elif left[0][0] == right[0][0]:
        right[0][1] = right[0][1] + 1
        return right
    return left + right
