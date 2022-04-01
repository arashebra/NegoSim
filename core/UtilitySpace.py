#######################################################
#
# UtilitySpace.py
# Python implementation of the Class UtilitySpace
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: DP
#
#######################################################
from core.Preference import Preference
from core.Bid import Bid
from core.Offer import Offer


class UtilitySpace:
    """
    In this class only linear utility function was developed.
    This class must be extended later
    """

    def __init__(self, preference: Preference):
        self.__preference = preference

    def get_preference(self) -> Preference:
        return self.__preference

    def get_utility(self, bid: Bid) -> float:
        weights = []
        scores = []
        issue_item = bid.get_issues_items()
        for issue in issue_item:
            weights.append(self.__preference.get_issue_weight(issue))
            score, max_value = self.__preference.get_issue_item_value(issue, issue_item[issue])
            scores.append(score)

        utility = 0
        i = 0
        for weight in weights:
            utility += float(weight) * (scores[i] / max_value)
            i += 1

        return utility

    def get_utility_distinct(self, offer: Offer) -> float:
        pass
