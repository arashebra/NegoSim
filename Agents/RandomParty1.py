from core.NegoPartyInterface import NegoPartyInterface
from core.BiddingStrategyInterface import BiddingStrategyInterface
from core.OpponentModelInterface import OpponentModelInterface
from core.AcceptanceStrategyInterface import AcceptanceStrategyInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace
from core.Bid import Bid
from core.ProtocolInterface import ProtocolInterface
from core.TimeLine import TimeLine


class RandomParty(NegoPartyInterface):

    def __init__(self, protocol: ProtocolInterface, preference: Preference, bidding_strategy: BiddingStrategyInterface,
                 opponent_model: OpponentModelInterface, acceptance_strategy: AcceptanceStrategyInterface):
        self.protocol = protocol
        self.bidding_strategy = bidding_strategy
        self.opponent_model = opponent_model
        self.acceptance_strategy = acceptance_strategy
        self.preference = preference
        self.utility_space = UtilitySpace(self.preference)

    def send_bid(self, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        parties = self.protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponen_offer = self.protocol.get_offers_on_table(opponent)
        bid = self.bidding_strategy.send_bid(timeline)
        if self.acceptance_strategy.is_acceptable(offer=opponen_offer, my_next_bid=bid, opponent_model=self.opponent_model):
            return opponen_offer.get_bid()
        return bid
