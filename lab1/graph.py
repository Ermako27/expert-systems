from graphviz import Digraph

def drawGraph(rules, graphName):
    graph = Digraph('{0}'.format(graphName), filename=graphName)
    graph.attr('node', shape='oval')
    for rule in rules:
        edge2 = '{}'.format(rule.consequent[0])
        for antecedent in rule.antecedents:
            edge1 = '{}'.format(antecedent)
            graph.edge(edge1, edge2)
    graph.render()

