from abc import ABC, abstractmethod
from core.Preference import Preference
from core.NegoPartyInterface import NegoPartyInterface
from core.NegoTable import NegoTable
from core.NegoPartyInterface import NegoPartyInterface


class AbstractAnalysisMan(ABC):

    '''
    analysis_data_structure = {
        'parties_utility': {party1: 0.74, party2: 0.85},
        'social_welfare': 1.59,
        ...
    }
    '''

    def __init__(self, party1, party2, nego_table, preference_of_party1, preference_of_party2, estimated_preference_of_party1 = None, estimated_preference_of_party2= None):
        if not isinstance(party1, NegoPartyInterface):
            raise TypeError('party1 argument must be an instance of NegoPartyInterface')
        if not isinstance(party2, NegoPartyInterface):
            raise TypeError('party2 argument must be an instance of NegoPartyInterface')
        if not isinstance(nego_table, NegoTable):
            raise TypeError('offers_on_table argument must be an instance of dict')
        if not isinstance(preference_of_party1, Preference):
            raise TypeError('preference_of_party1 argument must be an instance of NegoPartyInterface')
        if not isinstance(preference_of_party2, Preference):
            raise TypeError('preference_of_party2 argument must be an instance of NegoPartyInterface')
        if not (isinstance(estimated_preference_of_party1, Preference) or estimated_preference_of_party1 == None):
            raise TypeError('estimated_preference_of_party1 argument must be an instance of Preference')
        if not (isinstance(estimated_preference_of_party2, Preference) or estimated_preference_of_party2 == None):
            raise TypeError('estimated_preference_of_party2 argument must be an instance of Preference')
        self.__party1 = party1
        self.__party2 = party2
        self.__nego_table = nego_table
        self.__preference_of_party1 = preference_of_party1
        self.__preference_of_party2 = preference_of_party2
        self.__estimated_preference_of_party1 = estimated_preference_of_party1
        self.__estimated_preference_of_party2 = estimated_preference_of_party2

    def get_party1(self):
        return self.__party1

    def get_party2(self):
        return self.__party2

    def get_nego_table(self):
        return self.__nego_table

    def get_preference_of_party1(self):
        return self.__preference_of_party1

    def get_preference_of_party2(self):
        return self.__preference_of_party2

    def get_estimated_preference_of_party1(self):
        return self.__estimated_preference_of_party1

    def get_estimated_preference_of_party2(self):
        return self.__estimated_preference_of_party2

    @abstractmethod
    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''
        raise NotImplementedError()
