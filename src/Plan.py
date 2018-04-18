from src.Table import Table
import random


class Plan:
    """The class Plan represent a plan for the wedding, including a roster of guests, and their seating plan.
    """

    def __init__(self, roster, num_t, t_cap, objectives):
        """Constructor for the class Plan

        Args:
            roster (:obj: Roster): The roster for the wedding plan 
            num_t (int): The number of num tables for the wedding plan
            t_cap (int): The max capacity of each table
            objectives ('List' of :obj: Objective): The list of objectives to evaluate the plan  
            scores ('Dict' of string to int): A dictionary of scores for each objective  
        """
        self.roster = roster
        self.tables = self.createTables(num_t, t_cap)
        self.objectives = objectives
        self.scores = {}
        self.assign_by_party()

    def createTables(self, num_t, t_cap):
        """Initialize a list of tables with a given number of tables and capacity per table
        
        :param numTables: The number of tables for this wedding plan
        :param tableSize: The capacity of each table 
        """
        tables = []
        for i in range(num_t):
            tables.append(Table(t_cap))
        return tables

    def evaluate(self):
        """ Evaluates plan based on objectives
        """
        for obj in self.objectives:
            self.scores.update({obj.name : obj.evaluate(self)})
        return self.scores

    def nxt_avail(self, guest):
        """Search for the next available seat out of all the tables and assigns the guest to the seat. 
        
        Args:
            guest (:obj: Guest): The guest to be seated into the next available seat 
        """
        for t in self.tables:
            if t.size < t.capacity:
                t.addGuest(guest)
                break

    # Sit all the guests together by parties
    def assign_by_party(self):
        """Assigns all the guests to into their initial seats and sit them together according to their parties.
        """
        for k, v in self.roster.party_to_guests().items():
            for g in v:
                self.nxt_avail(g)
    def random_swap(self):
        rand_t_1 = random.randint(0,len(self.tables))
        rand_g_1 = self.tables[rand_t_1][random.randint(0, len(self.tables[rand_t_1]))]
        rand_t_2 = random.randint(0,len(self.tables))
        rand_g_2 = self.tables[rand_t_2][random.randint(0, len(self.tables[rand_t_2]))]




    def info(self):
        result = {}
        guests = {}
        count = 0
        for t in self.tables:
            guests.update({count : t.info()})
            count += 1
        result.update({"Seating" : guests})

        return result

