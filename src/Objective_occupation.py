import numpy as np

class Objective_occupation:
    """The objective that evaluates how many unique occupations are at the same table
    """

    def __init__(self):
        self.name = 'occupation'

    def evaluate(self, plan):
        # calculate score for each table
        scores = [i.occupation_score() for i in plan.tables]
        # calculate average variance
        score = np.mean(scores)
        return (score)