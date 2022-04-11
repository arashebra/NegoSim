from abc import ABC, abstractmethod
from core.NegoPartyInterface import NegoPartyInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace
from core.TimeLine import TimeLine
from core.Bid import Bid


class AbstractNegoParty(NegoPartyInterface, ABC):

    def __init__(self, preference: Preference):
        self.__preference = preference
        self.__utility_space = UtilitySpace(self.__preference)

    def get_preference(self):
        return self.__preference

    def get_utilitiy_space(self):
        return self.__utility_space

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