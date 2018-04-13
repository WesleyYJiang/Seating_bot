import pandas as pd
from src.Guest import Guest
from src.Objective_age import Objective_age
from src.Objective_gender import Objective_gender
from src.Roster import Roster
from src.Plan import Plan
import pandas
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.solutions

# import Guests from csv
def importGuests(path):
    df = pandas.read_csv(path)
    guests = []
    for index, row in df.iterrows():
        g = Guest(row[0], row[1], row[2], row[3], row[4], row[5],
                  row[6], row[7])
        guests.append(g)
    guest_book = Roster(guests)
    return guest_book

# obj1 = Objective_gender()
# obj2 = Objective_age()
# og_plan = Plan(importGuests(" "), 3, 5, [obj1, obj2])
# db.insert(og_plan)
#