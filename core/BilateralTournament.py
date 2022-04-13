from itertools import permutations
from core.BilateralSession import BilateralSession
from controller import Controller


class BilateralTournament:

    def __init__(self, protocol_name: str, analysis_man_name: str, deadline,
                 party1_names: list, party2_names: list, domain_names: list):

        self.__domain_names = domain_names
        self.__party1_names = party1_names
        self.__party2_names = party2_names
        self.__protocol_name = protocol_name
        self.__analysis_man_name = analysis_man_name
        self.__analysis_man_name = analysis_man_name
        self.__deadline = deadline

    def start_tournament(self):
        ctrl = Controller()
        for domain_name in self.__domain_names:
            preferences_of_domain = ctrl.fetch_preferences_of_domain(domain_name)
            for preference_permutations in permutations(preferences_of_domain, 2):
                for party1_name in self.__party1_names:
                    for party2_name in self.__party2_names:
                        if party1_name != party2_name:
                            bilateral_session = BilateralSession(protocol_name=self.__protocol_name,
                                                                 analysis_man_name=self.__analysis_man_name,
                                                                 deadline=self.__deadline,
                                                                 first_preference_name=preference_permutations[0],
                                                                 second_preference_name=preference_permutations[1],
                                                                 party1_name=party1_name,
                                                                 party2_name=party2_name,
                                                                 domain_name=domain_name)
                            bilateral_session.start_session()
