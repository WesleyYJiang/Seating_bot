import unittest
from src.Data_generator import data_generator
from src.Guest import Guest
from src.Roster import Roster
from src.Make_plan import import_guests
from src.Plan import Plan
from src.Objective_age import Objective_age
from src.Objective_gender import Objective_gender
from src.Objective_party import Objective_party
from src.Objective_college import Objective_college
from src.Objective_occupation import Objective_occupation
from src.Objective_connection import Objective_connection
from src.Table import Table
from src.Work_agent import Working_agent
import numpy as np
import pymongo

class TestingTables(unittest.TestCase):

    def test_data_generator(self):
        ex1 = data_generator(5)
        self.assertEqual(len(ex1.guest_list), 5)
        self.assertEqual(type(ex1.guest_list[0]), Guest)

    def test_import_guests(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        self.assertEqual(len(ex2.guest_list), 18)
        self.assertEqual(type(ex2), Roster)
        self.assertEqual(type(ex2.guest_list[0]), Guest)

    def test_get_parties(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p = [i.party for i in ex2.guest_list]
        self.assertEqual(len(p), 18)
        self.assertEqual(type(p[0]), int)

    def test_assign_by_party(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age])
        self.assertEqual(len(p1.tables), 3)
        self.assertEqual(p1.tables[0].capacity, 6)
        p1.assign_by_party()
        for i in range(3):
            self.assertLessEqual(len(p1.tables[i].guests), p1.tables[i].capacity)
            self.assertGreaterEqual(len(p1.tables[i].guests), 0)

    def test_age_variance(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age])
        for i in p1.tables:
            v = i.age_variance()
            print(type(v))
            self.assertEqual(type(v), np.float64)
            self.assertGreaterEqual(v, 0)
        t = Table(5)
        self.assertEqual(t.age_variance(), 0)

    def test_objective_age(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age])
        o = Objective_age
        v = o.evaluate(o, p1)
        self.assertEqual(type(v), np.float64)
        self.assertGreaterEqual(v, 0)

    def test_plan_evaluate(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age(), Objective_gender(), Objective_party(), Objective_college(),
                              Objective_occupation(), Objective_connection()])
        v = p1.evaluate()
        print(v)
        self.assertEqual(type(v), dict)

    def test_boy_girl(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age])
        self.assertEqual(p1.tables[0].boy_girl(), 6)

    def test_swapper(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age(), Objective_gender(), Objective_party(), Objective_college(),
                              Objective_occupation(), Objective_connection()])
        w = Working_agent(p1)
        print("before")
        for t in range(0,len(w.p.tables)):
            names1 = [i.name for i in w.p.tables[t].guests]
            print(names1)
        w.random_swap()
        print("after")
        for t in range(0,len(w.p.tables)):
            names2 = [i.name for i in w.p.tables[t].guests]
            print(names2)

        '''bool = False
        for t in range(0,len(w.p.tables)):
            if w1.p.tables[t].guests != w2.p.tables[t].guests:
                bool = True
        self.assertEqual(bool, True)'''

if __name__ == '__main__':
    unittest.main()