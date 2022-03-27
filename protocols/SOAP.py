from core.AbstractProtocl import AbstractProtocol
from core.Offer import Offer


class SOAP(AbstractProtocol):

    def negotiate(self, offers_on_the_table: dict):
        """This method ask a bid from party according to order and negotiation state then
        convert it to offer and add it to the table offers and update negotiation state

           negotiation state will be 1 if the last parties' offer are same
           negotiation state will be 0 if the last parties' offer are not same
           negotiation state will be -1 if the one of last parties' offer's Bid is {}
        """
        while True:
            parties = self.nego_table.get_parties()
            for party in parties:
                if self.get_time_line().is_time_ended():
                    self.nego_table.get_state_info().negotiation_state = -1
                if self.nego_table.get_state_info().negotiation_state == 0:
                    bid = party.send_bid(self.get_time_line())
                    offer = Offer(bid, self.get_time())
                    self.nego_table.add_offer(party, offer)

            if self.is_agreement():
                self.nego_table.get_state_info().negotiation_state = 1
            if self.nego_table.get_state_info().negotiation_state != 0:
                return 1

    def is_agreement(self):
        """
        :return: True if all parties lats offer is same
        """
        parties = self.nego_table.get_parties()
        agreement = True
        offer = None
        for party in parties:
            party_offer = self.nego_table.get_offers_on_table()[party]
            if offer is None:
                offer = party_offer[len(party_offer) - 1]
            elif offer != party_offer[len(party_offer) - 1]:
                agreement = False
        return agreement

    def get_offers_on_table(self, party) -> tuple:
        """This method gets a party name in string type and returns a tuple of offers
        related to the party name that has got through the object that has called the
        method.
           Before returning the offers, the method checks out whether the object that
        has called the method has authority to access the offers or not? if there is no
        permission it returns an error.

        This protocol lets all parties knows each other offers
        """
        return self.get_nego_table().get_offers_on_table()[party]



