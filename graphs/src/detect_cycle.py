""" Detect cycle in a directed graph. Return True if a cycle exits, False if it doesn't."""
from src.graph import Graph


def detect_cycle(g: Graph) -> bool:
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return False

    visited = [False] * num_of_vertices
    rec_node_stack = [False] * num_of_vertices
    for i in range(num_of_vertices):
        if detect_cycle_rec(g, i, visited, rec_node_stack):
            return True
    return False


def detect_cycle_rec(
    g: Graph, node: int, visited: list[bool], rec_node_stack: list[bool]
) -> bool:
    if rec_node_stack[node]:
        return True
    if visited[node]:
        return False

    visited[node] = True
    rec_node_stack[node] = True
    temp = g.array[node].head_node
    while temp is not None:
        if detect_cycle_rec(g, temp.data, visited, rec_node_stack):
            return True
        temp = temp.next_element
    rec_node_stack[node] = False
    return False
