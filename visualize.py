import ast
import graphviz

with open('graph.out') as f:
    graph = ast.literal_eval(f.read())

dot = graphviz.Digraph('chopsticks', format='svg', engine='sfdp')
dot.attr(overlap='prism', splines='false', fontsize='8')
dot.attr('node', shape='circle', style='filled', fontsize='6', width='0.3', height='0.3', fixedsize='true')
dot.attr('edge', arrowsize='0.3', color='#99999966')

for node in graph:
    if node == '0':
        dot.node(node, label='P1W', fillcolor='#4CAF50', fontcolor='white', shape='doublecircle', width='0.4')
    elif node == '1':
        dot.node(node, label='P2W', fillcolor='#F44336', fontcolor='white', shape='doublecircle', width='0.4')
    else:
        turn = int(node[0])
        label = f"{node[1]}{node[2]}|{node[3]}{node[4]}"
        if turn == 0:
            dot.node(node, label=label, fillcolor='#BBDEFB')
        else:
            dot.node(node, label=label, fillcolor='#FFCDD2')

for node, neighbors in graph.items():
    for neighbor in neighbors:
        dot.edge(node, neighbor)

dot.render('chopsticks_graph', cleanup=True)
print(f"Rendered chopsticks_graph.svg ({len(graph)} nodes, {sum(len(v) for v in graph.values())} edges)")
