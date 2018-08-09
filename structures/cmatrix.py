class ChangeMatrix:
    """
    The change matrix data structure
    """
    def __init__(self, column=None):
        """Creates and initializes the matrix"""
        if column is None:
            self._matrix = [[], []]  # Sets an empty matrix
        else:
            # Sets an empty matrix with the size of the viewpoints
            self._matrix = [[None]*column, [None]*column]

    def __len__(self):
        """Return the length of the matrix"""
        len(self._matrix)

    def add_node(self, node, *pos):
        """This adds a node to the matrix at a given position."""
        try:
            r, c = pos
            self._matrix[r][c] = node
        except IndexError:
            print("Location does not exist")

    def delete_node(self, *pos):
        """THis deletes a node on the matrix at a given position."""
        try:
            r, c = pos
            if self._matrix[r][c] is None:
                raise IndexError

            self._matrix[r][c] = None
        except IndexError:
            print("Location or node does not exist.")

    def add_column(self):
        """Adds a column at the end of the matrix"""
        for i in range(len(self._matrix)):
            self._matrix[i].append(None)

    def delete_column(self, pos: int):
        """Deletes a column from the grid"""
        for i in range(len(self._matrix)):
            del self._matrix[i][pos]

    def add_row(self):
        """Adds a new row at the end of the matrix"""
        self._matrix.append([None]*len(self._matrix[0]))

    def delete_row(self, r: int):
        """Deletes a row other than the first two row"""
        if r <= 1:
            print("Cannot delete that row. It is needed to effect change")
            return
        del self._matrix[r]

    def get_data(self, *pos):
        try:
            r, c = pos
            return self._matrix[r][c]
        except IndexError as exc:
            print(exc)

    def get_matrix(self):
        """Returns the matrix"""
        return self._matrix

    def display_matrix(self):
        """Displays the contents of the matrix"""
        for row in self._matrix:
            for col in row:
                print(col, end=" ")
            print()
