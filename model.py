from configurations import *
from os import listdir
from os.path import isfile, join
import os
from genericpath import isdir

PARTY_PATH = '.\Agents'
DOMAIN_PATH = '.\Domains'


class Model:
    def __init__(self):
        pass

    def fetch_agents(self):
        party_list = [f for f in listdir(
            PARTY_PATH) if isfile(join(PARTY_PATH, f))]
        return party_list

    def fetch_domins(self):
        domain_lists = [name for name in os.listdir(DOMAIN_PATH)]
        return domain_lists

    def fetch_preferences_of_domain(self, domain):
        path = '.\Domains'+'\\'+domain
        if isdir(path):
            preference_profile_list = [name for name in os.listdir(path)]
            return preference_profile_list
        return None


if __name__ == '__main__':
    model = Model()
    print(model.fetch_preferences_of_domain('car'))
