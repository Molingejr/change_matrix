import unittest
from structures.dependency_table import DependencyTable


class DependencyTableTest(unittest.TestCase):
    def setUp(self):
        self.dtable = DependencyTable()
        self.row = ['n1', 'm1', ['x1, x2'], ['Init. Values 1', 'Constraints 1', 'Proc. glue1'],
                    ['Instrum 1a'], 'a1->b1->c1']

    def test_add_node(self):
        
        self.dtable.add_node(self.row[0], self.row[1], self.row[2], self.row[3],
                             self.row[4], self.row[5])
        node = self.dtable.get_table()[-1]
        self.assertEqual(self.row, node)

    def test_delete_node(self):
        self.dtable.add_node(self.row[0], self.row[1], self.row[2], self.row[3],
                             self.row[4], self.row[5])
        self.dtable.delete_node(1)
        table = self.dtable.get_table()
        self.assertNotIn(self.row, table)


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
