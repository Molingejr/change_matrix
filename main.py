from structures.cmatrix import ChangeMatrix
from structures.dependency_graph import DependencyGraph
from structures.dependency_table import DependencyTable


from menu import start_menu


# Todo: Add try -- catch handlers to the functions in this module to prevent program breakdown
# Todo: program should use menus at appropriate locations rather just stream down


# Todo: Consider renaming this function
def start():
    links = ('c-link', 's-link', 'i-link', 't-link', 'p-link')
    choice = start_menu()
    if choice == 1:
        csource = ["Change Audits", "Basic Nature", "Business Issues",
                   "Mission & policies", "Technology"]
    elif choice == 2:
        csource = []
        # Todo: Should use a sentinel to create change sources
        for _ in range(int(input("How many change sources do you want to create: "))):
            csource.append(input("Enter change source: "))
    elif choice == 3:
        print("Exiting....")
        return

    print("Change source available are: ", csource)
    print("Create a set of viewpoints for one of the above change source")

    viewpoints = []
    # Todo: Should use a sentinel to create viewpoints
    v = int(input("How many viewpoints do you want to create: "))
    for _ in range(v):
        viewpoints.append(input("Enter viewpoint: "))

    print("\nCreating an empty change matrix with two rows and {} columns".format(len(viewpoints)))
    cmatrix = create_cmatrix(len(viewpoints))
    dgraph = create_dependency_graph()
    dtable = create_dependency_table()
    print("Change matrix created")
    print("An empty dependency graph has been created")
    print("An empty dependency table, created.")

    print("\nHere are your viewpoints ", viewpoints)

    # Todo: Need to differentiate between a structure and a process
    print("\nEnter a node to create or -1 to exit.")
    while True:
        node = input("Enter node: ")
        if node == "-1":
            break
        r, c = map(int, input("Enter position to store node (r c): ").split())
        cmatrix.add_node(node, r, c)
        dgraph.insert_vertex(node)
        dtable.add_node(node)

    print("\nHere is your updated change matrix")
    cmatrix.display_matrix()

    print("\nHere is your updated dependency table")
    dtable.display_table()

    print("\nHere is your updated dependency graph")
    for v in dgraph.vertices():
        print(v.element())

    # Todo: Establish differences between link types
    print("\nEnter two nodes and their link")
    #node1 = input("node 1: ")
    #node2 = input("node 2: ")


def create_cmatrix(column):
    # Todo: Validate the value of column
    return ChangeMatrix(column)


# Todo: This function has no special action. Delete it and replace its call with the object directly
def create_dependency_graph():
    return DependencyGraph()


# Todo: This function has no special actions. Delete it and replace it's call with the object directly
def create_dependency_table():
    return DependencyTable()


def display(matrix=None, table=None, graph=None):
    """Function to display data structures more visually"""
    def display_cmatrix():
        # Todo: Display change matrix contents along with row and column headers
        pass

    def display_dtable():
        # Todo: Display dependency table along with column headers
        pass

    def display_dgraph():
        # Todo: Visual preview of the dependency graph
        pass

    if matrix is not None:
        display_cmatrix()

    if table is not None:
        display_dtable()

    if graph is not None:
        display_dgraph()


if __name__ == "__main__":
    start()
