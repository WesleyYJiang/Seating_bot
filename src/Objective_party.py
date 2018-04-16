import numpy as np

class Objective_party:
    """The objective that tries to minimize number of parties at a table, can be used in a Plan
    """

    def __init__(self):
        self.name = 'party'

    def evaluate(self, plan):
        # calculate score for each table
        scores = [i.party_score() for i in plan.tables]
        # calculate average variance
        score = np.mean(scores)
        return (score)