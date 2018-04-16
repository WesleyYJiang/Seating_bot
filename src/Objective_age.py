import numpy as np


class Objective_age:

    def __init__(self):
        self.name = "age"

    def evaluate(self, plan):
        # calculate variance of ages at each table
        vars = [i.age_variance() for i in plan.tables]
        # calculate average variance
        avgVar = np.mean(vars)
        return (avgVar)