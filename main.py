from graph_reader import Graph
from utils import *
import numpy as np
import pandas as pd
from scipy.special import comb
import random
import time
import os
# [0] 3-star
# [1] 3-path
# [2] tailed-triangle
# [3] 4-cycle
# [4] chordal-4-cycle
# [5] 4-clique
#   indexing of motifs for all arrays
A = np.array([[1, 0, 1, 0, 2, 4], 
              [0, 1, 2, 4, 6, 12],
              [0, 0, 1, 0, 4, 12],
              [0, 0, 0, 1, 1, 3],
              [0, 0, 0, 0, 1, 6],
              [0, 0, 0, 0, 0, 1]])

def threepathsampler(G, k):
    count = [0,0,0,0,0,0]
    C_hat = [0,0,0,0,0,0]
    sample = random.choices(G.Edges, weights= G.tauList, k = k)
    for u,v in sample:
        u0 = sampleNbr(G.adj[u], v)
        v0 = sampleNbr(G.adj[v], u)
        S_l = (u0, u, v, v0)
        if u0==v0 or u0==None or v0==None:
            continue
        motif = determineMotifType(G,S_l)
        count[motif]+=1
    for i in range(1,6): # from 2-1, to 6-1
        C_hat[i] = (count[i]/k) * (G.W/A[1,i])
    N1 = sum([comb(G.getDegree(v),3) for v in G.adj.keys()])
    C_hat[0] = N1 - C_hat[2] - 2*C_hat[4] - 4*C_hat[5]
    return C_hat

def centeredSampler(G, k):
    count = [0,0,0,0,0,0]
    C_hat = [0,0,0,0,0,0]
    successful_samples = 0
    sample = random.choices(G.Edges, weights=G.lambdaList, k=k)
    for u, v in sample:
        u0 = sampleHigherDegNbr(G, G.adj[u], v)
        v0 = sampleHigherDegNbr(G, G.adj[v], u)
        S_l = (u0, u, v, v0)
        if u0==None or v0==None or (not G.isEdge(u0,v0)):
            continue
        motif = determineMotifType(G,S_l)
        count[motif] += 1
        successful_samples+=1

    for i in range(3, 6):
        C_hat[i] = (count[i]/k) * (G.L/A[3,i])
    return C_hat

def computeFreq(G, k=200000):
    C_hat1 = threepathsampler(G, k)
    C_hat2 = centeredSampler(G, k)
    print("1 algo: ", [f"{num:.2e}" for num in C_hat1])
    print("2 algo: ", [f"{num:.2e}" for num in C_hat2])
    C_hat = C_hat1[:3]+C_hat2[3:]
    return C_hat

if __name__ == '__main__':
    folder =  os.path.join(os.getcwd(), 'data')
    final_df = pd.DataFrame(columns =['Graph', 'ReadingTime', 'ExeTime', 'countV', 'countE', 'W', 'L', 'W/L', '3star', '3path', 'tailed_triangle', '4cycle', 'chordal_4cycle', '4clique'])
    for file in os.listdir(folder):
        #file = 'as-skitter.txt'    
        path = os.path.join(folder, file)
        
        start_time = time.time()
        B = Graph(path)
        print(f'Graph {file} reading time: {time.time()-start_time:.0f} s')
        print(f"Number of edges {len(B.Edges):.2e}", f"Number of nodes {len(B.adj.keys()):.2e}", f"W is {B.W:.2e}, L is {B.L:.2e}, W/L is {B.W/B.L:.1f}")
        t1 = time.time()-start_time
        
        start_time = time.time()
        C_hat = computeFreq(B, k=200000)
        print([f"{num:.2e}" for num in C_hat])
        print(f'Exe time: {time.time()-start_time:.0f} s')
        t2 = time.time()-start_time
        record = {'Graph': file, 'ReadingTime':t1, 'ExeTime':t2, 'countV': len(B.adj.keys()), 'countE':len(B.Edges), 
                    'W': B.W , 'L': B.L, 'W/L': B.W/B.L,'3star': C_hat[0], '3path': C_hat[1], 
                    'tailed_triangle': C_hat[2], '4cycle': C_hat[3], 'chordal_4cycle': C_hat[4], '4clique': C_hat[5]}
        final_df = final_df.append(record, ignore_index=True)
        
        final_df.to_csv('as-skitter.csv', index=False)