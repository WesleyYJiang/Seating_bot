import numpy as np

class Objective_college:
    """The objective that tries to minimize number of unique colleges at a table, can be used in a Plan
    """

    def __init__(self):
        self.name = "college"

    def evaluate(self, plan):
        scores = [i.college_score() for i in plan.tables]
        score = np.mean(scores)
        return (score)