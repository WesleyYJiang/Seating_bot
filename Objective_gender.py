import numpy as np

# objective that evaluates how often a girl is sitting next to a boy and vice versa
class Objective_gender:

    def evaluate(self, plan):
        # calculate score for each table
        vars = [i.boyGirl() for i in self.tables]
        # calculate average variance
        score = np.mean(vars)
        return (score)