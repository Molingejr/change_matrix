import unittest
from structures.dependency_graph import DependencyGraph


class DependencyGraphTest(unittest.TestCase):
    def setUp(self):
        self.dgraph = DependencyGraph()
        self.edges = (
            ('n1', 'n2', 'c-link'), ('n2', 'n1', 'i-link'), ('n2', 'n4', 't-link'),
            ('n1', 'n3', 's-link'), ('n3', 'n1', 'p-link')
        )

    def test_edges(self):
        self.dgraph.graph_from_edge_list(self.edges)  # Add tuple of edges to graph

        # Displays a list of endpoints and their links
        for e in self.dgraph.edges():
            e1, e2 = [v.element() for v in e.endpoints()]
            link = e.element()
            self.assertIn((e1, e2, link), self.edges)


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
