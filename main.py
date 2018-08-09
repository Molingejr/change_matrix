from structures.cmatrix import ChangeMatrix
from structures.dependency_graph import DependencyGraph
from structures.dependency_table import DependencyTable

from menu import start_menu


# Todo: Add more try -- except handlers to the functions in this module to prevent program breakdown
# Todo: program should use menus at appropriate locations rather just stream down
# Todo: Create data structures to represent viewpoints and change sources rather than use strings to represent them


# Todo: Consider renaming this function
def run():
    links = ('c-link', 's-link', 'i-link', 't-link', 'p-link')
    default_csources = ["Change Audits", "Basic Nature", "Business Issues", "Mission & policies", "Technology"]

    # Create an array of change sources with user inputs or default values
    choice = start_menu()
    if choice == 1:
        csources = default_csources
    elif choice == 2:
        csources = []
        while True:
            new_cs = input("Enter name of change source or -1 to exit: ")
            if new_cs == '-1':
                break
            csources.append(new_cs)
    elif choice == 3:
        print("Exiting....")
        return

    # Set change sources to default if user did not specify any
    if not csources:
        print("No change sources exist. Using default change sources...")
        csources = default_csources

    print("Change source available are: ", csources)

    # Allows user to choice change source to create viewpoints under
    print("\nCreate a set of viewpoints for one of the above change source")
    r = int(input("Enter the index of the change source: "))
    csource = csources[r]
    print("You have chosen to create viewpoints under the '{}' change source".format(csource))

    # Create an array of viewpoints with inputs from the user
    viewpoints = []
    while True:
        v = input("Enter viewpoint or -1 to exit: ")
        if v == '-1':
            break
        viewpoints.append(v)

    # Set viewpoints array to default if user failed to provide any
    if not viewpoints:
        print("No viewpoint created. Using default viewpoints...")
        viewpoints = ["Organisation & governance", "Business processes", "People", "Information (Asset)", "Technology"]

    print("\nCreating an empty change matrix with 2 rows and {} columns...".format(len(viewpoints)))
    cmatrix = create_cmatrix(len(viewpoints))
    dgraph = create_dependency_graph()
    dtable = create_dependency_table()

    print("Change matrix created")
    print("An empty dependency graph has been created")
    print("An empty dependency table, created.")

    print("\nHere are your viewpoints ", viewpoints)
    print("\nHere is your change matrix")
    display(matrix=cmatrix.get_matrix())

    # Insert a series of nodes into row 0 and row 1 of the change matrix as structures and processes respectively
    print("\nCreate processes and structures")
    print("----------------------------------")
    print("\nEnter a node to create or -1 to exit.")
    while True:
        node = input("Enter node: ")
        if node == "-1":
            break
        try:
            r = int(input("Enter 0 for structure and 1 for process:  "))
            c = int(input("Enter the column index to store node in: "))
            cmatrix.add_node(node, r, c)
            new_node = cmatrix.get_matrix()[r][c]
            dgraph.insert_vertex(node)
            dtable.add_node(node)
        except (IndexError, ValueError) as exc:
            print(exc)

    print("\nHere is your updated change matrix")
    display(matrix=cmatrix.get_matrix())

    print("\n\nHere is your updated dependency table")
    dtable.display_table()

    print("\nHere is your updated dependency graph")
    for v in dgraph.vertices():
        print(v.element())

    # Todo: Establish differences between link types
    print("\nEnter postions of two nodes and their link")
    print("Available links are ", links)
    new_link = True
    while new_link is True:
        try:
            node1 = tuple(map(int, input("node 1 index (r c): ").split()))
            node2 = tuple(map(int, input("node 2 index (r c): ").split()))
            node1 = cmatrix.get_data(*node1)
            node2 = cmatrix.get_data(*node2)
            link = input("Enter the link you wish to create: ")
            if (link in links) and (link == 'p-link'):
                # Todo: Ensure node1 is a process and node2 is a structure
                accept_link = True
            elif (link in links) and (link == 's-link'):
                # Todo: Ensure node1 is a structure and node2 is a process
                accept_link = True
            elif link in links:
                accept_link = True
            else:
                # Do not create links that are not available in our links array
                accept_link = False

            if accept_link:
                for v in dgraph.vertices():
                    if v.element() == node1:
                        node1 = v
                    elif v.element() == node2:
                        node2 = v
                dgraph.insert_edge(node1, node2, link)
            else:
                print("link is not available")

            cont = input("Do you want to create another one (y or n): ")
            if cont.lower() != 'y':
                new_link = False
        except Exception as exc:
            print(exc)
        
    print("Your updated graph is: ")

    vertices = []
    for e in dgraph.edges():
        e1, e2 = [v.element() for v in e.endpoints()]
        link = e.element()
        print(e1, e2, link)
        vertices.extend([e1, e2])

    for v in dgraph.vertices():
        if v.element() not in vertices:
            print(v.element())


def create_cmatrix(column: int = None):
    if column <= 0:
        column = None
    return ChangeMatrix(column)


# Todo: Consider deleting this function and replace its call with the object directly
def create_dependency_graph():
    return DependencyGraph()


# Todo: Consider deleting this function and replace it's call with the object directly
def create_dependency_table():
    return DependencyTable()


def display(matrix=None, table=None, graph=None):
    """Function to display data structures more visually"""
    def display_cmatrix():
        # Todo: Display change matrix contents along with row and column headers
        print("Structure", end='  ')
        for row in matrix[0]:
            print(row, end=' ')
        print("\nProcess", end='    ')
        for row in matrix[1]:
            print(row, end=' ')
        print()

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
    run()
