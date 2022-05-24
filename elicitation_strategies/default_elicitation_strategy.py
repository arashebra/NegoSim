from abc import ABC
from core.Offer import Offer
from core.AbstractElicitationStrategy import AbstractElicitationStrategy
from core.StateInfo import StateInfo
from core.UserModelInterface import UserModelInterface


class DefaultElicitationStrategy(AbstractElicitationStrategy, ABC):

    def is_asking_time_from_use(self, state_info: StateInfo):
        """
        This method decides about when and which bid elicit from user
        :param state_info:
        Cal ask_offer_rank_from_user method
        """
        if self.get_initial_ranked_bids() is None:
            # this line asks initial ranked bids (self.__initial_ranked_bids = initial ranked bids)
            self.ask_initial_ranked_bids_from_user()
            user_model: UserModelInterface = self.get_user_model()
            user_model.generate_initial_preference()

