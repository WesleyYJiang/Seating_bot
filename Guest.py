# Represents an individual guest, contains all demographic details as fields
class Guest:

    def __init__(self, name, age, gender, party, residence, college, occupation, connection):
        self.name = name
        self.age = age
        self.gender = gender
        self.party = party
        self.college = college
        self.occupation = occupation
        self.residence = residence
        self.connection = connection
        self.inclusion = []
        self.exclusion = []
        self.categories = []
