from src.Table import Table


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
        return (sum([i.evaluate(i, self) for i in self.objectives]))

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