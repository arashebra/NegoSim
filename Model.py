from configurations import *
from os import listdir
from os.path import isfile, join
import os
from genericpath import isdir
from xml.etree import ElementTree

PARTY_PATH = './Agents'
DOMAIN_PATH = './Domains'
USER_PATH = 'users'

class GUIContent:
    def __init__(self):
        pass

    def fetch_users(self):
        user_list = [f for f in listdir(
            USER_PATH) if isfile(join(USER_PATH, f))]
        user_list.remove('__init__.py')
        return user_list

    def fetch_agents(self):
        party_list = [f for f in listdir(
            PARTY_PATH) if isfile(join(PARTY_PATH, f))]
        party_list.remove('__init__.py')
        return party_list

    def fetch_domins(self):
        domain_lists = [name for name in os.listdir(DOMAIN_PATH)]
        return domain_lists

    def fetch_preferences_of_domain(self, domain):
        path = '.\Domains' + '\\' + domain
        if isdir(path):
            preference_profile_list = [name for name in os.listdir(path)]
            return preference_profile_list
        return None


class PreferenceXMLParser:
    """
        preference = {
                'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
                'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
                'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
            }
    """

    def __init__(self, domain_name: str, xml_file: str):
        self.file_name = xml_file
        self.domain_name = domain_name

    def get_preference(self):
        full_file = os.path.abspath(os.path.join(DOMAIN_PATH+'\\'+self.domain_name, self.file_name))
        dom = ElementTree.parse(full_file)

        preference = {}
        objectives = dom.findall('objective')
        for objective in objectives:
            issues = objective.findall('issue')
            for issue in issues:
                preference[issue.attrib['name']] = []
                items = issue.findall('item')
                item_value = {}
                for item in items:
                    item_value[item.attrib['value']] = item.attrib['evaluation']
                preference[issue.attrib['name']].append(item_value)

            weights = objective.findall('weight')
            i = 0
            for issue in preference:
                preference[issue].insert(0, weights[i].attrib['value'])
                i += 1

        return preference


if __name__ == '__main__':
    # model = GUIContent()
    # print(model.fetch_users())
    preferenceXMLParser = PreferenceXMLParser('laptop', 'laptop_buyer_utility.xml')
    print(preferenceXMLParser.get_preference())