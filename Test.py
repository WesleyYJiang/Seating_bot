from Data_generator import dataGenerator
from Guest import Guest
from Roster import Roster
from Make_plan import importGuests

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