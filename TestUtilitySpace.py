import unittest
from core.Preference import Preference
from core.UtilitySpace import UtilitySpace
from core.Bid import Bid


class TestUtilitySpace(unittest.TestCase):

    def setUp(self) -> None:
        issue_item = {
            'salary': '2500',
            'fte': '0.6',
            'work from home': '2',
            'lease car': 'no',
            'permanent contract': 'yes',
            'career development opportunities': 'medium'
        }

        self.bid = Bid(issue_item)

    def test_get_utility1(self):
        preference = Preference('job', 'Jobs_util1.xml')
        utility_space = UtilitySpace(preference)
        self.assertAlmostEqual(0.526, utility_space.get_utility(self.bid), places=2)

    def test_get_utility2(self):
        preference = Preference('job', 'Jobs_util2.xml')
        utility_space = UtilitySpace(preference)
        self.assertAlmostEqual(0.439864, utility_space.get_utility(self.bid), places=4)

    def test_get_utility3(self):
        m_issue_item = {'Laptop': 'HP', 'Harddisk': '120 Gb', 'External Monitor': "23'' LCD", }
        bid = Bid(m_issue_item)
        preference = Preference('laptop', 'laptop_bayer_utility.xml')
        utility_space = UtilitySpace(preference)
        self.assertAlmostEqual(1.0, utility_space.get_utility(bid), places=4)


if __name__ == '__main__':
    unittest.main()