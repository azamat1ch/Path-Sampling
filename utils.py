import random

def determineMotifType(G, S_l):
    u0, u, v, v0 = S_l
    num_edges =3
    cycled=False
    if G.isEdge(u0,v0):
        num_edges+=1
        cycled=True
    if G.isEdge(v, u0):
        num_edges+=1
    if G.isEdge(u, v0):
        num_edges+=1
    
    if num_edges in [5,6]:
        return num_edges-1
    elif num_edges==3:
        return 1
    else:
        if cycled: return 3
        else: return 2

def sampleNbr(uNbrs, v):
    if len(uNbrs) == 1:
        return None
    while True:
        i = random.randint(0, len(uNbrs)-1)
        u0 = uNbrs[i]
        if u0 != v:
            break
    return u0

def sampleHigherDegNbr(G, uNbrs, v):
    id = uNbrs.index(v)
    i = random.randint(id+1, len(uNbrs)-1)
    u0 = uNbrs[i]
    return u0