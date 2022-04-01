#######################################################
#
# User.py
# Python implementation of the Interface UserInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: Arash Ebrahimnezhad
#
#######################################################
from core.Preference import Preference
from core.Offer import Offer
from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_initial_preference(self) -> Preference:
        """This method returns initial preference in certain situation.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_utility(self, offer: Offer) -> float:
        """This method returns exact utility of an offer
        """
        raise NotImplementedError()
