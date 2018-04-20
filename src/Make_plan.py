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
import random


# import Guests from csv
def import_guests(path):
    df = pandas.read_csv(path)
    guests = []
    for index, row in df.iterrows():
        rowNew = []
        for i in row:
            if(type(i) == str):
                rowNew.append(i.lower())
            else:
                rowNew.append(i)
        row = rowNew
        g = Guest(row[0], row[1], row[2], row[3], row[4], row[5],
                  row[6], row[7])
        guests.append(g)
    guest_book = Roster(guests)
    return guest_book

def compare_sol(plan1, plan2):
    result = 0
    tie = 0
    for key, value in plan1.items():
        if value < plan2[key]: result += 1
        if value > plan2[key]: result -= 1
        if value == plan2[key]: tie += 1
    if result == len(plan1) or (result > 0 and (result + tie == len(plan1))): return "dominate"
    if result <= 0: return "dominated"
    else: return "neither"

def get_random_doc(coll):
    # coll refers to your collection
    count = coll.count()
    return coll.find()[random.randrange(count)]

def get_optimal_sol(sols):
    optimal = []
    for s in sols.find():
        if len(optimal) == 0: optimal.append(s)
        else:
            final = []
            to_insert = False
            for o in optimal:
                decision = compare_sol(s['Scores'], o['Scores'])
                if decision == "dominated":
                    to_insert = False
                    break
                if decision == "dominate":
                    to_insert = True
                if decision == "neither":
                    to_insert = True
                    final.append(o)
            if to_insert == True:
                final.append(s)
                optimal = final
    return optimal

def update_dominance(sols, sol_1):
    for sol in sols.find():
        decision = compare_sol(sol_1['Scores'], sol['Scores'])
        if decision == "dominated": sol_1['Dominated_by'] += 1
        if decision == 'dominate':
            new = sol['Dominated_by']
            id = sol['_id']
            sols.update( {'_id': id}, { '$set' : {'Dominated_by' : new + 1}})

def delete_sol(sol):
    for s in sol.find():
        if s['Dominated_by'] >= 10:
            sol.delete_one(s)

client = MongoClient()
db = client.plans
solutions = db.solutions
og_plan = Plan(import_guests("tim_leah_guests.csv"), 14, 6,
               [Objective_gender(), Objective_age(), Objective_college(), Objective_connection(),
                Objective_occupation(), Objective_party()])
solutions.delete_many({})
solutions.insert(og_plan.info())
work = Working_agent(og_plan)

term = 0
i = 0
while term < 1000:
    random_sol = get_random_doc(solutions)
    plan = og_plan.update_seats(random_sol['Seating'])
    w = Working_agent(plan)
    w.random_swap()
    sol_1 = w.p.info()
    update_dominance(solutions, sol_1)
    if sol_1['Dominated_by'] != 0: term += 1
    if sol_1['Dominated_by'] == 0: term = 0
    solutions.insert(sol_1)

    if i % 1000 == 0:
        delete_sol(solutions)
        print(i)
    i += 1
sols = get_optimal_sol(solutions)
for s in sols:
    s.pop("Dominated_by")
    print(s)