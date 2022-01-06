from rules import Rules
from graph import drawGraph
from core import dataToTargetBFS
class Tests:
    def case1(self):
        rulesObj = Rules()
        rules = rulesObj.rules1()
        initial = [1,2,3,8]
        target = 14
        [reached, workingMemory] = dataToTargetBFS(rules, initial, target)

        drawGraph(rules, 'whole_graph_1');

        print(reached, workingMemory)
