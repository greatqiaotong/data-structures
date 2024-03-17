import pytest

from src.detect_cycle import detect_cycle
from src.graph import Graph


@pytest.fixture
def empty_graph():
    g = Graph(1)
    return g


@pytest.fixture
def graph_with_circle():
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    return g


@pytest.fixture
def graph_without_circle():
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    return g


@pytest.mark.parametrize(
    "graph, expected",
    [
        ("empty_graph", False),
        ("graph_with_circle", True),
        ("graph_without_circle", False),
    ],
)
def test_detect_cycle(graph, expected, request):
    graph = request.getfixturevalue(graph)
    assert detect_cycle(graph) == expected
