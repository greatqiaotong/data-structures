import pytest

from src.dfs_traversal import dfs_traversal
from src.graph import Graph


@pytest.fixture
def simple_graph():
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    return g


def test_dfs_traversal(simple_graph):
    result = dfs_traversal(simple_graph, 1)
    assert result == "1245360"