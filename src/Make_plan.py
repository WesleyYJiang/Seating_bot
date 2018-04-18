import pandas as pd
from src.Guest import Guest
from src.Objective_age import Objective_age
from src.Objective_gender import Objective_gender
from src.Roster import Roster
from src.Plan import Plan
import pandas
import pymongo
from pymongo import MongoClient
from src.Work_agent import Working_agent
import json

# import Guests from csv
def import_guests(path):
    df = pandas.read_csv(path)
    guests = []
    for index, row in df.iterrows():
        g = Guest(row[0], row[1], row[2], row[3], row[4], row[5],
                  row[6], row[7])
        guests.append(g)
    guest_book = Roster(guests)
    return guest_book


def compare_sol(plan1, plan2):
    result = 0
    for key, value in plan1.items():
        if value > plan2[key]:
            result += 1
    if result == len(plan1): return "dominate"
    if result == 0: return "dominated"
    else: return "neither"

client = MongoClient()
db = client.plans
solutions = db.solutions
obj1 = Objective_gender()
obj2 = Objective_age()
og_plan = Plan(import_guests("DS4300-Final-Project-Example-Data.csv"), 3, 5, [obj1, obj2])
solutions.insert(og_plan.info())
#print(og_plan.info())

work = Working_agent(og_plan)


#solutions.delete_many({})

for i in range(10000):
    work.random_swap()
    sol_1 = work.p.info()['Scores']
    to_insert = False
    for sol in solutions.find():
        sol_2 = sol['Scores']
        decision = compare_sol(sol_1, sol_2)
        if decision == "dominate":
            solutions.delete_one(sol)
            to_insert = True
        if decision == "neither":
            to_insert = True
    if to_insert == True: solutions.insert(work.p.info())


for document in solutions.find():
    print(document)
    print(1)
        # if not dominated(work.p.scores):
        #     db.insert(work.p)



