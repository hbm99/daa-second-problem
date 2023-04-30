
import random as rd
from typing import List

from min_cost_binary_search import min_cost as m_c_bs
from min_cost_lineal_search import min_cost as m_c_ls
from neighbor import Neighbor


def build_case():
    n = rd.randint(1, 10)
    m = rd.randint(0, (n * (n - 1))/ 2)
    edges = []
    
    for _ in range(m):
        source = rd.randint(0, n - 1)
        destination = rd.randint(0, n - 1)
        if source == destination or (source, destination) in edges:
            continue
        edges.append((source, destination))
    
    graph: List[List[Neighbor]] = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(Neighbor(edge[1], rd.randint(1, 100)))
    
    return graph, [i for i in range(n)]

if __name__ == '__main__':
    
    graph, vertices = build_case()
    
    print(m_c_ls(graph, vertices))
    print(m_c_bs(graph, vertices))
    