import numpy as np

class Objective_age:
    """The objective that tries to minimize age, can be used in a Plan
    """

    def __init__(self):
        self.name = "age"

    def evaluate(self, plan):
        # calculate variance of ages at each table
        vars = [i.age_score() for i in plan.tables]
        # calculate average variance
        avgVar = np.mean(vars)
        return (avgVar)