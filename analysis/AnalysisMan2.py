from core.UtilitySpace import UtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan
import pickle
import time


class AnalysisMan2(AbstractAnalysisMan):
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
        party2 = self.get_party2()
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1]
        party2_offers = offers_on_table[party2]
        last_offer = party1_offers[len(party1_offers) - 1]

        final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0
        final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0

        social_welfare = final_utility_party1 + final_utility_party2

        offers1 = [(offer.get_bid(), offer.get_time(), utility_space_party1.get_utility_distinct(offer)) for offer in party1_offers]
        analysis_data_structure['party1 offers'] = offers1
        offers2 = [(offer.get_bid(), offer.get_time(), utility_space_party2.get_utility_distinct(offer)) for offer in party2_offers]
        analysis_data_structure['party2 offers'] = offers2

        analysis_data_structure['Utility party1'] = final_utility_party1
        analysis_data_structure['Utility party2'] = final_utility_party2
        analysis_data_structure['Social Welfare'] = social_welfare

        file_name = 'sessionData_picked'+str(time.time_ns())
        sessionData = open(f'./logs/{file_name}', 'ab')
        pickle.dump(analysis_data_structure, sessionData)
        sessionData.close()

        return analysis_data_structure