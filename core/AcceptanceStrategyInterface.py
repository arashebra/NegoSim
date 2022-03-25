#######################################################
#
# AcceptanceStrategy.py
# Python implementation of the Interface AcceptanceStrategyInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: DP
#
#######################################################
from core.Offer import Offer
from abc import ABC, abstractmethod


class AcceptanceStrategyInterface(ABC):

    @abstractmethod
    def is_acceptable(offer: Offer) -> int:
        """this method returns 0 refer to reject opponent's offer or 1 refer to accept
        opponent offer.
        """
        raise NotImplementedError()
