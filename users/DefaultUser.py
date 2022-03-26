from core.Offer import Offer
from core.Preference import Preference
from core.UserInterface import UserInterface


class DefaultUser(UserInterface):

    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """
        pass

    def get_initial_preference(self) -> Preference:
        """This method returns initial preference. the initial preference could be
        completed or uncompleted related to certainty or uncertainty respectively.
        """
        pass

    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        pass

    def get_utility(self, offer: Offer) -> float:
        """This method returns exact utility of an offer
        """
        pass
