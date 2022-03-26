from core.Offer import Offer
from core.UtilitySpace import UtilitySpace
from core.UserInterface import UserInterface


class DefaultUser(UserInterface):

    """
    Default user answers all question that has got from
    elicitation strategy
    """

    def __init__(self, utility_space):
        self.utility_space = utility_space

    def get_initial_bids_rank(self) -> list:
        """This method returns list of ranked bids in uncertain situation.
        """
        pass

    def get_initial_preference(self) -> UtilitySpace:
        """This method returns initial preference in certain situation.
        """
        return self.utility_space

    def get_offer_rank(self, offer: Offer) -> list:
        """This method returns a list of bids that exist special bid which has been sent
        to it.
        """
        pass

    def get_utility(self, offer: Offer) -> float:
        """This method returns exact utility of an offer
        """
        return self.utility_space.get_utility(offer.get_bid())


# from core.Bid import Bid
# from core.TimeLine import TimeLine
# from core.Preference import Preference
#
#
# if __name__ == '__main__':
#     test_bid = {
#         'Laptop': 'HP',
#         'Harddisk': '60 Gb',
#         'External Monitor': "19 LCD"
#     }
#     my_preference = Preference('laptop', {'Laptop': ['0.4452125771655631', {'Dell': '1', 'Macintosh': '2', 'HP': '3'}], 'Harddisk': ['0.37808251708013424', {'60 Gb': '3', '80 Gb': '2', '120 Gb': '1'}], 'External Monitor': ['0.1767567099260568', {"19 LCD": '3', "20 LCD": '1', "23 LCD": '2'}]})
#     utility_space = UtilitySpace(my_preference)
#     defaultUser = DefaultUser(utility_space)
#     bid = Bid(test_bid)
#     test_time_line = TimeLine()
#     offer = Offer(bid, test_time_line)
#     print(defaultUser.get_utility(offer))