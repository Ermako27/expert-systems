from graphviz import Digraph
from core import contains

def drawGraph(rules, graphName):
    graph = Digraph('{0}'.format(graphName), filename=graphName)
    graph.attr('node', shape='oval')
    for rule in rules:
        edge2 = '{}'.format(rule.consequent[0])
        for antecedent in rule.antecedents:
            edge1 = '{}'.format(antecedent)
            graph.edge(edge1, edge2)
    graph.render()


def drawResultGraph(result, rules, graphName):
    graph = Digraph('{0}'.format(graphName), filename=graphName)
    graph.attr('node', shape='oval')

    for rule in rules:
        antecedents = rule.antecedents
        isContains = contains(antecedents, result);
        if isContains:
            for antecedent in rule.antecedents:
                edge1 = edge1 = '{}'.format(antecedent)
                edge2 = '{}'.format(rule.consequent[0])
                graph.edge(edge1, edge2)
    
    graph.render()

