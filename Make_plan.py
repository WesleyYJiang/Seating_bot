import pandas as pd
from Guest import Guest
from Roster import Roster

# import Guests from csv
def importGuests(path):
    df = pd.read_csv(path)
    guests = []
    for index, row in df.iterrows():
        g = Guest(row[0], row[1], row[2], row[3], row[4], row[5],
                  row[6], row[7])
        guests.append(g)
    guest_book = Roster(guests)
    return guest_book
