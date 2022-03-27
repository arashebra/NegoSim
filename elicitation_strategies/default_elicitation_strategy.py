from core.Offer import Offer
from core.ElicitationStrategyInterface import ElicitationStrategyInterface


class DefaultElicitationStrategy(ElicitationStrategyInterface):

    def ask_offer_rank_from_user(self, offer: Offer) -> list:
        """This method returns a list of ranked bids
        """
        pass

    def ask_offer_utility_from_user(self, offer: Offer) -> float:
        pass
