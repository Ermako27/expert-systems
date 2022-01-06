class Rule:
    def __init__(self, config) -> None:
        self.name = config['name']
        self.antecedents = config['antecedents']
        self.consequent = config['consequent']
        

class Rules:
    def rules1(self):
        return [
            Rule({
                'name': 101,
                'antecedents': [1,2,3],
                'consequent': [4]
            }),
            Rule({
                'name': 102,
                'antecedents': [5,6],
                'consequent': [4]
            }),
            Rule({
                'name': 103,
                'antecedents': [4,8],
                'consequent': [9]
            }),
            Rule({
                'name': 104,
                'antecedents': [8,10,11],
                'consequent': [12]
            }),
            Rule({
                'name': 105,
                'antecedents': [12,13,6],
                'consequent': [14]
            }),
            Rule({
                'name': 106,
                'antecedents': [9],
                'consequent': [14]
            })
        ]