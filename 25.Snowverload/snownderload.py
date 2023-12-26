from networkx import Graph, minimum_cut
from itertools import combinations
from re import findall

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    COMPONENTS = Graph()
    for line in file:
        nodes = findall('[a-z]+', line)
        for node in nodes[1:]:
            COMPONENTS.add_edge(nodes[0], node, capacity=1)
    return COMPONENTS

def get_product_of_groups(COMPONENTS):
    for a, b in combinations(COMPONENTS.nodes, 2):
        cut, partition = minimum_cut(COMPONENTS, a, b)
        if cut == 3:
            return len(partition[0]) * len(partition[1])

path = "25.Snowverload\input.txt"
COMPONENTS = get_puzzle(path)
print(COMPONENTS)
print(get_product_of_groups(COMPONENTS))