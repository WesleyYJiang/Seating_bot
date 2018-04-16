import unittest
from src.Data_generator import data_generator
from src.Guest import Guest
from src.Roster import Roster
from src.Make_plan import import_guests
from src.Plan import Plan
from src.Objective_age import Objective_age
from src.Objective_gender import Objective_gender
from src.Table import Table
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
        p1 = Plan(ex2, 3, 6, [Objective_age(), Objective_gender()])
        v = p1.evaluate()
        print(v)
        self.assertEqual(type(v), dict)

    def test_boy_girl(self):
        ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        p1 = Plan(ex2, 3, 6, [Objective_age])
        self.assertEqual(p1.tables[0].boy_girl(), 6)


if __name__ == '__main__':
    unittest.main()
