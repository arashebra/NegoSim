from core.UserModelInterface import UserModelInterface
from core.Preference import Preference
from core.AbstractUserModel import AbstractUserModel
from core.Offer import Offer


class DefaultUserModel(AbstractUserModel):

    # def __init__(self, initial_preference: Preference):
    #     super().__init__(initial_preference)
    #

    def generate_initial_preference(self, initial_ranked_bids) -> Preference:
        initial_preference = self.get_initial_preference()

        raise NotImplementedError()

    def get_utility(self, offer: Offer) -> float:
        raise NotImplementedError()

    def update_preference(self, ranked_bids: list):
        raise NotImplementedError()

    def generate_preference(self, ranked_bids: list) -> Preference:
        preference = Preference()