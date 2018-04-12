from Roster import Roster
from Table import Table
from Make_plan import importGuests

# main class that evaluates objectives given table
class Plan:

    # constructor
    def __init__(self, roster, numTables, tableSize, objectives):
        self.roster = roster
        self.tables = self.createTables(numTables, tableSize)
        self.assignGuestsToTables()
        self.objectives = objectives

    # creates dictionary of empty tables
    def createTables(self, numTables, tableSize):
        tables = {}
        listOfDicts = [{i: Table(tableSize)} for i in range(numTables)]
        for i in listOfDicts:
            tables.update(i)
        return (tables)

    # evaluates plan based on objectives
    def evaluate(self):
        return (sum([i.evaluate(self) for i in self.objectives]))

    def __init__(self, roster, numTables, tableSize, objectives):
        self.roster = roster
        self.tables = self.createTables(numTables, tableSize)
        self.objectives = objectives

    # assigns a guest to the next avaliable
    def nxt_avail(self, guest):
        pass


    # Sit all the guests together by parties
    def assign_by_party(self):
        for guests in self.roster.getParties().ititervalues():
            for g in guests:
                self.nxt_avail(g)