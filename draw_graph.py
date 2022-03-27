# Author: jesus ponce
# GitHub: https://github.com/stronjol
# Date: 2022-03-27

from graphviz import Graph


def undirected_graph(wmat, name="weighted_undirected_graph"):

    n = len(wmat)
    f = Graph(name, filename=name+'.gv')
    f.attr('node', shape='circle')
    for i in range(n):
        f.node(str(i))

    for i in range(n):
        for j in range(n):
            if wmat[i][j] != 0 and i < j:
                f.edge(str(i), str(j), label=str(wmat[i][j]))

    return f.view()
