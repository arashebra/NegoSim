#######################################################
#
# TestUtilitySpace.py
# Python implementation of the Class UtilitySpace
# Generated by Enterprise Architect
# Created on:      26-����-2022 02:24:13 �.�
# Original author: Arash Ebrahimnezhad
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
        if not isinstance(preference, Preference):
            raise TypeError('preference argument must be an instance of Preference')
        self.__preference = preference

    def get_preference(self) -> Preference:
        return self.__preference

    def get_d(self):
        '''
        :return: discount_factor
        '''
        return self.__preference.get_d()

    def get_reservation(self):
        '''
        :return: reservation
        '''
        return self.__preference.get_reservation()

    def get_utility(self, bid: Bid) -> float:
        weights = []
        scores_max_values = []
        issue_item = bid.get_issues_items()
        for issue in issue_item:
            if issue != 'discount_factor' and issue != 'reservation': # don't cont in discount_factor and reservation
                weights.append(self.__preference.get_issue_weight(issue))
                score, max_value = self.__preference.get_issue_item_value(issue, issue_item[issue])
                scores_max_values.append((score, max_value))

        utility = 0
        i = 0
        for weight in weights:
            utility += float(weight) * (scores_max_values[i][0] / scores_max_values[i][1])
            i += 1

        return utility

    def get_utility_distinct(self, offer: Offer) -> float:
        '''
        If there is time pressure
        :param offer:
        :return: distinct utility (a float number between [0, 1]
        '''
        bid = offer.get_bid()
        time = offer.get_time()
        return self.get_utility(bid)* (self.__d**time)
