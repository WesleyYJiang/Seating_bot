import random

# Represents the guest book, contains the list of guests
class Roster(object):
    # constructor
    def __init__(self, guest_list):
        self.guest_list = guest_list
        self.sortGuestList()
        self.parties = self.getParties()



    def swapRandom(self):
        idx = range(len(self.guest_list))
        i1, i2 = random.sample(idx,2)
        self.guest_list[i1], self.guest_list[i2] = self.guest_list[i2], self.guest_list[i1]

    def sortGuestList(self):
        self.guest_list.sort(key=lambda x: x.party, reverse=False)

    def getParties(self):
        result = set()
        for g in self.guest_list:
            result.add(g.party)
        return result

# Returns a dictionary mapping parties to lists of guests for the party
    def party_to_guests(self):
        map = { }
    # initialize the dictionary with parties as key and empty list of guests
        for p in self.getParties():
            map.update({p, []})
    # add guests to each party
        for g in self.guest_list:
            map[g.party].append(g)
        return map