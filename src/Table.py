import numpy as np
import math
import pandas as pd

class Table:
    """Represents all seats and people at a table

        Attributes:
            capacity: The capacity of the table(number of guests can be seated)
            size: The number of guests currently sitting at the table
            guests: The list of guests currently sitting at the table
    """

    def __init__(self, capacity):
        """Adds a guest to the table

            param guest: The guest to be added to this table 
        """
        # max number of people that can sit at a table
        self.capacity = capacity
        # current number of people sitting at the table
        self.size = 0
        self.guests = []

    def update(self, list_of_guests):
        self.guests = list_of_guests
        self.size = len(list_of_guests)

    def addGuest(self, guest):
        """Adds a guest to the table

            param guest: The guest to be added to this table 
        """
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

    def age_score(self):
        """returns the age_score for the table

        :return: the square of the number of age groups at the table
        """
        ageValues = {'child':0, 'teenager':1, 'young adult':2, 'adult':3, 'senior':4, np.nan: 5}
        ages = [i.age for i in self.guests if not pd.isnull(i.age)]
        newAges = [ageValues[i] for i in ages]
        counter = 0
        for i in range(len(newAges)):

            left = newAges[(i - 1) % self.size]
            right = newAges[(i - 1) % self.size]
            counter += abs(left - newAges[i])
            counter += abs(right - newAges[i])
        return counter

    # calculate score for boy_girl Objective
    def boy_girl(self):
        """returns the boy_girl score for the table

        :return: the number of guests at the table that are sitting next to someone with the same gender
        """
        genders = [i.gender for i in self.guests]
        counter = 0
        for i in range(len(genders)):
            if(i == len(genders) - 1):
                if(genders[i] == genders[0] or genders[i-1] == genders[i]):
                    counter += 1
            elif (genders[i] == genders[i + 1] or genders[i-1] == genders[i]):
                counter += 1
        return counter

    def party_score(self):
        """returns the party_score for the table
        """

        parties = [i.party for i in self.guests]
        counter = 0
        for i in range(len(parties)):

            left = parties[(i-1) % self.size]
            right = parties[(i-1) % self.size]
            if parties[i] == left and parties[i] == right:
                counter -= 1
            elif not parties[i] in [left, right]:
                counter += 1
        return counter

    def college_score(self):
        """returns the college_score for the table

        :return: the number of unique colleges attended at the table
        """
        colleges = [i.age for i in self.guests if not pd.isnull(i.college)]
        numNulls = len([i for i in self.guests if pd.isnull(i.college)])
        return math.pow(len(set(colleges)) + numNulls, 2)

    def occupation_score(self):
        """returns the occupation_score for the table

        :return: the number of unique occupations attended at the table
        """
        occupations = [i.occupation for i in self.guests if not pd.isnull(i.occupation)]
        numNulls = len([i for i in self.guests if pd.isnull(i.occupation)])
        return math.pow(len(set(occupations)) + numNulls,2)

        # calculate score for boy_girl Objective
    def connection_score(self):
        """return: the number of guests at the table that are sitting next to someone who has the same connection
        """
        connections = [i.connection for i in self.guests]
        counter = 0
        for i in range(len(connections)):

            left = connections[(i - 1) % self.size]
            right = connections[(i - 1) % self.size]
            if connections[i] == left and connections[i] == right:
                counter -= 1
            elif not connections[i] in [left, right]:
                counter += 1
        return counter

    def info(self):
        """Makes an a dictionary of guests (guests are dictionaries containing all the information)

        :return: a dictionary of all the guests
        """
        # result = {}
        # for g in self.guests:
        #     result.update({g.name : g.info()})
        # return result
        result = ""
        for g in self.guests:
            result = result + ',' + g.name

        return result[1:]

