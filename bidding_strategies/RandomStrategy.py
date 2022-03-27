from core.AbstractBiddingStrategy import AbstractBiddingStrategy
from core.TimeLine import TimeLine
from core.Bid import Bid
import random


class RandomStrategy(AbstractBiddingStrategy):

    def send_bid(self, timeline: TimeLine) -> Bid:
        issue_items = {}
        preference_data_structure = self.get_preference().get_preference_data_structure()
        for issue in preference_data_structure:
            issue_item = list((preference_data_structure[issue][1]).keys())
            issue_items[issue] = random.choice(issue_item)
        bid = Bid(issue_items)
        return bid