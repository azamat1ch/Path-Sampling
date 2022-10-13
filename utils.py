import random

def determineMotifType(G, S_l):
    """
    If the motif is cycled, then it is either a 3-cycle or a 4-cycle. If it is not cycled, then it is
    either a 1-path, a 2-path, or a 3-path
    
    :param G: the graph
    :param S_l: a list of 4 nodes, [u0, u, v, v0]
    :return: The number of edges in the motif.
    """
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
    """
    It returns a random neighbor of u, except for v.
    
    :param uNbrs: the neighbors of u
    :return: A random neighbor of u that is not v.
    """
    if len(uNbrs) == 1:
        return None
    while True:
        i = random.randint(0, len(uNbrs)-1)
        u0 = uNbrs[i]
        if u0 != v:
            break
    return u0

def sampleHigherDegNbr(G, uNbrs, v):
    """ 
    :param G: the graph
    :param uNbrs: the neighbors of u
    :param v: the node we're trying to find a neighbor for
    :return: a random neighbor of u that has a higher degree than v.
    """
    id = uNbrs.index(v)
    i = random.randint(id+1, len(uNbrs)-1)
    u0 = uNbrs[i]
    return u0