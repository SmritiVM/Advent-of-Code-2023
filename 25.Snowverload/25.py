import re
def get_puzzle(path):
    with open(path) as file:
        parse_input(file)
    
def parse_input(file):
    #Return dot code for file
    dot = open("25.Snowverload\input_dot.txt","w")
    for line in file:
        nodes = re.findall('[a-z]+', line)
        newline = nodes[0] + ' -> ' + '{' + ', '.join(nodes[1:]) + '}' + '[dir=none]' + '\n'
        dot.write(newline)

path = "25.Snowverload\input.txt"
get_puzzle(path)

'''
Graphviz dot code for sample input
digraph G {

    jqt -> {rhn, xhk}[dir=none]
    rsh -> {frs, pzl, lsr}[dir=none]
    xhk -> hfx[dir=none]
    cmg -> {qnr, nvd, lhk}[dir=none]
    rhn -> {xhk, bvb, hfx}[dir=none]
    bvb -> {xhk, hfx}[dir=none]
    pzl -> {lsr, nvd}[dir=none]
    qnr -> nvd[dir=none]
    ntq -> {jqt, hfx, bvb, xhk}[dir=none]
    nvd -> lhk[dir=none]
    lsr -> lhk[dir=none]
    rzs -> {qnr, cmg, lsr, rsh}[dir=none]
    frs -> {qnr, lhk, lsr}[dir=none]
}
'''