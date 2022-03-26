#######################################################
# 
# Preference.py
# Python implementation of the Class Preference
# Generated by Enterprise Architect
# Created on:
# Original author: Arash Ebrahimnezhad
# 
#######################################################

from controller import Controller

class Preference:
    """
    preference has its own data structure and when an object asks preference, it returns that specific data structure.
    In the following there is an example:
    preference = {
        'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
        'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
        'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
    }
    """

    def __init__(self, domain_name: str, xml_file_name: str):
        """
        preference = {
            'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
            'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
            'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
        }
        :param domain_name:
        :param preference_name:
        """
        self.preference_data_structure = Controller.fetch_preference_data_structure(domain_name, xml_file_name)

    def get_preference(self):
        return self.preference_data_structure

    def get_issue_weight(self, issue: str):
        return self.preference_data_structure[issue][0]

    def get_issue_item_value(self, issue: str, item: str):
        """
        :param issue: str
        :param value: str
        :return: value, max_value
        """
        item_value_dict = self.preference_data_structure[issue][1]
        max_value = max(int(x) for x in item_value_dict.values())
        return int(item_value_dict[item]), max_value
