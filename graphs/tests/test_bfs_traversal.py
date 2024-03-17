import pytest

from src.bfs_traversal import bfs_traversal
from src.graph import Graph


@pytest.fixture
def simple_graph():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    return g


def test_bfs_traversal(simple_graph):
    result = bfs_traversal(simple_graph, 0)
    assert result == "02143"
