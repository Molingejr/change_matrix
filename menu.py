"""This module contains all the menus for our application"""

# Todo: Design the text user interface for our application


def main_menu():
    # Todo: construct a general menu to control the application
    pass


def start_menu():
    print("*************************************\n")
    print("1. Use default change sources")
    print("2. Create an array of change source")
    print("3. Exit\n")

    c = int(input("Enter choice: "))
    while c < 1 or c > 3:
        print("Choice doesn't exist")
        c = int(input("Enter choice: "))

    return c


def viewpoint_menu():
    "Displays menu for creating viewpoints"
    print("Create viewpoints")
    print("---------------------")
    print("1. Choose change source")
    print("2. Create viewpoints")

    c = int(input("Enter choice: "))
    while c < 1 or c > 2:
        print("Choice doesn't exist")
        c = int(input("Enter choice: "))

    return c


def matrix_menu():
    """Displays a menu to manipulates the change matrix class"""
    print("\nOPERATIONS ON THE CHANGE MATRIX")
    print("---------------------------------\n")
    print("1. Create change matrix")
    print("2. Add node")
    print("3. Delete node")
    print("4. Create link")  # This is option 4 in the dep_graph_menu
    print("5. Display change matrix")
    print("6. Quit\n")

    c = int(input("Enter a choice: "))
    while c < 1 or c > 6:
        print("Invalid choice")
        c = int(input("Enter choice: "))

    return c


def dep_graph_menu():
    """Displays the menu for manipulating the dependency graph"""
    print("\nOPERATIONS ON THE DEPENDENCY GRAPH")
    print("---------------------------------\n")
    print("1. Create the dependency graph")
    print("2. Add node")
    print("3. Delete node")
    print("4. Create an edge/link")
    print("5. Display dependency graph")
    print("6. Quit\n")

    c = int(input("Enter a choice: "))
    while c < 1 or c > 6:
        print("Invalid choice")
        c = int(input("Enter choice: "))

    return c


def dep_table_menu():
    """Displays a menu to manipulate the dependency table"""
    print("\nOPERATIONS ON THE DEPENDENCY TABLE")
    print("------------------------------------\n")
    print("1. Create dependency table")
    print("2. Add node")
    print("3. Delete node")
    print("4. Display dependency table")
    print("5. Quit\n")

    c = int(input("Enter a choice: "))
    while c < 1 or c > 5:
        print("Invalid choice")
        c = int(input("Enter choice: "))

    return c
