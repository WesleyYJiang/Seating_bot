import numpy as np
import Guest as Guest

# represents all seats and people at a table
class Table:

    def __init__(self, capacity):
        # max number of people that can sit at a table
        self.capacity = capacity
        # current number of people sitting at the table
        self.guests = []

    def addGuest(self, guest):
        self.guests.append(guest)

    # calculate variance of ages at the table
    def ageVariance(self):
        ages = [i.age for i in self.guests]
        var = np.var(ages)
        return var

    # calculate score for BoyGirl Objective
    def boyGirl(self):
        genders = [i.gender for i in self.guests]
        counter = 0
        for i in range(len(genders) - 1):
            if (genders[i] == genders[i + 1]):
                counter += 2  # since you count both elements
        return counter

t = Table(3)
t.addGuest(Guest)
print(t.boyGirl())