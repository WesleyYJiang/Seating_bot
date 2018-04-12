from src.Data_generator import dataGenerator
from src.Guest import Guest
from src.Roster import Roster
from src.Make_plan import importGuests
from src.Plan import Plan
from src.Objective_age import Objective_age
import numpy as np

# test datagenerator
ex1 = dataGenerator(5)
print(len(ex1.guest_list) == 5)
print(type(ex1.guest_list[0]) == Guest)

# test importGuest
ex2 = importGuests('DS4300-Final-Project-Example-Data.csv')
print(len(ex2.guest_list) == 18)
print(type(ex2) == Roster)
print(type(ex2.guest_list[0]) == Guest)

# test getParties
print([i.party for i in ex2.guest_list])

# test assign_by_party
p1 = Plan(ex2, 3, 6, [Objective_age])
print(p1.tables)
p1.assign_by_party()

for i in p1.tables[0].guests:
    print(i.name + " " + str(i.party))
print("***********************")
for i in p1.tables[1].guests:
    print(i.name + " " + str(i.party))
print("***********************")
for i in p1.tables[2].guests:
    print(i.name + " " + str(i.party))

# test ageVariance (Table)
v = p1.tables[0].ageVariance()
print(type(v) == np.float64)
print(v > 0)

# test evaluate (Objective_age)
o = Objective_age
v = o.evaluate(o,p1)
print(type(v) == np.float64)
print(v > 0)

# test evaluate (Plan)
v = p1.evaluate()
print(type(v) == np.float64)
print(v > 0)