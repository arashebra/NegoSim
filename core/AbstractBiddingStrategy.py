from core.BiddingStrategyInterface import BiddingStrategyInterface
from abc import abstractmethod
from core.Bid import Bid
from core.OpponentModelInterface import OpponentModelInterface
from core.TimeLine import TimeLine
from core.Preference import Preference


class AbstractBiddingStrategy(BiddingStrategyInterface):

    def __init__(self, opponent_model: OpponentModelInterface, preference: Preference):
        if not isinstance(opponent_model, OpponentModelInterface):
            raise TypeError('opponent_model argument must be an instance of OpponentModelInterface')
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')

        self.__opponent_model = opponent_model
        self.__preference = preference

    @abstractmethod
    def send_bid(self, timeline: TimeLine) -> Bid:
        raise NotImplementedError()

    def get_opponent_model(self):
        return self.__opponent_model

    def get_preference(self):
        return self.__preference
