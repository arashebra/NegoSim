from core.UserModelInterface import UserModelInterface
from core.Preference import Preference
from core.ElicitationStrategyInterface import ElicitationStrategyInterface


class DefaultUserModel(UserModelInterface):

    def __init__(self):
        pass

    def generate_initial_preference(self) -> Preference:
        pass