import Model
from Model import PreferenceXMLParser


class Controller:
    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = Model.GUIContent()

    def fetch_users(self):
        users = self.model.fetch_users()
        return users

    def fetch_protocols(self):
        protocols = self.model.fetch_protocols()
        return protocols

    def fetch_agents(self):
        agents = self.model.fetch_agents()
        return agents

    def fetch_domains(self):
        domains = self.model.fetch_domins()
        return domains

    def fetch_preferences_of_domain(self, domain):
        preferences_of_domain = self.model.fetch_preferences_of_domain(domain)
        return preferences_of_domain

    def fetch_preference_data_structure(self, domain_name: str, xml_file_name: str):
        preference_data_structure = PreferenceXMLParser(domain_name, xml_file_name).get_preference()
        return preference_data_structure

    def fetch_elicitation_strategies(self):
        elicitation_strategies = self.model.fetch_elicitation_strategies()
        return elicitation_strategies

    def fetch_user_models(self):
        user_models = self.model.fetch_user_models()
        return user_models

    def fetch_bidding_strategies(self):
        bidding_strategies = self.model.fetch_bidding_strategies()
        return bidding_strategies

    def fetch_opponent_models(self):
        opponent_models = self.model.fetch_opponent_models()
        return opponent_models

    def fetch_acceptance_strategies(self):
        acceptance_strategies = self.model.fetch_acceptance_strategies()
        return acceptance_strategies


if __name__ == '__main__':
    c = Controller()
    print(c.fetch_preference_data_structure('laptop', 'laptop_buyer_utility.xml'))
