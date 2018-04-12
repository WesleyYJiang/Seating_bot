import numpy as np


class Objective_age:

    def __init__(self):
        pass

    def evaluate(self, plan):
        # calculate variance of ages at each table
        vars = [i.ageVariance() for i in plan.tables]
        # calculate average variance
        avgVar = np.mean(vars)
        return (avgVar)