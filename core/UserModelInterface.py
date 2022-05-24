#######################################################
#
# UserModel.py
# Python implementation of the Interface UserModelInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: Arash Ebrahimnezhad
#
#######################################################
from core.Preference import Preference
from abc import ABC, abstractmethod
from core.Offer import Offer


class UserModelInterface(ABC):

    @abstractmethod
    def generate_initial_preference(self, initial_ranked_bids) -> Preference:
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        raise NotImplementedError()

    @abstractmethod
    def update_preference(self, ranked_bids: list):
        raise NotImplementedError()
