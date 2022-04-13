from core.UtilitySpace import UtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan
import pickle
import time


class AnalysisMan1(AbstractAnalysisMan):

    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''

        self.analysis_data_structure = {}

        negotiation_state = self.get_nego_table().get_state_info().get_negotiation_state()
        preference_party1 = self.get_preference_of_party1()
        utility_space_party1 = UtilitySpace(preference_party1)
        preference_party2 = self.get_preference_of_party2()
        utility_space_party2 = UtilitySpace(preference_party2)
        party1 = self.get_party1()
        offers_on_table = self.get_nego_table().get_offers_on_table()
        party1_offers = offers_on_table[party1]
        if len(party1_offers) > 0:
            last_offer = party1_offers[len(party1_offers)-1]

            final_utility_party1 = utility_space_party1.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0
            final_utility_party2 = utility_space_party2.get_utility_distinct(last_offer) if negotiation_state == 1 else 0.0

            social_welfare = final_utility_party1 + final_utility_party2

            self.analysis_data_structure['Utility party1'] = final_utility_party1
            self.analysis_data_structure['Utility party2'] = final_utility_party2
            self.analysis_data_structure['Social Welfare'] = social_welfare

        return self.analysis_data_structure

    def save_analysis_data(self):
        file_name = 'sessionData_picked' + str(time.time_ns())
        sessionData = open(f'./logs/{file_name}', 'ab')
        data = self.analysis_data_structure if len(self.analysis_data_structure) > 0 else self.get_analysis_data()
        pickle.dump(data, sessionData)
        sessionData.close()