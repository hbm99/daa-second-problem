from __future__ import annotations

from typing import List

from neighbor import Neighbor
from utils import dfs, model


def min_cost(graph: List[List[Neighbor]], vertices: List[int]) -> int:
    model_graph, weights = model(graph, vertices)
    
    min_cost = -1
 
    left = 0
    right = len(weights)
    
    while (left < right):
        mid = int((left + right) / 2)
        visited = [False] * len(vertices)
        result = []
        allowed_weight = weights[mid]
        for vertice in vertices:
            if visited[vertice]:
                continue
            dfs(model_graph, vertice, visited, allowed_weight, result)
        
        visited = [False] * len(vertices)
        dfs(model_graph, result[-1], visited, allowed_weight, [])
        
        if sum([1 if x else 0 for x in visited]) == len(vertices):
            min_cost = allowed_weight
            right = mid
        else:
            left = mid + 1
    return min_cost

