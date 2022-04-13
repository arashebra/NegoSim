from abc import ABC, abstractmethod
from core.NegoPartyInterface import NegoPartyInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace
from core.TimeLine import TimeLine
from core.Bid import Bid
import random


class AbstractNegoParty(NegoPartyInterface, ABC):

    def __init__(self, preference: Preference):
        self.__preference = preference
        self.__utility_space = UtilitySpace(self.__preference)
        self.opponent_model = None

    def get_preference(self):
        return self.__preference

    def get_utility_space(self):
        return self.__utility_space

    def get_opponent_model(self):
        return self.opponent_model

    def generate_random_bid(self):
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            if issue != 'discount_factor' and issue != 'reservation':
                issue_item = list((preference_data_structure[issue][1]).keys())
                issue_items[issue] = random.choice(issue_item)

        bid = Bid(issue_items)
        return bid

    @abstractmethod
    def send_bid(self, protocol, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()