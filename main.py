import numpy as np
import utils

class User:
    def __init__(self):
        self.risk = None
        self.attributes = None
        self.city_infection_rate = 0.41

    def parse_responses(self, qa_list: list):
        """Extract responses and set them as class attributes"""
        [setattr(self, qa['attribute_name'], qa['response']) for qa in qa_list]
        self.attributes = [qa['attribute_name'] for qa in qa_list]

    def calculate_risk(self):
        """Calculate accumulated risk based on question responses"""
        risk_scores = utils.json_loader('risk_scores.json')
        risk_score_list = [risk_scores[attribute][getattr(self, attribute)]
                           for attribute in self.attributes]
        self.risk = np.prod(risk_score_list)*self.city_infection_rate


class Decision:
    def __init__(self):
        self.response_list = None

    def parse_responses(self, qa_list: list):
        """Extract responses and set them as class attributes"""
        [setattr(self, qa['attribute_name'], qa['response']) for qa in qa_list]
        self.attributes = [qa['attribute_name'] for qa in qa_list]

    def evaluate_responses(self):
        """Store feedback to user based on decisions"""
        decision_responses = utils.json_loader('decision_responses.json')
        self.response_list = [decision_responses[attribute][getattr(self, attribute)]
                              for attribute in self.attributes]
