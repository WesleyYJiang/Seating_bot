import numpy as np


class Objective_age:

    def name(self):
        return "Age"

    def __init__(self):
        pass

    def evaluate(self, plan):
        # calculate variance of ages at each table
        vars = [i.age_variance() for i in plan.tables]
        # calculate average variance
        avgVar = np.mean(vars)
        return (avgVar)