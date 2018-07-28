# Data Structures
This part of the project contains our data structures which interface with our application.

### Change Matrix
A change matrix, is a two-dimensional array whose rows and columns are defined as follows:
* Row 1: The ID of the structure resulting from a change, as identified by the change instance considered is held in
this cell.
* Row 2: The process(es) that induce the new structure placed in Row 1.
* Row 3 and 4: These are optional, as their values can be inferred from entries in row 1 and 2. Row 3 is the initial
source structure for Row 1; row 4 is any constraints on processes(or structures) worth examining.

Each column corresponds to a domain application level, and so its rows express the structures and processes as viewed
from the application domain. We have the following links relating changes:
* A **constraint link** or c-link from changes at higher domain application levels to those at lower levels.
* An **implementation link** or i-link from changes at lower domain application levels to those at higher levels.
* An **associated link** or a-link that groups nodes together according to criteria determined by the user of the system.

### Dependency Table
Initiative dependency is a table technically a **dependency graph** that records how structures and initiatives implement
others, when using the integration matrix. Each row in the table has a column for each of the following:
* reference stub
* list of independent structures
* Requisite implementation conditions.
The dependency link is abstractly a dependency graph where nodes are initiatives and arcs implementation constrains.

### Dependency Graph
This is a graph representation of the structures and process within a change matrix along with link between vertices.
* Contains vertices which represent nodes
* Contains edges (u, v) with links between vertices