import unittest
from structures.cmatrix import ChangeMatrix


class ChangeMatrixTest(unittest.TestCase):
    def setUp(self):
        self.viewpoints = ["Organisation & governance", "Business processes",
                           "People", "Information (Asset)", "Technology"]
        self.cmatrix = ChangeMatrix(len(self.viewpoints))

    def test_add_node(self):
        self.cmatrix.add_node('n1', 0, 0)
        node = self.cmatrix.get_matrix()[0][0]
        self.assertEqual(node, 'n1')

    def test_delete_node(self):
        self.cmatrix.add_node('n2', 0, 1)
        self.cmatrix.delete_node(0, 1)
        node = self.cmatrix.get_matrix()[0][1]
        self.assertEqual(node, None)


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
