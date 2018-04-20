import random

class Working_agent:

    def __init__(self, plan):
        self.p = plan

    def rand_t(self):
        return random.randint(0, len(self.p.tables) - 1)
    def rand_seat(self, t):
        return random.randint(0, self.p.tables[t].size - 1)

    def random_swap(self):
        t1 = self.rand_t()
        s1 = self.rand_seat(t1)
        t2 = self.rand_t()
        s2 = self.rand_seat(t2)
        while s1 == s2 and t1 == t2:
            s2 = self.rand_seat(t2)

        t = self.p.tables

        if(t[t1].guests[s1].age == 'child'):
            if not self.good_child_seat(t1, s1, t2, s2):
                self.random_swap()

        t[t1].guests[s1], t[t2].guests[s2] = t[t2].guests[s2], t[t1].guests[s1]

    def good_child_seat(self, t1, s1, t2, s2):

        t = self.p.tables

        tableSize = t[t2].capacity
        child = t[t1].guests[s1]
        good_child_seat = False

        if (len(t[t2].guests) > (s2 - 1) % tableSize):
            left_of_child = t[t2].guests[(s2 - 1) % tableSize]
            if (left_of_child.age == 'child' or left_of_child.party == child.party):
                good_child_seat = True

        if (len(t[t2].guests) > (s2 + 1) % tableSize):
            right_of_child = t[t2].guests[(s2 + 1) % tableSize]
            if (right_of_child.age == 'child' or right_of_child == child.party):
                good_child_seat = True

        return good_child_seat

    def rand_swap_within_table(self, tNum):
        rand_s_1 = self.rand_seat(tNum)
        rand_s_2 = self.rand_seat(tNum)
        while rand_s_1 == rand_s_2:
            rand_2 = self.rand_seat(self.rand_t())
        g1 = self.p.tables[tNum].guests[rand_s_1]
        g2 = self.p.tables[tNum].guests[rand_s_2]
        self.p.tables[tNum].guests.insert(rand_s_1, g2)
        self.p.tables[tNum].guests.insert(rand_s_2, g1)

    def shuffle_guests(self):
        self.plan.clearTables()
        self.plan.assign_random()