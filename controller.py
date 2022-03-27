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
