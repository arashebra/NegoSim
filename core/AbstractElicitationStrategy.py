from abc import ABC, abstractmethod
from core.ElicitationStrategyInterface import ElicitationStrategyInterface
from core.UserInterface import UserInterface
from core.Offer import Offer
from core.StateInfo import StateInfo


class AbstractElicitationStrategy(ElicitationStrategyInterface):

    def __init__(self, user: UserInterface):
        self.__user = user

    def ask_initial_preference_from_user(self):
        initial_preference = self.__user.get_initial_preference()
        return initial_preference

    @abstractmethod
    def is_asking_time_from_use(self, state_info: StateInfo):
        """
        This method decides about when and which bid elicit from user
        :param state_info:
        Cal ask_offer_rank_from_user method
        """
        raise NotImplementedError()

    def ask_offer_rank_from_user(self, offer: Offer) -> list:
        """This method returns a list of ranked bids
        """
        self.__user.get_utility(offer)

    def ask_offer_utility_from_user(self, offer: Offer) -> float:
        raise NotImplementedError()

    def get_user(self) -> UserInterface:
        return self.__user
