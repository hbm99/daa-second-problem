from __future__ import annotations

from typing import List

from utils import back_dfs, dfs, model
from neighbor import Neighbor


def min_cost(graph: List[List[Neighbor]], vertices: List[int]) -> int:
    model_graph, weights = model(graph, vertices)
    
    min_cost = -1
    
    for w in weights:
        visited = [False] * len(vertices)
        result = []
        for vertice in vertices:
            if visited[vertice]:
                continue
            dfs(model_graph, vertice, visited, w, result)
        
        visited = [False] * len(vertices)
        back_dfs(model_graph, result[-1], visited, w)
        
        if sum([1 if x else 0 for x in visited]) == len(vertices):
            min_cost = w
            break
    
    return min_cost
        
