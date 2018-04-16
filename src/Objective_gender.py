import numpy as np

class Objective_gender:
    """The objective that evaluates how often a guest is sitting next to someone of the same gender, used in a Plan
    """

    def __init__(self):
        self.name = 'gender'

    def evaluate(self, plan):
        # calculate score for each table
        scores = [i.boy_girl() for i in plan.tables]
        # calculate average variance
        score = np.mean(scores)
        return (score)