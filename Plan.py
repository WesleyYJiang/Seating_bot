from Roster import Roster
from Table import Table
from Make_plan import importGuests

# main class that evaluates objectives given table
class Plan:

    # constructor
    def __init__(self, roster, numTables, tableSize, objectives):
        self.roster = roster
        self.tables = self.createTables(numTables, tableSize)
        self.objectives = objectives

    def createTables(self, num_t, t_cap):
        """Initialize a list of tables with a given number of tables and capacity per table
        
        :param numTables: The number of tables for this wedding plan
        :param tableSize: The capacity of each table 
        """
        tables = []
        for i in range(num_t):
            tables.append(Table(t_cap))
        return tables

    # evaluates plan based on objectives
    def evaluate(self):
        return (sum([i.evaluate(self) for i in self.objectives]))

    # assigns a guest to the next available
    def nxt_avail(self, guest):
        for t in self.tables:
            if t.size < t.capacity:
                t.addGuest(guest)
                break

    # Sit all the guests together by parties
    def assign_by_party(self):
        for k, v in self.roster.party_to_guests().items():
            for g in v:
                self.nxt_avail(g)