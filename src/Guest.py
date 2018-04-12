
class Guest:
    """""Represents an individual guest, contains all demographic details as fields
    
        Attributes:
            name: Name of the Guest
            age: Age of the Gust
            gender: gender 
            party: party
            college: college
            occupation: occupation
            residence: residence
            connection:  connection
            inclusion:  []
            exclusion: []
            categories: []
    """""

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
