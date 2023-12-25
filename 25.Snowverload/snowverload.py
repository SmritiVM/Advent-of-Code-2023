from collections import defaultdict, deque
from re import findall

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Creating a component dictionary and generating the code for a dot file simultaneously
    dot = open("25.Snowverload\input.dot","w")
    dot.write("digraph G{\n")

    COMPONENT = defaultdict(set)
    for line in file:
        nodes = findall('[a-z]+', line)
        COMPONENT[nodes[0]].update(set(nodes[1:]))
        for node in nodes[1:]:
            COMPONENT[node].add(nodes[0])
            # For dot file
            newline = nodes[0] + ' -> ' + node + '[tooltip="' + nodes[0] + " to " + node + '"]' + '\n'
            dot.write(newline)
    dot.write('}')
    return COMPONENT

def get_product_of_groups(COMPONENT):
    remove_lines(COMPONENT)
    size1 = find_connected_group(COMPONENT, start="vgz")
    size2 = len(COMPONENT) - size1
    return size1 * size2

def remove_lines(COMPONENT):
    to_be_removed = [('hcd','cnr'), ('bqp','fqr'), ('fhv','zsp')] #hardcoded values based on observation from graphviz visualization
    for node1, node2 in to_be_removed:
        COMPONENT[node1].remove(node2)
        COMPONENT[node2].remove(node1)

def find_connected_group(COMPONENT, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for adjacent in COMPONENT[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited)

path = "25.Snowverload\input.txt"
COMPONENT = get_puzzle(path)
print(get_product_of_groups(COMPONENT))

'''
Copy pasted .dot code into an online graphviz compiler to generate svg file
Noted down the nodes that have to be removed from observation
hcd to cnr
bqp to fqr
fhv to zsp
'''