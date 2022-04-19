from core.UtilitySpace import UtilitySpace
from core.AbstractAnalysisMan import AbstractAnalysisMan
import math
from statistics import mean


class AnalysisMan2(AbstractAnalysisMan):

    def get_analysis_data(self) -> dict:
        '''
        :return: a dict
        '''
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

        offers1 = [(offer.get_bid(), offer.get_time(), utility_space_party1.get_utility_distinct(offer)) for offer in
                   party1_offers]
        self.analysis_data_structure['party1 offers'] = offers1
        offers2 = [(offer.get_bid(), offer.get_time(), utility_space_party2.get_utility_distinct(offer)) for offer in
                   party2_offers]
        self.analysis_data_structure['party2 offers'] = offers2

        self.analysis_data_structure['party1_'+party1.get_name()] = final_utility_party1
        self.analysis_data_structure['party2_'+party2.get_name()] = final_utility_party2
        self.analysis_data_structure[party1.get_name()+'_SocialWelfare'] = social_welfare

        if self.get_opponent_model_party1() != None:
            estimated_preferance = self.get_opponent_model_party1().get_preference()
            total = 0
            issue_weights = preference_party1.get_weights()

            for issue, weight in issue_weights.items():
                item_value = preference_party1.get_issue_ItemValue(issue=issue)
                estimated_item_value = estimated_preferance.get_issue_ItemValue(issue=issue)
                avg_values = mean(float(x) for x in item_value.values())
                for item, _ in item_value.items():
                    v = avg_values - float(estimated_item_value[item])
                    total += float(weight) * (v ** 2)
            wrmse1 = math.sqrt(total)
            self.analysis_data_structure['WRMSE 1'] = wrmse1

        if self.get_opponent_model_party2() != None:
            estimated_preferance = self.get_opponent_model_party2().get_preference()
            total = 0
            issue_weights = preference_party2.get_weights()

            for issue, weight in issue_weights.items():
                item_value = preference_party2.get_issue_ItemValue(issue=issue)
                estimated_item_value = estimated_preferance.get_issue_ItemValue(issue=issue)
                avg_values = mean(float(x) for x in item_value.values())
                for item, _ in item_value.items():
                    v = avg_values - float(estimated_item_value[item])
                    total += float(weight) * (v ** 2)
            wrmse2 = math.sqrt(total)
            self.analysis_data_structure['WRMSE 2'] = wrmse2

        return self.analysis_data_structure

