import numpy as np
import Plan as Plan

class Objective_age:

    def evaluate(self, plan):
        # calculate variance of ages at each table
        vars = [i.ageVariance() for i in self.tables]
        # calculate average variance
        avgVar = np.mean(vars)
        return (avgVar)