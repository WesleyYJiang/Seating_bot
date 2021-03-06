import random
from src.Guest import Guest
from src.Roster import Roster

# generates a random roster with the desired number of rows
def data_generator(numRows):

    # sample data
    names = ['Tim', 'Wes', 'John', 'Dan', 'Eddie']
    ages = ['child', 'teenager', 'young adult', 'adult', 'senior']
    genders = ['male', 'female']
    parties = range(1, numRows//2)
    residences = ['Boston', 'Roxbury', 'Cali', 'Connecticut', 'Shenzen']
    colleges = ['Northeastern', 'BU', 'Harvard', 'MIT']
    occupations = ['Data Scientist', 'Bio Engineer', 'Professor', 'Businessman']
    connections = ['Bride', 'Groom', 'Both']

    # start with empty guest list
    guestlist = []

    # add numRows randomguests to guest lsit
    for i in range(numRows):
        guest = Guest(random.choice(names), random.choice(ages), random.choice(genders), random.choice(parties),
                      random.choice(residences), random.choice(colleges), random.choice(occupations),
                      random.choice(connections))
        guestlist.append(guest)

    # return a roster with the guest list
    return (Roster(guestlist))

