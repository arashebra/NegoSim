from core.NegoPartyInterface import NegoPartyInterface
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace
from core.Bid import Bid
from acceptance_strategies.ACNext import ACNext
from core.TimeLine import TimeLine
from opponent_models.DefaultOpponentModel import DefaultOpponentModel
from bidding_strategies.RandomStrategy import RandomStrategy


class RandomParty2(NegoPartyInterface):

    def __init__(self, preference: Preference):
        self.preference = preference
        self.opponent_model = DefaultOpponentModel(preference=self.preference)
        self.bidding_strategy = RandomStrategy(opponent_model=self.opponent_model, preference=self.preference)
        self.utility_space = UtilitySpace(preference=self.preference)
        self.acceptance_strategy = ACNext(utility_space=self.utility_space)

    def send_bid(self, protocol, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponen_offers = protocol.get_offers_on_table(opponent)
        bid = self.bidding_strategy.send_bid(timeline)
        if len(opponen_offers) > 0:
            op_offer = opponen_offers[len(opponen_offers) - 1]
            self.opponent_model.update_preference(op_offer)
            if self.acceptance_strategy.is_acceptable(offer=op_offer, my_next_bid=bid,
                                                      opponent_model=self.opponent_model):
                return op_offer.get_bid()
        return bid

    def get_name(self):
        return 'Random2'
