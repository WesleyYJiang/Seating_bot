import numpy as np

class Objective_connection:
    """The objective that evaluates how often a guest is sitting next to someone who has the same connection
    (knows bride, knows groom)
    """

    def __init__(self):
        self.name = 'connection'

    def evaluate(self, plan):
        # calculate score for each table
        scores = [i.connection_score() for i in plan.tables]
        # calculate average variance
        score = np.mean(scores)
        return (score)