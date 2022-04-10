from core.UtilitySpace import UtilitySpace
import itertools
from core.Bid import Bid


class BidSpace:
    """
    preference = {
        'Brand': [0.45, {'Lenovo': 10, 'Assus': 20, 'Mac': 30}],
        'Monitor': [0.18, {'15': 30, '10': 25, '11': 20}],
        'HDD': [0.38, {'1T': 25, '2T': 32, '3T': 35}]
    }
    """

    def __init__(self, preference):
        self.preference = preference
        self.utility_space = UtilitySpace(preference)

    # ////////////////////////////////////////////////////////////////////////////
    def get_all_bids(self) -> tuple:
        q = []
        values = self.preference.get_preference_data_structure().values()
        for x in values:
            q.append(list(x[1]))
        print(tuple(itertools.product(*q)))

    def get_all_bids_with_utility(self):
        issues = self.preference.get_preference_data_structure().keys()
        issue_item = {}
        bids_with_utility = {}
        q = []
        values = self.preference.get_preference_data_structure().values()
        for x in values:
            q.append(list(x[1]))
        for i in itertools.product(*q):
            for j in range(len(issues)):
                issue_item[tuple(issues)[j]] = i[j]
            bid = Bid(issue_item)
            utility = self.utility_space.get_utility(bid)
            bids_with_utility[bid] = utility

        return bids_with_utility

    def get_all_bids_utility(self):
        issues = self.preference.get_preference_data_structure().keys()
        issue_item = {}
        bids_utility = []
        q = []
        values = self.preference.get_preference_data_structure().values()
        for x in values:
            q.append(list(x[1]))
        for i in itertools.product(*q):
            for j in range(len(issues)):
                issue_item[tuple(issues)[j]] = i[j]
            bid = Bid(issue_item)
            utility = self.utility_space.get_utility(bid)
            bids_utility.append(utility)

        return bids_utility


    # def product(self, *iterables):
    #     """ which does NOT build intermediate results.
    #         Omitted 'repeat' option.
    #         product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    #     """
    #     nIters = len(iterables)
    #     lstLenths = []
    #     lstRemaining = [1]
    #     for i in range(nIters-1, -1, -1):
    #         m = len(iterables[i])
    #         lstLenths.insert(0, m)
    #         lstRemaining.insert(0, m * lstRemaining[0])
    #     nProducts = lstRemaining.pop(0)
    #
    #     for p in range(nProducts):
    #         lstVals = []
    #         for i in range(nIters):
    #             j = p/lstRemaining[i]%lstLenths[i]
    #             lstVals.append(iterables[int(i)][int(j)])
    #         yield tuple(lstVals)


# if __name__ == '__main__':
#     get_all_bids_with_utility()