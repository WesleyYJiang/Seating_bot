import numpy as np


class Table:
    """"Represents all seats and people at a table

        Attributes:
            capacity: The capacity of the table(number of guests can be seated)
            size: The number of guests currently sitting at the table
            guests: The list of guests currently sitting at the table
    """""

    def __init__(self, capacity):
        """"Adds a guest to the tabble 

            param guest: The guest to be added to this table 
        """""
        # max number of people that can sit at a table
        self.capacity = capacity
        # current number of people sitting at the table
        self.size = 0
        self.guests = []


    def addGuest(self, guest):
        """"Adds a guest to the tabble 

            param guest: The guest to be added to this table 
        """""
        if self.size < self.capacity:
            self.guests.append(guest)
            self.size += 1
        else:
            raise Exception('Table is Full!')


    def is_full(self):
        """Check if table is full

        return: boolean 
        """
        return self.size == self.capacity

    # calculate variance of ages at the table
    def ageVariance(self):
        if(len(self.guests) == 0):
            return 0
        ages = [i.age for i in self.guests]
        var = np.var(ages)
        return var

    # calculate score for BoyGirl Objective
    def boyGirl(self):
        genders = [i.gender for i in self.guests]
        counter = 0
        for i in range(len(genders) - 1):
            if (genders[i] == genders[i + 1]):
                counter += 2  #since you count both elements
        return counter

    def info(self):
        """Makes an a dictionary of guests (guests are dictionaries containing all the information)

        :return: a dictionary of all the guests
        """
        result = {}
        for g in self.guests:
            result.update({g.name : g.info()})
        return result