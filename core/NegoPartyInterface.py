#######################################################
#
# NegoPartInterface.py
# Python implementation of the Interface NegoPartInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: DP
#
#######################################################
from core.Bid import Bid
from abc import ABC, abstractmethod
from core.TimeLine import TimeLine


class NegoPartyInterface(ABC):

    @abstractmethod
    def send_bid(self, protocol, timeline: TimeLine) -> Bid:
        """
        send new bid, send same bid refer to accept, send {} refer to end negotiation
        :return: Bid
        """
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        """
        :return: Party Name
        """
        raise NotImplementedError()