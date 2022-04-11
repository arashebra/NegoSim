from core.UtilitySpace import UtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan


class AnalysisMan1(AbstractAnalysisMan):

    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''

        analysis_data_structure = {}

        negotiation_state = self.get_nego_table().get_state_info().get_negotiation_state()
        preference_party1 = self.get_preference_of_party1()
        utility_space_party1 = UtilitySpace(preference_party1)
        preference_party2 = self.get_preference_of_party2()
        utility_space_party2 = UtilitySpace(preference_party2)
        party1 = self.get_party1()
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1]
        last_offer = party1_offers[len(party1_offers)-1]

        final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0
        final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0

        social_welfare = final_utility_party1 + final_utility_party2

        analysis_data_structure['Utility party1'] = final_utility_party1
        analysis_data_structure['Utility party2'] = final_utility_party2
        analysis_data_structure['Social Welfare'] = social_welfare

        return analysis_data_structure
