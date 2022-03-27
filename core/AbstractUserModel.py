from abc import abstractmethod
from core.UserModelInterface import UserModelInterface
from core.ElicitationStrategyInterface import ElicitationStrategyInterface
from core.Preference import Preference
from core.Offer import Offer


class AbstractUserModel(UserModelInterface):

    def __init__(self, elicitation_strategy: ElicitationStrategyInterface):
        self.elicitation_strategy = elicitation_strategy

    @abstractmethod
    def generate_initial_preference(self) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        raise NotImplementedError()

    def get_elicitation_strategy(self):
        return self.elicitation_strategy
