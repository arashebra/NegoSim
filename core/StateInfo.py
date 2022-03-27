from core.TimeLine import TimeLine
from core.Offer import Offer

class StateInfo:

    def __init__(self, time_line: TimeLine, my_agent_offers: list, opponent_offers: dict):
        """
        :param time_line:
        :param agent_offers: [offer1, offer2, ...]
        :param opponent_offers: {opponent1:[offer1, offer2, ...], opponent2:[offer1, offer2, ...]}
        """
        self.time_line = time_line
        self.my_agent_offers = my_agent_offers
        self.opponent_offers = opponent_offers
        """
        This attribute is an integer that can get 3 different numbers, 
        0 for negotiation continuing, 
        1 negotiation has ended with an agreement and 
        -1 that refer to the end negotiation ended without agreement.
        """
        self.negotiation_state = 0

    def get_time_line(self) -> TimeLine:
        return self.time_line

    def get_my_agent_offers(self) -> list:
        return self.my_agent_offers

    def get_opponent_offers(self) -> dict:
        return self.opponent_offers

    def get_negotiation_state(self):
        return self.negotiation_state


