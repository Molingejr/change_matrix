class DependencyTable:
    """Holds data for the dependency table"""
    def __init__(self):
        self._headers = ["Node ID", "Ref Stub", "Stub Args",
                         "Implemen Constraints", "Facilitating Instruments",
                         "Closure Remarks"]

        # Creates a table with headers at the first row
        self._table = [self._headers]

    def __len__(self):
        """Returns the length of the table"""
        return len(self._table)

    def add_node(self, nid: str, stub: str = "", args: list = [],
                 cons: list = [], fac_inst: list = [], remarks: str = ""):
        """
        Collects data for a new node and add the
        node to the table
        """
        node = [nid, stub, args, cons, fac_inst, remarks]
        self._table.append(node)

    def delete_node(self, r):
        """Deletes a node from the dependency table"""
        del self._table[r]

    def get_table(self):
        """Returns the dependency table"""
        return self._table

    def display_table(self):
        """Display the contents of the dependency table"""
        for r in self._table:
            for c in r:
                print(c, end="   ")
            print()
