import random

class Working_agent:

    def __init__(self, plan):
        self.p = plan

    def rand_t(self):
        return random.randint(0, len(self.p.tables))
    def rand_seat(self, t):
        return self.p.tables[t][random.randint(0, len(self.p.tables[t]))]

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


