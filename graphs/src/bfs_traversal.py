from src.graph import Graph, MyQueue


def bfs_traversal(g: Graph, source: int) -> str:
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    
    visited = [False] * num_of_vertices
    result, visited = bfs_traversal_helper(g, source, visited)

    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result
    

def bfs_traversal_helper(g: Graph, source: int, visited: list[bool]) -> tuple[str, list]:
    result = ""
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True

    while not queue.is_empty():
        current_node = queue.dequeue()
        result += str(current_node)

        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited
