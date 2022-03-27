from core.OpponentModelInterface import OpponentModelInterface
from core.Preference import Preference
from core.Offer import Offer
from abc import ABC, abstractmethod


class AbstractOpponentModel(OpponentModelInterface):

    def __init__(self, preference: Preference):
        self.preference = preference
        self.preference_data_structure = self.preference.get_preference_data_structure()
        for issue in self.preference_data_structure:
            self.preference_data_structure[issue][0] = 1.0 / len(self.preference_data_structure)
            for key in self.preference_data_structure[issue][1]:
                self.preference_data_structure[issue][1][key] = 1

    def get_initial_opponent_preference(self) -> Preference:
        return self.preference_data_structure

    def get_preference(self) -> Preference:
        return self.preference

    @abstractmethod
    def update_preference(self, offer: Offer) -> Preference:
        pass

