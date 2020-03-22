import utils

class User:
    def __init__(self):
        self.age = None
        self.sex = None
        self.medical_risks = None
        self.symptoms = None
        self.local_risk = None
        self.city_infection_rate = 0.41



print(utils.json_loader('questions.json'))