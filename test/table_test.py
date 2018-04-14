import unittest
from src.Data_generator import data_generator
from src.Guest import Guest
from src.Roster import Roster
from src.Make_plan import import_guests
from src.Plan import Plan
from src.Objective_age import Objective_age
import numpy as np
import pymongo

class TestingTables(unittest.TestCase):

        self.ex2 = import_guests('DS4300-Final-Project-Example-Data.csv')
        self.p1 = Plan(self.ex2, 3, 6, [Objective_age])

    def test_addGuest(self):
        self.assertEqual(True, False)

    def test_data_generator(self):
        ex1 = data_generator(5)
        self.assertEqual(len(ex1.guest_list), 5)
        self.assertEqual(type(ex1.guest_list[0]), Guest)

    def test_import_guests(self):
        self.assertEqual(len(self.ex2.guest_list), 18)
        self.assertEqual(type(self.ex2), Roster)
        self.assertEqual(type(self.ex2.guest_list[0]) == Guest)

    def test_get_parties(self):
        p = [i.party for i in self.ex2.guest_list]
        self.assertEqual(len(p), 18)
        self.assertEqual(type(p[0]), int)

    def test_assign_by_party(self):
        self.assertEqual(len(self.p1.tables), 3)
        self.assertEqual(self.p1.tables[0].capacity, 6)
        self.p1.assign_by_party()
        for i in range(3):
            self.assertLessEqual(len(self.p1.tables[i].guests) <= self.p1.tables[i].capacity)
            print()
            print(len(self.p1.tables[i].guests) >= 0)

    def test_ageVariance(self):
        v = self.p1.tables[0].ageVariance()
        self.assertEqual(type(v), np.float64)
        self.assertGreaterEqual(v, 0)

    def test_objective_age(self):
        o = Objective_age
        v = o.evaluate(o, self.p1)
        self.assertEqual(type(v), np.float64)
        self.assertGreaterEqual(v, 0)

    def test_plan_evaluate(self):
        v = self.p1.evaluate()
        self.assertEqual(type(v), np.float64)
        self.assertGreaterEqual(v > 0)


if __name__ == '__main__':
    unittest.main()
