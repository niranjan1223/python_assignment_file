# disjoint sets
def disjoint(s,A,B): #s is list
    a=set(A)
    b=set(B)
    happiness=0
    for i in s:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    return happiness