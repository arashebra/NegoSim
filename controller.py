import model
from configurations import *


class Controller:
    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = model.Model()

    def fech_agents(self):
        agents = self.model.fetch_agents()
        return agents

    def fetch_domains(self):
        domains = self.model.fetch_domins()
        return domains

    def fetch_preferences_of_domain(self, domain):
        preferences_of_domain = self.model.fetch_preferences_of_domain(domain)
        return preferences_of_domain
