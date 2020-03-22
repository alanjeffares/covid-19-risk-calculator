import utils

class User:
    def __init__(self):
        self.age = None
        self.sex = None
        self.medical_risks = None
        self.symptoms = None
        self.local_risk = None
        self.city_infection_rate = 0.41

    def parse_responses(self, qa_list: list):
        """Extract responses and set them as class attributes"""
        [setattr(self, qa['attribute_name'], qa['response']) for qa in qa_list]

    def calculate_risk(self):

