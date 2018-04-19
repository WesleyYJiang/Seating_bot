import pandas as pd
from src.Guest import Guest
from src.Objective_age import Objective_age
from src.Objective_college import Objective_college
from src.Objective_connection import Objective_connection
from src.Objective_gender import Objective_gender
from src.Objective_occupation import Objective_occupation
from src.Objective_party import Objective_party
from src.Roster import Roster
from src.Plan import Plan
import src
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
    tie = 0
    for key, value in plan1.items():
        if value > plan2[key]: result += 1
        if value < plan2[key]: result -= 1
        if value == plan2[key]: tie += 1
    if result == len(plan1) or (result + tie == len(plan1) and result > 0): return "dominate"
    if result <= 0: return "dominated"
    else: return "neither"

def print_solutions(s):
    print("*********************************FINAL Solutions****************************************")
    for document in s.find():
        print(document)

client = MongoClient()
db = client.plans
solutions = db.solutions
obj1 = Objective_gender()
obj2 = Objective_age()
og_plan = Plan(import_guests("DS4300-Final-Project-Example-Data.csv"), 3, 5,
               [obj1, obj2, Objective_college(), Objective_connection(), Objective_occupation(),
                Objective_party()])
solutions.delete_many({})
solutions.insert(og_plan.info())
work = Working_agent(og_plan)

for i in range(10000):
    # print("****************************ROUND***************************")
    # for document in solutions.find():
    #     print(document['Scores'])
    work.random_swap()
    sol_1 = work.p.info()['Scores']
    to_insert = False
    # print("CHECK:")
    # print(sol_1)
    for sol in solutions.find():
        sol_2 = sol['Scores']
        decision = compare_sol(sol_1, sol_2)
        # print("Compare: " + decision)
        if decision == "dominated":
            to_insert = False
            break
        if decision == "dominate":
            solutions.delete_one(sol)
            # print("DELETED: ")
            # print(sol['Scores'])
            to_insert = True
        if decision == "neither":
            to_insert = True
    if to_insert == True:
        solutions.insert(work.p.info())
        # print("INSERTED:")
        # print(work.p.info()['Scores'])

print_solutions(solutions)