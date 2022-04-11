from core.AbstractNegoParty import AbstractNegoParty
from core.Bid import Bid
from core.TimeLine import TimeLine


class RandomParty1(AbstractNegoParty):

    def send_bid(self, protocol, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        parties = protocol.get_parties()
        opponent = list(filter(lambda party: party is not self, parties))[0]
        opponen_offer = protocol.get_offers_on_table(opponent)

        bid = self.generate_random_bid()
        if len(opponen_offer) > 0:
            op_bid = opponen_offer[len(opponen_offer) - 1].get_bid()
            if self.get_utilitiy_space().get_utility(op_bid) >= self.get_utilitiy_space().get_utility(bid) and self.get_utilitiy_space().get_utility(op_bid) > 0.7:
                return op_bid
        return bid

    def get_name(self):
        return 'Random1'
