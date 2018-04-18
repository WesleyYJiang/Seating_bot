import random

class Working_agent:

    def __init__(self, plan):
        self.p = plan

    def rand_t(self):
        return random.randint(0, len(self.p.tables) - 1)
    def rand_seat(self, t):
        return random.randint(0, self.p.tables[t].size - 1)

    def random_swap(self):
        rand_t_1 = self.rand_t()
        rand_s_1 = self.rand_seat(rand_t_1)
        rand_t_2 = self.rand_t()
        rand_s_2 = self.rand_seat(rand_t_2)
        while rand_s_1 == rand_s_2 and rand_t_1 == rand_t_2:
            rand_2 = self.rand_seat(self.rand_t())
        g1 = self.p.tables[rand_t_1].guests[rand_s_1]
        g2 = self.p.tables[rand_t_2].guests[rand_s_2]
        self.p.tables[rand_t_1].guests.insert(rand_s_1, g2)
        self.p.tables[rand_t_2].guests.insert(rand_s_2, g1)

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