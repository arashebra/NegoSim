#######################################################
#
# BiddingStrategy.py
# Python implementation of the Interface BiddingStrategyInterface
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: DP
#
#######################################################
from core.Bid import Bid
from abc import ABC, abstractmethod


class BiddingStrategyInterface(ABC):

    @abstractmethod
    def send_bid(timline) -> Bid:
        raise NotImplementedError()