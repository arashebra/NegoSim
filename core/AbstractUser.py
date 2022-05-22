from abc import abstractmethod

from core.Offer import Offer
from core.UserInterface import UserInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace


class AbstractUser(UserInterface):

    def __init__(self, preference: Preference):
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')
        self.__preference = preference
        self.__utility_space = UtilitySpace(preference)

    def get_preference(self):
        return self.__preference

    def get_utility_space(self):
        return self.__utility_space

    @abstractmethod
    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_initial_preference(self) -> Preference:
        """This method returns initial preference in certain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        """This method returns exact utility of an offer
        """
        raise NotImplementedError()
