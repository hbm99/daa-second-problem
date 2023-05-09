
from typing import List, Tuple

from neighbor import Neighbor

def dfs(graph: List[List[Neighbor]], current: int, visited: List[bool], allowed_weight: int, result: List[int]) -> None:
    visited[current] = True
    for neighbor in graph[current]:
        if visited[neighbor.id]:
            continue
        if neighbor.weight > allowed_weight:
            continue
        dfs(graph, neighbor.id, visited, allowed_weight, result)
    result.append(current)
        
def model(graph: List[List[Neighbor]], vertices: List[int]) -> Tuple[List[List[Neighbor]], List[int]]:
    model_graph: List[List[Neighbor]] = [[] for _ in range(len(vertices))]
    weigths: List[int] = []
    
    for v in range(len(graph)):
        for neighbor in graph[v]:
            reverse_neighbor = Neighbor(v, 0)
            model_graph[neighbor.id].append(reverse_neighbor)
            
            original_neighbor = Neighbor(neighbor.id, neighbor.weight)
            model_graph[v].append(original_neighbor)
            
            weigths.append(neighbor.weight)
        
    weigths = sorted(list(set(weigths)))
    
    return model_graph, weigths