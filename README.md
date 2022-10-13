### Path Sampling - Estimating 4-Vertex Subgraph Counts
In this project, I implemented a sampling algorithm from a paper titled “[Path sampling: A Fast and Provable Method for Estimating 4-Vertex Subgraph Counts” to estimate the frequencies of the 4-vertex subgraph.](https://arxiv.org/abs/1411.4942)"

### Background info 

Subgraph counting has played an important role in providing insights into the entire
graph’s structure. Moreover, it has been used as a powerful feature for matching and
recognizing patterns of the graph. However, the task of subgraph counting in a massive data set is extremely time and compute-intensive.

- For example: counting 4-vertex subgraphs for a Twitter graph with more than 21 million nodes, takes more than a week to finish using the exact counting algorithm.

In order to tackle this problem, research about subgraph counting shifted towards **estimating
subgraph frequencies**.

### Algorithm 
![motifs](/ph/motifs.png)

>The input of the algorithm is an undirected graph G = (V, E) - with n vertices and m edges, for vertex v, dv is the degree of v. Our aim is to get an estimate of all 𝐶 values where is the 𝑖 𝐶𝑖 number of induced occurrences of the i-th subgraph (i.e. i-th motif).

There are 2 processes to estimate all occurrences of each subgraph. 
* First is 3 path sampler : which samples a vanilla 3-path from the graph. But it does not produce accurate results for 4-cycles, chordal-4-cycle, and 4-clique.
* Hence, a better algorithm using centered-3 paths is proposed. The centered sampling is introduced because of the fact that every induced 4-cycle and chordal-4-cycle involves one centered 3-path and 4-clique involves three centered 3-paths.

**Please refer to the paper to understand math behind both algorithms.** 

### Results

> "Algorithm takes only a few minutes or even seconds to read the large graphs with millions of edges. For instance, it takes around 3 minutes to read the ‘cit-Pattents.txt’ graph with around 3M nodes and 16M edges." - Tested on 8GB Laptop

I tested the algorithm on the 7 datasets mentioned in paper. A graph below shows the error of each type of 4-vertex graph in seven different datasets. 
![results](/ph/results.png)
Algorithm performed well, obtaining less than 1% of error in counting all types of 4-vertex graphs except for 4-clique. In counting 4-clique graphs, we obtained the
highest error in As-skitter datasets which is 5.67%, however, this error is still within the acceptable error
bar.