import numpy as np

# objective that evaluates how often a girl is sitting next to a boy and vice versa
class Objective_party:

    def __init__(self):
        self.name = 'party'

    def evaluate(self, plan):
        # calculate score for each table
        scores = [i.party_score() for i in plan.tables]
        # calculate average variance
        score = np.mean(scores)
        return (score)