from core.NegoPartyInterface import NegoPartyInterface
from core.BiddingStrategyInterface import BiddingStrategyInterface
from core.OpponentModelInterface import OpponentModelInterface
from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Bid import Bid
from core.TimeLine import TimeLine


class RandomParty(NegoPartyInterface):

    def __init__(self, bidding_strategy: BiddingStrategyInterface, opponent_model: OpponentModelInterface,
                 acceptance_strategy: AcceptanceStrategyInterface):
        self.bidding_strategy = bidding_strategy
        self.opponent_model = opponent_model
        self.acceptance_strategy = acceptance_strategy

    def send_bid(self, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        self.bidding_strategy.send_bid(timeline)
