from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Offer import Offer
from abc import ABC, abstractmethod
from core.UtilitySpace import UtilitySpace


class AbstractAcceptanceStrategy(AcceptanceStrategyInterface):

    def __init__(self, utility_space: UtilitySpace):
        if not isinstance(utility_space, UtilitySpace):
            raise TypeError('utility_space argument must be an instance of UtilitySpace')
        self.__utility_space = utility_space

    @abstractmethod
    def is_acceptable(self, offer: Offer) -> int:
        """this method returns 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        """
        raise NotImplementedError()

    def get_utility_space(self):
        return self.__utility_space
