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

    def info(self):
        """Makes an a dictionary of the guest and the information 
    
        :return: a dictionary of all the guest information 
        """
        return {
            'name' : self.name,
            'age' : self.age,
            'gender' : self.gender,
            'party' : self.party,
            'college' : self.college,
            'occupation' : self.occupation,
            'residence' : self.residence,
            'connection' : self.connection
        }