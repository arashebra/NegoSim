import unittest
from core.Preference import Preference


class TestPreference(unittest.TestCase):

    def setUp(self) -> None:
        self.preference = Preference('laptop', 'laptop_buyer_utility.xml')

    def test_get_preference_data_structure(self):
        print(self.preference.get_preference_data_structure())

    def test_get_issue_weight(self):
        print(self.preference.get_issue_weight('Laptop'))

if __name__ == '__main__':
    unittest.main()
