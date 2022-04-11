import unittest
from core.Preference import Preference
from core.BidSpace import BidSpace


class TestBidSpace(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Preference('laptop', 'laptop_buyer_utility.xml')
        self.bid_space = BidSpace(self.p)

    def test_get_all_bids(self):
        print(self.bid_space.get_all_bids_with_utility())


if __name__ == '__main__':
    unittest.main()