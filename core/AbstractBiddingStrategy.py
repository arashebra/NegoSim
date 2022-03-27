from core.BiddingStrategyInterface import BiddingStrategyInterface
from abc import abstractmethod
from core.Bid import Bid
from core.OpponentModelInterface import OpponentModelInterface
from core.TimeLine import TimeLine
from core.Preference import Preference


class AbstractBiddingStrategy(BiddingStrategyInterface):

    def __init__(self, opponent_model: OpponentModelInterface, preference: Preference):
        self.opponent_model = opponent_model
        self.preference = preference

    @abstractmethod
    def send_bid(self, timeline: TimeLine) -> Bid:
        raise NotImplementedError()

    def get_opponent_model(self):
        return self.opponent_model

    def get_preference(self):
        return self.preference
