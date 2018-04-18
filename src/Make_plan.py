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

def dominated(plan1, plan2):
    for key, value in plan1.items():
        if value > plan2[key]:
            return True
    return False

client = MongoClient()
db = client.plans
solutions = db.solutions
obj1 = Objective_gender()
obj2 = Objective_age()
og_plan = Plan(import_guests("/Users/wesleyjiang/Documents/GitHub"
                             "/Seating_bot/test/DS4300-Final-Project-Example-Data.csv"), 3, 5, [obj1, obj2])

#print(og_plan.info())

work = Working_agent(og_plan)


for i in range(5):
    work.random_swap()
    solutions.insert(work.p.info())
for document in solutions.find():
    print(document)
        # if not dominated(work.p.scores):
        #     db.insert(work.p)



